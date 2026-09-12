"""Diagrama 15 — botao NA (normalmente aberto) vs NF (normalmente fechado).

Dois circuitos lado a lado (fonte+resistor genericos identicos), so o tipo
de contato muda — para contrastar a corrente de repouso: NA nao conduz em
repouso (I≈0), NF conduz continuamente em repouso (I≈V/R).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 15;
usado no Deck Entrada, slide 9.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "botao_na_nf"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    # Circuito NA (esquerda)
    src_na = d.add(elm.BatteryCell().at((0, 0)).up().label("9V", loc="top"))
    d.add(elm.Resistor().right().label("R"))
    d.add(elm.Switch().right().label("NA\naberto em repouso\nI ≈ 0", loc="bottom"))
    d.add(elm.Line().down().length(3.2))
    d.add(elm.Line().left().tox(src_na.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    # Circuito NF (direita)
    src_nf = d.add(elm.BatteryCell().at((6.5, 0)).up().label("9V", loc="top"))
    d.add(elm.Resistor().right().label("R"))
    d.add(elm.Switch(nc=True).right().label("NF\nfechado em repouso\nI ≈ V/R", loc="bottom"))
    d.add(elm.Line().down().length(3.2))
    d.add(elm.Line().left().tox(src_nf.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
