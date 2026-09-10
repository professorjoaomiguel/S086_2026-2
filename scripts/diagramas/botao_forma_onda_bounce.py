"""Diagrama 9 — forma de onda do bounce mecanico do botao.

Tensao x tempo com resistor de referencia (pull-up/pull-down) presente:
idle -> pressiona (bounce) -> segura -> solta (bounce) -> idle. O bounce e
o "chacoalhar" mecanico dos contatos por poucos milissegundos apos cada
transicao — nao um ruido continuo (contraste com o diagrama 10,
botao_forma_onda_flutuante, que mostra o pino sem resistor nenhum).

Eixo de tensao anotado com HIGH / zona indefinida / LOW, convencao geral
dos diagramas do storyboard.

Storyboard: slides/storyboard_gpio.md, tabela de diagramas, linha 9;
usado no Deck Entrada, slide 13.
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "images"
OUT_DIR.mkdir(exist_ok=True)
NAME = "botao_forma_onda_bounce"

VCC = 5.0
V_IH = 0.7 * VCC
V_IL = 0.3 * VCC


def bounce_segment(t0, start_v, settle_v, deltas=(0.3, 0.15, 0.2, 0.1, 0.25)):
    """Gera pontos (t, v) de um trecho de bounce que comeca em start_v,
    chacoalha entre os dois niveis e termina (settle) em settle_v."""
    ts = [t0]
    vs = [start_v]
    t = t0
    level = start_v
    other = settle_v if start_v != settle_v else start_v
    other = VCC if start_v == 0.0 else 0.0
    for i, dt in enumerate(deltas):
        t += dt
        level = other if i % 2 == 0 else start_v
        ts += [t, t]
        vs += [vs[-1], level]
    # forca o ultimo ponto a assentar em settle_v
    t += deltas[-1]
    ts += [t, t]
    vs += [vs[-1], settle_v]
    return ts, vs, t


t, v = [0.0], [VCC]

# idle (pull-up: HIGH em repouso)
t_end = 8.0
t += [t_end]
v += [VCC]

# bounce ao pressionar (settle em LOW)
bt, bv, t_end = bounce_segment(t_end, start_v=VCC, settle_v=0.0)
t += bt[1:]
v += bv[1:]

# segura (LOW)
t_hold_end = t_end + 10
t += [t_hold_end]
v += [0.0]

# bounce ao soltar (settle em HIGH)
bt, bv, t_end2 = bounce_segment(t_hold_end, start_v=0.0, settle_v=VCC)
t += bt[1:]
v += bv[1:]

# idle novamente (HIGH)
t += [t_end2 + 8]
v += [VCC]

fig, ax = plt.subplots(figsize=(9, 4))

ax.axhspan(V_IL, V_IH, color="#dddddd", zorder=0)
ax.axhline(V_IH, color="gray", linestyle="--", linewidth=1)
ax.axhline(V_IL, color="gray", linestyle="--", linewidth=1)

ax.step(t, v, where="post", color="black", linewidth=2)

ax.set_ylim(-0.5, VCC + 1.0)
ax.set_xlim(0, t[-1])
ax.set_yticks([0, V_IL, V_IH, VCC])
ax.set_yticklabels(["0V\n(LOW)", "V_IL", "V_IH", f"{VCC:.0f}V\n(HIGH)"])
ax.set_xlabel("tempo (ms, escala ilustrativa)")
ax.set_ylabel("tensão no pino")
ax.set_title("Bounce mecânico do botão (com resistor de referência)")

ax.text(4, VCC + 0.5, "idle", ha="center")
ax.text((8 + t_hold_end) / 2 - 3, VCC + 0.5, "pressiona\n(bounce)", ha="center")
ax.text((t_hold_end + t_end2) / 2, 0.6, "segura (LOW)", ha="center", va="bottom")
ax.text(t_end2 + 2, VCC + 0.5, "solta\n(bounce)", ha="center")
ax.text(t[-1] - 4, VCC + 0.5, "idle", ha="center")
ax.text(t[-1] * 0.98, (V_IL + V_IH) / 2, "zona\nindefinida", ha="right", va="center", fontsize=8, color="gray")

fig.tight_layout()
fig.savefig(str(OUT_DIR / f"{NAME}.svg"))
fig.savefig(str(OUT_DIR / f"{NAME}.png"), dpi=200)

print("Generated:", OUT_DIR / f"{NAME}.svg")
