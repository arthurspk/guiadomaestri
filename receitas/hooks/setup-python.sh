#!/usr/bin/env bash
# Hook de Setup de andar (Floor) — projetos Python.
# Cole em ⚡ → Setup no andar.
set -euo pipefail
cd "$MAESTRI_FLOOR_PATH"

# ambiente virtual isolado por andar
python3 -m venv ".venv-$MAESTRI_FLOOR_NAME"
# shellcheck disable=SC1090
source ".venv-$MAESTRI_FLOOR_NAME/bin/activate"

if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then pip install -e . 2>/dev/null || true; fi

# exemplo: sobe um servidor de dev em background
# (uvicorn app:app --reload) > "/tmp/dev-$MAESTRI_FLOOR_NAME.log" 2>&1 &

echo "Andar Python '$MAESTRI_FLOOR_NAME' pronto (venv .venv-$MAESTRI_FLOOR_NAME)."
