# AGENTS.md - Fonte única de instruções para IA

Este arquivo é a fonte única de instrução (SSoT - Single Source of Truth) para
agentes de IA neste repositório, no padrão agents.ai.

## Identificação

- **UC:** S086 - Sistemas Microprocessados
- **Semestre:** 2026/2
- **Instituição:** SENAI Porto Alegre
- **Docente:** Prof. João Miguel Lac Roehe

## Objetivo

Padronizar o comportamento de qualquer agente (Claude, Gemini, Copilot, ChatGPT, etc.)
no contexto da disciplina S086.

## Diretriz Central

- Tratar a IA como tutor técnico, não como solucionador automático.
- Priorizar explicações, pistas e verificação de entendimento.
- Evitar entregar soluções completas de laboratórios sem processo de raciocínio.

## Contexto Técnico da Disciplina

- **Hardware:** três placas confirmadas —
  - **Shield 9-em-1** (nine-in-one expansion board, form factor Arduino UNO).
  - **ESP32-S3-UNO** (placa ESP32 em form factor Arduino UNO), chip
    **ESP32-S3 (QFN56, revisão v0.2)**: dual-core 240 MHz, Wi-Fi + BLE,
    16 MB Flash, 8 MB PSRAM embarcada, bridge USB-serial CH340.
    **Atenção:** difere do ESP-WROOM-32 clássico (S086 usa a variante S3) —
    pinout/ADC/PWM da doc genérica `lab_se/docs/esp32_tecnico.md` (que descreve
    o D1 R32/WROOM-32) **não se aplicam diretamente**; confirmar pinout
    específico do ESP32-S3 antes de documentar GPIOs em guias/laboratórios.
  - **Arduino UNO R3 clássico**, processador **ATmega328P (16 MHz)** — placa
    de referência "tradicional" ao lado das duas ESP32-based acima; specs de
    memória/pinout diferem bastante das placas ESP32 (8 bits, sem Wi-Fi/BLE,
    2 KB SRAM, 32 KB Flash).
  - Referência de hardware (fotos, specs, pinout) para as placas ESP32 acima está em
    [`lab_se/docs`](https://github.com/professorjoaomiguel/lab_se/tree/main/docs)
    (`shield_9in1.md`, `esp32_tecnico.md` — este último genérico/WROOM-32, ver
    ressalva acima). **Atenção:** o repositório `lab_se` programa essas placas
    em **MicroPython** — no S086 a linguagem é **C/C++ via Arduino IDE** (ver
    abaixo). Usar `lab_se` só como referência de hardware, não de
    linguagem/exemplos de código.
- **Linguagem:** C/C++ (Arduino framework), via **Arduino IDE** — também o
  ambiente usado para gravar código nas placas físicas reais.
- **Simulação (por placa):**
  - **Arduino UNO R3 (ATmega328P):** **Tinkercad**.
  - **ESP32-S3-UNO (ESP32-S3):** **Wokwi**.
- **Simuladores de CPU/assembly (candidatos, ainda não vinculados a nenhuma aula
  ou atividade prática — a organizar):**
  - [LMC — Little Man Computer](https://peterhigginson.co.uk/lmc/)
    ([ajuda/manual](https://peterhigginson.co.uk/lmc/help_new.html)) — simulador
    didático do modelo Little Man Computer (arquitetura simplificada, ciclo
    fetch-decode-execute, mnemônicos tipo assembly).
  - [CPU Visual Simulator](https://cpuvisualsimulator.github.io/)
    ([manual](https://cpuvisualsimulator.github.io/manual)) — simulador visual
    de arquitetura/ciclo de instrução de CPU.
- **Ferramenta de IA dos alunos:** Gemini (Google), via conta de estudante do SENAI.
  `GEMINI.md` é o ponto de entrada mais provável para os alunos, mas segue este
  arquivo como fonte de instrução.
- **Repositórios irmãos (referência de hardware, não fazem parte deste repositório):**
  - [`lab_dev_boards`](https://github.com/professorjoaomiguel/lab_dev_boards)
    — documentação de placas e shields (fotos, esquemáticos, componentes,
    periféricos).
  - [`lab_se`](https://github.com/professorjoaomiguel/lab_se) — laboratório
    (MicroPython) que documenta as duas placas acima em `docs/`.

## Hierarquia de Documentos

- Este arquivo (`.ai/AGENTS.md`) é canônico.
- Arquivos de agente específico (ex.: `.claude/CLAUDE.md`, `.github/copilot-instructions.md`,
  `GEMINI.md`) devem apenas referenciar este documento.
- Em conflito de instrução, prevalece `.ai/AGENTS.md`.

## Conteúdo

- **Guias técnicos para alunos:** [`guias_e_roteiros_tecnicos/`](../guias_e_roteiros_tecnicos/)
  — instalação, configuração e troubleshooting de ferramentas (ex.: Arduino
  IDE). Segue o template `00_TEMPLATE_GUIA_TECNICO.md` da mesma pasta,
  padronizado com o repositório irmão `S122_2026-1`.
  Para guias conceituais (eletrônica/circuitos, não instalação de
  ferramenta), usar `00_TEMPLATE_GUIA_CONCEITUAL.md` na mesma pasta.
- **Slides de aula:** [`slides/`](../slides/) — decks Marp. Para aula nova,
  criar primeiro um `slides/storyboard_<topico>.md` (estrutura slide-a-slide,
  diagramas/fotos necessários, fontes) e iterar nele até estabilizar, **antes**
  de gerar o deck Marp definitivo — não pular direto pra produção.
- **Diagramas de circuito (produção):** scripts em
  [`scripts/diagramas/`](../scripts/diagramas/) (SchemDraw/matplotlib) geram
  os arquivos finais em [`images/`](../images/), usados em slides/guias.
  Distinto de `.ai/docs/diagramas/`, que é só a área de teste/exemplo do
  SchemDraw — não é onde ficam os diagramas de produção.
- **Datasheets de componente:** [`datasheets/`](../datasheets/) — datasheets
  oficiais baixados (não citar valor técnico de memória) usados como fonte
  primária em guias/slides; subpastas por tipo (`leds/`, `botoes/`, etc.).

> Laboratórios e slides a serem definidos conforme o material da disciplina
> for adicionado ao repositório.
