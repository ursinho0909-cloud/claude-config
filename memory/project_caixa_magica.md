---
name: project-caixa-magica
description: "Info-produto \"Caixa Mágica de Atividades\" - landing no Cloudflare Pages, checkout Cakto, tracking UTMify"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1f808c8d-a073-4ef3-a9cf-97aa6dd08528
---

Info-produto **"Caixa Mágica de Atividades"** (+1.000 atividades infantis pra imprimir, sem telas). Mais um lançamento do mesmo usuário do [[user-business]], no estilo info-produto BR.

**Stack / live (2026-05-25):**
- Landing: `https://caixamagica.pages.dev` — Cloudflare Pages, projeto **`caixamagica`** (direct-upload, sem Git), conta Cloudflare `ursinho0909@gmail.com` (Account ID `3efe40850575dec18923b50db72942fc`).
- Checkout: **Cakto** — R$27 VIP (`pay.cakto.com.br/82q6g3i_890962`) e R$10 básico (`pay.cakto.com.br/9jvzsub_891218`).
- Tracking: **UTMify** (pixel id `6a144c1991fc0bca95e81934`) + Meta Pixel `978195135098250` + script de UTM `utms/latest.js`.
- Cópia local do site (com pixel) em `C:\Users\User\caixamagica-deploy`. Deploy: `wrangler pages deploy C:\Users\User\caixamagica-deploy --project-name caixamagica --branch main`. Não há fonte/repo do site no PC além dessa cópia reconstruída do ar.

**Funil de conversão UTMify (Meta Ads):** colunas = Cliques (Meta) → Vis. Página (pixel) → ICs (pixel+regra IC) → Vendas Inic. (webhook Cakto pendente) → Vendas Apr. (webhook aprovada). Em 2026-05-25 injetei o `pixel.js` da UTMify no `<head>` e publiquei (faltava — só tinha o script de UTM). Pixel confirmado live.

**Config concluída (2026-05-25):**
1. Regra de **Initiate Checkout** = detecção por texto `QUERO`. Os 4 botões de compra foram padronizados pra conter "QUERO" (o do topo virou "QUERO Minha Caixa Mágica") → IC dispara em todos.
2. **ID do Pixel Meta** na UTMify ajustado pra `978195135098250` (igual ao da página).

Tudo pronto pra o funil (Meta Ads) encher daqui pra frente. Funil não é retroativo — precisa de tráfego/cliques novos. OBS: o funil de conversão da UTMify é recurso PAGO — no plano free do usuário ele nem aparece. Alternativa grátis: ler Gerenciador de Eventos do Meta + Ads Manager + Cakto.

**Diagnóstico da campanha Meta (2026-05-25, lido de vídeo do Ads Manager):** conjunto "anuncio teste", 10 criativos, otimizando Compras (correto). Meta concentrou orçamento em 1 criativo (CRIATIVO01VIDEO): R$61,17 gastos, 1.230 impressões, **2 compras a R$30,59/compra**, ROAS 0.39. **Problema estrutural: CPA (R$30,59) > ticket (R$27/R$10) → toda venda no prejuízo.** Pixel/funil estão certos; o que quebra é a economia. Playbook recomendado: (1) subir AOV com order bump + upsell de 1 clique na Cakto pra ticket R$50-70; (2) tirar o R$10 da entrada (usar só como downsell); (3) backend/e-mail; (4) só depois testar criativo (ABO budget pequeno por criativo).
