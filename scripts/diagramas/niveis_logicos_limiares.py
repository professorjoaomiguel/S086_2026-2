"""Diagrama 13 — faixas de niveis logicos: ATmega328P (5V) vs ESP32-S3 (3,3V).

Duas retas de tensao (0 -> VCC) lado a lado, cada uma com as zonas
LOW / indefinida / HIGH marcadas pelos limiares V_IL/V_IH do datasheet de
cada chip. Valores calculados a partir das formulas do datasheet
(V_IL=0,3xVCC / V_IH=0,6xVCC no ATmega328P; V_IL=0,25xVDD / V_IH=0,75xVDD
no ESP32-S3) — conferir contra a edicao exata do datasheet usada no guia
tecnico antes de publicar.

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 13;
usado no Deck Entrada, slide 19.
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "niveis_logicos_limiares"

chips = [
    {
        "nome": "ATmega328P\n(Arduino UNO R3)",
        "vcc": 5.0,
        "vil": 1.5,
        "vih": 3.0,
        "formula": "V_IL ≤ 0,3×VCC\nV_IH ≥ 0,6×VCC",
    },
    {
        "nome": "ESP32-S3\n(ESP32-S3-UNO)",
        "vcc": 3.3,
        "vil": 0.825,
        "vih": 2.475,
        "formula": "V_IL ≤ 0,25×VDD\nV_IH ≥ 0,75×VDD",
    },
]

fig, axes = plt.subplots(1, 2, figsize=(7, 6), sharey=False)

for ax, chip in zip(axes, chips):
    vcc = chip["vcc"]
    vil = chip["vil"]
    vih = chip["vih"]

    ax.axhspan(0, vil, color="#f0f0f0")
    ax.axhspan(vil, vih, color="#bbbbbb")
    ax.axhspan(vih, vcc, color="#f0f0f0")

    ax.axhline(vil, color="black", linewidth=1)
    ax.axhline(vih, color="black", linewidth=1)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, vcc * 1.15)
    ax.set_xticks([])
    ax.set_yticks([0, vil, vih, vcc])
    ax.set_yticklabels([f"0V", f"V_IL={vil:g}V", f"V_IH={vih:g}V", f"VCC={vcc:g}V"])

    ax.text(0.5, vil / 2, f"LOW: 0 – {vil:g}V", ha="center", va="center")
    ax.text(0.5, (vil + vih) / 2, "indefinida", ha="center", va="center", fontsize=8)
    ax.text(0.5, vih + (vcc - vih) / 2, f"HIGH: {vih:g} – {vcc:g}V", ha="center", va="center")

    ax.set_title(chip["nome"], fontsize=11)
    ax.text(0.5, -vcc * 0.12, chip["formula"], ha="center", va="top", fontsize=8, color="gray")

fig.suptitle("Níveis lógicos de entrada — limiares V_IL / V_IH", fontsize=13)
fig.tight_layout(rect=(0, 0.03, 1, 0.95))
fig.savefig(str(OUT_DIR / f"{NAME}.svg"))
fig.savefig(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
