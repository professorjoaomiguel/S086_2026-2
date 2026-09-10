"""Diagrama 10 — pino flutuante (sem resistor de referencia).

Mesmo eixo/escala do diagrama 9 (botao_forma_onda_bounce), mas SEM
resistor de pull-up/pull-down: sem um caminho definido para VCC ou GND, o
pino capta ruido eletromagnetico ambiente e fica lendo transicoes
aleatorias continuas — nao um bounce mecanico de poucos ms, um ruido sem
fim enquanto o pino permanecer desconectado.

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 10;
usado no Deck Entrada, slides 14 e 23.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "botao_forma_onda_flutuante"

VCC = 5.0
V_IH = 0.7 * VCC
V_IL = 0.3 * VCC

rng = np.random.default_rng(42)

n = 400
t = np.linspace(0, 28, n)
# ruido de alta frequencia em torno do meio da faixa, com alguns picos
# batendo perto dos trilhos — pino sem referencia nao "escolhe" um lado
noise = rng.normal(loc=VCC / 2, scale=1.6, size=n)
noise = np.clip(noise, -0.3, VCC + 0.3)
# suaviza um pouco para parecer transicao de comparador, nao serrilhado puro
kernel = np.ones(5) / 5
v = np.convolve(noise, kernel, mode="same")

fig, ax = plt.subplots(figsize=(9, 4))

ax.axhspan(V_IL, V_IH, color="#dddddd", zorder=0)
ax.axhline(V_IH, color="gray", linestyle="--", linewidth=1)
ax.axhline(V_IL, color="gray", linestyle="--", linewidth=1)

ax.plot(t, v, color="black", linewidth=1.3)

ax.set_ylim(-0.5, VCC + 1.0)
ax.set_xlim(0, t[-1] * 1.1)
ax.set_yticks([0, V_IL, V_IH, VCC])
ax.set_yticklabels(["0V\n(LOW)", "V_IL", "V_IH", f"{VCC:.0f}V\n(HIGH)"])
ax.set_xlabel("tempo (ms, escala ilustrativa)")
ax.set_ylabel("tensão no pino")
ax.set_title("Pino flutuante — sem resistor de referência")

ax.text(t[-1] * 1.01, (V_IL + V_IH) / 2, "zona\nindefinida", ha="left", va="center", fontsize=8, color="gray")
ax.text(1, VCC + 0.5, "sem resistor: ruído contínuo, sem nível estável", ha="left")

fig.tight_layout()
fig.savefig(str(OUT_DIR / f"{NAME}.svg"))
fig.savefig(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
