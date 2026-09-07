# Diagramas de circuito

Diagramas eletronicos simples (resistor, LED, capacitor, transistor, MCU,
etc.) para uso em documentos Markdown e slides, gerados com
[SchemDraw](https://schemdraw.readthedocs.io/en/stable/) — biblioteca Python
pura, sem dependencia de LaTeX. Cada diagrama e um script `.py` versionado
que gera os artefatos `.svg` (vetorial, preferir em Markdown/web) e `.png`
(quando um raster for necessario, ex.: PowerPoint).

## Uso

```bash
pip install schemdraw matplotlib
python exemplo_led_esp32.py
```

## Exemplos

[`exemplo_led_esp32.py`](./exemplo_led_esp32.py) — LED com resistor limitador
de corrente acionado por um GPIO do ESP32-S3-UNO.

![Exemplo LED + resistor no GPIO do ESP32-S3](./exemplo_led_esp32.svg)

[`mcu_boards.py`](./mcu_boards.py) — blocos reutilizaveis (`arduino_uno()`,
`esp32s3_uno()`) para representar as placas do S086 em qualquer diagrama,
sem redesenhar a caixa de pinos toda vez. O SchemDraw nao tem simbolos
prontos de microcontrolador; os blocos usam o elemento generico `elm.Ic`
com os rotulos do header form-factor Arduino UNO (`D0`-`D13`, `A0`-`A5`,
alimentacao). **Atencao:** o bloco `esp32s3_uno()` usa os mesmos rotulos de
header do form-factor UNO, e nao o mapeamento de GPIO interno do chip
ESP32-S3 — confirmar o pinout especifico antes de documentar GPIOs em
guias/laboratorios (ver `.ai/AGENTS.md`).

Exemplo de uso em [`exemplo_mcu_boards.py`](./exemplo_mcu_boards.py):

![Blocos Arduino UNO R3 e ESP32-S3-UNO](./exemplo_mcu_boards.svg)
