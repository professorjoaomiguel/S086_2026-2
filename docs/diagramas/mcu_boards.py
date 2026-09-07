"""Blocos reutilizaveis de microcontroladores para diagramas SchemDraw.

O SchemDraw nao tem simbolos prontos de Arduino/ESP32 (biblioteca de
elementos: https://schemdraw.readthedocs.io/en/stable/circuit_elements.html).
Este modulo usa o elemento generico `elm.Ic` para desenhar uma caixa com os
pinos do header (silkscreen) das placas usadas no S086, para reuso nos
diagramas de circuito.

Uso:
    import schemdraw
    from mcu_boards import arduino_uno, esp32s3_uno

    with schemdraw.Drawing() as d:
        d.add(arduino_uno())
"""

import schemdraw.elements as elm

_PODER = ["VIN", "5V", "3V3", "GND"]
_DIGITAIS = [f"D{n}" for n in range(13, -1, -1)]  # D13..D0, header form-factor UNO
_ANALOGICAS = [f"A{n}" for n in range(6)]  # A0..A5


def _mcu_box(titulo: str, subtitulo: str = "", **kwargs) -> elm.Ic:
    """Caixa generica com o layout de pinos do header form-factor Arduino UNO."""
    pins = [elm.IcPin(name=nome, side="left") for nome in _PODER]
    pins += [elm.IcPin(name=nome, side="right") for nome in _DIGITAIS]
    pins += [elm.IcPin(name=nome, side="bottom") for nome in _ANALOGICAS]

    label = titulo if not subtitulo else f"{titulo}\n{subtitulo}"
    kwargs.setdefault("size", (7, 11))
    kwargs.setdefault("pinspacing", 0.7)
    kwargs.setdefault("fontsize", 13)
    return elm.Ic(pins=pins, label=label, **kwargs)


def arduino_uno(**kwargs) -> elm.Ic:
    """Arduino UNO R3 (ATmega328P) — pinos do header, sem detalhe interno do chip."""
    return _mcu_box("Arduino UNO R3", **kwargs)


def esp32s3_uno(**kwargs) -> elm.Ic:
    """ESP32-S3-UNO (placa ESP32-S3 em form factor Arduino UNO).

    Usa os MESMOS rotulos de header (D0..D13, A0..A5) do form-factor UNO —
    NAO representa o mapeamento de GPIO interno do chip ESP32-S3 (QFN56),
    que difere do ESP-WROOM-32 classico. Confirmar o pinout especifico do
    ESP32-S3 antes de usar rotulos de GPIO em guias/laboratorios
    (ver .ai/AGENTS.md, secao "Contexto Tecnico da Disciplina").
    """
    return _mcu_box("ESP32-S3-UNO", "(rotulos form-factor UNO)", **kwargs)
