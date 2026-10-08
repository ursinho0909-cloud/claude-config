---
name: feedback-manus-prompt-order
description: "No Manus, lista de conteúdo exata (enunciados/números) vai no TOPO do prompt marcada como literal, senão ele inventa conteúdo próprio"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9e16daa4-40e6-4d88-a8e5-6e23d2978dbf
  modified: 2026-07-23T14:46:53.808Z
---

Quando o Manus tem que reproduzir uma **lista de conteúdo exata** (enunciados de exercício,
números, datas, nomes), a lista tem que vir **primeiro no prompt**, marcada como texto literal,
com proibições explícitas ("NÃO invente, NÃO substitua números, NÃO reformule") e um checklist
final que repita a lista item a item pra ele conferir antes de entregar. Uma ficha por conversa
— o drift cresce quando se gera várias seguidas.

**Why:** em jul/2026, no módulo de problemas do [[project_matematicabloques_area]], os prompts
estavam corretos mas a lista de enunciados estava enterrada no meio de instruções de design.
O Manus ignorou a lista em 3 de 10 fichas e inventou conteúdo próprio — inclusive porcentagens
de nível de 7.º ano numa ficha de 5.º, e desenhos de volume que não batiam com o enunciado.
Também dropou silenciosamente elementos obrigatórios (caixa de resposta de metade da ficha,
faixa de rodapé) que estavam especificados.

**How to apply:** estrutura de prompt em 4 partes — PARTE 1 conteúdo literal · PARTE 2
OBLIGATORIO (o que ele costuma dropar, listado como critério de rejeição) · PARTE 3 design ·
PARTE 4 checklist de verificação repetindo o conteúdo. Modelo pronto em
`Desktop\matematicabloques-area\PROBLEMAS_prompts_v2\*.txt`. E **sempre revisar imagem por
imagem** antes de publicar: ler cada uma e conferir enunciado a enunciado, não bater o olho —
foi assim que os defeitos apareceram.
