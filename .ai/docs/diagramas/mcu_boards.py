"""Reusable microcontroller blocks for SchemDraw diagrams.

SchemDraw has no built-in Arduino/ESP32 symbols (element library:
https://schemdraw.readthedocs.io/en/stable/circuit_elements.html).
This module uses the generic `elm.Ic` element to draw a box with the
header (silkscreen) pins of the boards used in S086, for reuse across
circuit diagrams.

Usage:
    import schemdraw
    from mcu_boards import arduino_uno, esp32s3_uno

    with schemdraw.Drawing() as d:
        d.add(arduino_uno())
"""

import schemdraw.elements as elm

_ANALOG = [f"A{n}" for n in range(6)]  # A0..A5 (the Uno only has 6 analog pins)
_POWER = ["VIN", "GND", "GND", "5V", "3V3", "RESET", "IOREF"]  # Uno power header order
_DIGITAL = [f"D{n}" for n in range(14)]  # D0..D13

# Pins are added bottom-up (the first list item ends up at the bottom of the
# box), reproducing the Uno's physical header order/position: left side =
# analog pins (A0 at the bottom) with the power header stacked above them;
# right side = digital pins (D0 at the bottom ... D13 at the top).
_LEFT = _ANALOG + _POWER
_RIGHT = _DIGITAL


def _mcu_box(title: str, subtitle: str = "", **kwargs) -> elm.Ic:
    """Generic box with the Arduino UNO form-factor header pin layout."""
    pins = [elm.IcPin(name=name, side="left") for name in _LEFT]
    pins += [elm.IcPin(name=name, side="right") for name in _RIGHT]

    label = title if not subtitle else f"{title}\n{subtitle}"
    kwargs.setdefault("size", (7, 11))
    kwargs.setdefault("pinspacing", 0.7)
    kwargs.setdefault("fontsize", 13)
    return elm.Ic(pins=pins, label=label, **kwargs)


def arduino_uno(**kwargs) -> elm.Ic:
    """Arduino UNO R3 (ATmega328P) — header pins only, no internal chip detail."""
    return _mcu_box("Arduino UNO R3", **kwargs)


def esp32s3_uno(**kwargs) -> elm.Ic:
    """ESP32-S3-UNO (ESP32-S3 board in Arduino UNO form factor).

    Uses the SAME header labels (D0..D13, A0..A5) as the UNO form factor —
    this does NOT represent the ESP32-S3 chip's (QFN56) internal GPIO
    mapping, which differs from the classic ESP-WROOM-32. Confirm the
    ESP32-S3's actual pinout before using GPIO labels in guides/labs
    (see .ai/AGENTS.md, "Contexto Tecnico da Disciplina" section).
    """
    return _mcu_box("ESP32-S3-UNO", "(UNO form-factor header labels)", **kwargs)
