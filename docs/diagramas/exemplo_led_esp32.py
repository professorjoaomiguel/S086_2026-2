"""Exemplo minimo de diagrama de circuito com SchemDraw.

Circuito: LED com resistor limitador de corrente, acionado por um GPIO
do ESP32-S3-UNO (nivel logico 3,3 V), retornando ao GND da placa.

Uso:
    pip install schemdraw matplotlib
    python exemplo_led_esp32.py

Gera exemplo_led_esp32.svg e exemplo_led_esp32.png na mesma pasta.

Referencia: https://schemdraw.readthedocs.io/en/stable/
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUT_DIR = Path(__file__).parent

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5)

    fonte = d.add(elm.SourceV().up().label("GPIO13\n(3,3 V)", loc="top"))
    d.add(elm.Resistor().right().label("R1\n330 Ω"))
    d.add(elm.LED().right().label("D1\nLED vermelho", loc="bottom"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(fonte.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    d.save(str(OUT_DIR / "exemplo_led_esp32.svg"))
    d.save(str(OUT_DIR / "exemplo_led_esp32.png"), dpi=200)

print("Gerado:", OUT_DIR / "exemplo_led_esp32.svg")
print("Gerado:", OUT_DIR / "exemplo_led_esp32.png")
