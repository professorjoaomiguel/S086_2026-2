"""Minimal circuit diagram example with SchemDraw.

Circuit: LED with current-limiting resistor, driven by a GPIO on the
ESP32-S3-UNO (3.3 V logic level), returning to the board's GND.

Usage:
    pip install schemdraw matplotlib
    python exemplo_led_esp32.py

Generates exemplo_led_esp32.svg and exemplo_led_esp32.png in the same folder.

Reference: https://schemdraw.readthedocs.io/en/stable/
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).parent

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    source = d.add(elm.SourceV().up().label("GPIO13\n(3,3 V)", loc="top"))
    d.add(elm.Resistor().right().label("R1\n330 Ω"))
    d.add(elm.LED().right().label("D1\nLED vermelho", loc="bottom"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(source.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / "exemplo_led_esp32.svg"))
    d.save(str(OUT_DIR / "exemplo_led_esp32.png"), dpi=200)

print("Generated:", OUT_DIR / "exemplo_led_esp32.svg")
print("Generated:", OUT_DIR / "exemplo_led_esp32.png")
