#!/usr/bin/env python3
"""
validate_partituras.py — Valida cada .maestripartitura gerado contra o formato oficial.

Referência: o **schema embutido** do formato `.maestripartitura` (formatVersion 1) do
Maestri, definido nas constantes abaixo. Não depende de nenhum arquivo de exemplo.

Checagens (zero divergências permitidas):
  1. json.load carrega todo arquivo.
  2. Chaves de TOPO batem EXATAMENTE com o schema.
  3. Chaves de PAYLOAD batem EXATAMENTE com o schema.
  4. Cada nó tem content/frame/id/zIndex (e createdAt/isLocked/lastModifiedAt).
     As chaves de _0 de cada tipo (terminal/stickyNote/portal) batem com o schema
     (com as chaves opcionais conhecidas: terminal.assignedRoleId, portal.currentURL).
  5. Cada role tem id/name/prompt/color/icon + schemaVersion.
  6. Integridade referencial: connections/noteConnections/portalConnections/noteToNote
     apontam para ids que existem; toda conexão tem 21 ropePoints.
  7. Os pacotes coletivos (por área + o mestre) somam corretamente.

Uso: python3 tests/validate_partituras.py  (sai com código != 0 se algo falhar).
"""

import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PART = os.path.join(ROOT, "partituras")

# --- Schema embutido do formato .maestripartitura (formatVersion 1) ---
TOP = {"appVersion", "color", "createdAt", "description", "formatVersion", "icon",
       "id", "name", "payload", "roles", "workspaceId"}
PAYLOAD = {"connections", "drawings", "nodes", "noteConnections", "noteTexts",
           "noteToNoteConnections", "portalConnections", "portalToPortalConnections",
           "sourceWorkingDirectory", "sourceWorkspaceId"}
NODE = {"content", "createdAt", "frame", "id", "isLocked", "lastModifiedAt", "zIndex"}
ROLE = {"color", "icon", "id", "name", "prompt", "schemaVersion"}
# kind -> (chaves obrigatórias, chaves opcionais) de content.<kind>._0
INNER = {
    "terminal": (
        {"agentType", "autoScrollLocked", "color", "command", "icon", "id", "isManager",
         "isUnloaded", "lastActiveAt", "monitorWithOmbro", "name", "scrollbackFile",
         "scrollbackLineCount", "shellPath", "shortcutMode", "status", "workingDirectory"},
        {"assignedRoleId"},
    ),
    "stickyNote": (
        {"color", "fileName", "fontSize", "hasCustomName", "isContentLocked",
         "isPreviewing", "storageMode"},
        set(),
    ),
    "portal": (
        {"chromeHidden", "id", "isUnloaded", "name", "source", "status",
         "storageScope", "surface"},
        {"currentURL"},
    ),
}


def _node_kind(node):
    return next(iter(node["content"]))


def main():
    files = sorted(glob.glob(os.path.join(PART, "*", "*.maestripartitura")))
    if not files:
        print("FALHA: nenhum .maestripartitura encontrado — rode o gerador primeiro.")
        return 1

    errors = []
    total_nodes = 0
    for path in files:
        name = os.path.basename(path)
        try:
            d = json.load(open(path, encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: json.load falhou: {e}")
            continue

        if set(d) != TOP:
            errors.append(f"{name}: chaves de topo divergem: "
                          f"faltam {TOP - set(d)}, sobram {set(d) - TOP}")
        p = d.get("payload", {})
        if set(p) != PAYLOAD:
            errors.append(f"{name}: chaves de payload divergem: "
                          f"faltam {PAYLOAD - set(p)}, sobram {set(p) - PAYLOAD}")

        # Nós
        node_ids = set()
        term_ids = set()
        portal_node_ids = set()
        for n in p.get("nodes", []):
            total_nodes += 1
            if set(n) != NODE:
                errors.append(f"{name}: nó com chaves divergentes: {set(n) ^ NODE}")
            node_ids.add(n["id"])
            kind = _node_kind(n)
            inner = set(n["content"][kind]["_0"].keys())
            if kind in INNER:
                req, opt = INNER[kind]
                if not (req <= inner <= (req | opt)):
                    errors.append(f"{name}: {kind}._0 chaves divergem: "
                                  f"faltam {req - inner}, sobram {inner - (req | opt)}")
            if kind == "terminal":
                term_ids.add(n["content"][kind]["_0"]["id"])
            elif kind == "portal":
                portal_node_ids.add(n["id"])

        # Roles
        for r in d.get("roles", []):
            if set(r) != ROLE:
                errors.append(f"{name}: role com chaves divergentes: {set(r) ^ ROLE}")
            if not str(r.get("prompt", "")).strip():
                errors.append(f"{name}: role '{r.get('name')}' com prompt vazio")

        # Integridade referencial + ropePoints
        for c in p.get("connections", []):
            if c["terminalIdA"] not in term_ids or c["terminalIdB"] not in term_ids:
                errors.append(f"{name}: connection aponta para terminal inexistente")
            if len(c.get("ropePoints", [])) != 21:
                errors.append(f"{name}: connection sem 21 ropePoints")
        for c in p.get("noteConnections", []):
            if c["terminalId"] not in term_ids or c["noteNodeId"] not in node_ids:
                errors.append(f"{name}: noteConnection aponta para id inexistente")
        for c in p.get("portalConnections", []):
            if c["terminalId"] not in term_ids or c["portalNodeId"] not in portal_node_ids:
                errors.append(f"{name}: portalConnection aponta para id inexistente")
        for c in p.get("noteToNoteConnections", []):
            if c["noteNodeIdA"] not in node_ids or c["noteNodeIdB"] not in node_ids:
                errors.append(f"{name}: noteToNoteConnection aponta para id inexistente")

    # Pacotes coletivos: um por área + o mestre. Cada um soma as partituras da pasta.
    packs = sorted(glob.glob(os.path.join(PART, "*", "*.maestripartituras")))
    packs.append(os.path.join(PART, "Guia-do-Maestri.maestripartituras"))
    if len(packs) < 2:
        errors.append("nenhum pacote .maestripartituras por área encontrado")
    total_in_area_packs = 0
    for pkpath in packs:
        if not os.path.exists(pkpath):
            errors.append(f"pacote ausente: {os.path.basename(pkpath)}")
            continue
        pk = json.load(open(pkpath, encoding="utf-8"))
        if set(pk) != {"formatVersion", "partituras"}:
            errors.append(f"{os.path.basename(pkpath)}: chaves de pacote erradas: {set(pk)}")
            continue
        is_master = os.path.dirname(pkpath) == PART
        n = len(pk["partituras"])
        if is_master:
            if n != len(files):
                errors.append(f"pacote mestre tem {n} partituras, esperado {len(files)}")
        else:
            area_dir = os.path.dirname(pkpath)
            area_files = glob.glob(os.path.join(area_dir, "*.maestripartitura"))
            total_in_area_packs += n
            if n != len(area_files):
                errors.append(f"{os.path.basename(pkpath)}: {n} partituras, esperado {len(area_files)}")
    if total_in_area_packs != len(files):
        errors.append(f"soma dos pacotes de área ({total_in_area_packs}) != total ({len(files)})")

    if errors:
        print(f"FALHA: {len(errors)} divergência(s):")
        for e in errors[:60]:
            print("  -", e)
        return 1

    print(f"OK: {len(files)} partituras validadas contra o schema do formato "
          f"({total_nodes} nós no total). Zero divergências.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
