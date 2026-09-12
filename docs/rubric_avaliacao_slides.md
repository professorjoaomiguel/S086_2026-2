# Rubric de Avaliação de Slides — Design Visual + Aprendizagem

Combina quatro referências para dar um parecer estruturado (não só
estético) sobre um deck de aula: **CRAP** (design gráfico), **WCAG**
(contraste, mensurável), **Mayer** (cognição multimídia) e **Sweller**
(carga cognitiva). Pensado pra rodar contra slides já renderizados
(PNG/JPEG de cada página), slide a slide ou por deck inteiro.

---

## Bloco 1 — CRAP (percepção visual)

| Critério | Pergunta | O que falha parece |
|---|---|---|
| **C**ontraste | Título, corpo e legenda têm peso visual diferente? O olho sabe por onde entrar? | Tudo do mesmo tamanho/peso; nada "puxa" o olhar primeiro |
| **R**epetição | Cores, ícones, posição de elementos se repetem de forma previsível pelo deck? | Cada slide "reinventa" o próprio estilo |
| **A**linhamento | Todo elemento tem uma relação de eixo com outro (não fica "solto")? | Elementos flutuando sem grade; texto e diagrama desalinhados |
| **P**roximidade | Elementos relacionados estão agrupados; não-relacionados têm espaço entre si? | Legenda de um componente longe do componente; texto de blocos diferentes colados |

## Bloco 2 — WCAG (contraste de cor, mensurável)

- Texto normal: razão de contraste **mínima 4,5:1**
- Texto grande (≥18pt bold ou ≥24pt regular): mínimo **3:1**
- Cálculo: luminância relativa de cada cor (fórmula sRGB→linear→luminância) e razão `(L_clara+0.05)/(L_escura+0.05)`
- Rodar contra todas as combinações fundo/texto do tema, não só a "principal"

## Bloco 3 — Mayer (Teoria Cognitiva da Aprendizagem Multimídia)

| Princípio | O que verificar |
|---|---|
| **Coerência** | Existe imagem/texto decorativo que não serve à ideia central do slide? |
| **Contiguidade espacial** | Rótulo/legenda está fisicamente colado ao elemento que explica? |
| **Contiguidade temporal** | (mais relevante em vídeo/animação — narração e imagem aparecem juntas) |
| **Modalidade** | Informação crítica passa por fala do professor + imagem, não só texto lido |
| **Redundância** | O slide repete, palavra por palavra, o que o professor vai falar? |
| **Sinalização** | Negrito/cor guia o olho pro ponto-chave da frase? |
| **Segmentação** | O conteúdo é quebrado em unidades pequenas no ritmo do aluno (não uma parede só)? |

## Bloco 4 — Sweller (Carga Cognitiva)

- **Intrínseca**: complexidade inerente do conteúdo (controlável só por sequenciamento/chunking, não por design)
- **Extrínseca**: carga desperdiçada por poluição visual, layout confuso, "split attention" (ter que integrar mentalmente duas fontes separadas de informação) — **é aqui que bugs de diagramação doem mais**
- **Germinativa**: esforço que constrói esquema mental de verdade (comparações, exemplos trabalhados, worked examples) — quanto mais espaço sobra depois de cortar a extrínseca, mais germinativa cabe

---

## Checklist por slide (modelo)

| # | Tipo de slide | CRAP | WCAG | Mayer | Sweller (extrínseca) | Nota |
|---|---|---|---|---|---|---|
| ex: 25 | Diagrama (pull-up) | Proximidade falha | OK | Contiguidade espacial falha | Alta (split attention) | Rótulo cortado |

---

## Aplicação — Deck GPIO Entrada + Saída (S086)

*(baseado na inspeção visual já feita: 74 páginas rasterizadas, amostra revisada)*

### CRAP
- **Contraste**: ✅ forte — hierarquia título/corpo/legenda clara e consistente nos dois decks.
- **Repetição**: ✅ muito forte — cores por tipo de slide (pausa/alerta/revelação) e posição de ícone+título se repetem de forma confiável; é o ponto mais bem executado do deck.
- **Alinhamento**: ⚠️ parcial — bom na maioria; falha nos diagramas que estouram a altura do frame (ver Sweller abaixo).
- **Proximidade**: ❌ falha localizada — em 3 slides (Entrada #6, Entrada #25, Saída #38) o rótulo de um componente do circuito fica cortado/colado na borda inferior, quebrando a relação visual rótulo↔componente.

### WCAG
- Todas as combinações fundo/texto testadas (capa escura, 4 variantes de pausa, corpo padrão) ficaram **acima de 11:1** — muito acima do mínimo de 4,5:1. Contraste de cor não é um problema neste deck.

### Mayer
- **Coerência**: ✅ majoritariamente forte (fotos reais de componentes/datasheets, não decoração). ⚠️ uma exceção: Entrada #3, a foto da botoeira mostra "PUSH TO STOP" gravado no botão, mas a legenda diz "aciona a partida de um motor" — o elemento visual compete com a mensagem em vez de reforçá-la.
- **Contiguidade espacial**: ❌ mesma falha do CRAP acima — os 3 diagramas cortados são exatamente uma violação de contiguidade espacial (rótulo separado fisicamente do que explica pelo corte de layout).
- **Redundância**: ✅ forte — texto nos slides é telegráfico (frases curtas), não parágrafo que o professor leria em voz alta.
- **Sinalização**: ✅ boa — negrito usado com moderação nos pontos-chave ("HIGH acende", "aterra o pino").
- **Segmentação**: ✅ muito forte — é o princípio mais bem aplicado do deck inteiro. A regra do storyboard de "um slide, uma ideia" e a quebra em frames sequenciais (fotos, V_F por cor) é segmentação de manual.

### Sweller
- **Extrínseca**: ⚠️ o único ponto real de carga extrínseca desnecessária é justamente o corte de diagrama — o aluno precisa gastar atenção tentando entender um circuito com informação faltando/sobreposta, em vez de processar o conceito.
- **Germinativa**: ✅ boa — as pausas de previsão/cálculo/garimpo são exatamente o tipo de esforço que constrói esquema (worked examples com engajamento ativo antes da revelação).

### Veredito resumido

| Categoria | Resultado |
|---|---|
| CRAP | 3/4 forte (Proximidade falha localizada) |
| WCAG | Aprovado sem ressalvas |
| Mayer | 5/6 forte (Contiguidade espacial falha; Coerência com 1 ressalva) |
| Sweller | Extrínseca com 1 fonte de ruído identificável; Germinativa boa |

**Conclusão prática**: o deck está pedagogicamente bem desenhado (segmentação, redundância e carga germinativa são pontos fortes reais, não genéricos) — o problema não é de método, é de **execução técnica de um tipo específico de diagrama** (circuitos com 5+ elementos empilhados verticalmente no SchemDraw). Corrigir isso resolve simultaneamente a falha de CRAP-Proximidade e a falha de Mayer-Contiguidade espacial, porque são a mesma causa raiz vista por dois frameworks diferentes.
