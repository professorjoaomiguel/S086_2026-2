"""Diagrama 7 — chave high-side com MOSFET-P.

Mesma logica invertida do diagrama 6 (pnp_chave_high_side), mas comandada
por tensao no gate + resistor de pull-up ao VCC no gate, garantindo que a
chave fique desligada em estado indefinido/flutuante (ex.: durante o
boot) — mesma funcao de seguranca que o pull-down cumpre no MOSFET-N
(diagrama 5).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 7;
usado no Deck Saida, slide 38.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "mosfet_p_chave_high_side"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.8)

    Q1 = d.add(elm.PMos().label("Q1\n(MOSFET-P)", loc="right"))

    d.add(elm.Line().at(Q1.source).up().length(0.6))
    d.add(elm.SourceV().up().label("VCC\n12V", loc="right"))
    d.add(elm.Ground())

    d.add(elm.Line().at(Q1.drain).down().length(0.6))
    d.add(elm.Resistor().down().label("Carga\n(ex.: relé)"))
    d.add(elm.Line().down().length(0.4))
    d.add(elm.Ground())

    gate_node = d.add(elm.Dot().at(Q1.gate))
    d.add(elm.Resistor().at(gate_node.center).left().length(3.0).label("R_gate", loc="top"))
    d.add(elm.Line().left().length(1.2))
    d.add(elm.SourceV().down().label("GPIO\nLOW", loc="bottom"))
    d.add(elm.Ground())

    d.add(elm.Resistor().at(gate_node.center).up().length(1.8).label("R_pullup\n(→ VCC)", loc="bottom"))
    d.add(elm.Dot().label("VCC", loc="top"))

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
