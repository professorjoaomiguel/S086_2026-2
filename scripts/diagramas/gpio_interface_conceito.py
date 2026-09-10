"""Diagrama 14 — GPIO como interface eletrica (bloco conceitual).

MICROCONTROLADOR/GPIO no centro; seta para SAIDA (LED) — o microcontrolador
poe uma tensao no mundo; seta vinda de ENTRADA (botao) — o microcontrolador
le uma tensao que vem do mundo. E a mesma fronteira eletrica em dois
sentidos, nao duas APIs desconectadas (tese que conecta os dois decks).

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 14;
usado no Deck Saida, slide 7 (frame final) e Deck Entrada, slide 6
(retomada, slide unico).
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "gpio_interface_conceito"

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    d.add(elm.Rect(corner1=(0, 0), corner2=(4.5, 2.2)))
    d.add(elm.Label().at((2.25, 1.1)).label("MICROCONTROLADOR\n(GPIO)", loc="center"))

    d.add(elm.Arrow().at((4.5, 1.5)).right().length(2.2).label("SAÍDA\n(LED)\npõe tensão", loc="top"))
    d.add(elm.Arrow().at((-2.2, 0.7)).right().length(2.2).label("ENTRADA\n(botão)\nlê tensão", loc="bottom"))

    d.save(str(OUT_DIR / f"{NAME}.svg"))
    d.save(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
