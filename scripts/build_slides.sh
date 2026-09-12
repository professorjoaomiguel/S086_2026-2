#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# Aceita uma lista opcional de arquivos .md como argumentos; sem
# argumentos, usa os dois decks atuais (comportamento de sempre).
DECKS=("$@")
if [ ${#DECKS[@]} -eq 0 ]; then
  DECKS=(slides/gpio_saida_leds.md slides/gpio_entrada_botoes.md)
fi

echo "Build concluido:"
for deck in "${DECKS[@]}"; do
  base="$(basename "$deck" .md)"
  out="slides/build/${base}.pdf"
  marp --theme-set=slides/theme/s086.css --allow-local-files --pdf \
    "$deck" -o "$out"
  echo "  $out"
done
