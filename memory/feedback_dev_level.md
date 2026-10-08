---
name: feedback-dev-level
description: "Usuário é dev capaz (ships Next.js + Cloudflare Workers + Supabase em produção). NÃO explicar coisas básicas de web dev, ir direto pra arquitetura e decisões."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee771611-29c7-428f-8237-a58c14834760
---

Usuário shipa software de verdade em produção: Next.js 14 + App Router + Supabase + Cloudflare Workers + Resend + magic link auth + webhooks Cakto + Meta CAPI forwarder (ver [[project-fitness-app]], [[project-controle-ml]]). Ele constrói, integra, deploya, debugga sozinho — não precisa de "o que é JSON" nem "como funciona uma API route".

**Quando ele perguntar "o que preciso fazer/construir pra X":**
- Vai DIRETO pra: arquitetura (multi-tenant, escala, isolation), decisões de stack que mudam o jogo (Postgres RLS vs schemas, SSG vs SSR, custom domain strategy, billing recorrente BR), trade-offs reais entre opções, e a parte de NEGÓCIO que ele não delegou pra outros projetos ainda (CNPJ, NFe, cobrança B2B, churn metrics).
- NÃO faça: tutorial de "como criar um componente", "o que é Next.js", listar ferramentas óbvias, explicar JSON, explicar webhook, listar etapas de "instala node, roda npm install".

**Por que:** em 2026-05-28 eu enchi 3 telas explicando o que é um template configurável com JSON, como funciona Vercel, e ele cortou: "voce esquece que eu sei fazer site, webapp isso é piada". Tinha razão.

**Como aplicar:** quando ele pedir conselho técnico, antes de responder me pergunto: "isso aqui é informação nova pro [[project-fitness-app]] caliber dev, ou é tutorial de YouTube?". Se for tutorial, corta e vai pro próximo nível: arquitetura, trade-off, ou o lado business que ele ainda não enfrentou (B2B SaaS recorrente é diferente de info-produto one-shot).
