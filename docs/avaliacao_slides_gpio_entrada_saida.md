# Avaliação slide-a-slide — Decks GPIO (Saída/LEDs + Entrada/Botões)

Avaliação feita sobre as páginas **renderizadas** (rasterizadas do PDF exportado, 110dpi), não sobre o texto-fonte `.md`, seguindo `docs/rubric_avaliacao_slides.md`. 41 slides no deck Saída, 33 no deck Entrada — 74 no total, todos inspecionados individualmente.

Apenas o que falhou ou é digno de nota está listado; slides sem problema real são citados em uma linha, sem tabela.

---

## Deck "Do LED ao GPIO" (Saída)

Slides sem problemas reais (OK nos 4 blocos do rubric): **1, 2, 5, 6, 8, 9, 10, 12, 13, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 39, 40, 41**.

| # | O que falha | Bloco do rubric | Sugestão concreta |
|---|---|---|---|
| 3 | Foto (painel de CNC com botão de emergência/chaves rotativas) não mostra uma lâmpada de sinalização, mas o título/legenda promete isso — imagem não sustenta a afirmação do texto | Mayer — Coerência | Trocar por foto de luz-piloto/sinalizador aceso, ou reescrever o texto para descrever o que a foto de fato mostra |
| 4 | Foto (chão de fábrica genérico) não mostra um contator — legenda promete componente específico que a imagem não evidencia | Mayer — Coerência | Substituir por foto real de contator (bobina + contatos) ou datasheet, no mesmo padrão de fidelidade dos slides 9–10 |
| 7 | Rótulo "SAÍDA (LED) põe tensão" do diagrama de blocos fica colado/tocando a linha da seta de saída, sem respiro | CRAP — Alinhamento/Proximidade | Adicionar espaço vertical entre o rótulo e a seta, ou mover o rótulo para cima do traço |
| 11 | Foto do LED RGB tem fundo preto (recorte de produto), destoando do padrão de fundo neutro usado nas outras fotos de componente do deck | CRAP — Repetição | Recortar/tratar com fundo neutro consistente, ou assumir como exceção deliberada (imagem de datasheet) |
| 14–17 | Quatro slides seguidos (V_F por cor) só com texto — espaço em branco considerável sem elemento visual que reforce o achado central ("todas as cores batem em 2,2V") | Sweller — germinativa (oportunidade perdida) / Mayer — Coerência | Fechar a sequência (slide 17) com mini-gráfico/tabela comparativa de V_F por cor, consolidando visualmente o padrão |
| 24 | Última frase do slide é cortada pela borda inferior do frame ("...não assumir" fica truncado/colado na margem) | CRAP — Alinhamento / Mayer — Contiguidade espacial | Encurtar o texto ou remover 1 linha acima para a frase final caber inteira; alternativa: reduzir para sub-bullet menor |
| 35 | Diagrama SchemDraw (chave low-side NPN): retorno/GND do circuito cortado na borda inferior, símbolo de terra ausente/incompleto | CRAP — Alinhamento; Mayer — Contiguidade espacial | Reduzir altura do diagrama (compactar espaçamento vertical) ou reescalar para caber com margem |
| 36 | Mesmo padrão do #35: diagrama MOSFET-N (low-side) com traço de retorno a GND cortado/colado na borda | CRAP — Alinhamento; Mayer — Contiguidade espacial | Mesma correção do #35 |
| 38 | Diagrama MOSFET-P (high-side): resistor de carga é o último elemento visível sem símbolo de terra que feche o circuito, cortado pela borda | CRAP — Alinhamento; Mayer — Contiguidade espacial | Mesma correção do #35/#36 |

Observação (não é falha): o slide 37 usa o mesmo tipo de diagrama dos 35/36/38 (chave high-side PNP) e **não** apresenta corte — reforça que o problema é de altura específica de cada render, não do template.

---

## Deck "Do Botão ao GPIO" (Entrada)

Slides sem problemas reais (OK nos 4 blocos do rubric): **1, 2, 4, 5, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 29, 30, 32**.

| # | O que falha | Bloco do rubric | Sugestão concreta |
|---|---|---|---|
| 3 | Foto da botoeira mostra "PUSH TO STOP" gravado no botão, mas a legenda diz "aciona a partida de um motor" — a imagem sugere parar, o texto diz iniciar | Mayer — Coerência | Trocar por botoeira START/verde, ou reescrever a legenda para "interrompe a partida de um motor", coerente com a foto atual |
| 6 | Rótulo "SAÍDA (LED) põe tensão" do diagrama de blocos sobrepõe a borda superior do retângulo "MICROCONTROLADOR (GPIO)" | CRAP — Alinhamento / Mayer — Contiguidade espacial | Aumentar espaçamento vertical entre o rótulo e o topo do retângulo (mover ~15–20px) |
| 9 | Os dois mini-diagramas (NA/NF) na parte inferior são cortados pela borda do frame, faltando o retorno/terra visível | CRAP — Alinhamento / Sweller — Extrínseca | Reduzir altura dos dois circuitos ou subir o bloco de texto para abrir espaço, garantindo que o GND apareça inteiro |
| 13 | Rótulo "segura (LOW)" do gráfico fica colado/muito próximo à linha de tensão plotada, competindo visualmente com o traço | CRAP — Proximidade / Mayer — Contiguidade espacial (falha menor) | Deslocar o rótulo para cima/esquerda ou usar leader line |
| 25 | Diagrama de pull-up: rótulo "Botão" colado/cortado na borda inferior junto com o traço do símbolo de chave incompleto (compare com #27, mesmo tipo de diagrama, onde funciona) | CRAP — Proximidade / Mayer — Contiguidade espacial | Subir a margem inferior do SchemDraw ou reduzir altura do circuito ~15–20%; replicar o layout do #27 |

Observação (não é falha): slides 23, 31 e 33 têm bastante espaço vazio na metade inferior do frame (texto curto). Compatível com "segmentação" (uma ideia por slide), mas registrado caso o padrão se repita em decks futuros. Slide 33 (encerramento) é minimalista — decisão de conteúdo, não falha de design.

---

## Padrões sistêmicos (causa raiz, não repetição por slide)

### 1. Diagramas SchemDraw estourando a altura do frame, cortando o retorno/GND
**Slides afetados: Saída #35, #36, #38; Entrada #9, #25** — 5 slides no total (o rubric, com base em amostra anterior, havia identificado apenas 3: Entrada #6, Entrada #25, Saída #38; a inspeção exaustiva desta rodada confirma #25 e #38, mas reclassifica Entrada #6 como problema diferente — ver padrão 3 — e encontra 2 casos adicionais não catalogados antes: Saída #35, #36, e Entrada #9).

Todos são circuitos com transistor/MOSFET/chave + resistor + LED empilhados verticalmente, onde o símbolo de terra (GND) fica na base do circuito e é a primeira vítima do corte de frame. O contraponto (Saída #37) prova que o mesmo template, quando o circuito é ~1 elemento mais curto, cabe com folga — é um problema de altura/margem por render individual, não do template SchemDraw em si.

**Correção de causa raiz sugerida**: revisar o script de geração desses diagramas específicos (circuitos com 5+ elementos empilhados) para reduzir o espaçamento vertical entre elementos ou aumentar a margem inferior padrão, e regerar os 5 diagramas afetados — não é necessário mexer nos diagramas que já cabem (ex. #37, #12).

### 2. Fotos que não sustentam a legenda (falha de Coerência/Mayer)
**Slides afetados: Saída #3, Saída #4, Entrada #3** — em todos os três, a legenda promete um componente ou comportamento específico (lâmpada de sinalização, contator, "partida" de motor) e a foto mostra outra coisa (painel genérico, chão de fábrica, ou o oposto textual gravado no próprio botão). É o mesmo tipo de gap já registrado como feedback do professor sobre fidelidade de imagem — aqui são casos concretos e localizáveis.

### 3. Rótulo de diagrama de blocos colidindo com a caixa/seta (não é o mesmo problema do padrão 1 — aqui é diagrama conceitual, não circuito SchemDraw)
**Slides afetados: Saída #7, Entrada #6** — parece ser o mesmo asset de diagrama de blocos "GPIO de saída" reaproveitado nos dois decks, com margem de rótulo insuficiente nos dois casos. Corrigir o asset uma vez (adicionar respiro entre rótulo e seta/caixa) resolve ambos os slides.

---

## O que já está funcionando bem

- **Segmentação**: ponto mais forte dos dois decks — "um slide, uma ideia" é seguido com disciplina; nenhuma parede de texto encontrada nas 74 páginas.
- **Repetição/consistência visual**: cores por tipo de slide (pausa/alerta/revelação), posição de ícone+título e estilo de capa/encerramento são consistentes e prováveis do deck inteiro — só 1 exceção pontual (Saída #11, fundo da foto).
- **Redundância**: texto telegráfico, não é o roteiro do professor lido em voz alta.
- **Contraste WCAG**: nenhuma combinação fundo/texto encontrada chega perto do limite — segue confirmado que não é um problema neste deck.
- **Sinalização**: negrito usado com moderação em pontos-chave, sem poluição.
- **Carga germinativa**: pausas de previsão/cálculo/garimpo (ex. slide 29, comparação UNO vs ESP32-S3 lado a lado) são exemplos de worked examples bem construídos — referência de boa prática, não mexer.
- A maioria esmagadora dos slides (57 de 74) não teve nenhuma observação real — os problemas encontrados são localizados e concentram-se em 3 causas raiz claras, não espalhados aleatoriamente pelo deck.
