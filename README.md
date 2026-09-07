# S086 - Sistemas Microprocessados (2026/2) 🔧🖥️

Bem-vindo ao repositório central da Unidade Curricular **S086 - Sistemas Microprocessados**
da Faculdade de Tecnologia SENAI Porto Alegre.

Este espaço será o guia técnico e laboratório prático durante o semestre.

---

## 👨‍🏫 Docente
**Prof. Me. João Miguel Lac Roehe**
📧 [joao.roehe@senairs.org.br](mailto:joao.roehe@senairs.org.br)

---

## 🔧 Hardware e Ferramentas

- **Placas:** Shield 9-em-1 + **ESP32-S3-UNO** (placa ESP32 em form factor
  Arduino UNO, chip ESP32-S3: dual-core 240 MHz, Wi-Fi + BLE, 16 MB Flash,
  8 MB PSRAM) + **Arduino UNO R3 clássico** (ATmega328P, 16 MHz).
- **Linguagem:** C/C++ (Arduino framework), via **Arduino IDE**.
- **Simulação:** [Wokwi](https://wokwi.com) — para montar e testar circuitos e código
  antes de ir para a placa física.
- **Simuladores de CPU/assembly (candidatos, uso ainda a definir em aula):**
  [LMC — Little Man Computer](https://peterhigginson.co.uk/lmc/)
  ([ajuda](https://peterhigginson.co.uk/lmc/help_new.html)) e
  [CPU Visual Simulator](https://cpuvisualsimulator.github.io/)
  ([manual](https://cpuvisualsimulator.github.io/manual)).
- **Documentação de placas e shields:** repositórios irmãos
  [`lab_dev_boards`](https://github.com/professorjoaomiguel/lab_dev_boards) e
  [`lab_se`](https://github.com/professorjoaomiguel/lab_se) (fotos, esquemáticos,
  componentes e periféricos das placas/shields usadas em aula — `lab_se` usa
  MicroPython em seu próprio laboratório, mas aqui a linguagem é C/C++/Arduino IDE).

## 📂 Estrutura do Repositório

- [`guias_e_roteiros_tecnicos/`](./guias_e_roteiros_tecnicos/) — guias técnicos
  para os alunos (instalação, configuração e troubleshooting de ferramentas).
  Segue o mesmo padrão de template usado no repositório irmão `S122_2026-1`.
- [`slides/`](./slides/) — fontes Markdown das apresentações de aula
  ([Marp](https://github.com/marp-team/marp), CLI instalada globalmente:
  `npm install -g @marp-team/marp-cli`). `marp slides --output slides/build --html`
  gera o HTML em `slides/build/` (fora do git).

> Em construção. Pastas de laboratórios e slides serão adicionadas conforme
> o material da disciplina for publicado.

---

## 💡 Filosofia de Aprendizado

Este curso utiliza a **Filosofia de Aprendizado Ativo**: o aluno é o protagonista
da construção do conhecimento, utilizando a IA como um **Tutor** e não como um
substituto para o raciocínio.

### 🤖 IA para os Alunos

Os alunos têm acesso ao **Gemini (Google)** pela conta de estudante do SENAI, que
é a ferramenta de IA recomendada para apoio nos laboratórios. Veja [`GEMINI.md`](./GEMINI.md).

---

## 🚀 Como Começar

1. Faça o clone deste repositório.
2. Leia o [`.ai/AGENTS.md`](./.ai/AGENTS.md) como fonte única de instruções para IA.

---
*Senai Porto Alegre - Tecnologia em Análise e Desenvolvimento de Sistemas / Automação Industrial*
