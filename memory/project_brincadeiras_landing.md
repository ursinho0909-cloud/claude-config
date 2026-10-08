---
name: project-brincadeiras-landing
description: "Landing page +150 Brincadeiras Sem Tela (info-produto), deploy via Cloudflare Pages, checkout via Lowify, tracking via UTMify"
metadata: 
  node_type: memory
  type: project
  originSessionId: 63298d28-f5e7-4dd7-a31f-069f386a563c
---

Landing live em `brincadeiras-sem-tela.pages.dev` (Cloudflare Pages, projeto `brincadeiras-sem-tela`). Single-page HTML/CSS/JS, sem build.

**Pasta local (deploy):** `Desktop\brincadeiras-sem-tela-deploy\` — index.html + styles.css + script.js + assets/. Esse projeto NÃO tem repo git nem CI; deploy é manual via `wrangler pages deploy . --project-name=brincadeiras-sem-tela --commit-dirty=true`.

**OBS:** `Desktop\ebook-brincadeiras\` é OUTRO projeto — é o e-book em si (single-file HTML com sidebar de atividades). Não confundir.

**Estrutura da landing (ordem fixada 2026-06-02):**
hero (VSL) → dores → autoridade → o-que-recebe → bonus → **depoimentos carrossel "O que estão dizendo"** → planos → **depoimentos prints** → garantia → faq → cta final.

**Checkout — Lowify (3 ofertas, configuradas em `script.js` linhas 182-184):**
- CHECKOUT_FULL: `pay.lowify.com.br/go.php?offer=iu2q7ns` — R$ 14,90 (plano completo, botão `data-cta="completo"`)
- CHECKOUT_DOWNSELL: `pay.lowify.com.br/go.php?offer=n8j9x5y` — R$ 9,90 (modal downsell, `data-cta="downsell-aceita"`)
- CHECKOUT_BASIC: `pay.lowify.com.br/go.php?offer=45rkf9a` — R$ 5,90 (plano básico, `data-cta="basico"`)

CTAs externos (hero/features/depoimentos/final) só rolam para `#planos` — não são checkout.

**UTMify Pixel atual: `6a1f39f9bf3b382137cd7613`** (trocado 2x em 2026-06-02; histórico: `6a1cec8329cb7ec87a1bfc1a` → `6a1f36822114005a6374e473` → atual). Eventos não estavam chegando no Meta — provável causa: Meta Pixel ID/Access Token/domínio verificado faltando na config UTMify (não no script).

**Regra de IC na UTMify:** detectar por URL contendo `pay.lowify.com.br` (NÃO por texto — vários botões têm "QUERO" mas só rolam página). Purchase depende de integração Lowify ↔ UTMify ativa.

Why: usuário fez um pixel novo no Meta, então criou também novo pixel UTMify pra esse produto separar das outras ofertas.
How to apply: ao mexer em qualquer botão/checkout/pixel da landing, editar em `Desktop\brincadeiras-sem-tela-deploy\` e redeployar via wrangler. Ver [[project_caixa_magica]] e [[project_fitness_app]] para padrão UTMify+Cakto/Lowify+Meta CAPI.
