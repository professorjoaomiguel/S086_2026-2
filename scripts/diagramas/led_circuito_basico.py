"""Diagrama 1 — circuito basico de LED, sem microcontrolador.

Fonte generica (pilha) + resistor + LED. Usado no Deck Saida, slide 12 —
antes de qualquer numero de V_F ser revelado, entao R e o LED ficam so com
o rotulo do componente (o calculo entra so a partir do slide 18).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 1.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "led_circuito_basico"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    source = d.add(elm.BatteryCell().up().label("Fonte\n9V", loc="top"))
    d.add(elm.Resistor().right().label("R\n(a calcular)"))
    d.add(elm.LED().right().label("LED\n(V_F a determinar)", loc="bottom"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(source.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
