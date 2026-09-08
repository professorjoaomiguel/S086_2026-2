# Storyboard — Da Porta Lógica ao Circuito Integrado (Evolução da Eletrônica e dos Semicondutores)

**Status: rascunho de backlog, registrado para expandir em sprint futuro.** Ainda
não quebrado em slide-a-slide (comparar com o nível de detalhe de
`storyboard_gpio.md` quando for a hora de aprofundar) — aqui só o fio condutor
da narrativa e os blocos de conteúdo, na ordem em que a aula foi pensada.

**Formato pretendido:** aula simples, muitas imagens, poucas fórmulas — o peso
da aula é a narrativa falada do professor em cima dos slides (fio condutor
único), não texto/dados densos no slide (diferente do estilo mais denso dos
guias técnicos de GPIO). Cada bloco abaixo tende a virar poucos slides,
majoritariamente visuais (fotos, diagramas, ilustrações), com o professor
narrando a transição entre eles.

**Diretriz de ritmo (quantidade de slides não é fator limitante):** um slide
com uma imagem representando uma única ideia passa rápido — o tempo em aula
é dominado pela fala, não pela contagem de slides. Por isso, quando um bloco
puder ser quebrado em vários frames visuais sequenciais (ex.: uma progressão
tipo "porta → wafer → cidade 3D → CPU" mostrada passo a passo, cada passo em
seu próprio slide), preferir isso a comprimir tudo num slide só — narrativa
mais "cinematográfica" (mais frames por unidade de tempo) rende uma aula mais
dinâmica. Já os slides mais densos (tabelas, comparações, fórmulas) naturalmente
seguram mais tempo cada um — não forçar esses a virarem vários frames. Ou
seja: 50 slides com esse ritmo podem ocupar o mesmo tempo de aula que 25 —
dimensionar a quebra de slides pelo conteúdo/ritmo pretendido, não por um
teto de contagem.

## A tese / fio condutor

A aula percorre uma escala física única, sem pular etapas: do **transistor
individual** → **porta lógica** → **bloco lógico** (somador, ULA) →
**CPU/memória** (tudo isso "gravado" fisicamente num wafer de silício) →
**die frágil precisa de encapsulamento** → **encapsulamento é montado numa
PCB**. A cada etapa, é a mesma pergunta que se repete em escala crescente:
"como isso é construído fisicamente, e por que a etapa seguinte é necessária?"

## Blocos de conteúdo (ordem da narrativa)

1. **Portas lógicas — como são implementadas de verdade**
   Não é uma "caixa preta" AND/OR/NOT: mostrar o circuito com transistor por
   trás de uma porta lógica básica (ex. inversor CMOS, depois NAND/NOR CMOS).
   Ideia central: lógica booleana é implementada como chave elétrica
   (transistor ligado/desligado), não é uma abstração matemática pura.

2. **MOS, CMOS e bipolar — evolução da tecnologia de fabricação**
   Comparar as três famílias de tecnologia usadas para construir a chave do
   item 1: **bipolar** (TTL, mais antiga, maior consumo de corrente), **MOS**
   (NMOS/PMOS puro) e **CMOS** (combinação complementar N+P, dominante hoje).
   Fio condutor: **evolução do consumo de corrente e da tensão de operação**
   ao longo do tempo — de TTL em 5V com consumo estático relevante, passando
   por gerações de CMOS em tensões cada vez menores (5V → 3,3V → 1,8V → abaixo
   de 1V nos processos mais modernos), com o CMOS quase não consumindo
   corrente em repouso (só durante a comutação) — é essa característica que
   permite integrar bilhões de transistores sem derreter o chip. Boa ponte
   com a aula de GPIO já feita (5V do UNO vs. 3,3V do ESP32-S3 como um
   exemplo concreto e já visto pelo aluno dessa mesma tendência histórica).

3. **Layout de circuito integrado: antigo vs. moderno**
   Comparação visual direta de dois die shots (foto do silício por dentro do
   encapsulamento): um CI **antigo/simples** (ex.: um op-amp clássico tipo
   LM741, ou o timer **555**) ao lado de um CI **moderno mas não
   excessivamente complexo** (ex.: die shot de um **Intel Core i3** ou **AMD
   Ryzen**, sem entrar em detalhe arquitetural). Objetivo do slide é puramente
   visual/de escala: mesma ideia de "cidade" do item 5 abaixo, mas comparando
   uma cidade pequena de poucas dezenas/centenas de transistores com uma
   metrópole de bilhões — reforça por que precisou evoluir de bipolar/MOS
   para CMOS (item 2) para essa escala ser fisicamente viável.

4. **Semicondutores e wafers**
   Salto de escala: os blocos lógicos (portas) não são montados um a um como
   componentes discretos — são **fabricados dentro de um wafer de
   semicondutor**. Introduzir o wafer como a "placa-mãe física" onde
   milhões/bilhões de transistores são construídos por processos de
   fabricação (litografia/dopagem, em nível bem simplificado, sem entrar em
   detalhe de processo).

5. **O chip como uma "cidade em 3D"**
   Analogia central da aula: o die de silício visto como uma cidade
   tridimensional — camadas empilhadas, **vias** de conexão (elevadores/ruas
   entre andares), fluxo de corrente e tensão como o "tráfego" que percorre
   essa cidade e implementa funcionalidades específicas dependendo do
   caminho. Boa oportunidade de imagem forte (renderizações de die shot,
   ilustração estilo "cidade" se possível).

6. **De blocos lógicos a blocos funcionais**
   Portas lógicas agrupadas formam blocos maiores com função definida:
   somador → ULA (unidade lógica-aritmética) → CPU. Mostrar a escala
   crescente de composição (porta → bloco → unidade funcional → processador)
   como o mesmo princípio de Lego se repetindo.

7. **Memórias**
   Panorama simples dos tipos de memória (ex. registradores, RAM, ROM/Flash —
   nível de detalhe a decidir na expansão), como parte do mesmo wafer/chip ou
   como chips companheiros.

8. **Por que o circuito integrado precisa de encapsulamento**
   O die de silício é fisicamente frágil e precisa de conexão elétrica para o
   mundo externo. O encapsulamento (ex. epóxi) dá **resistência mecânica** e
   ajuda a **dissipar calor**.

9. **Wire bonds — a conexão interna**
   Dentro do encapsulamento, fios finíssimos (wire bonds) ligam os pontos de
   contato do die de silício aos terminais/pinos do encapsulamento.

10. **Montagem em PCB — PTH vs. SMD**
   Fechamento da aula: o componente encapsulado é finalmente montado numa
   placa de circuito impresso, nas duas tecnologias de montagem — **PTH**
   (through-hole) e **SMD** (surface-mount).

## Pendências para a expansão futura

- Decidir profundidade técnica de cada bloco (ex.: até que ponto entrar em
  CMOS/dopagem/litografia sem perder o público-alvo da disciplina).
- Levantar imagens/fotos reais para cada bloco (die shots, wafers, wire bond
  em microscopia, encapsulamentos PTH/SMD reais, PCBs — mesmo padrão de
  "fotos reais" usado no storyboard de GPIO, cortadas de datasheets ou fotos
  próprias).
- Achar/licenciar os dois die shots do item 3 (antigo: 555 ou LM741; moderno:
  i3 ou Ryzen) — checar direitos de uso de imagem antes de publicar no
  material da disciplina (die shots de fabricante ou de fontes com licença
  clara, ex. fotos de desencapsulamento de hobbistas com atribuição).
- Levantar números reais de tensão/corrente por geração para o item 2 (ex.:
  TTL 5V, CMOS clássico 5V, gerações modernas 3,3V/1,8V/<1V) com fonte
  citável, mesmo padrão de rigor usado nos datasheets do storyboard de GPIO
  (não citar número de memória sem conferir a fonte primária).
- Definir se isso vira 1 deck único ou é dividido em mais de uma aula (o
  material dá para pelo menos 2: "do transistor ao chip" e "do die à PCB").
- Escolher onde entram exemplos concretos das placas do curso (ATmega328P,
  ESP32-S3) como estudo de caso de "isso que você acabou de ver por dentro é
  o chip que você já usa no laboratório".
- Guia técnico correspondente (se fizer sentido para este tema, dado que é
  mais conceitual/história da tecnologia do que prático como os guias de
  GPIO).
