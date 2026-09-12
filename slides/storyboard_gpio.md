# Storyboard — GPIO: Entrada (Botões) e Saída (LEDs)

Rascunho para revisão antes de escrever os 2 decks Marp e os 2 guias técnicos.
Placas de referência em todos os exemplos: **Arduino UNO R3** (ATmega328P, 5V)
e **ESP32-S3-UNO** (ESP32-S3, 3,3V), lado a lado.

**Princípio de ordenação:** em cada deck, o circuito básico (LED+resistor ou
botão+resistor) é ensinado **antes** de entrar em GPIO/microcontrolador —
primeiro o conceito de eletrônica com uma fonte genérica, depois "trocamos a
fonte genérica pelo pino do microcontrolador" e herdamos as regras de níveis
lógicos/corrente que isso traz.

**A tese que conecta os dois decks:** o GPIO é a interface elétrica entre o
mundo do microcontrolador e o mundo físico externo. Na aula de **saída**, o
microcontrolador **põe** uma tensão no mundo (aciona o LED). Na aula de
**entrada**, ele **lê** uma tensão que vem do mundo (o botão). Ambos os decks
abrem com essa mesma ideia (deck de Saída na íntegra, deck de Entrada como
retomada), para o aluno perceber que é a mesma fronteira elétrica em dois
sentidos — não duas APIs desconectadas.

**Diretriz de ritmo (contagem de slides não é fator limitante):** um slide
com uma imagem representando uma única ideia passa rápido em aula — o tempo
é dominado pela fala do professor, não pela contagem de slides. Por isso,
blocos que puderem ser quebrados em vários frames visuais sequenciais (uma
progressão mostrada passo a passo, cada passo em seu próprio slide) preferem
isso a comprimir tudo num slide só — ritmo mais "cinematográfico" rende uma
aula mais dinâmica. Já os slides mais densos (tabelas, comparações, fórmulas)
seguram mais tempo cada um e não precisam virar vários frames. Aplicado
abaixo em 4 pontos: a abertura conceitual do GPIO (3 frames), as fotos reais
de LED (3 frames) e de botão/chave (2 frames), a revelação do V_F por cor
(4 frames) e as quatro topologias de chave/transistor (4 frames em vez de
2 slides emparelhados).

**Convenção de pausas ativas:** cada deck tem 5 slides de pausa — visualmente
distintos (fundo/cor diferente, ícone de tipo), sem revelar a resposta no
mesmo slide (a resposta vem no slide seguinte). Três tipos:

- 🔮 **Previsão** — pergunta aberta, sem cálculo, respondida antes de ver o
  diagrama/dado real. O objetivo é criar expectativa para a revelação
  seguinte, não acertar.
- 🧮 **Cálculo** — aplicar uma fórmula já ensinada a um caso novo, antes do
  próximo exemplo trabalhado ser mostrado.
- 🔍 **Garimpo no datasheet** — abrir um PDF já baixado em `datasheets/` e
  achar um número específico, cronometrado (~2 min).

**Regra de produção para a revelação:** o slide seguinte a uma pausa mostra
só o fato/valor (ex.: "Vermelho — 2,2V @ 20mA"), **nunca** um rótulo
"Resposta:" impresso. A revelação acontece pela discussão oral — o
professor pergunta "quem chutou X? quem chegou perto?" — não pela leitura
de um gabarito na tela. Onde o storyboard abaixo anota entre parênteses o
valor calculado de uma pausa 🧮 (ex. slide de cálculo do LED verde), é nota
de produção para o professor conferir, não texto a imprimir no slide.

**Regra de produção geral: um slide, uma ideia.** Evitar empilhar
imagem + fórmula + código + tabela no mesmo slide — quando isso acontecer
naturalmente ao escrever o `.md`, quebrar em vários slides (pergunta →
circuito → observação → fórmula → cálculo → conclusão) em vez de
comprimir. Isso é uma extensão direta da diretriz de ritmo cinematográfico
acima, a aplicar também na hora de escrever os decks Marp de verdade (o
storyboard já aponta a divisão macro; a divisão fina de cada slide denso
acontece na produção).

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

## Diagramas e fotos necessários

Scripts em `scripts/diagramas/`, saída (`.svg` + `.png`) em `images/`.
Esquemáticos e diagramas de bloco via SchemDraw; formas de onda e o gráfico
de faixas de tensão via matplotlib direto (mesma dependência do SchemDraw).
As fotos reais (não geradas por script — recortadas das capas dos datasheets
já baixados em `datasheets/leds/` e `datasheets/botoes/`, ou foto própria de
uma peça em mãos) agora viram sequências de frames, um componente por slide,
em vez de um slide só com várias fotos juntas.

**Convenção de anotação (todos os esquemáticos):** cada componente relevante
leva o valor numérico de tensão e/ou corrente que está sob ele no exemplo
mostrado — não só o nome/rótulo. Ex.: a fonte traz o valor da tensão (`5V`,
`3,3V`, ou um valor genérico tipo `9V` nos circuitos sem GPIO); o LED traz a
queda direta V_F usada no exemplo (ex. `V_F ≈ 2,2V`) e a corrente que passa
por ele (ex. `I ≈ 10mA`); o resistor traz o valor calculado (ex. `R = 330Ω`)
e a queda de tensão sobre ele (`V_R = V_fonte − V_F`, reforçando que o
resistor limita **corrente**, a tensão excedente é quem "sobra" nele); nos
transistores, a tensão/corrente de acionamento na base/gate e a corrente de
carga no coletor/dreno. Nas formas de onda, o eixo de tensão é anotado com
os níveis HIGH/LOW/zona indefinida (não só uma curva sem escala).

**Estados dos dois lados do pino (pull-up/pull-down):** os diagramas 11
(`gpio_pullup`) e 12 (`gpio_pulldown`) anotam a tensão no pino nos **dois
estados** — solto (idle) e pressionado —, não só um. Pull-up: pino ≈VCC
solto, pino ≈0V pressionado (o botão aterra). Pull-down: pino ≈0V solto,
pino ≈VCC pressionado. Mesma ideia nos diagramas de LED (1, 2, 3): anotar a
tensão no pino/GPIO e a queda sobre o LED (V_F) e o resistor no estado
**aceso** (é o estado de interesse — é quando a corrente calculada
realmente circula).

**Sem números "de gaveta" no slide para corrente do ESP32-S3:** o diagrama e
o slide de limite de corrente por pino carregam só o **princípio**
(dimensionar de forma conservadora, nunca pelo limite absoluto) — os mA
específicos por chip (que variam com a fonte/documentação exata) ficam
reservados ao guia técnico, citando o datasheet usado. **Mesma decisão vale
para o valor do resistor de pull-up/pull-down** (tipicamente 10kΩ, mas
depende do valor do resistor interno do chip quando se usa `INPUT_PULLUP`):
o deck fica só com o princípio de que o valor precisa ser "alto o bastante
para não desperdiçar corrente parado, baixo o bastante para vencer
ruído/capacitância" — o valor numérico específico de cada placa vai para o
guia técnico. **Cuidado para o guia:** o resistor interno de pull-up/pull-down
do ESP32-S3 é de ≈45kΩ (datasheet oficial) — isso **não** é o valor
recomendado para o resistor **externo** usado nos diagramas 11/12 (esses
costumam ficar na faixa de 1k–10kΩ, por critérios diferentes de
ruído/consumo/tempo de resposta). Deixar essa distinção explícita no guia
para ninguém usar 45kΩ como resistor externo por engano.

| # | Arquivo (sem extensão)       | Tipo             | Conteúdo                                                              | Usado em |
|---|--------------------------------|------------------|--------------------------------------------------------------------------|-----------|
| 1 | `led_circuito_basico`         | esquemático      | Fonte genérica (pilha) + resistor + LED, sem microcontrolador             | Deck Saída, slide 12 |
| 2 | `led_ativo_alto`              | esquemático      | LED com ânodo no GPIO, cátodo→resistor→GND                                | Deck Saída, slide 23 |
| 3 | `led_ativo_baixo`             | esquemático      | LED com cátodo no GPIO, ânodo→resistor→VCC                                | Deck Saída, slide 24 |
| 4 | `npn_chave_low_side`          | esquemático      | NPN como chave low-side: GPIO→R base→base; carga no coletor               | Deck Saída, slide 35 |
| 5 | `mosfet_n_chave_low_side`     | esquemático      | MOSFET-N como chave low-side: GPIO→R gate (+pull-down); carga no dreno    | Deck Saída, slide 36 |
| 6 | `pnp_chave_high_side`         | esquemático      | PNP como chave high-side: GPIO→R base (lógica invertida); carga no coletor | Deck Saída, slide 37 |
| 7 | `mosfet_p_chave_high_side`    | esquemático      | MOSFET-P como chave high-side: GPIO→R gate (+pull-up ao VCC); lógica invertida; carga no dreno | Deck Saída, slide 38 |
| 8 | `botao_circuito_basico`       | esquemático      | Fonte genérica + resistor + botão, sem microcontrolador                   | Deck Entrada, slide 7 |
| 9 | `botao_forma_onda_bounce`     | forma de onda    | Tensão × tempo: idle → pressiona (bounce) → segura → solta (bounce) → idle | Deck Entrada, slide 13 |
| 10| `botao_forma_onda_flutuante` | forma de onda    | Mesmo gráfico, mas sem resistor de referência: ruído aleatório contínuo   | Deck Entrada, slide 14 e 23 |
| 11| `gpio_pullup`                 | esquemático      | Resistor externo entre VCC e o pino; botão para GND → **entrada ativo-baixa** (botão aterra o pino) | Deck Entrada, slide 25 |
| 12| `gpio_pulldown`               | esquemático      | Resistor externo entre GND e o pino; botão para VCC → **entrada ativo-alta** (botão leva o pino ao VCC) | Deck Entrada, slide 27 |
| 13| `niveis_logicos_limiares`     | gráfico (faixas) | Duas retas de tensão (0→VCC) lado a lado: ATmega328P (V_IL≤1,5V, V_IH≥3,0V @5V) e ESP32-S3 (V_IL≤0,825V, V_IH≥2,475V @3,3V), com zonas LOW/indefinido/HIGH marcadas — valores calculados de V_IL=0,3×VCC/V_IH=0,6×VCC (ATmega328P) e V_IL=0,25×VDD/V_IH=0,75×VDD (ESP32-S3), conferir contra a edição exata do datasheet no guia | Deck Entrada, slide 19 |
| 14| `gpio_interface_conceito`     | bloco            | MICROCONTROLADOR/GPIO no centro, seta para SAÍDA (LED) e seta vinda de ENTRADA (botão) — "GPIO é a interface elétrica" | Deck Saída, slide 7 (frame final de 2); Deck Entrada, slide 6 (retomada, slide único) |
| 15| `botao_na_nf`                 | esquemático      | Dois botões lado a lado no mesmo circuito (fonte+resistor genérico): NA (aberto em repouso, sem corrente) e NF (fechado em repouso, corrente contínua ≈V/R) — anotar a corrente de repouso em cada um | Deck Entrada, slide 9 |
| — | *(foto real)* `led_tht`            | foto ✅ resolvida | LED de 5mm (THT) genérico — Wikimedia Commons, "5mm Red LED.jpg", CC BY-SA 2.0 | Deck Saída, slide 9 |
| — | *(foto real)* `led_smd`            | foto ✅ resolvida | Chip SMD ROHM SML-D12 — recortada da capa do datasheet (PyMuPDF)         | Deck Saída, slide 10 |
| — | *(foto real)* `led_rgb`            | foto ✅ resolvida | LED RGB PLCC6 — recortada da capa do datasheet ROHM SMLP34 (PyMuPDF)     | Deck Saída, slide 11 |
| — | *(foto real)* `botao_pushbutton`   | foto ✅ resolvida | Tactile pushbutton 4 pinos (NA típico, o que os alunos usam no kit) — foto de catálogo Eletrogate.com.br (fornecedor de componentes, não licença aberta — uso educacional com fonte citada) | Deck Entrada, slide 10 |
| — | *(foto real)* `chave_d2f`          | foto ✅ resolvida | Microchave Omron D2F — recortada da capa do datasheet (PyMuPDF), mostra COM/NO/NC | Deck Entrada, slide 11 |
| — | *(foto real)* `chave_boia`         | foto ✅ resolvida | Chave-boia real — Wikimedia Commons, "Float switch for open tanks.JPG", CC BY 2.5 | Deck Entrada, slide 5 |
| — | *(genérico/estoque)* `industrial_saida_1/2/3`  | foto ✅ resolvida | Lâmpada de sinalização + contator + painel de máquina em operação — fotos Pixabay (licença livre) | Deck Saída, slides 3-5 |
| — | *(foto real)* `botoeira_start`     | foto ✅ resolvida | Botoeira START/verde (par START/STOP de máquina industrial) — Wikimedia Commons, "Start_Stop_Power_Switch.jpg" (Michael Holley / Swtpc6800), domínio público | Deck Entrada, slide 3 |
| — | *(genérico/estoque)* `industrial_entrada_2`    | foto ✅ resolvida | Sensor de fim de curso — Wikimedia Commons, "Limit_Switches.JPG" (Mixabest), CC BY-SA 3.0 | Deck Entrada, slide 4 |

---

## Deck 1 — `gpio_saida_leds.md` ("Do LED ao GPIO — Acionando Saídas Digitais")

1. **Capa**.
2. **Objetivo da aula** — calcular o resistor certo para acender um LED com segurança, depois entender como um GPIO (e, quando necessário, um transistor) assume o papel de fonte desse circuito.
3. **Um CLP aciona uma lâmpada de sinalização.** (frame 1/3 — contexto industrial, frase + imagem, abertura.)
4. **Um controlador liga um contator.** (frame 2/3.)
5. **Um módulo eletrônico informa que uma máquina está em operação. Para entender sistemas maiores, vamos começar pelo menor atuador possível: um LED** — mesma lógica elétrica (um sinal de controle aciona uma carga), em escala de bancada. (frame 3/3 — transição para a aula.)
6. **Mas por trás de acender esse LED, algo mais fundamental** — o microcontrolador vai **pôr uma tensão no mundo físico**, através de um único pino. (frame 1/2.)
7. **Esse pino se chama GPIO** — é a interface elétrica entre o microcontrolador e o mundo. Hoje vemos o sentido *saída*; na próxima aula, o sentido *entrada* (ler uma tensão que vem de fora). (frame 2/2 — revela o diagrama completo.) *Diagrama 14.*
8. **Como um LED acende** — é um diodo: a corrente cresce fortemente conforme a tensão direta aumenta; a tensão de operação V_F depende da corrente e do dispositivo, não é um limiar rígido de "liga/desliga". Por isso usamos um resistor — para controlar a corrente, não para "ligar" o LED.
9. **LED de verdade — o clássico** — foto: LED de 5mm (THT), o que a maioria já viu ou usou. (frame 1/3.)
10. **LED de verdade — em miniatura** — foto: chip SMD ROHM SML-D12 (1,6×0,8mm, capa do datasheet) — o mesmo símbolo triangular do diagrama representa isso, só que do tamanho de um grão de arroz. (frame 2/3.)
11. **LED de verdade — três em um** — foto: LED RGB de 3 chips num só encapsulamento (capa Everlight/ROHM SMLP34) — adiantando o que vem no slide 31. (frame 3/3.)
12. **Circuito básico: fonte + resistor + LED** — sem microcontrolador ainda, só uma fonte de tensão qualquer (pilha/fonte de bancada). *Diagrama 1.*
13. **🔮 Pausa — Previsão** — "Chutem: qual é a tensão direta (V_F) de um LED vermelho comum?" Anotem o palpite — comparamos com o dado real nos próximos slides.
14. **V_F — vermelho** — datasheet ROHM SML-D12U8W (0603, @I_F=20mA): V_F típico = **2,2V**. (frame 1/4.)
15. **V_F — laranja** — datasheet ROHM SML-D12D8W (mesma condição, I_F=20mA): V_F típico = **2,2V**. Igual ao vermelho — coincidência? (frame 2/4.)
16. **V_F — amarelo** — datasheet ROHM SML-D12Y8W (I_F=20mA): V_F típico = **2,2V**. De novo? (frame 3/4.)
17. **V_F — verde, e a virada** — datasheet ROHM SML-D12P8W (I_F=20mA): V_F típico = **2,2V**. As quatro cores desta família batem exatamente em 2,2V — o que muda entre elas é o comprimento de onda (λD) e a intensidade luminosa (I_V), **não o V_F**. V_F depende do componente e da corrente de teste, não é uma propriedade fixa da cor. Fonte: `datasheets/leds/ROHM_SML-D12*.pdf` (ver seção de datasheets abaixo). (frame 4/4.)
18. **Calculando o resistor limitador** — fórmula R = (V_fonte − V_F) / I, aplicada com uma fonte genérica (ex.: pilha de 9V, LED vermelho **ROHM SML-D12U8W**, V_F=2,2V @20mA, I=10mA — o mesmo componente visto nos slides anteriores, não "vermelho" em geral). Duas frases-chave: "o resistor não limita a tensão do LED — limita a corrente" e "a tensão que sobra depois do LED aparece no resistor" (V_R = V_fonte − V_F). Pergunta para a turma: **"Se o LED tem V_F=2,2V, por que não uso uma fonte de 2,2V direto nele?"** — resposta: V_F não é "a tensão que o LED precisa para funcionar", é a tensão que aparece sobre ele quando uma certa corrente já está circulando; sem um elemento limitador, a corrente pode crescer para valores destrutivos — é a característica I-V extremamente não linear do diodo (vista informalmente no slide 8), não um "curto-circuito" literal.
19. **🧮 Pausa — Cálculo** — "Com a fórmula do slide anterior: qual o resistor para o LED verde **ROHM SML-D12P8W** (V_F=2,2V @20mA — o mesmo componente do slide 17, não 'verde' em geral) numa fonte de 9V, com I=15mA? Calculem antes de eu revelar." (Nota de produção — não imprimir no slide: R=(9−2,2)/0,015≈453Ω → comercial 470Ω; revelar só verbalmente/em discussão, sem rótulo "Resposta:" na tela.)
20. **O que muda quando a fonte é um GPIO?** — o pino não é uma fonte ideal: tem um nível de tensão fixo e limitado (5V no UNO, 3,3V no ESP32-S3-UNO) e uma capacidade de corrente limitada. Ponte para a próxima ideia.
21. **🔮 Pausa — Previsão** — "Se eu quiser que o LED apague quando o GPIO estiver em HIGH (em vez de acender), o que precisa mudar no circuito?" Pensem antes da explicação.
22. **GPIO como fonte ou sumidouro de corrente** — GPIO em HIGH **fornece** corrente (source): alimenta o LED diretamente → circuito **ativo-alto**. GPIO em LOW **absorve** corrente (sink): completa o caminho de um LED alimentado pelo VCC → circuito **ativo-baixo**. A origem do ativo-alto/ativo-baixo é elétrica, não uma escolha arbitrária de fiação.
23. **Ativo-alto** — ânodo no GPIO, cátodo → resistor → GND. HIGH acende. *Diagrama 2.*
24. **Ativo-baixo** — cátodo no GPIO, ânodo → resistor → VCC. LOW acende. Por que isso existe na prática: alguns módulos/placas vêm cabeados assim de fábrica (ex.: LED onboard) — importante ler o esquemático, não assumir. *Diagrama 3.*
25. **🔍 Pausa — Garimpo no datasheet** — abram `datasheets/ATmega328P_Datasheet_Microchip.pdf` e achem, na seção de características elétricas (DC Characteristics), o valor de corrente máxima absoluta por pino de I/O. Anotem o número e a página onde acharam (~2 min).
26. **Limite de corrente por pino** — três categorias de número no datasheet, não intercambiáveis: (1) **limite máximo absoluto** — o que acabaram de achar no garimpo — (o que nunca pode ser ultrapassado, sob risco de dano ao chip); (2) **condição de teste/especificação elétrica** (o valor de I_OH/I_OL sob o qual o fabricante garante os níveis V_OH/V_OL — não é uma recomendação de uso contínuo); (3) **corrente de projeto recomendada** — bem mais conservadora que as duas anteriores. Nunca dimensionar pelo limite absoluto nem confundi-lo com a condição de teste. Tabela com os três números de cada chip (ATmega328P vs ESP32-S3), citando datasheet e página/tabela exata, fica no guia técnico.
27. **Exemplo de cálculo — UNO (5V)** — LED vermelho (V_F=2,2V, datasheet ROHM SML-D12), I=10mA → R = (5−2,2)/0,01 = 280Ω → valor comercial 330Ω (fica levemente abaixo dos 10mA planejados, o que é seguro — errar para menos corrente, nunca para mais).
28. **Exemplo de cálculo — ESP32-S3 (3,3V)** — mesmo LED (V_F=2,2V), mesma corrente I=10mA → R = (3,3−2,2)/0,01 = 110Ω → valor comercial 120Ω — mesmo LED, mesma corrente, resistor menor só porque a fonte (o pino) tem menos tensão sobrando para "queimar".
29. **Código** — `digitalWrite` ativo-alto e ativo-baixo, UNO e ESP32-S3-UNO lado a lado.
30. **🔮 Pausa — Previsão** — "Um LED RGB tem 3 chips diferentes dentro do mesmo encapsulamento. Vocês acham que os 3 têm o mesmo V_F? Por quê?"
31. **LED RGB: três LEDs, três V_F diferentes, um só encapsulamento** — componente real ROHM SMLP34RGBN1W (4 pinos, um ânodo comum + 3 cátodos R/G/B): a I_F=5mA, V_F típico é vermelho=1,9V, verde=2,9V, azul=3,0V. **Cada canal de cor precisa do seu próprio cálculo de resistor** — mesma fórmula do slide 18, aplicada 3 vezes (e é aqui que finalmente aparece um V_F real de LED azul, que não existe na família SML-D12 de cor única). Fonte: `datasheets/leds/ROHM_SMLP34RGBN1W_RGB.pdf`.
32. **V_F não é um valor fixo — Min/Typ/Max** — datasheet de um segundo componente real (Everlight 67-63-RGB0201H-AM, RGB automotivo) especifica, a I_F=20mA: vermelho V_F mín/típ/máx = 1,75/1,95/2,75V; verde = 2,75/3,10/3,75V; azul = 2,75/3,00/3,75V — e ainda dá uma faixa aceitável de I_F por cor (vermelho 5–50mA; verde/azul 3–30mA). Pergunta para a turma: **"Se eu disser simplesmente V_F=2V, estou dizendo toda a verdade?"** — a resposta é o datasheet: um intervalo, não um ponto. Fonte: `datasheets/leds/Everlight_67-63-RGB0201H-AM_RGB_MinTypMax.pdf`.
33. **Quando o GPIO não basta** — cargas que puxam mais corrente do que o pino aguenta (motor, relé, fita de LED, lâmpada) — voltando aos exemplos do início (o contator, a lâmpada de sinalização de maior potência): é exatamente aqui que essas cargas "de verdade" entram. GPIO não alimenta a carga diretamente.
34. **Transistor como chave** — conceito geral: o GPIO só controla (base/gate), quem alimenta a carga é uma fonte externa. Duas famílias (BJT/MOSFET) × duas topologias (low-side/high-side).
35. **Chave low-side: NPN** — GPIO HIGH liga a chave (precisa de corrente de base contínua), conectando o lado "baixo" da carga ao GND; a fonte externa alimenta o lado "alto" direto. (frame 1/4.) *Diagrama 4.*
36. **Chave low-side: MOSFET-N** — mesma topologia, mas comandada por tensão no gate (não corrente contínua) + resistor de pull-down para garantir que fique desligada quando o GPIO estiver em estado indefinido/flutuante. (frame 2/4.) *Diagrama 5.*
37. **Chave high-side: PNP** — lógica invertida (GPIO LOW liga a chave); fica entre a fonte externa e o lado "alto" da carga. (frame 3/4.) *Diagrama 6.*
38. **Chave high-side: MOSFET-P** — mesma lógica invertida, comandada por tensão; resistor de pull-up ao VCC no gate garante que fique desligada em estado indefinido/flutuante (ex. durante o boot) — mesma função de segurança que o pull-down cumpre no MOSFET-N. (frame 4/4.) *Diagrama 7.*
39. **Comparativo rápido** — tabela: BJT vs MOSFET (corrente de acionamento vs tensão de acionamento), low-side vs high-side (lógica direta vs invertida, facilidade de projeto). Critério prático de escolha do transistor: dois parâmetros do componente que precisam cobrir a carga — corrente máxima entre coletor/dreno e emissor/fonte, e tensão máxima suportada nesse mesmo par. Aviso: dimensionar resistor de base/gate e checar compatibilidade de tensão fica para um estudo de caso à parte — aqui é só o mapa mental de qual usar quando.
40. **Checklist de revisão** — V_F como dado de datasheet (não valor fixo por cor) e fórmula do resistor, ativo-alto vs ativo-baixo (fonte vs sumidouro de corrente), limite de corrente do pino, LED RGB (3 cálculos independentes), quando/qual transistor usar.
41. **Encerramento** — próxima aula: a mesma fronteira elétrica, no sentido contrário — lendo uma tensão que vem de fora (botão).

## Deck 2 — `gpio_entrada_botoes.md` ("Do Botão ao GPIO — Lendo Entradas Digitais")

1. **Capa**.
2. **Objetivo da aula** — entender por que um botão sozinho não basta, ver o ruído que isso causa, e ler um botão de forma confiável nas duas placas.
3. **Uma botoeira aciona a partida de um motor.** (frame 1/3 — contexto industrial, abertura.)
4. **Um sensor de fim de curso detecta que uma porta está fechada.** (frame 2/3.)
5. **Uma chave-boia informa o nível de um reservatório. Para entender sistemas maiores, vamos começar pelo menor sensor possível: um botão** — mesma lógica elétrica (um contato informa um estado), em escala de bancada. (frame 3/3 — transição para a aula.)
6. **De volta à interface elétrica do GPIO** — retomada do diagrama 14 (visto na aula de saída): hoje o pino passa a **ler** uma tensão que vem de fora, em vez de impô-la. Mesma fronteira, sentido contrário. *Diagrama 14.*
7. **Circuito básico: fonte + resistor + botão** — sem microcontrolador ainda, só pra observar a tensão em um ponto do circuito ao apertar/soltar. *Diagrama 8.*
8. **🔮 Pausa — Previsão** — "O botão fecha o circuito ou abre o circuito quando está solto (sem ninguém tocando)? Será que todo botão funciona igual?"
9. **NA vs. NF: os dois tipos de contato** — a maioria dos botões usados com GPIO é **NA** (normalmente aberto / *Normally Open*, NO): em repouso o contato está aberto (sem caminho de corrente), pressionar fecha o circuito. Existe também o **NF** (normalmente fechado / *Normally Closed*, NC): em repouso o contato já está fechado (conduzindo), pressionar é que abre o circuito. **NA e NF não são "melhor" e "pior" — são escolhas de projeto: cada um define qual estado elétrico existe quando ninguém está acionando o dispositivo.** No NF esse estado de repouso já conduz corrente pelo resistor de referência (relevante em projetos sensíveis a consumo, ex. bateria); em compensação, é justamente por já estar "fechado por padrão" que o NF costuma aparecer em circuitos de segurança/fail-safe, onde um fio rompido já é detectado como acionamento — como o sensor de fim de curso do slide 4. (Detalhamento de consumo/fail-safe fica para o guia.) *Diagrama 15.*
10. **Botão de verdade — o que você já usou** — foto: tactile pushbutton de 4 pinos (o do kit), quase sempre NA. (frame 1/2.)
11. **Chave de verdade — COM/NO/NC no mesmo componente** — foto: microchave Omron D2F, capa do datasheet mostrando várias variantes e o diagrama de terminais COM/NO/NC — uma única chave mecânica pode oferecer os dois contatos ao mesmo tempo (você escolhe qual fiar), diferente do pushbutton do frame anterior, que só tem NA. (frame 2/2.)
12. **🔮 Pausa — Previsão** — "Sem nenhum resistor conectado, o que a tensão faz no ponto entre o botão e o fio, quando ninguém está tocando? Desenhem um palpite do gráfico tensão × tempo." Comparamos com os dados reais nos próximos dois slides.
13. **Forma de onda: o que a tensão faz ao pressionar/soltar** — nível parado (idle), transição ao pressionar, pequenas "quicadas" (bounce, ruído mecânico do contato) antes de estabilizar, e o mesmo ao soltar. (Exemplo usa um botão NA, o caso padrão.) *Diagrama 9.*
14. **E sem nenhum resistor de referência?** — mesmo tipo de gráfico, mas agora o ponto fica "flutuando": ruído aleatório contínuo, não só nas transições — antecipa o problema antes de falar em GPIO. *Diagrama 10.*
15. **O que é um GPIO** — pino de propósito geral, configurável como `INPUT` ou `OUTPUT` via `pinMode()`.
16. **O que é um nível lógico** — HIGH e LOW são uma interpretação digital de uma faixa de tensão; quem decide é o circuito de entrada do chip.
17. **Limiares dependem da tensão de operação e da tecnologia** — faixa que garante LOW (V_IL máx.), faixa que garante HIGH (V_IH mín.), e uma **zona indefinida** no meio — é essa zona que o ruído do slide 14 fica cruzando.
18. **🔍 Pausa — Garimpo no datasheet** — abram `datasheets/ESP32-S3_Datasheet_v2.2_Espressif.pdf` e achem, na tabela de características DC, o valor de V_IH mínimo (tensão de entrada garantida como HIGH). Anotem o valor e como ele se relaciona com VDD (~2 min).
19. **Na prática: ATmega328P (5V) vs ESP32-S3 (3,3V)** — diagrama de faixas de tensão (0V até VCC) para os dois chips lado a lado, com V_IL/V_IH marcados — mais didático que só uma tabela. Valores calculados a partir das frações especificadas no datasheet de cada chip (V_IL/V_IH como fração de VCC/VDD — ver tabela do diagrama 13); confirmar sempre contra a edição exata do datasheet usada no guia. *Diagrama 13.*
20. **Alerta rápido** — não ligar uma saída de 5V direto em um pino de entrada 3,3V-only: ultrapassa o V_IH e também o limite absoluto de tensão do pino — no ESP32-S3 esse limite é VDD+0,3V para os pinos do domínio padrão de 3,3V (**3,6V** com VDD=3,3V; alguns pinos especiais do chip operam em outro domínio de tensão — não generalizar sem checar o datasheet). Não é um risco só teórico: 5V está bem acima desse teto. Colocado logo aqui porque é exatamente o diagrama 13 (slide anterior) que torna essa diferença de domínio de tensão visualmente explícita.
21. **E se os níveis de tensão forem diferentes?** — quando um sensor/módulo 5V precisa conversar com um GPIO 3,3V-only (ou vice-versa), existem circuitos de adaptação de nível (*level shifting*). Fica só o mapa mental de que a solução existe — as técnicas específicas (divisor resistivo, level-shifter dedicado, etc.) ficam para outra aula/o guia técnico, junto com o dimensionamento de transistor visto na aula de saída.
22. **O mesmo botão, agora num GPIO** — trocamos a fonte genérica do slide 7 pelo pino do microcontrolador; a pergunta agora é "o pino consegue decidir HIGH ou LOW com confiança?"
23. **O problema: entrada flutuante no GPIO** — reconecta com o gráfico do slide 14: sem pull-up/pull-down, o pino passa a maior parte do tempo na zona indefinida. *Diagrama 10.*
24. **🔮 Pausa — Previsão/Proposta** — "Com o que já sabemos sobre resistores (das aulas de LED): como vocês resolveriam o problema da entrada flutuante? Proponham uma solução antes de eu mostrar as duas oficiais."
25. **Solução 1: Pull-up → entrada ativo-baixa** — resistor entre VCC e o pino; o botão (NA) **aterra** o pino ao ser pressionado. Repouso = HIGH, pressionado = LOW. Pull-up **é**, por construção, uma entrada ativo-baixa. *Diagrama 11.*
26. **Pull-up interno** — `pinMode(pino, INPUT_PULLUP)` — dispensa resistor externo, continua sendo ativo-baixa. Código lado a lado UNO / ESP32-S3-UNO.
27. **Solução 2: Pull-down → entrada ativo-alta** — resistor entre GND e o pino; o botão (NA) leva o pino ao VCC ao ser pressionado. Repouso = LOW, pressionado = HIGH. Pull-down **é**, por construção, uma entrada ativo-alta. *Diagrama 12.*
28. **Ativo-alto vs. ativo-baixo — tabela-resumo** — pull-up = ativo-baixo (botão aterra), pull-down = ativo-alto (botão leva ao VCC); e o paralelo com a aula de saída: GPIO fonte de corrente ↔ ativo-alto, GPIO sumidouro de corrente ↔ ativo-baixo — a mesma simetria elétrica nos dois sentidos. (Nota: com um botão NF a lógica de repouso/pressionado se inverte — reforça por que "ativo-alto/baixo" depende da fiação e do tipo de contato, não é uma propriedade fixa do botão.)
29. **🔮 Pausa — Previsão** — "Com `INPUT_PULLUP`, o que o Monitor Serial vai mostrar quando o botão estiver solto? E quando pressionado? Prevejam antes de rodar o código."
30. **Código completo** — leitura de botão com `INPUT_PULLUP`, UNO e ESP32-S3-UNO lado a lado, `Serial.println` do estado.
31. **Bounce revisitado: como lidar com ele** — o pull-up/pull-down resolve o "flutuante" mas não elimina o bounce nas transições (visto no slide 13, diagrama 9); solução (debounce por software/hardware) fica para outra aula — a título de gancho, cita-se a técnica mais simples (ler, esperar ~50ms, ler de novo) como prévia.
32. **Checklist de revisão** — nível lógico e seus limiares, NA vs NF, flutuante vs pull-up vs pull-down, ativo-alto vs ativo-baixo, pull-up interno vs externo, bounce, adaptação de nível 3,3V↔5V.
33. **Encerramento**.

---

## Referências já disponíveis em `livros/`

Levantamento no acervo local (`livros/*.md`, já convertidos de PDF). Nenhum
livro cobre exatamente ATmega328P + ESP32-S3 lado a lado, mas dois trazem
material prático diretamente aproveitável nos guias técnicos (citar como
fonte, não copiar sem atribuição):

- **`livros/esp8266_nodemcu_-_do_pisca_led_a_internet_das_coisas.md`** — o
  mais relevante do acervo. Traz: (a) pull-up (botão entre o pino e 3,3V) vs
  pull-down (botão entre o pino e a referência) com resistor "entre 1k e
  4k7Ω" — um dado real de fonte publicada para contrastar com o "10kΩ
  típico" mais comum na prática, reforçando por que o valor exato fica só no
  guia, com a fonte citada; (b) exemplo de LED ativo-alto com resistor de
  270Ω (ânodo no GPIO, cátodo→270Ω→GND) — mesma topologia do slide 23 do
  Deck Saída; (c) especificação do ESP8266 NodeMCU: "9 portas digitais,
  tensão 3,3V, corrente máxima 15mA" — exemplo real de um fabricante/autor
  documentando um limite conservador (não o absoluto do chip), que serve de
  modelo para como apresentar o dado equivalente do ESP32-S3 no guia; (d)
  técnica de debounce por software mostrada em código (lê, espera ~50ms,
  lê de novo antes de aceitar o estado) — referência direta para o slide 31
  do Deck Entrada; (e) critério de dois parâmetros para escolher um
  transistor (corrente e tensão máximas entre coletor e emissor) — usado no
  slide 39 do Deck Saída.
- **`livros/819676056-IoT-com-MicroPython-e-NodeMCU-Claudio-Luis-Vieira-Oliveira-H.md`**
  — listas de material de projetos reais: resistores de 220Ω ou 330Ω para
  LED (bate com os valores comerciais calculados nos slides 27-28 do Deck
  Saída) e resistores de 10kΩ para botão (contraponto ao "1k–4k7Ω" do outro
  livro — evidência concreta de que a prática varia, o que sustenta a
  decisão de não fixar um número único no slide).

Os demais livros do acervo (IoT industrial, automação com CLP, ESP32
MicroPython/Explore ESP32) foram verificados e não trazem conteúdo
diretamente aproveitável para estes dois decks especificamente (cobrem
protocolos de rede, CLPs e sensores industriais, fora do escopo de GPIO
básico/botão/LED). Nenhum arquivo do acervo documenta os limiares V_IL/V_IH,
a corrente máxima por pino do ATmega328P/ESP32-S3, ou V_F/I_F de LEDs reais
— esses números vêm dos datasheets de componente, baixados para
`datasheets/` (ver abaixo).

## Datasheets de microcontrolador (fonte primária de V_IL/V_IH/corrente)

Baixados para `datasheets/` (fora do escopo do `livros/`, que é o acervo de
livros-texto/e-books; aqui são documentos de referência de componente).
Números conferidos via busca independente nesta sessão, cruzando múltiplas
fontes secundárias (ODG Electronic, PCBSync, componentes101, busca web) além
do PDF oficial:

- **`datasheets/ATmega328P_Datasheet_Microchip.pdf`** — Atmel/Microchip,
  "ATmega328P — 8-bit AVR Microcontroller" (doc. 7810/DS40002061), baixado de
  `ww1.microchip.com/downloads/en/DeviceDoc/`. Seção de características
  elétricas (DC Characteristics): V_IL(máx.) = 0,3×VCC, V_IH(mín.) = 0,6×VCC
  → em 5V: LOW garantido ≤1,5V, HIGH garantido ≥3,0V. Corrente: 40mA é o
  limite máximo absoluto por pino de I/O; a condição de teste elétrico usa
  20mA a VCC=5V; a corrente total agregada por grupo de pinos (VCC/GND) tem
  limite próprio (~200mA) — **três números diferentes, não confundir** (ver
  slide 26 do Deck Saída — é o mesmo garimpo do slide 25). **Nota:** o nome
  do arquivo no servidor da Microchip inclui "Automotive" — confirmar no
  guia se há alguma ressalva de faixa de temperatura/qualificação que não se
  aplique ao componente comercial usado em sala; as características
  elétricas de V_IL/V_IH citadas aqui são as mesmas em ambas as versões.
- **`datasheets/ESP32-S3_Datasheet_v2.2_Espressif.pdf`** — Espressif
  Systems, "ESP32-S3 Series Datasheet", Version 2.2, baixado diretamente de
  `documentation.espressif.com` (domínio oficial do fabricante — confirmado
  na capa do PDF). Tabela DC Characteristics (VDD=3,3V): V_IH(mín.) =
  0,75×VDD (até VDD+0,3V), V_IL(máx.) = 0,25×VDD → LOW garantido ≤0,825V,
  HIGH garantido ≥2,475V (é o número que o garimpo do slide 18 do Deck
  Entrada deve encontrar); **limite absoluto de tensão = VDD+0,3V = 3,6V
  para os pinos do domínio padrão de 3,3V (VDD1)** — **não generalizar para
  "qualquer pino"**: o ESP32-S3 tem pinos de domínio de tensão diferente
  (ex.: IO47/IO48, usados em configurações de flash/PSRAM octal, operam a
  1,8V) — confirmar no guia a que domínio cada pino usado no exemplo
  pertence antes de citar 3,6V como limite (número usado no slide 20 do
  Deck Entrada, com essa mesma ressalva). I_OH=40mA e I_OL=28mA são
  correntes de saída sob condição de teste específica (PAD_DRIVER=3,
  V_OH≥2,64V / V_OL=0,495V), não uma corrente de projeto recomendada;
  resistores internos de pull-up/pull-down ≈45kΩ (não confundir com o
  resistor externo dos diagramas 11/12 — ver nota acima).

Ambos os PDFs foram baixados e o conteúdo da capa/primeira página conferido
nesta sessão para garantir que são o documento certo (não um mirror errado
ou desatualizado). Ainda assim, ao escrever o guia técnico, citar a
página/tabela exata de cada número (não só "ver datasheet") — os PDFs estão
no repositório justamente para isso.

## Datasheets de LED (fonte primária de V_F/I_F — `datasheets/leds/`)

Todos conferidos nesta sessão abrindo a própria capa/tabela do PDF (não só
aceitos de segunda mão) — ver nota de correção ao final desta seção.

- **`ROHM_SML-D12U8W_Vermelho.pdf`**, **`..._D8W_Laranja.pdf`**,
  **`..._Y8W_Amarelo.pdf`**, **`..._P8W_Verde.pdf`** — série ROHM SML-D12
  (chip SMD 0603/1,6×0,8mm, mono-color), cada arquivo é o datasheet de uma
  cor. Confirmado por página 1 de cada PDF: **as quatro cores têm V_F
  típico = 2,2V a I_F=20mA** (o que muda é I_V e λD — ver slides 14-17 do
  Deck Saída, revelados um por um depois da pausa de previsão do slide 13).
  Rev.006, 2025.3, `www.rohm.com`. Não existe uma variante **azul** nesta
  sub-família (confirmado tentando várias URLs no domínio oficial
  `fscdn.rohm.com` — só retornam 404); azul vem das duas fontes RGB abaixo.
- **`ROHM_SMLP34RGBN1W_RGB.pdf`** — ROHM SMLP34RGBN1W (PicoLED-RGB, 4 pinos,
  ânodo comum + 3 cátodos). Tabela de especificações (página 1) confirma V_F
  típico a I_F=5mA: vermelho=1,9V, verde=2,9V, azul=3,0V. Usado no slide 31
  do Deck Saída (depois da pausa de previsão do slide 30) — é a fonte do
  primeiro V_F de LED azul real do material.
- **`Everlight_67-63-RGB0201H-AM_RGB_MinTypMax.pdf`** — Everlight
  Automotive, PLCC6, RGB. Tabela "1. Characteristics" (página 3) confirma,
  a I_F=20mA: vermelho V_F mín/típ/máx=1,75/1,95/2,75V, I_F aceitável
  5–50mA; verde V_F=2,75/3,10/3,75V, I_F 3–30mA; azul V_F=2,75/3,00/3,75V,
  I_F 3–30mA. Rev.4, 2019, `www.everlight.com`. Usado no slide 32 do Deck
  Saída para mostrar que V_F é uma faixa, não um ponto.

**Correção registrada nesta sessão:** uma consulta anterior (de segunda mão,
outra ferramenta de IA) atribuiu à "ROHM SML-D12" os valores "verde
V_F≈3,0V@5mA, azul V_F≈2,9V@5mA". Ao baixar e abrir os datasheets reais da
SML-D12, isso **não confere** — a série SML-D12 não tem variante azul, e o
verde real (P8W) é V_F=2,2V a 20mA (não 3,0V a 5mA). Os números "verde
≈2,9V/azul≈3,0V @5mA" existem, sim, mas pertencem à SMLP34RGBN1W (com
verde/azul corretos, só a atribuição ao componente errado é que estava
equivocada na fonte secundária). Lição para o guia: sempre abrir o PDF
primário antes de citar um número específico de datasheet — uma IA
resumindo "de memória" pode trocar a peça mesmo quando os números em si
existem em algum datasheet real.

## Datasheets de botão/chave (`datasheets/botoes/`)

- **`Omron_D2F_Microswitch_NA-NF.pdf`** — Omron D2F, microchave ultra-
  subminiatura, domínio oficial `omronfs.omron.com`. Capa mostra fotos reais
  de várias variantes (pino, alavanca, rolete) e o diagrama de terminais
  **COM / NO / NC** — usado no slide 11 do Deck Entrada como exemplo real de
  uma chave que expõe os dois contatos (NA e NF) ao mesmo tempo, diferente
  do pushbutton simples do kit (que só tem NA). Nota para o guia: o D2F é
  SPDT (um COM chaveando entre NO e NC) — não são "dois produtos, um NA e
  um NF", é a mesma chave com os dois contatos disponíveis; vale deixar essa
  nuance explícita para não confundir com a dicotomia NA-vs-NF de dois
  componentes diferentes usada no slide 9.

## Guias técnicos (espelham os decks, com código completo)

- `guias_e_roteiros_tecnicos/Guia_GPIO_Saida_LEDs.md`
- `guias_e_roteiros_tecnicos/Guia_GPIO_Entrada_Botoes.md`

Mesmo princípio de ordenação dos decks: circuito básico (sem microcontrolador)
antes da aplicação em GPIO. Usam o template novo
`00_TEMPLATE_GUIA_CONCEITUAL.md` (Conceito → Diagrama → Passo a passo com
código UNO + ESP32-S3-UNO → Erros comuns → Checklist → Referências). O guia
de saída é onde entram os números específicos de corrente máxima/recomendada
por pino do ATmega328P e do ESP32-S3, cada um citando a seção exata do
datasheet usado (não repetidos de memória) — os slides ficam só com o
princípio de dimensionamento conservador. Na seção "Referências" de cada
guia, citar também os dois livros do acervo local listados acima
(`esp8266_nodemcu_...md` e `819676056-IoT-com-MicroPython...md`), os
datasheets de LED (`datasheets/leds/`) e o datasheet de chave
(`datasheets/botoes/`), ao lado dos datasheets oficiais de microcontrolador.

**Nota sobre os garimpos de datasheet (slides de pausa 🔍):** as respostas
que os alunos vão achar nos slides 25 (Deck Saída) e 18 (Deck Entrada) são
exatamente os números documentados nas seções acima — o professor já sabe
onde estão (página/tabela) para ajudar quem travar.

**Contagem final:** Deck Saída 41 slides, Deck Entrada 33 slides — acima da
faixa 20-22 sugerida em avaliações anteriores, e conscientemente assim: por
diretriz do professor, contagem de slides não é fator limitante quando o
ritmo é cinematográfico (ver nota no topo do arquivo). Os slides dos frames
de foto/revelação/contexto industrial são rápidos de passar em aula; os
slides densos (tabelas, fórmulas, comparativos) continuam concentrando o
tempo de fala.

**Fotos/ícones de contexto industrial (slides 3-5 de cada deck):** genéricos
de estoque — lâmpada de sinalização, contator, painel de máquina (Saída);
botoeira, sensor de fim de curso, chave-boia (Entrada). Não são componentes
específicos do S086 nem têm datasheet associado — servem só de moldura
motivacional, sem números técnicos para verificar. Todas resolvidas —
Pixabay (licença livre, sem atribuição obrigatória), Wikimedia Commons
(CC BY / CC BY-SA, atribuição citada no comentário do slide) e, para o
`botao_pushbutton` (que nenhum banco de imagem livre tinha em boa
qualidade), foto de catálogo do fornecedor Eletrogate.com.br (uso
educacional, fonte citada). Ver a tabela de diagramas acima e
`scripts/diagramas/README.md` para a fonte exata de cada arquivo.
