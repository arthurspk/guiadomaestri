#!/usr/bin/env python3
"""
maestri_build.py — Builder de arquivos `.maestripartitura` para o Guia do Maestri.

Produz JSON no `formatVersion` 1 do Maestri (appVersion 0.45.x), com a MESMA
estrutura dos arquivos exportados pelo próprio app:

  * chaves de topo: appVersion, color, createdAt, description, formatVersion,
    icon, id, name, workspaceId, payload, roles
  * payload: connections, drawings, nodes, noteConnections, noteTexts,
    noteToNoteConnections, portalConnections, portalToPortalConnections,
    sourceWorkingDirectory, sourceWorkspaceId
  * nós: terminal / stickyNote / portal, cada um embrulhado em `_0`
  * roles: id, name, prompt, color, icon, schemaVersion

Calibrado contra as partituras oficiais em `referencia/partituras-oficiais/`
(KYC BFF Validation, Money Send Pipeline, Ship Goats, Slop Haters,
The Bug is on the Canvas). Regras extraídas delas:

  * `connections` referenciam o id INTERNO do terminal (content.terminal._0.id),
    que é diferente do id do nó.
  * `noteConnections` referenciam o id do NÓ da nota + id interno do terminal.
  * `portalConnections` referenciam o id do NÓ do portal + id interno do terminal.
  * `noteToNoteConnections` usam noteNodeIdA / noteNodeIdB.
  * Toda conexão carrega `ropePoints`: 21 pontos [x, y] de borda a borda dos nós.

UUIDs são DETERMINÍSTICOS (sha1 do seed, em maiúsculas): regerar produz o mesmo
arquivo byte a byte, o que mantém o repositório estável entre execuções.

Sem dependências além da stdlib.
"""

from __future__ import annotations

import hashlib
import math
from typing import Dict, List, Optional, Sequence, Tuple

APP_VERSION = "0.45.6"
FORMAT_VERSION = 1
CREATED_AT = "2026-09-08T12:00:00Z"
ROLE_ICON = "person.text.rectangle"
WORKSPACE_SEED = "ws:guia-do-maestri"

# Paleta oficial (Apple system colors) usada em roles, terminais e destaque.
COLORS: Dict[str, str] = {
    "red": "#FF3B30",
    "pink": "#FF2D55",
    "orange": "#FF9500",
    "yellow": "#FFCC00",
    "green": "#34C759",
    "teal": "#5AC8FA",
    "blue": "#007AFF",
    "indigo": "#5856D6",
    "purple": "#AF52DE",
    "gray": "#8E8E93",
}

# Cores de nota adesiva aceitas pelo app.
NOTE_COLORS: Sequence[str] = (
    "blue", "green", "yellow", "purple", "slate", "orange", "pink", "red", "teal",
)

# Comandos de terminal (política de modelos: fable rege, opus executa,
# codex/gemini revisam de forma adversarial).
CMD_FABLE = "claude --dangerously-skip-permissions --model fable"
CMD_OPUS = "claude --dangerously-skip-permissions --model opus"
CMD_SONNET = "claude --dangerously-skip-permissions --model sonnet"
CMD_CLAUDE = "claude --dangerously-skip-permissions"
CMD_CODEX = "codex"
CMD_GEMINI = "gemini"
CMD_OPENCODE = "opencode"
CMD_SHELL = ""  # terminal shell puro, sem agente

ROPE_POINTS = 21   # como nos arquivos oficiais
ROPE_SAG = 24.0    # "gravidade" no meio do cabo, em pontos do canvas


def det_uuid(seed: str) -> str:
    """UUID determinístico (formato 8-4-4-4-12, maiúsculas) a partir de um seed."""
    h = hashlib.sha1(seed.encode("utf-8")).hexdigest()
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}".upper()


# alias retro-compatível com o gerador de referência
_det_uuid = det_uuid


Frame = Tuple[Tuple[float, float], Tuple[float, float]]


def _center(frame: Frame) -> Tuple[float, float]:
    (x, y), (w, h) = frame
    return (x + w / 2.0, y + h / 2.0)


def edge_anchor(src: Frame, dst: Frame) -> Tuple[float, float]:
    """Ponto médio da borda de `src` voltada para `dst` (é assim que o app
    ancora os cabos: no meio da aresta mais próxima, não no centro do nó)."""
    (x, y), (w, h) = src
    cx, cy = _center(src)
    dx_, dy_ = _center(dst)
    dx, dy = dx_ - cx, dy_ - cy
    # normaliza pela metade do tamanho para decidir qual borda "aponta" melhor
    if abs(dx) / max(w, 1) >= abs(dy) / max(h, 1):
        return (x + w, cy) if dx >= 0 else (x, cy)
    return (cx, y + h) if dy >= 0 else (cx, y)


def rope(a: Tuple[float, float], b: Tuple[float, float],
         n: int = ROPE_POINTS, sag: float = ROPE_SAG) -> List[List[float]]:
    """Curva de rope points entre dois pontos, com leve sag senoidal
    (o cabo "pesa" no meio, como a física do canvas)."""
    (ax, ay), (bx, by) = a, b
    pts: List[List[float]] = []
    for i in range(n):
        t = i / (n - 1)
        x = ax + (bx - ax) * t
        y = ay + (by - ay) * t + math.sin(t * math.pi) * sag
        pts.append([round(x, 6), round(y, 6)])
    pts[0] = [round(float(ax), 6), round(float(ay), 6)]
    pts[-1] = [round(float(bx), 6), round(float(by), 6)]
    return pts


class Partitura:
    """Builder de uma partitura. Coordenadas em pontos do canvas infinito,
    relativas a `origin` (o Maestro costuma ficar em (0, 0))."""

    TERM_W, TERM_H = 860, 600
    NOTE_W, NOTE_H = 520, 300
    PORTAL_W, PORTAL_H = 1200, 760

    def __init__(self, name: str, description: str, icon: str = "sparkles",
                 color: str = COLORS["indigo"], origin: Tuple[int, int] = (9000, 8000),
                 created_at: str = CREATED_AT, app_version: str = APP_VERSION):
        self.name = name
        self.description = description
        self.icon = icon
        self.color = color
        self.ox, self.oy = origin
        self.created_at = created_at
        self.app_version = app_version
        self.pid = det_uuid(f"partitura:{name}")
        self.roles: Dict[str, dict] = {}
        self.nodes: List[dict] = []
        self.note_texts: Dict[str, str] = {}
        self.connections: List[dict] = []
        self.note_connections: List[dict] = []
        self.portal_connections: List[dict] = []
        self.note_to_note: List[dict] = []
        self.portal_to_portal: List[dict] = []
        self._frames: Dict[str, Frame] = {}      # qualquer id (nó ou terminal) -> frame
        self._term_node: Dict[str, str] = {}     # terminal content id -> node id
        self._z = 50

    # ------------------------------------------------------------------ roles
    def role(self, name: str, prompt: str, color: str = COLORS["purple"],
             icon: str = ROLE_ICON) -> str:
        """Registra uma responsabilidade (role). Devolve o id. Vários terminais
        podem compartilhar o mesmo role."""
        rid = det_uuid(f"role:{self.name}:{name}")
        self.roles[name] = {
            "color": color,
            "icon": icon,
            "id": rid,
            "name": name,
            "prompt": prompt.strip(),
            "schemaVersion": 1,
        }
        return rid

    def role_id(self, name: str) -> str:
        return self.roles[name]["id"]

    # -------------------------------------------------------------- terminais
    def terminal(self, name: str, role: Optional[str] = None, x: float = 0, y: float = 0,
                 manager: bool = False, command: str = CMD_OPUS,
                 color: str = COLORS["blue"], icon: str = "seal",
                 agent_type: str = "claude_code", w: Optional[int] = None,
                 h: Optional[int] = None) -> str:
        """Cria um terminal. Devolve o id INTERNO do terminal (o que as
        conexões usam). O id do nó fica em `node_id_of()`."""
        self._z += 1
        tid = det_uuid(f"term:{self.name}:{name}")
        nid = det_uuid(f"termnode:{self.name}:{name}")
        content = {
            "agentType": agent_type,
            "autoScrollLocked": False,
            "color": color,
            "command": command,
            "icon": icon,
            "id": tid,
            "isManager": bool(manager),
            "isUnloaded": False,
            "lastActiveAt": "1970-01-01T00:00:00Z",
            "monitorWithOmbro": True,
            "name": name,
            "scrollbackFile": "",
            "scrollbackLineCount": 0,
            "shellPath": "",
            "shortcutMode": {"kind": "automatic"},
            "status": "restored",
            "workingDirectory": "",
        }
        if role is not None:
            content["assignedRoleId"] = self.role_id(role)
        frame: Frame = ((self.ox + x, self.oy + y), (w or self.TERM_W, h or self.TERM_H))
        self.nodes.append(self._node({"terminal": {"_0": content}}, nid, frame))
        self._frames[tid] = frame
        self._frames[nid] = frame
        self._term_node[tid] = nid
        return tid

    # ------------------------------------------------------------------ notas
    def note(self, filename: str, text: str, x: float = 0, y: float = 0,
             color: str = "blue", w: Optional[int] = None, h: Optional[int] = None,
             font_size: int = 14, previewing: bool = True) -> str:
        """Cria uma nota adesiva (markdown gerenciado pelo app). Devolve o id do nó."""
        if color not in NOTE_COLORS:
            raise ValueError(f"cor de nota inválida: {color!r}")
        self._z += 1
        nid = det_uuid(f"note:{self.name}:{filename}")
        content = {
            "color": color,
            "fileName": filename,
            "fontSize": font_size,
            "hasCustomName": True,
            "isContentLocked": False,
            "isPreviewing": previewing,
            "storageMode": {"managed": {}},
        }
        frame: Frame = ((self.ox + x, self.oy + y), (w or self.NOTE_W, h or self.NOTE_H))
        self.nodes.append(self._node({"stickyNote": {"_0": content}}, nid, frame))
        self._frames[nid] = frame
        self.note_texts[nid] = text.strip() + "\n"
        return nid

    # ---------------------------------------------------------------- portais
    def portal(self, name: str, url: str, x: float = 0, y: float = 0,
               w: Optional[int] = None, h: Optional[int] = None) -> str:
        """Cria um portal de navegador. Devolve o id do NÓ (o que
        `portalConnections` usa)."""
        self._z += 1
        pid = det_uuid(f"portal:{self.name}:{name}")
        nid = det_uuid(f"portalnode:{self.name}:{name}")
        content = {
            "chromeHidden": False,
            "currentURL": url,
            "id": pid,
            "isUnloaded": False,
            "name": name,
            "source": {"url": {"_0": url}},
            "status": "idle",
            "storageScope": "isolated",
            "surface": {"browser": {}},
        }
        frame: Frame = ((self.ox + x, self.oy + y), (w or self.PORTAL_W, h or self.PORTAL_H))
        self.nodes.append(self._node({"portal": {"_0": content}}, nid, frame))
        self._frames[nid] = frame
        self._frames[pid] = frame
        return nid

    # ------------------------------------------------------------ lookups
    def note_node_id(self, filename: str) -> str:
        return det_uuid(f"note:{self.name}:{filename}")

    def portal_node_id(self, name: str) -> str:
        return det_uuid(f"portalnode:{self.name}:{name}")

    def terminal_id(self, name: str) -> str:
        return det_uuid(f"term:{self.name}:{name}")

    def node_id_of(self, terminal_id: str) -> str:
        return self._term_node[terminal_id]

    # ---------------------------------------------------------------- conexões
    def _rope_between(self, a_id: str, b_id: str) -> List[List[float]]:
        fa, fb = self._frames[a_id], self._frames[b_id]
        return rope(edge_anchor(fa, fb), edge_anchor(fb, fa))

    def connect(self, a: str, b: str) -> None:
        """Conecta dois terminais (ids internos de terminal)."""
        self.connections.append({
            "createdAt": self.created_at,
            "id": det_uuid(f"conn:{self.name}:{a}:{b}"),
            "ropePoints": self._rope_between(a, b),
            "terminalIdA": a,
            "terminalIdB": b,
        })

    def connect_note(self, note_node_id: str, terminal_id: str) -> None:
        self.note_connections.append({
            "createdAt": self.created_at,
            "id": det_uuid(f"nconn:{self.name}:{note_node_id}:{terminal_id}"),
            "noteNodeId": note_node_id,
            "ropePoints": self._rope_between(terminal_id, note_node_id),
            "terminalId": terminal_id,
        })

    def connect_portal(self, portal_node_id: str, terminal_id: str) -> None:
        self.portal_connections.append({
            "createdAt": self.created_at,
            "id": det_uuid(f"pconn:{self.name}:{portal_node_id}:{terminal_id}"),
            "portalNodeId": portal_node_id,
            "ropePoints": self._rope_between(terminal_id, portal_node_id),
            "terminalId": terminal_id,
        })

    def chain_notes(self, a_node: str, b_node: str) -> None:
        """Encadeia duas notas (mapa mental que o agente percorre)."""
        self.note_to_note.append({
            "createdAt": self.created_at,
            "id": det_uuid(f"nn:{self.name}:{a_node}:{b_node}"),
            "noteNodeIdA": a_node,
            "noteNodeIdB": b_node,
            "ropePoints": self._rope_between(a_node, b_node),
        })

    def link_portals(self, a_node: str, b_node: str) -> None:
        """Liga dois portais para compartilharem sessão de armazenamento."""
        self.portal_to_portal.append({
            "createdAt": self.created_at,
            "id": det_uuid(f"pp:{self.name}:{a_node}:{b_node}"),
            "portalNodeIdA": a_node,
            "portalNodeIdB": b_node,
            "ropePoints": self._rope_between(a_node, b_node),
        })

    # ------------------------------------------------------------ internos
    def _node(self, content: dict, nid: str, frame: Frame) -> dict:
        (x, y), (w, h) = frame
        return {
            "content": content,
            "createdAt": self.created_at,
            "frame": [[x, y], [w, h]],
            "id": nid,
            "isLocked": False,
            "lastModifiedAt": self.created_at,
            "zIndex": self._z,
        }

    # -------------------------------------------------------------- resumo
    @property
    def counts(self) -> Dict[str, int]:
        out = {"terminal": 0, "stickyNote": 0, "portal": 0}
        for n in self.nodes:
            out[next(iter(n["content"]))] += 1
        return out

    # --------------------------------------------------------- serialização
    def to_dict(self) -> dict:
        ws = det_uuid(WORKSPACE_SEED)
        return {
            "appVersion": self.app_version,
            "color": self.color,
            "createdAt": self.created_at,
            "description": self.description,
            "formatVersion": FORMAT_VERSION,
            "icon": self.icon,
            "id": self.pid,
            "name": self.name,
            "payload": {
                "connections": self.connections,
                "drawings": [],
                "nodes": self.nodes,
                "noteConnections": self.note_connections,
                "noteTexts": self.note_texts,
                "noteToNoteConnections": self.note_to_note,
                "portalConnections": self.portal_connections,
                "portalToPortalConnections": self.portal_to_portal,
                "sourceWorkingDirectory": "",
                "sourceWorkspaceId": ws,
            },
            "roles": list(self.roles.values()),
            "workspaceId": ws,
        }


def pack(partituras: Sequence[dict]) -> dict:
    """Pacote coletivo `.maestripartituras` (mesmo formato do app)."""
    return {"formatVersion": FORMAT_VERSION, "partituras": list(partituras)}


# ------------------------------------------------------------ helpers de layout

def grid_positions(n: int, cols: int = 3, gx: int = 980, gy: int = 760,
                   y0: int = 760) -> List[Tuple[float, float]]:
    """`n` posições (x, y) numa grade centralizada abaixo do Maestro (0, 0)."""
    pos: List[Tuple[float, float]] = []
    for i in range(n):
        r, c = divmod(i, cols)
        row_count = min(cols, n - r * cols)
        offset = -(row_count - 1) * gx / 2.0
        pos.append((offset + c * gx, y0 + r * gy))
    return pos


def hub_layout(p: Partitura, manager_tid: str, worker_tids: Sequence[str],
               note_nodes: Optional[Sequence[str]] = None,
               portal_nodes: Optional[Sequence[str]] = None,
               mesh: bool = True) -> None:
    """Topologia estrela: Maestro ligado a todos os workers, malha leve entre
    vizinhos, notas ligadas a todo mundo e portais ligados ao Maestro."""
    for w in worker_tids:
        p.connect(manager_tid, w)
    if mesh:
        for i in range(len(worker_tids) - 1):
            p.connect(worker_tids[i], worker_tids[i + 1])
    for nn in note_nodes or []:
        p.connect_note(nn, manager_tid)
        for w in worker_tids:
            p.connect_note(nn, w)
    for pn in portal_nodes or []:
        p.connect_portal(pn, manager_tid)


__all__ = [
    "APP_VERSION", "FORMAT_VERSION", "CREATED_AT", "COLORS", "NOTE_COLORS",
    "CMD_FABLE", "CMD_OPUS", "CMD_SONNET", "CMD_CLAUDE", "CMD_CODEX", "CMD_GEMINI",
    "CMD_OPENCODE", "CMD_SHELL", "Partitura", "pack", "grid_positions", "hub_layout",
    "det_uuid", "_det_uuid", "rope", "edge_anchor",
]
