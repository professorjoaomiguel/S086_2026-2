"""Diagrama 11 — pull-up externo (entrada ativo-baixa).

Resistor externo entre VCC e o pino; botao para GND. Anota a tensao no
pino nos dois estados: solto (idle, pino≈VCC via pull-up) e pressionado
(botao aterra o pino, pino≈0V) — entrada ativo-baixa porque o estado
"ativo" (botao pressionado) corresponde a nivel logico baixo no pino.

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 11;
usado no Deck Entrada, slide 25.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "gpio_pullup"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    vcc_dot = d.add(elm.Dot().label("VCC", loc="top"))
    d.add(elm.Resistor().at(vcc_dot.center).down().label("R_pullup\n(externo)"))
    pin = d.add(elm.Dot().label("GPIO (pino)\nsolto: ≈VCC\npressionado: ≈0V", loc="right"))
    d.add(elm.Switch().at(pin.center).down().label("Botão", loc="left"))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
