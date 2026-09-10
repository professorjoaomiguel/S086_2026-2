"""Diagrama 2 — LED ativo-alto (GPIO fornece corrente / source).

Anodo no GPIO, catodo -> resistor -> GND. HIGH acende. Numeros do exemplo
UNO (5V) do slide 27: LED vermelho ROHM SML-D12U8W (V_F=2,2V @20mA),
I=10mA planejado, R comercial 330 Ohm.

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 2;
usado no Deck Saida, slide 23.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "led_ativo_alto"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    gpio = d.add(elm.SourceV().up().label("GPIO\nHIGH (5V)", loc="top"))
    d.add(elm.LED().right().label("LED vermelho\nV_F ≈ 2,2V", loc="top"))
    d.add(elm.Resistor().right().label("R = 330 Ω\nI ≈ 10mA", loc="top"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(gpio.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground().label("GND", loc="bottom"))

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
