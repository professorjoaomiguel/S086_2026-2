# Diagramas de produção — Storyboard GPIO

Diagramas finais (não exemplos) usados nos decks/guias de GPIO, gerados a
partir de `slides/storyboard_gpio.md` (seção "Diagramas e fotos
necessários"). Saída em `.svg` (preferir em Markdown/Marp) e `.png` em
`../../images/`. Distinto de `.ai/docs/diagramas/`, que é só a área de
teste/exemplo do SchemDraw.

## Uso

```bash
pip install schemdraw matplotlib numpy
python led_circuito_basico.py
```

Cada script gera seu próprio par `.svg`/`.png` em `images/`; rodar todos:

```bash
for f in *.py; do python "$f"; done
```

## Esquemáticos/bloco (SchemDraw)

| Script | Diagrama # | Conteúdo |
|---|---|---|
| `led_circuito_basico.py` | 1 | Fonte genérica + resistor + LED, sem microcontrolador |
| `led_ativo_alto.py` | 2 | LED ânodo no GPIO — HIGH acende |
| `led_ativo_baixo.py` | 3 | LED cátodo no GPIO — LOW acende |
| `npn_chave_low_side.py` | 4 | Chave low-side com transistor NPN |
| `mosfet_n_chave_low_side.py` | 5 | Chave low-side com MOSFET-N + pull-down no gate |
| `pnp_chave_high_side.py` | 6 | Chave high-side com transistor PNP (lógica invertida) |
| `mosfet_p_chave_high_side.py` | 7 | Chave high-side com MOSFET-P + pull-up no gate |
| `botao_circuito_basico.py` | 8 | Fonte genérica + resistor + botão, sem microcontrolador |
| `gpio_pullup.py` | 11 | Pull-up externo — entrada ativo-baixa, dois estados anotados |
| `gpio_pulldown.py` | 12 | Pull-down externo — entrada ativo-alta, dois estados anotados |
| `gpio_interface_conceito.py` | 14 | Bloco: GPIO como interface elétrica (saída/entrada) |
| `botao_na_nf.py` | 15 | Contraste NA (I≈0 em repouso) vs NF (I≈V/R em repouso) |

## Formas de onda / gráficos (matplotlib)

| Script | Diagrama # | Conteúdo |
|---|---|---|
| `botao_forma_onda_bounce.py` | 9 | Tensão×tempo: bounce mecânico com resistor de referência |
| `botao_forma_onda_flutuante.py` | 10 | Mesmo eixo, pino flutuante sem resistor — ruído contínuo |
| `niveis_logicos_limiares.py` | 13 | Faixas V_IL/V_IH: ATmega328P (5V) vs ESP32-S3 (3,3V) |

## Convenção de anotação

Cada componente relevante leva o valor numérico (tensão e/ou corrente) do
exemplo mostrado, não só o nome — ver `slides/storyboard_gpio.md` para a
convenção completa (inclusive os dois estados idle/pressionado anotados
nos diagramas de pull-up/pull-down).

## Notas de layout SchemDraw (lições desta sessão)

- Em elemento vertical (`.up()`/`.down()`), o rótulo por padrão (sem
  `loc=`) cai à esquerda do traço — costuma bastar. `loc="top"`/`"bottom"`
  tendem a mover o rótulo para o lado oposto (a rotação do elemento
  rotaciona também o referencial do `loc`); testar visualmente.
- Para ramificar dois componentes do mesmo nó (ex.: R_gate e R_pulldown
  saindo do gate), criar um `elm.Dot().at(nó)` explícito e usar
  `.at(dot.center)` nos dois ramos — evita que um resistor comece "no
  meio" do outro.
- Sempre gerar o `.png` e inspecionar visualmente antes de considerar um
  diagrama pronto — sobreposição de texto é comum e só aparece no render.

## Pendente (não gerado por script)

Fotos reais — não são diagramas gerados, mas registradas aqui por serem
parte do mesmo levantamento de imagens do storyboard.

**Resolvidas:**
- `led_smd.png`, `led_rgb.png`, `chave_d2f.png` — recortadas via PyMuPDF
  (`pip install pymupdf`) da página 1 dos datasheets já baixados em
  `datasheets/leds/` e `datasheets/botoes/` (script ad-hoc, não versionado
  — renderizar a página 1 em alta resolução e cortar a região da foto).
- `industrial_saida_1/2/3.jpg`, `industrial_entrada_1.jpg` — fotos de
  estoque do Pixabay (licença livre, uso comercial/educacional sem
  atribuição obrigatória), buscadas via WebSearch/WebFetch.
- `led_tht.jpg`, `chave_boia.jpg`, `industrial_entrada_2.jpg` — fotos do
  Wikimedia Commons (CC BY / CC BY-SA — **exigem atribuição**, incluída
  no comentário do slide correspondente e na tabela de
  `slides/storyboard_gpio.md`). Baixadas via
  `https://commons.wikimedia.org/wiki/Special:FilePath/<nome-do-arquivo>`
  (redireciona pro arquivo original — mais confiável do que pedir pro
  WebFetch "listar a URL exata" de uma página de busca, que às vezes
  alucina/deforma o caminho com hash).

**Nota sobre os bancos usados:** Pixabay tem cobertura fraca pra peças
eletrônicas/industriais de nicho, mas boa pra fotos amplas de
painel/quadro de comando industrial. Wikimedia Commons é o oposto — fraco
pra fotos "de estoque" genéricas, mas tem fotos reais de componentes
técnicos específicos (fim-de-curso, chave-boia, LED THT) contribuídas por
hobbistas/engenheiros, sempre com licença que exige atribuição.

**Ainda pendente:** `botao_pushbutton` (tactile 4 pinos genérico) — nenhum
dos dois bancos tem uma foto de qualidade desse componente especificamente
(pequeno/genérico demais pra ter foto dedicada). Melhor caminho: foto
própria de uma peça do kit em mãos.
