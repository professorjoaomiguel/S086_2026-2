# Design — Template Marp compartilhado + correção das 3 causas raiz (decks GPIO)

Data: 2026-09-12
Contexto: `docs/avaliacao_slides_gpio_entrada_saida.md` avaliou os 74 slides dos
decks "Do LED ao GPIO" (saída) e "Do Botão ao GPIO" (entrada) contra
`docs/rubric_avaliacao_slides.md` e encontrou 17 slides com observação,
agrupáveis em 3 causas raiz. Este documento define como corrigir essas 3
causas E, ao mesmo tempo, estabelecer um template Marp compartilhado
(tema + rodapé + script de build) como convenção sistêmica para os decks
futuros do S086 — sem retrofit de decks fora do escopo GPIO nesta rodada.

## Escopo

- Só os 2 decks GPIO existentes (`slides/gpio_saida_leds.md`,
  `slides/gpio_entrada_botoes.md`) são corrigidos/migrados nesta rodada.
- O template compartilhado é construído de forma que decks **futuros**
  herdem automaticamente (referenciando o mesmo tema), mas nenhum outro
  deck/storyboard existente (ex. `storyboard_semicondutores.md`) é tocado
  agora.

## Ordem de execução

**Fluxo B (infraestrutura) primeiro, Fluxo A (correção de conteúdo)
depois** — decisão do usuário, para terminar com um único re-export dos
PDFs já com tudo corrigido, em vez de exportar duas vezes.

## Fluxo B — Template Marp compartilhado

### Tema

Novo arquivo `slides/theme/s086.css`, tema Marp real (`/* @theme s086 */`
no topo). Migra pra lá o bloco `style: |` hoje duplicado nos dois decks:
cores de `section.lead`, `section.pausa-previsao/calculo/garimpo`,
`section.revelacao`, `section.alerta`, `.columns`, `table`, `img`.

Frontmatter dos dois decks passa a ser:
```
---
marp: true
theme: s086
paginate: true
footer: '@professorjoaomiguel'
---
```

### Rodapé

- Numeração de página: mantém o contador nativo do Marp (`paginate: true`),
  sem mudar posição/estilo — hoje já fica no canto inferior direito.
- Handle: usa a diretiva nativa `footer:` do Marp (frontmatter,
  aplicada a todo slide automaticamente) com `@professorjoaomiguel`,
  estilizado no tema pra ancorar no canto inferior **esquerdo**.
- Aplica em **100% dos slides**, sem exceção de classe (capa, pausas,
  revelação, alerta incluídos) — decisão do usuário.

### Script de build

Novo `scripts/build_slides.sh` (bash — ambiente já usa git-bash/poppler
nesta sessão), sem `package.json`/npm:
```bash
#!/usr/bin/env bash
set -euo pipefail
marp --theme-set slides/theme --pdf slides/gpio_saida_leds.md -o slides/build/gpio_saida_leds.pdf
marp --theme-set slides/theme --pdf slides/gpio_entrada_botoes.md -o slides/build/gpio_entrada_botoes.pdf
```
Motivo: `--theme-set` é fácil de esquecer digitando o comando na mão;
um script elimina esse risco e vira o jeito único de exportar.

### Storyboard como spec

`slides/storyboard_gpio.md` ganha uma seção curta "Template e convenções
de produção" apontando para `slides/theme/s086.css` e
`scripts/build_slides.sh` como fonte única de como o deck é gerado — sem
duplicar CSS/código Marp dentro do storyboard (o storyboard continua
sendo prosa + spec, não markup Marp real).

### `.ai/AGENTS.md`

Como é a fonte única de instruções pra agentes de IA no repo, ganha uma
linha nova documentando o tema compartilhado + o script de build, ao
lado da menção já existente ao fluxo storyboard-antes-do-deck.

## Fluxo A — Correção das 3 causas raiz

### Causa 1 — diagramas SchemDraw cortando GND/rótulo na borda do frame

Afeta 5 scripts: `npn_chave_low_side.py` (Saída #35),
`mosfet_n_chave_low_side.py` (Saída #36), `mosfet_p_chave_high_side.py`
(Saída #38), `gpio_pullup.py` (Entrada #25), `botao_na_nf.py`
(Entrada #9).

- `gpio_pullup.py`: causa já identificada — `elm.Switch()...label("Botão",
  loc="left")` num elemento `.down()` usa `loc="left"` explícito, indo
  contra a própria lição já documentada no README ("`loc=` explícito
  tende a rotacionar pro lado oposto em elemento vertical; o padrão sem
  `loc=` costuma bastar"). Fix: remover o `loc="left"` explícito,
  regenerar, inspecionar.
- Os outros 4 scripts: mesma classe de bug (rótulo/GND estourando a bbox
  calculada pelo SchemDraw) — corrigir script a script (ajustar `loc`,
  `unit`, ou espaçamento vertical do componente final), regenerar
  `.png`, inspecionar visualmente antes de considerar pronto (mesma
  disciplina já documentada no README). Adicionar 1 lição nova ao README
  (`scripts/diagramas/README.md`, seção "Notas de layout SchemDraw")
  sempre que a causa raiz encontrada for diferente da já documentada.
- Sem refatoração de um helper compartilhado — 5 fixes pontuais, risco
  baixo, não mexe nos scripts que já funcionam (ex. `pnp_chave_high_side.py`,
  slide 37, que usa o mesmo tipo de circuito sem cortar).

### Causa 2 — foto incoerente com a legenda

Afeta Saída #3, Saída #4, Entrada #3. Decisão do usuário: **trocar a
foto** nos 3 casos (não reescrever a legenda), buscando fonte real do
componente certo:
- Entrada #3: botoeira START/verde (troca a atual, que mostra "PUSH TO
  STOP" contradizendo a legenda "aciona a partida de um motor")
- Saída #3: lâmpada de sinalização/piloto real
- Saída #4: contator real (bobina + contatos)

Ampliar a busca além do que já foi usado no levantamento original
(Wikimedia Commons, Pixabay, Eletrogate): incluir mais sites de venda de
componentes (Filipeflop/MakerHero, Robocore, squids.com.br — já
registrado como referência) e busca de imagem via Google Images/outros
mecanismos de busca, com termos de busca específicos em PT/EN (nome
técnico do componente, não termo genérico). Seguir a mesma disciplina de
licença/atribuição já documentada em `scripts/diagramas/README.md`
("Fotos reais") — foto comercial de catálogo é aceitável com fonte
citada no comentário do slide, licença aberta (Wikimedia/CC) exige
atribuição, foto própria é preferível quando existir.

### Causa 3 — rótulo do diagrama de blocos colidindo com caixa/seta

Afeta Saída #7 e Entrada #6 — mesmo PNG (`gpio_interface_conceito.py`)
usado nos dois decks. Causa já confirmada no código: a seta de "SAÍDA
(LED) põe tensão" ancora em `y=1.5` com `loc="top"`, mas o retângulo vai
até `y=2.2` — sobra só 0.7 unidade pra empilhar as 3 linhas do rótulo
antes de esbarrar na borda do retângulo. Fix: afastar o ponto de
ancoragem da seta da borda do retângulo, ou mover o rótulo pra fora
(`loc` diferente) em vez de empilhar por cima. Corrige o script uma vez,
regenera 1 imagem, resolve os 2 slides simultaneamente.

## Re-export final

Depois de Fluxo A completo, rodar `scripts/build_slides.sh` uma única
vez para gerar os PDFs finais com tema+rodapé+correções todos juntos.

## Fora de escopo (explicitamente)

- Migrar `storyboard_semicondutores.md` ou qualquer deck futuro para o
  novo tema agora.
- Refatorar os scripts de diagrama que já funcionam corretamente.
- Reescrever legendas em vez de trocar foto (decisão do usuário: sempre
  trocar foto nos 3 casos da Causa 2).
