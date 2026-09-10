"""Diagrama 4 — chave low-side com transistor NPN.

GPIO -> R_base -> base (corrente de base continua liga a chave); coletor
liga o lado "baixo" da carga; emissor no GND comum (mesmo GND do GPIO e da
fonte externa da carga — ponto pedagogico: os tres GNDs precisam ser o
mesmo no).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 4;
usado no Deck Saida, slide 35.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "npn_chave_low_side"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.8)

    Q1 = d.add(elm.BjtNpn().label("Q1\n(NPN)", loc="bottom"))

    d.add(elm.Resistor().at(Q1.base).left().label("R_base", loc="top"))
    d.add(elm.SourceV().down().label("GPIO\nHIGH", loc="bottom"))
    d.add(elm.Ground())

    d.add(elm.Line().at(Q1.collector).up().length(0.6))
    d.add(elm.Resistor().up().label("Carga\n(ex.: relé)"))
    d.add(elm.Line().up().length(0.4))
    d.add(elm.SourceV().up().label("Fonte externa\n12V", loc="right"))
    d.add(elm.Ground())

    d.add(elm.Line().at(Q1.emitter).down().length(0.5))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
