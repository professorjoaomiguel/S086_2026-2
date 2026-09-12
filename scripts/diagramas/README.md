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
- Confirmado de novo nesta rodada: `loc=` explícito em elemento vertical
  colidindo com outro rótulo próximo (`gpio_pullup.py` — `Botão` com
  `loc="left"` colidindo com o rótulo do GND; `mosfet_p_chave_high_side.py`
  — `R_pullup` com `loc="bottom"` colidindo com `VCC`/`R_gate`) — reforça a
  lição acima: prefira o `loc` padrão e só ajuste depois de ver o render.
- Fio de retorno/conexão cruzando um rótulo de várias linhas: a correção
  certa é alongar o trecho vertical antes da curva do fio (dar mais
  espaço ao rótulo), não mover o rótulo em si.
- **Lição mais valiosa desta rodada:** quando um diagrama aparece "cortado"
  no slide renderizado, renderize primeiro o PNG isolado (fora do Marp)
  antes de supor que o script SchemDraw está com bug — nesta rodada, 3 dos
  5 diagramas aparentemente cortados eram na verdade overflow do frame do
  Marp (texto demais empurrando a imagem para baixo), não bug no script. O
  render isolado diz de imediato qual dos dois problemas você realmente tem.

## Fotos reais (não geradas por script)

Não são diagramas gerados, mas registradas aqui por serem parte do mesmo
levantamento de imagens do storyboard. Todas as 12 fotos da tabela de
`slides/storyboard_gpio.md` estão resolvidas.
- `led_smd.png`, `led_rgb.png`, `chave_d2f.png` — recortadas via PyMuPDF
  (`pip install pymupdf`) da página 1 dos datasheets já baixados em
  `datasheets/leds/` e `datasheets/botoes/` (script ad-hoc, não versionado
  — renderizar a página 1 em alta resolução e cortar a região da foto).
- `industrial_saida_3.jpg` — foto de estoque do Pixabay (licença
  livre, uso comercial/educacional sem atribuição obrigatória), buscada
  via WebSearch/WebFetch.
- `contator.jpg` — Wikimedia Commons, "Contactor DIN IEK.jpg" (autor Kae,
  CC BY-SA 3.0 / GFDL, **exige atribuição**, incluída no comentário do
  slide correspondente e na tabela de `slides/storyboard_gpio.md`) —
  contator tripolar (3 polos) real, IEK KMI-11810, mostrando claramente
  bobina (terminais A1/A2) e contatos principais (L1/L2/L3 → T1/T2/T3).
  Baixada via `https://commons.wikimedia.org/wiki/Special:FilePath/<nome-do-arquivo>`.
  Substitui `industrial_saida_2.jpg` (foto Pixabay de chão de fábrica
  genérico que não mostrava o componente citado).
- `lampada_sinalizacao.jpg` — foto de produto do vendor MakerHero
  ("Sinaleiro LED Iluminado 22mm",
  https://www.makerhero.com/produto/sinaleiro-led-iluminado-22mm/), foto
  comercial de catálogo (não open-licensed, uso educacional/ilustrativo,
  como outras fotos de vendor já usadas no deck) — mostra claramente a
  lâmpada piloto/sinalizadora com lente translúcida colorida.
- `led_tht.jpg`, `chave_boia.jpg`, `industrial_entrada_2.jpg`,
  `botoeira_start.jpg` — fotos do Wikimedia Commons. As três primeiras
  são CC BY / CC BY-SA (**exigem atribuição**, incluída no comentário do
  slide correspondente e na tabela de `slides/storyboard_gpio.md`);
  `botoeira_start.jpg` ("Start_Stop_Power_Switch.jpg", Michael Holley /
  Swtpc6800) é domínio público (PD-self, atribuição não obrigatória, mas
  citada mesmo assim por boa prática). Baixadas via
  `https://commons.wikimedia.org/wiki/Special:FilePath/<nome-do-arquivo>`
  (redireciona pro arquivo original — mais confiável do que pedir pro
  WebFetch "listar a URL exata" de uma página de busca, que às vezes
  alucina/deforma o caminho com hash).

- `botao_pushbutton.jpg` — nem Pixabay nem Wikimedia Commons tinham uma
  foto de qualidade desse componente especificamente (pequeno/genérico
  demais pra ter foto dedicada nesses bancos). Resolvida com foto de
  catálogo do fornecedor **Eletrogate.com.br** ("Push Button (Chave
  Táctil) 6x6x7mm") — foto comercial, **não** licença aberta; uso
  educacional/ilustrativo em material de aula, com fonte citada no
  comentário do slide. Diferente das fotos Pixabay/Commons acima, que têm
  licença livre explícita.

**Nota sobre os bancos usados:** Pixabay tem cobertura fraca pra peças
eletrônicas/industriais de nicho, mas boa pra fotos amplas de
painel/quadro de comando industrial. Wikimedia Commons é o oposto — fraco
pra fotos "de estoque" genéricas, mas tem fotos reais de componentes
técnicos específicos (fim-de-curso, chave-boia, LED THT) contribuídas por
hobbistas/engenheiros, sempre com licença que exige atribuição. Sites de
venda de componentes eletrônicos (Eletrogate, Filipeflop/MakerHero,
Robocore etc.) são o melhor lugar pra achar a foto exata de um componente
"de kit" pequeno e padronizado (pushbutton tátil, resistor, jumper) que
não é fotografado por hobbistas nem por bancos de imagem — mas a foto é
comercial (catálogo do fornecedor), não licença aberta; citar a fonte no
comentário do slide é obrigatório. Filipeflop bloqueou o fetch direto
(HTTP 403); Eletrogate funcionou sem problema.
