"""Diagrama 12 — pull-down externo (entrada ativo-alta).

Resistor externo entre GND e o pino; botao para VCC. Anota a tensao no
pino nos dois estados: solto (idle, pino≈0V via pull-down) e pressionado
(botao leva o pino ao VCC) — entrada ativo-alta porque o estado "ativo"
(botao pressionado) corresponde a nivel logico alto no pino. Espelho do
diagrama 11 (gpio_pullup).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 12;
usado no Deck Entrada, slide 27.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "gpio_pulldown"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    vcc_dot = d.add(elm.Dot().label("VCC", loc="top"))
    d.add(elm.Switch().at(vcc_dot.center).down().label("Botão", loc="top"))
    d.add(elm.Line().down().length(0.4))
    pin = d.add(elm.Dot().label("GPIO (pino)\nsolto: ≈0V\npressionado: ≈VCC", loc="right"))
    d.add(elm.Resistor().at(pin.center).down().label("R_pulldown\n(externo)"))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
