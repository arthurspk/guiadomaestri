#!/usr/bin/env bash
# Hook de Setup de andar (Floor) — projetos Node/JS.
# Cole em ⚡ → Setup no andar. Roda ao criar o andar; sobe o dev server em background.
set -euo pipefail
cd "$MAESTRI_FLOOR_PATH"

# instala dependências de forma reprodutível
if [ -f package-lock.json ]; then npm ci; else npm install; fi

# sobe o app de dev em background, com log por andar (o Maestro é dono do runtime)
npm run dev > "/tmp/dev-$MAESTRI_FLOOR_NAME.log" 2>&1 &

echo "Andar '$MAESTRI_FLOOR_NAME' (branch $MAESTRI_BRANCH_NAME) pronto."
echo "Dev subindo; log em /tmp/dev-$MAESTRI_FLOOR_NAME.log"
