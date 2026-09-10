"""Diagrama 8 — circuito basico de botao, sem microcontrolador.

Fonte generica + resistor + botao. Espelha o diagrama 1 (led_circuito_
basico) do lado da entrada. Usado no Deck Entrada, slide 7 — antes da
ideia de bouncing/pull-up/pull-down ser introduzida.

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 8.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "botao_circuito_basico"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    source = d.add(elm.BatteryCell().up().label("Fonte\n9V", loc="top"))
    d.add(elm.Resistor().right().label("R"))
    d.add(elm.Switch().right().label("Botão", loc="bottom"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(source.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
