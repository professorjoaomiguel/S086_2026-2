#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

marp --theme-set=slides/theme/s086.css --allow-local-files --pdf \
  slides/gpio_saida_leds.md -o slides/build/gpio_saida_leds.pdf

marp --theme-set=slides/theme/s086.css --allow-local-files --pdf \
  slides/gpio_entrada_botoes.md -o slides/build/gpio_entrada_botoes.pdf

echo "Build concluido:"
echo "  slides/build/gpio_saida_leds.pdf"
echo "  slides/build/gpio_entrada_botoes.pdf"
