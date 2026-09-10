"""Diagrama 5 — chave low-side com MOSFET-N.

Mesma topologia do diagrama 4 (npn_chave_low_side), mas comandada por
tensao no gate (nao corrente continua de base) + resistor de pull-down
entre gate e GND, garantindo que a chave fique desligada quando o GPIO
estiver em estado indefinido/flutuante (ex.: durante o boot).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 5;
usado no Deck Saida, slide 36.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "mosfet_n_chave_low_side"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.8)

    Q1 = d.add(elm.NMos().label("Q1\n(MOSFET-N)", loc="right"))
    gate_node = d.add(elm.Dot().at(Q1.gate))

    d.add(elm.Resistor().at(gate_node.center).left().length(3.0).label("R_gate", loc="top"))
    d.add(elm.Line().left().length(1.2))
    d.add(elm.SourceV().down().label("GPIO\nHIGH", loc="bottom"))
    d.add(elm.Ground())

    d.add(elm.Resistor().at(gate_node.center).down().length(2.2).label("R_pulldown\n(→ GND)"))
    d.add(elm.Ground())

    d.add(elm.Line().at(Q1.drain).up().length(0.6))
    d.add(elm.Resistor().up().label("Carga\n(ex.: relé)"))
    d.add(elm.Line().up().length(0.4))
    d.add(elm.SourceV().up().label("Fonte externa\n12V", loc="right"))
    d.add(elm.Ground())

    d.add(elm.Line().at(Q1.source).down().length(0.5))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
