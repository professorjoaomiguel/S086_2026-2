# Template Marp Compartilhado + Correção das 3 Causas Raiz (Decks GPIO) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Dar aos 2 decks Marp de GPIO (`slides/gpio_saida_leds.md`, `slides/gpio_entrada_botoes.md`) um tema compartilhado com rodapé (`@professorjoaomiguel` + numeração), e corrigir os 17 slides com observação da avaliação `docs/avaliacao_slides_gpio_entrada_saida.md`, agrupados em 3 causas raiz.

**Architecture:** Fluxo B (infraestrutura) primeiro — tema Marp real (`slides/theme/s086.css`), script de build (`scripts/build_slides.sh`), documentação (storyboard + `.ai/AGENTS.md`). Fluxo A (conteúdo) depois — 2 bugs reais de script SchemDraw (colisão de rótulo), ajustes de layout Marp (altura de imagem / split de slide) para os casos que são overflow de frame (não bug de script), e 3 trocas de foto. Termina com 1 único re-export dos 2 PDFs e checagem de regressão nos 17 pontos.

**Tech Stack:** Marp CLI (`@marp-team/marp-cli` v4.5.1, já instalado globalmente), SchemDraw 0.23 + matplotlib (Python), bash, poppler (`pdftoppm`/`pdfinfo`, já instalado via winget).

**Spec:** `docs/superpowers/specs/2026-09-12-decks-gpio-template-e-correcoes-design.md`

## Global Constraints

- Escopo: só os 2 decks GPIO (`slides/gpio_saida_leds.md`, `slides/gpio_entrada_botoes.md`) nesta rodada — não tocar `storyboard_semicondutores.md` nem outro deck.
- `marp --pdf` **exige** `--allow-local-files` neste repo (as imagens são referenciadas por caminho relativo `../images/...`) — sem essa flag, o PDF gera mas com as imagens em branco (confirmado empiricamente nesta sessão). Todo comando de build/verificação usa essa flag.
- `--theme-set` do marp-cli espera o **caminho do arquivo `.css`**, não de um diretório, e deve ser passado com `=` (`--theme-set=slides/theme/s086.css`) — passar como diretório ou com espaço antes do próximo argumento trava o CLI esperando stdin (confirmado empiricamente).
- Rodapé: usar a diretiva nativa `footer:` do Marp no frontmatter — já nasce ancorada no canto inferior esquerdo por padrão (confirmado empiricamente), sem precisar de CSS de posicionamento.
- Não reescrever o texto pedagógico do professor para "consertar" overflow de frame — preferir reduzir a altura da imagem (`h:NNN`) ou dividir o slide em dois, nunca cortar/reescrever frases existentes.
- Cada correção de diagrama/slide é verificada **rasterizando o PDF de verdade** (`marp --allow-local-files --pdf` + `pdftoppm`) e lendo a imagem — não basta olhar o `.png` do script isolado, porque um script correto ainda pode estourar o frame por excesso de texto no slide (achado desta sessão: 3 dos 5 "diagramas cortados" originais eram overflow de frame, não bug de script).

---

### Task 1: Tema Marp compartilhado (`slides/theme/s086.css`) + migração de frontmatter

**Files:**
- Create: `slides/theme/s086.css`
- Modify: `slides/gpio_saida_leds.md:1-28` (frontmatter)
- Modify: `slides/gpio_entrada_botoes.md:1-29` (frontmatter)

**Interfaces:**
- Produces: `slides/theme/s086.css` com nome de tema `s086` (declarado via `/* @theme s086 */`), consumido pelo frontmatter `theme: s086` dos 2 decks e pelo `--theme-set` do script de build (Task 2).

- [ ] **Step 1: Criar o arquivo de tema**

Criar `slides/theme/s086.css`:

```css
/* @theme s086 */
@import 'default';

section.lead {
  background: #1a1a2e;
  color: white;
}
section.lead h1,
section.lead h2,
section.lead h3 {
  color: white;
}
section.pausa-previsao { background: #eef3ff; }
section.pausa-calculo { background: #fff8e1; }
section.pausa-garimpo { background: #eafaf0; }
section.revelacao { background: #f7f7f7; }
section.alerta { background: #fdecea; }
.columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1em;
}
.columns h3 { margin-top: 0; }
table { font-size: 0.85em; }
img { display: block; margin: 0 auto; }
```

(É a união dos dois blocos `style:` hoje duplicados nos dois decks — o deck de Saída não tinha `section.alerta`, mas incluir não quebra nada.)

- [ ] **Step 2: Migrar o frontmatter de `slides/gpio_saida_leds.md`**

Substituir as linhas 1-28 (todo o bloco frontmatter atual, de `---` a `---`) por:

```
---
marp: true
theme: s086
paginate: true
footer: '@professorjoaomiguel'
---
```

- [ ] **Step 3: Migrar o frontmatter de `slides/gpio_entrada_botoes.md`**

Mesma substituição (linhas 1-29) pelo mesmo bloco:

```
---
marp: true
theme: s086
paginate: true
footer: '@professorjoaomiguel'
---
```

- [ ] **Step 4: Verificar visualmente (build manual + rasterização)**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_saida_leds.md -o /tmp/check_saida.pdf
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_entrada_botoes.md -o /tmp/check_entrada.pdf
pdftoppm -jpeg -r 110 -f 1 -l 1 /tmp/check_saida.pdf /tmp/check_saida_capa
pdftoppm -jpeg -r 110 -f 3 -l 3 /tmp/check_saida.pdf /tmp/check_saida_pausa
```

Ler `/tmp/check_saida_capa-1.jpg` (Ferramenta Read): confirmar capa com fundo escuro `#1a1a2e`, título branco, rodapé `@professorjoaomiguel` no canto inferior esquerdo, número de página no canto inferior direito.

Ler qualquer slide de pausa (`pausa-previsao`/`pausa-calculo`/`pausa-garimpo`) em ambos os decks: confirmar fundo colorido igual ao que já existia antes da migração (comparar com a avaliação `docs/avaliacao_slides_gpio_entrada_saida.md`, que não reportou nenhuma falha de contraste/cor — a migração não deve mudar isso).

- [ ] **Step 5: Commit**

```bash
git add slides/theme/s086.css slides/gpio_saida_leds.md slides/gpio_entrada_botoes.md
git commit -m "feat(slides): tema Marp compartilhado com rodape @professorjoaomiguel"
```

---

### Task 2: Script de build (`scripts/build_slides.sh`)

**Files:**
- Create: `scripts/build_slides.sh`

**Interfaces:**
- Consumes: `slides/theme/s086.css` (Task 1)
- Produces: `slides/build/gpio_saida_leds.pdf`, `slides/build/gpio_entrada_botoes.pdf` — consumidos por qualquer verificação/re-export posterior neste plano (Tasks 3-12).

- [ ] **Step 1: Criar o script**

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

marp --theme-set=slides/theme/s086.css --allow-local-files --pdf \
  slides/gpio_saida_leds.md -o slides/build/gpio_saida_leds.pdf

marp --theme-set=slides/theme/s086.css --allow-local-files --pdf \
  slides/gpio_entrada_botoes.md -o slides/build/gpio_entrada_botoes.pdf

echo "Build concluido:"
echo "  slides/build/gpio_saida_leds.pdf"
echo "  slides/build/gpio_entrada_botoes.pdf"
```

- [ ] **Step 2: Tornar executável e rodar**

```bash
chmod +x scripts/build_slides.sh
./scripts/build_slides.sh
```

Expected: os dois PDFs são regravados em `slides/build/`, cada um com mais de 400KB (o deck de Saída tinha 590998 bytes, o de Entrada 955603 bytes antes desta rodada — arquivos muito menores indicam imagem em branco, ver Global Constraints).

```bash
ls -la slides/build/gpio_saida_leds.pdf slides/build/gpio_entrada_botoes.pdf
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build_slides.sh
git commit -m "feat(slides): script de build com tema e --allow-local-files"
```

---

### Task 3: Documentar a convenção no storyboard e no `.ai/AGENTS.md`

**Files:**
- Modify: `slides/storyboard_gpio.md`
- Modify: `.ai/AGENTS.md:85-88`

**Interfaces:**
- Consumes: nomes de arquivo de `slides/theme/s086.css` (Task 1) e `scripts/build_slides.sh` (Task 2).

- [ ] **Step 1: Adicionar seção ao storyboard**

Adicionar, logo após a linha `**Regra de produção geral: um slide, uma ideia.** ...` (antes da seção `## Diagramas e fotos necessários`) em `slides/storyboard_gpio.md`, o seguinte bloco novo:

```markdown
## Template e convenções de produção

Os dois decks usam o tema Marp compartilhado `slides/theme/s086.css`
(cores de pausa/revelação/alerta, capa escura, rodapé) — não duplicar
CSS no frontmatter de cada deck; qualquer ajuste visual (cor, espaçamento)
vai no arquivo de tema, não em um deck individual.

Rodapé: `footer: '@professorjoaomiguel'` no frontmatter, aplicado a todo
slide sem exceção (Marp posiciona automaticamente no canto inferior
esquerdo; a numeração de página via `paginate: true` continua no canto
inferior direito).

Exportar PDF sempre via `scripts/build_slides.sh` — nunca `marp` direto
na linha de comando. O script já inclui `--theme-set` e
`--allow-local-files`: esquecer o primeiro gera um deck sem tema (volta
pro tema `default` puro); esquecer o segundo gera um PDF com todas as
imagens em branco, sem erro visível no terminal.
```

- [ ] **Step 2: Atualizar `.ai/AGENTS.md`**

Modificar o bullet existente em `.ai/AGENTS.md:85-88`, de:

```
- **Slides de aula:** [`slides/`](../slides/) — decks Marp. Para aula nova,
  criar primeiro um `slides/storyboard_<topico>.md` (estrutura slide-a-slide,
  diagramas/fotos necessários, fontes) e iterar nele até estabilizar, **antes**
  de gerar o deck Marp definitivo — não pular direto pra produção.
```

para:

```
- **Slides de aula:** [`slides/`](../slides/) — decks Marp. Para aula nova,
  criar primeiro um `slides/storyboard_<topico>.md` (estrutura slide-a-slide,
  diagramas/fotos necessários, fontes) e iterar nele até estabilizar, **antes**
  de gerar o deck Marp definitivo — não pular direto pra produção.
- **Tema e build de slides:** tema Marp compartilhado em
  [`slides/theme/s086.css`](../slides/theme/s086.css) (`theme: s086` no
  frontmatter) — não duplicar CSS por deck. Exportar PDF sempre via
  [`scripts/build_slides.sh`](../scripts/build_slides.sh), nunca `marp`
  direto na mão (ele já inclui as flags `--theme-set` e
  `--allow-local-files`, ambas fáceis de esquecer e que quebram o
  resultado silenciosamente).
```

- [ ] **Step 3: Commit**

```bash
git add slides/storyboard_gpio.md .ai/AGENTS.md
git commit -m "docs: documentar tema Marp compartilhado e script de build"
```

---

### Task 4: Corrigir `gpio_pullup.py` (Entrada #25 — bug real de script)

**Files:**
- Modify: `scripts/diagramas/gpio_pullup.py`
- Modify: `images/gpio_pullup.svg`, `images/gpio_pullup.png` (regenerados, não editados à mão)

**Interfaces:**
- Produces: `images/gpio_pullup.svg` sem sobreposição do rótulo "Botão" com o símbolo de GND, consumido por `slides/gpio_entrada_botoes.md:357`.

- [ ] **Step 1: Aplicar a correção**

Em `scripts/diagramas/gpio_pullup.py`, na linha:

```python
    d.add(elm.Switch().at(pin.center).down().label("Botão", loc="left"))
```

remover o `loc="left"` explícito (o padrão sem `loc=` já posiciona corretamente em elemento `.down()`, per a lição já documentada em `scripts/diagramas/README.md`):

```python
    d.add(elm.Switch().at(pin.center).down().label("Botão"))
```

- [ ] **Step 2: Regenerar e inspecionar isoladamente**

```bash
cd scripts/diagramas && python gpio_pullup.py
```

Ler `images/gpio_pullup.png` (Ferramenta Read). Esperado: rótulo "Botão" flutua à esquerda da chave, sem tocar o símbolo de GND abaixo (era exatamente esse o defeito confirmado nesta sessão antes da correção).

- [ ] **Step 3: Verificar no contexto real do slide**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_entrada_botoes.md -o /tmp/check_entrada.pdf
pdftoppm -jpeg -r 110 -f 25 -l 25 /tmp/check_entrada.pdf /tmp/check_e25
```

Ler `/tmp/check_e25-25.jpg`. Esperado: rótulo "Botão" e símbolo de GND totalmente visíveis, sem sobreposição, com margem até a borda inferior do frame.

- [ ] **Step 4: Commit**

```bash
git add scripts/diagramas/gpio_pullup.py images/gpio_pullup.svg images/gpio_pullup.png
git commit -m "fix(diagramas): remover loc explicito que colidia rotulo Botao com GND (gpio_pullup)"
```

---

### Task 5: Corrigir `gpio_interface_conceito.py` (Saída #7 + Entrada #6 — bug real de script, mesmo PNG nos dois decks)

**Files:**
- Modify: `scripts/diagramas/gpio_interface_conceito.py`
- Modify: `images/gpio_interface_conceito.svg`, `images/gpio_interface_conceito.png` (regenerados)

**Interfaces:**
- Produces: `images/gpio_interface_conceito.svg` sem colisão de rótulo, consumido por `slides/gpio_saida_leds.md:113` **e** `slides/gpio_entrada_botoes.md:101` (mesmo arquivo, 1 correção resolve os 2 slides).

- [ ] **Step 1: Aplicar a correção**

Em `scripts/diagramas/gpio_interface_conceito.py`, substituir as duas linhas de seta:

```python
    d.add(elm.Arrow().at((4.5, 1.5)).right().length(2.2).label("SAÍDA\n(LED)\npõe tensão", loc="top"))
    d.add(elm.Arrow().at((-2.2, 0.7)).right().length(2.2).label("ENTRADA\n(botão)\nlê tensão", loc="bottom"))
```

por (afasta o ponto de ancoragem da borda do retângulo e move o rótulo pro lado da seta, não empilhado por cima/baixo — a causa raiz confirmada era o rótulo de 3 linhas estourando o espaço de 0.7 unidade entre a seta e a borda do retângulo em y=2.2):

```python
    d.add(elm.Arrow().at((4.5, 1.8)).right().length(2.4).label("SAÍDA\n(LED)\npõe tensão", loc="right"))
    d.add(elm.Arrow().at((-2.4, 0.4)).right().length(2.4).label("ENTRADA\n(botão)\nlê tensão", loc="left"))
```

- [ ] **Step 2: Regenerar e inspecionar isoladamente**

```bash
cd scripts/diagramas && python gpio_interface_conceito.py
```

Ler `images/gpio_interface_conceito.png`. Esperado: as duas setas com rótulo ao lado (não em cima/baixo), sem tocar as bordas do retângulo "MICROCONTROLADOR (GPIO)".

- [ ] **Step 3: Verificar nos 2 slides reais**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_saida_leds.md -o /tmp/check_saida.pdf
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_entrada_botoes.md -o /tmp/check_entrada.pdf
pdftoppm -jpeg -r 110 -f 7 -l 7 /tmp/check_saida.pdf /tmp/check_s7
pdftoppm -jpeg -r 110 -f 6 -l 6 /tmp/check_entrada.pdf /tmp/check_e6
```

Ler `/tmp/check_s7-7.jpg` e `/tmp/check_e6-6.jpg`. Esperado nos dois: rótulo "SAÍDA (LED) põe tensão" sem tocar a seta/retângulo.

- [ ] **Step 4: Commit**

```bash
git add scripts/diagramas/gpio_interface_conceito.py images/gpio_interface_conceito.svg images/gpio_interface_conceito.png
git commit -m "fix(diagramas): afastar ancoragem das setas da borda do retangulo (gpio_interface_conceito, usado em Saida #7 e Entrada #6)"
```

---

### Task 6: Corrigir Saída #38 — MOSFET-P (bug real de script + overflow de frame, mesmo slide)

**Files:**
- Modify: `scripts/diagramas/mosfet_p_chave_high_side.py`
- Modify: `images/mosfet_p_chave_high_side.svg`, `images/mosfet_p_chave_high_side.png` (regenerados)
- Modify: `slides/gpio_saida_leds.md:605`

**Interfaces:**
- Produces: `images/mosfet_p_chave_high_side.svg` sem colisão de rótulo R_pullup/VCC, em `h:260` no slide (reduzido de `h:330`) para não estourar o frame com o parágrafo de 4 linhas do slide.

- [ ] **Step 1: Corrigir a colisão de rótulo no script**

Em `scripts/diagramas/mosfet_p_chave_high_side.py`, substituir:

```python
    gate_node = d.add(elm.Dot().at(Q1.gate))
    d.add(elm.Resistor().at(gate_node.center).left().length(3.0).label("R_gate", loc="top"))
    d.add(elm.Line().left().length(1.2))
    d.add(elm.SourceV().down().label("GPIO\nLOW", loc="bottom"))
    d.add(elm.Ground())

    d.add(elm.Resistor().at(gate_node.center).up().length(1.8).label("R_pullup\n(→ VCC)", loc="bottom"))
    d.add(elm.Dot().label("VCC", loc="top"))
```

por (achado nesta sessão: `loc="bottom"` colidia "R_pullup"/"(→ VCC)" com o rótulo "VCC" do topo e com a linha do gate; removendo o `loc=` explícito e alongando o resistor de 1.8 para 2.6 abre espaço suficiente — confirmado visualmente):

```python
    gate_node = d.add(elm.Dot().at(Q1.gate))
    d.add(elm.Resistor().at(gate_node.center).left().length(3.0).label("R_gate", loc="top"))
    d.add(elm.Line().left().length(1.2))
    d.add(elm.SourceV().down().label("GPIO\nLOW", loc="bottom"))
    d.add(elm.Ground())

    d.add(elm.Resistor().at(gate_node.center).up().length(2.6).label("R_pullup\n(→ VCC)"))
    d.add(elm.Dot().label("VCC", loc="top"))
```

- [ ] **Step 2: Regenerar e inspecionar isoladamente**

```bash
cd scripts/diagramas && python mosfet_p_chave_high_side.py
```

Ler `images/mosfet_p_chave_high_side.png`. Esperado: "R_pullup (→ VCC)" claramente à esquerda do resistor, sem tocar "VCC" do topo nem a linha "R_gate"/Q1.

- [ ] **Step 3: Reduzir a altura da imagem no slide**

Em `slides/gpio_saida_leds.md:605`, mudar:

```
![h:330](../images/mosfet_p_chave_high_side.svg)
```

para:

```
![h:260](../images/mosfet_p_chave_high_side.svg)
```

(valor confirmado empiricamente nesta sessão — com o parágrafo de 4 linhas deste slide, o circuito completo, incluindo o GND final, cabe com margem em `h:260`.)

- [ ] **Step 4: Verificar no slide real**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_saida_leds.md -o /tmp/check_saida.pdf
pdftoppm -jpeg -r 110 -f 38 -l 38 /tmp/check_saida.pdf /tmp/check_s38
```

Ler `/tmp/check_s38-38.jpg`. Esperado: circuito completo visível (GND final da carga incluído, com margem até a borda), sem colisão de rótulo no topo.

- [ ] **Step 5: Commit**

```bash
git add scripts/diagramas/mosfet_p_chave_high_side.py images/mosfet_p_chave_high_side.svg images/mosfet_p_chave_high_side.png slides/gpio_saida_leds.md
git commit -m "fix(slides): corrigir colisao de rotulo e reduzir altura de imagem (Saida #38, MOSFET-P)"
```

---

### Task 7: Corrigir Saída #35 e #36 — NPN e MOSFET-N (overflow de frame, sem bug de script)

**Files:**
- Modify: `slides/gpio_saida_leds.md:563` (Saída #35, NPN)
- Modify: `slides/gpio_saida_leds.md:577` (Saída #36, MOSFET-N)

**Interfaces:**
- Nenhuma — os scripts `npn_chave_low_side.py` e `mosfet_n_chave_low_side.py` já geram diagramas completos e corretos (confirmado visualmente nesta sessão); o defeito é só o parágrafo do slide empurrando a imagem além da altura do frame de 540pt.

- [ ] **Step 1: Reduzir a altura da imagem no slide 35**

Em `slides/gpio_saida_leds.md:563`, mudar:

```
![h:400](../images/npn_chave_low_side.svg)
```

para:

```
![h:330](../images/npn_chave_low_side.svg)
```

- [ ] **Step 2: Reduzir a altura da imagem no slide 36**

Em `slides/gpio_saida_leds.md:577`, mudar:

```
![h:400](../images/mosfet_n_chave_low_side.svg)
```

para:

```
![h:330](../images/mosfet_n_chave_low_side.svg)
```

(ambos os valores confirmados empiricamente nesta sessão — com o texto atual de cada slide, o circuito completo cabe com margem em `h:330`.)

- [ ] **Step 3: Verificar nos slides reais**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_saida_leds.md -o /tmp/check_saida.pdf
pdftoppm -jpeg -r 110 -f 35 -l 36 /tmp/check_saida.pdf /tmp/check_s3536
```

Ler `/tmp/check_s3536-35.jpg` e `/tmp/check_s3536-36.jpg`. Esperado nos dois: circuito completo (incluindo os GNDs de emissor/source e da fonte GPIO) visível com margem até a borda inferior.

- [ ] **Step 4: Commit**

```bash
git add slides/gpio_saida_leds.md
git commit -m "fix(slides): reduzir altura de imagem para caber no frame (Saida #35 NPN, #36 MOSFET-N)"
```

---

### Task 8: Corrigir Entrada #9 — NA vs. NF (bug real de script + slide sobrecarregado, split em 2)

**Files:**
- Modify: `scripts/diagramas/botao_na_nf.py`
- Modify: `images/botao_na_nf.svg`, `images/botao_na_nf.png` (regenerados)
- Modify: `slides/gpio_entrada_botoes.md:135-156`

**Interfaces:**
- Produces: `images/botao_na_nf.svg` sem sobreposição de rótulo com o fio de retorno; slide 9 original dividido em 2 slides (bullets isolados + comparação com o diagrama), seguindo a convenção já estabelecida do storyboard ("um slide, uma ideia").

- [ ] **Step 1: Corrigir a colisão de rótulo/fio no script**

Em `scripts/diagramas/botao_na_nf.py`, substituir:

```python
    # Circuito NA (esquerda)
    src_na = d.add(elm.BatteryCell().at((0, 0)).up().label("9V", loc="top"))
    d.add(elm.Resistor().right().label("R"))
    d.add(elm.Switch().right().label("NA\naberto em repouso\nI ≈ 0", loc="bottom"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(src_na.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    # Circuito NF (direita)
    src_nf = d.add(elm.BatteryCell().at((6.5, 0)).up().label("9V", loc="top"))
    d.add(elm.Resistor().right().label("R"))
    d.add(elm.Switch(nc=True).right().label("NF\nfechado em repouso\nI ≈ V/R", loc="bottom"))
    d.add(elm.Line().down())
    d.add(elm.Line().left().tox(src_nf.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())
```

por (achado nesta sessão: o fio de retorno horizontal passava por cima do texto do rótulo de 3 linhas; alongar o primeiro trecho vertical de 0.6/padrão para 1.4 antes de virar à esquerda dá clearance suficiente — confirmado visualmente):

```python
    # Circuito NA (esquerda)
    src_na = d.add(elm.BatteryCell().at((0, 0)).up().label("9V", loc="top"))
    d.add(elm.Resistor().right().label("R"))
    d.add(elm.Switch().right().label("NA\naberto em repouso\nI ≈ 0", loc="bottom"))
    d.add(elm.Line().down().length(3.2))
    d.add(elm.Line().left().tox(src_na.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())

    # Circuito NF (direita)
    src_nf = d.add(elm.BatteryCell().at((6.5, 0)).up().label("9V", loc="top"))
    d.add(elm.Resistor().right().label("R"))
    d.add(elm.Switch(nc=True).right().label("NF\nfechado em repouso\nI ≈ V/R", loc="bottom"))
    d.add(elm.Line().down().length(3.2))
    d.add(elm.Line().left().tox(src_nf.start))
    d.add(elm.Line().down().length(0.6))
    d.add(elm.Ground())
```

- [ ] **Step 2: Regenerar e inspecionar isoladamente**

```bash
cd scripts/diagramas && python botao_na_nf.py
```

Ler `images/botao_na_nf.png`. Esperado: os rótulos "NA .../I ≈ 0" e "NF .../I ≈ V/R" não são mais cruzados pelo fio de retorno horizontal.

- [ ] **Step 3: Dividir o slide 9 em dois**

Em `slides/gpio_entrada_botoes.md`, substituir o bloco (linhas 143-156):

```
**NA e NF não são "melhor" e "pior" — são escolhas de projeto:** cada um
define qual estado elétrico existe quando ninguém está acionando o
dispositivo.

![h:170](../images/botao_na_nf.svg)

<!--
Diagrama 15. No NF, o estado de repouso já conduz corrente pelo resistor
de referência (relevante em projetos sensíveis a consumo, ex. bateria);
em compensação, é justamente por já estar "fechado por padrão" que o NF
costuma aparecer em circuitos de segurança/fail-safe, onde um fio
rompido já é detectado como acionamento — como o sensor de fim de curso
do slide 4. Detalhamento de consumo/fail-safe fica para o guia.
-->

---
```

por (mesmo texto, agora em 2 slides — o primeiro mantém só os 2 bullets já existentes acima deste trecho, o segundo isola a frase de comparação + o diagrama):

```
---

## 🔀 NA vs. NF: comparando os dois circuitos

**NA e NF não são "melhor" e "pior" — são escolhas de projeto:** cada um
define qual estado elétrico existe quando ninguém está acionando o
dispositivo.

![h:260](../images/botao_na_nf.svg)

<!--
Diagrama 15. No NF, o estado de repouso já conduz corrente pelo resistor
de referência (relevante em projetos sensíveis a consumo, ex. bateria);
em compensação, é justamente por já estar "fechado por padrão" que o NF
costuma aparecer em circuitos de segurança/fail-safe, onde um fio
rompido já é detectado como acionamento — como o sensor de fim de curso
do slide 4. Detalhamento de consumo/fail-safe fica para o guia.
-->

---
```

(o `---` extra no início do bloco novo cria o slide adicional; o slide anterior, com o título "## 🔀 NA vs. NF: os dois tipos de contato" e os 2 bullets, permanece inalterado logo acima — ver `slides/gpio_entrada_botoes.md:135-141`.)

- [ ] **Step 4: Verificar no contexto real (agora são 2 slides, deck com 34 páginas)**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_entrada_botoes.md -o /tmp/check_entrada.pdf
pdfinfo /tmp/check_entrada.pdf | grep Pages
pdftoppm -jpeg -r 110 -f 9 -l 10 /tmp/check_entrada.pdf /tmp/check_e910
```

Expected: `Pages: 34` (33 originais + 1 novo). Ler `/tmp/check_e910-09.jpg` (só bullets, sem diagrama) e `/tmp/check_e910-10.jpg` (diagrama completo, com GND visível nos dois circuitos, margem até a borda).

- [ ] **Step 5: Commit**

```bash
git add scripts/diagramas/botao_na_nf.py images/botao_na_nf.svg images/botao_na_nf.png slides/gpio_entrada_botoes.md
git commit -m "fix(slides): dividir slide NA/NF sobrecarregado em 2 e corrigir colisao rotulo/fio (Entrada #9)"
```

---

### Task 9: Trocar foto Entrada #3 — botoeira (atualmente "PUSH TO STOP" contradiz a legenda)

**Files:**
- Modify: `slides/gpio_entrada_botoes.md:52-61`
- Modify: `scripts/diagramas/README.md` (seção "Fotos reais")
- Create: `images/botoeira_start.jpg` (ou extensão equivalente, conforme o que for baixado)
- Delete: `images/industrial_entrada_1.jpg` (se não usado em mais nenhum lugar após a troca)

**Interfaces:**
- Nenhuma — troca isolada de asset de imagem + texto de comentário.

- [ ] **Step 1: Buscar uma foto real de botoeira START/verde**

Ordem de busca (mesma hierarquia já documentada em `scripts/diagramas/README.md`: foto própria > vendor/catálogo > Wikimedia > Pixabay > busca ampla):

1. Sites de venda de componentes industriais/automação: buscar "botoeira start verde industrial" e "green start pushbutton industrial 22mm" em `eletrogate.com.br`, `filipeflop.com`/`makerhero.com`, `robocore.net`, `squids.com.br` (via WebSearch/WebFetch).
2. Wikimedia Commons: buscar "green start push button" / "start pushbutton switch industrial" — se achar, baixar via `https://commons.wikimedia.org/wiki/Special:FilePath/<nome-do-arquivo>` (padrão já usado no repo, mais confiável que pedir URL exata de página de busca).
3. Google Images (ou outro mecanismo de busca de imagem) com os termos "green start button industrial control panel" / "botão start verde painel industrial" — priorizar resultado de site de vendor/fabricante (Siemens, Schneider, ABB, etc.) sobre banco de imagem genérico.
4. Pixabay como último recurso, com os mesmos termos.

Critério de aceite: a foto deve mostrar claramente um botão do tipo START (verde, ou com "START"/símbolo de "play" gravado) — não pode ter "STOP" ou vermelho de parada gravado no próprio botão (é exatamente o defeito a corrigir).

- [ ] **Step 2: Baixar e salvar em `images/`**

Salvar como `images/botoeira_start.jpg` (ou `.png`, conforme o formato original). Anotar a fonte exata (URL, licença) para o Step 4.

- [ ] **Step 3: Atualizar o slide**

Em `slides/gpio_entrada_botoes.md:52-61`, trocar:

```
### 🔴 Uma botoeira aciona a partida de um motor

![h:420](../images/industrial_entrada_1.jpg)

<!--
Frame 1/3 — contexto industrial, abertura. Foto: Pixabay (licença livre)
— botoeira industrial de verdade (o exemplar fotografado é "PUSH TO
STOP", não "START" — mesmo estilo de botoeira, usado aqui só como
moldura visual, sem pretensão de ser o botão exato da frase).
-->
```

por (o comentário deve citar a fonte/licença real do arquivo baixado no Step 2 — preencher `<FONTE>`/`<LICENCA>` com o valor real, não deixar literal):

```
### 🟢 Uma botoeira aciona a partida de um motor

![h:420](../images/botoeira_start.jpg)

<!--
Frame 1/3 — contexto industrial, abertura. Foto: <FONTE>, <LICENCA> —
botoeira START/verde real, coerente com a legenda (substitui a foto
anterior, que mostrava "PUSH TO STOP" contradizendo o texto).
-->
```

(nota: o emoji do título mudou de 🔴 para 🟢 para acompanhar a nova foto — ajustar se a foto final não for verde.)

- [ ] **Step 4: Atualizar `scripts/diagramas/README.md`**

Na seção "Fotos reais", substituir a linha sobre `industrial_entrada_1.jpg` (dentro do bullet que lista as fotos Pixabay) por uma entrada nova para `botoeira_start.jpg`, seguindo o mesmo formato das entradas existentes (fonte, licença, se exige atribuição).

- [ ] **Step 5: Remover o asset antigo (se não usado em outro lugar)**

```bash
grep -rn "industrial_entrada_1" --include="*.md" .
```

Se não houver mais nenhuma ocorrência (fora da própria linha do README já editada no Step 4 e da tabela do storyboard, que deve ser atualizada também):

```bash
git rm images/industrial_entrada_1.jpg
```

Atualizar também a linha correspondente em `slides/storyboard_gpio.md` (tabela de fotos, linha do `industrial_entrada_1`) para refletir `botoeira_start`.

- [ ] **Step 6: Verificar no slide real**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_entrada_botoes.md -o /tmp/check_entrada.pdf
pdftoppm -jpeg -r 110 -f 3 -l 3 /tmp/check_entrada.pdf /tmp/check_e3
```

Ler `/tmp/check_e3-3.jpg`. Esperado: foto de botoeira START/verde, coerente com o título "Uma botoeira aciona a partida de um motor".

- [ ] **Step 7: Commit**

```bash
git add slides/gpio_entrada_botoes.md scripts/diagramas/README.md slides/storyboard_gpio.md images/botoeira_start.jpg
git commit -m "fix(slides): trocar foto da botoeira (Entrada #3) - START coerente com a legenda"
```

---

### Task 10: Trocar foto Saída #3 — lâmpada de sinalização

**Files:**
- Modify: `slides/gpio_saida_leds.md:56-66`
- Modify: `scripts/diagramas/README.md`
- Modify: `slides/storyboard_gpio.md` (tabela de fotos)
- Create: `images/lampada_sinalizacao.jpg`
- Delete: `images/industrial_saida_1.jpg` (se não usado em mais nenhum lugar)

**Interfaces:**
- Nenhuma — mesma estrutura da Task 9, aplicada a este slide.

- [ ] **Step 1: Buscar uma foto real de lâmpada de sinalização/piloto**

Ordem de busca: sites de componentes/automação (`eletrogate.com.br`, `filipeflop.com`/`makerhero.com`, `robocore.net`, `squids.com.br`) com termos "lâmpada piloto sinalização 22mm" / "pilot light signal lamp industrial 22mm"; depois Wikimedia Commons ("pilot lamp indicator industrial panel"); depois Google Images/outro mecanismo com "industrial signal light indicator lamp panel"; Pixabay como último recurso.

Critério de aceite: a foto deve mostrar claramente uma luz-piloto/sinalizador (de preferência aceso ou com o elemento translúcido colorido visível) — não um painel genérico sem foco no componente citado.

- [ ] **Step 2: Baixar e salvar como `images/lampada_sinalizacao.jpg`**

- [ ] **Step 3: Atualizar o slide**

Em `slides/gpio_saida_leds.md:56-66`, trocar:

```
### 🏭 Um CLP aciona uma lâmpada de sinalização

![h:420](../images/industrial_saida_1.jpg)

<!--
Frame 1/3 — contexto industrial, abertura. Frase + imagem, sem mais
explicação ainda — a ideia é só ambientar. Foto: Pixabay (licença livre
para uso comercial/educacional, sem atribuição obrigatória) — painel de
máquina com botão luminoso, usado aqui como metáfora visual de
sinalização industrial.
-->
```

por (preencher `<FONTE>`/`<LICENCA>` com o valor real do Step 2):

```
### 🏭 Um CLP aciona uma lâmpada de sinalização

![h:420](../images/lampada_sinalizacao.jpg)

<!--
Frame 1/3 — contexto industrial, abertura. Foto: <FONTE>, <LICENCA> —
lâmpada piloto/sinalizadora real, coerente com o título (substitui a
foto anterior, um painel genérico que não mostrava o componente citado).
-->
```

- [ ] **Step 4: Atualizar `scripts/diagramas/README.md` e `slides/storyboard_gpio.md`**

Mesmo processo da Task 9, Step 4 — substituir a entrada de `industrial_saida_1` pela de `lampada_sinalizacao`.

- [ ] **Step 5: Remover o asset antigo (se órfão)**

```bash
grep -rn "industrial_saida_1" --include="*.md" .
git rm images/industrial_saida_1.jpg
```

- [ ] **Step 6: Verificar no slide real**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_saida_leds.md -o /tmp/check_saida.pdf
pdftoppm -jpeg -r 110 -f 3 -l 3 /tmp/check_saida.pdf /tmp/check_s3
```

Ler `/tmp/check_s3-3.jpg`. Esperado: foto de lâmpada de sinalização real, coerente com o título.

- [ ] **Step 7: Commit**

```bash
git add slides/gpio_saida_leds.md scripts/diagramas/README.md slides/storyboard_gpio.md images/lampada_sinalizacao.jpg
git commit -m "fix(slides): trocar foto da lampada de sinalizacao (Saida #3)"
```

---

### Task 11: Trocar foto Saída #4 — contator

**Files:**
- Modify: `slides/gpio_saida_leds.md:70-76`
- Modify: `scripts/diagramas/README.md`
- Modify: `slides/storyboard_gpio.md` (tabela de fotos)
- Create: `images/contator.jpg`
- Delete: `images/industrial_saida_2.jpg` (se não usado em mais nenhum lugar)

**Interfaces:**
- Nenhuma — mesma estrutura da Task 9/10, aplicada a este slide.

- [ ] **Step 1: Buscar uma foto real de contator**

Ordem de busca: sites de componentes/automação com termos "contator tripolar 220V" / "AC contactor industrial 3 phase"; Wikimedia Commons ("magnetic contactor relay industrial"); Google Images/outro mecanismo com "electrical contactor coil contacts industrial"; Pixabay como último recurso.

Critério de aceite: foto mostrando claramente um contator real (corpo com bobina + contatos visíveis) — não chão de fábrica genérico sem o componente em foco.

- [ ] **Step 2: Baixar e salvar como `images/contator.jpg`**

- [ ] **Step 3: Atualizar o slide**

Em `slides/gpio_saida_leds.md:70-76`, trocar:

```
### ⚙️ Um controlador liga um contator

![h:420](../images/industrial_saida_2.jpg)

<!--
Frame 2/3. Foto: Pixabay — chão de fábrica/automação industrial.
-->
```

por (preencher `<FONTE>`/`<LICENCA>` com o valor real do Step 2):

```
### ⚙️ Um controlador liga um contator

![h:420](../images/contator.jpg)

<!--
Frame 2/3. Foto: <FONTE>, <LICENCA> — contator real (bobina + contatos),
coerente com o título (substitui a foto anterior, de chão de fábrica
genérico que não mostrava o componente citado).
-->
```

- [ ] **Step 4: Atualizar `scripts/diagramas/README.md` e `slides/storyboard_gpio.md`**

Mesmo processo — substituir a entrada de `industrial_saida_2` pela de `contator`.

- [ ] **Step 5: Remover o asset antigo (se órfão)**

```bash
grep -rn "industrial_saida_2" --include="*.md" .
git rm images/industrial_saida_2.jpg
```

- [ ] **Step 6: Verificar no slide real**

```bash
marp --theme-set=slides/theme/s086.css --allow-local-files --pdf slides/gpio_saida_leds.md -o /tmp/check_saida.pdf
pdftoppm -jpeg -r 110 -f 4 -l 4 /tmp/check_saida.pdf /tmp/check_s4
```

Ler `/tmp/check_s4-4.jpg`. Esperado: foto de contator real, coerente com o título.

- [ ] **Step 7: Commit**

```bash
git add slides/gpio_saida_leds.md scripts/diagramas/README.md slides/storyboard_gpio.md images/contator.jpg
git commit -m "fix(slides): trocar foto do contator (Saida #4)"
```

---

### Task 12: Re-export final + verificação de regressão dos 17 pontos

**Files:**
- Modify: `slides/build/gpio_saida_leds.pdf`, `slides/build/gpio_entrada_botoes.pdf` (regravados via script, não editados)

**Interfaces:**
- Consumes: todos os arquivos modificados nas Tasks 1-11.

- [ ] **Step 1: Rodar o build final**

```bash
./scripts/build_slides.sh
```

- [ ] **Step 2: Rasterizar os dois decks completos**

```bash
mkdir -p /tmp/final_saida /tmp/final_entrada
pdftoppm -jpeg -r 110 slides/build/gpio_saida_leds.pdf /tmp/final_saida/slide
pdftoppm -jpeg -r 110 slides/build/gpio_entrada_botoes.pdf /tmp/final_entrada/slide
pdfinfo slides/build/gpio_saida_leds.pdf | grep Pages
pdfinfo slides/build/gpio_entrada_botoes.pdf | grep Pages
```

Expected: Saída continua com 41 páginas; Entrada agora com 34 páginas (33 + 1 do split da Task 8).

- [ ] **Step 3: Conferir os 17 pontos da avaliação original, um a um**

Ler (Ferramenta Read) e confirmar contra `docs/avaliacao_slides_gpio_entrada_saida.md`:

- Deck Saída: slides 3, 4, 7, 11, 14-17, 24, 35, 36, 38 — cada um sem o defeito original listado no relatório.
- Deck Entrada: slides 3, 6, 9 (agora 9 e 10, devido ao split), 13, 25 — cada um sem o defeito original.

Qualquer um que ainda apresente o defeito original volta pra task correspondente antes de prosseguir.

- [ ] **Step 4: Conferir que nada mais regrediu**

Ler pelo menos 3 slides adicionais aleatórios de cada deck (fora da lista de 17) para confirmar que a migração de tema (Task 1) e o split de slide (Task 8) não introduziram nenhum problema novo de contraste/alinhamento.

- [ ] **Step 5: Commit dos PDFs finais**

```bash
git add slides/build/gpio_saida_leds.pdf slides/build/gpio_entrada_botoes.pdf
git commit -m "build: re-exportar PDFs finais com tema, rodape e as 3 causas raiz corrigidas"
```
