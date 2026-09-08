#!/usr/bin/env bash
# Hook de Run de andar (Floor) — roda a suíte sob demanda.
# Cole em ⚡ → Run no andar. Use quando quiser rodar testes no andar isolado.
set -euo pipefail
cd "$MAESTRI_FLOOR_PATH"

echo "== Testes no andar '$MAESTRI_FLOOR_NAME' (branch $MAESTRI_BRANCH_NAME) =="
# ajuste ao seu projeto:
npm test 2>&1 | tee "/tmp/test-$MAESTRI_FLOOR_NAME.log"
