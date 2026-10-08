---
name: project-coreano-meta-ads-latam
description: "Campanha Meta Ads ativa do Coreano Sin Complicaciones (LATAM). Conjuntos nomeados CONJUNTO01-04 dentro de campanha 'Caixa Magica de Atividades' (nome reaproveitado), checkout Hotmart Internacional, comeco em 2026-06-24"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1cf9c87a-6d1f-4fcd-bcdd-7264de96e618
---

# Coreano Sin Complicaciones · Meta Ads LATAM

## Setup
- **Campanha**: nomeada "Caixa Mágica de Atividades" no Ads Manager (nome REAPROVEITADO de campanha antiga, NAO é pro produto Caixa Magica). Anuncia o coreano LATAM.
- **Produto**: Coreano Sin Complicaciones — mapas mentais coreano em ES, ticket US$ 9,90 + back US$ 5,90 via Hotmart Internacional
- **Conjuntos**: CONJUNTO01, CONJUNTO02, CONJUNTO03, CONJUNTO04 (4 ativos)
- **Início**: 2026-06-24
- **Orçamento**: ABO (por conjunto), oCPM ABSOLUTE, otimização Purchase via pixel
- **Atribuição**: 7d clique / 1d view / 1d engaged view
- **Currency conjunto**: BRL (gasto em reais, faturamento em USD via Hotmart)

## Performance histórica
- **2026-06-24 (dia 1)**: dia OK
- **2026-06-25 (dia 2, EXCELENTE)**: gasto total R$1.068, 93 vendas, faturamento R$4.532, ROAS médio 4,24x
  - CONJ03 foi destaque: R$361 gasto, 45 vendas, ROAS 6,16x, CPA R$8,02 — VENCEDOR
  - CONJ04: R$358, 30 vendas, ROAS 3,99x, CPA R$11,95 — segundo melhor
  - CONJ01: R$206, 12 vendas, ROAS 2,77x — médio
  - CONJ02: R$142, 6 vendas, ROAS 2,16x — fraco estrutural
- **2026-06-26 (dia 3, RUIM por erro de scaling)**: usuário cortou budget de R$361 → R$50 overnight, disparou reset learning, dia caiu pra R$80 gasto/R$101 faturado/R$20 lucro

## Erro de scaling identificado (2026-06-26)
Usuário tem mecânica de "subir budget no dia bom, resetar todos pra R$50 no dia seguinte". Pro Meta, esse reset é edit significativa = reseta learning phase. Vencedor que gastou R$361 cortado pra R$50 = -86% de redução = algoritmo perde momentum e otimiza errado.

**Why:** vencedor (ROAS ≥4x) precisa manter budget próximo ao gasto real do dia anterior, não voltar pra base de teste.

**How to apply:** quando user mencionar Meta Ads e "voltei tudo pra R$50" / "resetei budget" / "não mexi em nada", apontar imediatamente que o reset overnight é o problema. Regra correta: vencedor mantém budget +20% do dia anterior, só perdedor pausa/reseta.

## Playbook escalonamento (decidido com user 2026-06-26)
- **Regra dos 20%**: edits +/-20% não disparam reset de learning. Faz +20%/dia em vencedor.
- **Duplicação horizontal > vertical**: em vez de subir budget num conjunto, duplicar o conjunto. Cada cópia tem próprio pacing.
- **Sábado/domingo são BONS dias pra esse público** (jovens LATAM K-pop/K-drama, fim de semana = consumo + impulso de compra), diferente de info-produto BR de mãe.
- **Pico de hora**: 21h-1h. Bump de budget deve ser feito de manhã pra dar pacing.
- **Câmbio favorece**: gasta BRL, fatura USD. ROAS calculado em BRL/BRL subestima rentabilidade real.
- Audiência LATAM hispano interessada em coreano = pool grande (5-10M+) = bastante headroom pra escalar.

## Continuidade multi-PC (criado 2026-06-27)
Repo `meta-ads-escala` no GitHub (`ursinho0909-cloud/meta-ads-escala`, privado) pra levar a estratégia entre os 2 PCs. Pasta local `Desktop\meta-ads-escala\`. Contém:
- `ESTRATEGIA_ESCALA.md` — playbook condensado (regras, horários, bump por ROAS, duplicação)
- `LOG_DECISOES.md` — histórico diário desde 24/jun com tabelas de números + decisões + racional
- Workflow: `git pull` antes do bump das 9h, `git push` depois de fechar o dia

Ver [[project-github-sync]] pra workflow geral.

Relacionado: [[project-coreano-launch-latam]]
