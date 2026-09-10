"""Diagrama 6 — chave high-side com transistor PNP.

Logica invertida: GPIO LOW liga a chave. Fica entre a fonte externa e o
lado "alto" da carga (emissor no VCC, coletor alimenta a carga, que
retorna ao GND).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 6;
usado no Deck Saida, slide 37.
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "pnp_chave_high_side"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.8)

    Q1 = d.add(elm.BjtPnp().label("Q1\n(PNP)", loc="right"))

    d.add(elm.Line().at(Q1.emitter).up().length(0.6))
    d.add(elm.SourceV().up().label("VCC\n12V", loc="right"))
    d.add(elm.Ground())

    d.add(elm.Line().at(Q1.collector).down().length(0.6))
    d.add(elm.Resistor().down().label("Carga\n(ex.: relé)"))
    d.add(elm.Line().down().length(0.4))
    d.add(elm.Ground())

    d.add(elm.Resistor().at(Q1.base).left().length(3.0).label("R_base", loc="top"))
    d.add(elm.Line().left().length(1.2))
    d.add(elm.SourceV().down().label("GPIO\nLOW", loc="bottom"))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
