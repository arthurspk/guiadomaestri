#!/usr/bin/env python3
"""
validate_partituras.py — Valida cada .maestripartitura gerado contra o formato oficial.

Referência: referencia/partituras-oficiais/Money_Send_Pipeline.maestripartitura.

Checagens (zero divergências permitidas):
  1. json.load carrega todo arquivo.
  2. Chaves de TOPO batem EXATAMENTE com a referência.
  3. Chaves de PAYLOAD batem EXATAMENTE com a referência.
  4. Cada nó tem content/frame/id/zIndex (e createdAt/isLocked/lastModifiedAt).
     As chaves de _0 de cada tipo (terminal/stickyNote/portal) batem com a referência.
  5. Cada role tem id/name/prompt/color/icon (e schemaVersion).
  6. Integridade referencial: connections/noteConnections/portalConnections/noteToNote
     apontam para ids que existem; toda conexão tem 21 ropePoints.
  7. O pacote coletivo Tecnologia.maestripartituras tem formatVersion + partituras.

Uso: python3 tests/validate_partituras.py  (sai com código != 0 se algo falhar).
"""

import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "partituras", "tecnologia")
REF = os.path.join(ROOT, "referencia", "partituras-oficiais", "Money_Send_Pipeline.maestripartitura")


def _node_kind(node):
    return next(iter(node["content"]))


def main():
    ref = json.load(open(REF, encoding="utf-8"))
    ref_top = set(ref)
    ref_payload = set(ref["payload"])
    ref_role = set(ref["roles"][0])
    ref_node = set(next(iter(ref["payload"]["nodes"])).keys())
    ref_inner = {}  # kind -> set de chaves do _0
    for n in ref["payload"]["nodes"]:
        ref_inner.setdefault(_node_kind(n), set(n["content"][_node_kind(n)]["_0"].keys()))

    files = sorted(glob.glob(os.path.join(OUT, "*.maestripartitura")))
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

        if set(d) != ref_top:
            errors.append(f"{name}: chaves de topo divergem: "
                          f"faltam {ref_top - set(d)}, sobram {set(d) - ref_top}")
        p = d.get("payload", {})
        if set(p) != ref_payload:
            errors.append(f"{name}: chaves de payload divergem: "
                          f"faltam {ref_payload - set(p)}, sobram {set(p) - ref_payload}")

        # Nós
        node_ids = set()
        term_ids = set()
        portal_node_ids = set()
        for n in p.get("nodes", []):
            total_nodes += 1
            if set(n) != ref_node:
                errors.append(f"{name}: nó com chaves divergentes: {set(n) ^ ref_node}")
            for req in ("content", "frame", "id", "zIndex"):
                if req not in n:
                    errors.append(f"{name}: nó sem '{req}'")
            node_ids.add(n["id"])
            kind = _node_kind(n)
            inner = n["content"][kind]["_0"]
            if kind in ref_inner and set(inner) != ref_inner[kind]:
                errors.append(f"{name}: {kind}._0 chaves divergem: {set(inner) ^ ref_inner[kind]}")
            if kind == "terminal":
                term_ids.add(inner["id"])
            elif kind == "portal":
                portal_node_ids.add(n["id"])

        # Roles
        for r in d.get("roles", []):
            if not {"id", "name", "prompt", "color", "icon"} <= set(r):
                errors.append(f"{name}: role sem chave obrigatória: {r.get('name')}")
            if set(r) != ref_role:
                errors.append(f"{name}: role com chaves divergentes: {set(r) ^ ref_role}")
            if not r.get("prompt", "").strip():
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

    # Pacote coletivo
    packpath = os.path.join(OUT, "Tecnologia.maestripartituras")
    if not os.path.exists(packpath):
        errors.append("Tecnologia.maestripartituras não existe")
    else:
        pk = json.load(open(packpath, encoding="utf-8"))
        if set(pk) != {"formatVersion", "partituras"}:
            errors.append(f"pacote coletivo com chaves erradas: {set(pk)}")
        elif len(pk["partituras"]) != len(files):
            errors.append(f"pacote tem {len(pk['partituras'])} partituras, esperado {len(files)}")

    if errors:
        print(f"FALHA: {len(errors)} divergência(s):")
        for e in errors[:60]:
            print("  -", e)
        return 1

    print(f"OK: {len(files)} partituras validadas contra {os.path.basename(REF)} "
          f"({total_nodes} nós no total). Zero divergências.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
