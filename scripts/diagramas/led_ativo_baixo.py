"""Diagrama 3 — LED ativo-baixo (GPIO absorve corrente / sink).

Anodo -> resistor -> VCC; catodo no GPIO. LOW acende. Mesmos numeros do
exemplo UNO (5V) usado no diagrama 2 (led_ativo_alto), para deixar o
contraste ativo-alto vs ativo-baixo direto (mesmo LED, mesmo R, so a
topologia muda: aqui a fonte fixa (VCC) fica no lugar do GPIO, e o GPIO
vira o retorno/sumidouro no lugar do GND).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 3;
usado no Deck Saida, slide 24.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "led_ativo_baixo"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    vcc = d.add(elm.SourceV().up().label("VCC\n(5V)", loc="top"))
    d.add(elm.Resistor().right().label("R = 330 Ω\nI ≈ 10mA", loc="top"))
    d.add(elm.LED().right().label("LED vermelho\nV_F ≈ 2,2V", loc="top"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(vcc.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground().label("GPIO\nLOW (0V)", loc="bottom"))

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
