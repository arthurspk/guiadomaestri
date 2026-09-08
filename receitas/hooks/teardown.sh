#!/usr/bin/env bash
# Hook de Teardown de andar (Floor) — limpa ao apagar o andar.
# Cole em ⚡ → Teardown no andar. Derruba processos e apaga logs temporários.
set -uo pipefail

# derruba o dev server desse andar (best-effort)
pkill -f "$MAESTRI_FLOOR_PATH" 2>/dev/null || true

# limpa logs temporários do andar
rm -f "/tmp/dev-$MAESTRI_FLOOR_NAME.log" "/tmp/test-$MAESTRI_FLOOR_NAME.log" 2>/dev/null || true

echo "Andar '$MAESTRI_FLOOR_NAME' limpo."
