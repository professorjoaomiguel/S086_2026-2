"""Exemplo de uso dos blocos reutilizaveis de mcu_boards.py.

Mostra as duas placas UNO form-factor lado a lado, apenas para conferir o
layout de pinos do bloco generico (nao e um circuito funcional).

Uso:
    pip install schemdraw matplotlib
    python exemplo_mcu_boards.py
"""

from pathlib import Path

import schemdraw

from mcu_boards import arduino_uno, esp32s3_uno

OUT_DIR = Path(__file__).parent

with schemdraw.Drawing(show=False) as d:
    d.add(arduino_uno())
    d.move(10, 0)
    d.add(esp32s3_uno())

    d.save(str(OUT_DIR / "exemplo_mcu_boards.svg"))
    d.save(str(OUT_DIR / "exemplo_mcu_boards.png"), dpi=200)

print("Gerado:", OUT_DIR / "exemplo_mcu_boards.svg")
print("Gerado:", OUT_DIR / "exemplo_mcu_boards.png")
