#!/usr/bin/env python3
"""
validate_hub.py — Valida os recursos do hub gerados por scripts/generate_hub.py.

Checagens:
  1. Cada roles/**/*.role.json carrega com json.load e tem
     name/prompt/color/icon/id/schemaVersion, com prompt não vazio e cor em hex.
  2. Existe roles/CATALOGO.md e cada arquivo linkado existe.
  3. notas/ tem os .md esperados (não vazios) e um README.
  4. instrucoes/ tem, por pasta, CLAUDE.md e AGENTS.md idênticos e não vazios, e um README.

Sai com código != 0 se algo falhar.
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    errors = []

    # 1) role.json
    roles = sorted(glob.glob(os.path.join(ROOT, "roles", "*", "*.role.json")))
    if not roles:
        errors.append("nenhum role.json encontrado — rode scripts/generate_hub.py")
    hexre = re.compile(r"^#[0-9A-Fa-f]{6}$")
    for path in roles:
        try:
            d = json.load(open(path, encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{os.path.relpath(path, ROOT)}: json inválido: {e}")
            continue
        for k in ("schemaVersion", "id", "name", "prompt", "color", "icon"):
            if k not in d:
                errors.append(f"{os.path.relpath(path, ROOT)}: falta '{k}'")
        if not str(d.get("prompt", "")).strip():
            errors.append(f"{os.path.relpath(path, ROOT)}: prompt vazio")
        if not hexre.match(str(d.get("color", ""))):
            errors.append(f"{os.path.relpath(path, ROOT)}: cor não-hex: {d.get('color')}")

    # 2) CATALOGO
    cat = os.path.join(ROOT, "roles", "CATALOGO.md")
    if not os.path.exists(cat):
        errors.append("roles/CATALOGO.md ausente")
    else:
        txt = open(cat, encoding="utf-8").read()
        for m in re.finditer(r"\]\((\./[^)]+\.role\.json)\)", txt):
            p = os.path.normpath(os.path.join(ROOT, "roles", m.group(1)))
            if not os.path.exists(p):
                errors.append(f"CATALOGO aponta para arquivo inexistente: {m.group(1)}")

    # 3) notas
    notas = glob.glob(os.path.join(ROOT, "notas", "*.md"))
    if not any(os.path.basename(n) == "README.md" for n in notas):
        errors.append("notas/README.md ausente")
    if len([n for n in notas if os.path.basename(n) != "README.md"]) < 5:
        errors.append("notas/ tem poucos templates")
    for n in notas:
        if os.path.getsize(n) == 0:
            errors.append(f"nota vazia: {os.path.relpath(n, ROOT)}")

    # 4) instrucoes
    instr_dirs = [d for d in glob.glob(os.path.join(ROOT, "instrucoes", "*"))
                  if os.path.isdir(d)]
    if not instr_dirs:
        errors.append("instrucoes/ sem pastas")
    for d in instr_dirs:
        c = os.path.join(d, "CLAUDE.md")
        a = os.path.join(d, "AGENTS.md")
        if not os.path.exists(c) or not os.path.exists(a):
            errors.append(f"{os.path.basename(d)}: falta CLAUDE.md ou AGENTS.md")
            continue
        if open(c, encoding="utf-8").read() != open(a, encoding="utf-8").read():
            errors.append(f"{os.path.basename(d)}: CLAUDE.md e AGENTS.md divergem")
    if not os.path.exists(os.path.join(ROOT, "instrucoes", "README.md")):
        errors.append("instrucoes/README.md ausente")

    if errors:
        print(f"FALHA: {len(errors)} problema(s):")
        for e in errors[:60]:
            print("  -", e)
        return 1
    print(f"OK: {len(roles)} roles, {len([n for n in notas if os.path.basename(n)!='README.md'])} "
          f"notas, {len(instr_dirs)} conjuntos de instruções. Zero problemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
