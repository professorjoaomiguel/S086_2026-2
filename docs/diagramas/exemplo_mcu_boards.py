"""Usage example for the reusable blocks in mcu_boards.py.

Shows both UNO form-factor boards side by side, just to check the pin
layout of the generic block (this is not a functional circuit).

Usage:
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

print("Generated:", OUT_DIR / "exemplo_mcu_boards.svg")
print("Generated:", OUT_DIR / "exemplo_mcu_boards.png")
