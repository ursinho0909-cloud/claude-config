---
name: feedback_regra_trafego_teste_escala
description: "Regra de tráfego Meta do usuário (teste CBO 1-1-1 → escala CBO), com os números que ajustamos em 26/09/2026 após queda de lucro na DASH-EUROPA"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 80b64b3b-e408-4949-a3eb-38b779ea569a
  modified: 2026-10-05T19:18:22.067Z
---

Fluxo do usuário: teste de oferta = 4 campanhas CBO 1-1-1 (1 criativo cada), 1-2 dias. Teste de criativo = CBO 1-1-1 a R$40, 2 dias. O que vende vai pra UMA campanha de escala CBO por produto+país, e o original do teste é desligado. O que não vende morre.

Ajustes combinados:
- Critério: vencedor = 2+ vendas com CPA ≤ média do produto. Matar cedo com ~R$25-30 e CTR <1%; matar com 2× CPA sem venda.
- Alemanha (CPM R$200+): R$40 × 2 dias não dá leitura → R$60-80 ou 3 dias.
- Levar pra escala pelo ID DA PUBLICAÇÃO, nunca "duplicar" (cópia zera prova social; CTR da cópia foi bem menor).
- Nunca o mesmo criativo em 2 campanhas (canibalizou GER em 25-26/09: CTR de 7,5% → 3,5% em todos).
- Escala: +20% no máximo, a cada 2-3 dias, de manhã, uma edição por vez. Nunca editar várias de madrugada.
- Teste = 10-20% do orçamento total.
- Usuário PREFERE escala CBO 1-1-X (Meta escolhe o criativo). Não insistir em 1-X-1; só adicionar vencedores em lote pra não resetar aprendizado toda hora.
- Novos criativos do dia (ex.: GER 05/06/07, TEAES CBO 5/6/7) são teste — não recomendar pausar como perdedor.

- ATUALIZAÇÃO 05/10/2026: usuário testou CBO de escala e NÃO funcionou para ele; hoje escala os próprios 1-1-1 vencedores (+R$1k/dia de lucro). Não insistir em consolidar — sugerir escalar 1-1-1 vencedores (+20%/2-3d), pausar perdedores, máx ~4-5 ativos por país, CBO só como teste paralelo com dinheiro novo sem desligar os 1-1-1. Ele também baixa orçamento à noite (170→70) e sobe de dia — desaconselhado: madrugada BR (manhã EU) é o horário mais lucrativo dele (UTMify EUROPA 2, 7d: 3h +R$621, 4h +R$440; 16-17h negativos).

**Why:** lucro caiu de ~R$1.950 (24/09) pra -R$200 (26/09) com gasto igual; causa foi escala 3,5× na Alemanha + cópias duplicadas + edição de orçamento de madrugada.
**How to apply:** ao analisar UTMify/Meta Ads do usuário, avaliar contra essa regra; checar duplicação de criativo entre campanhas antes de culpar orçamento.
