---
name: project-adesiva-pro
description: "Landing APP ADESIVA PRO (info-produto figurinhas Stories Instagram) — R$19,90 plano anual, LIVE em adesiva-pro.pages.dev. Cliente externo. Sem checkout plugado ainda."
metadata: 
  node_type: memory
  type: project
  originSessionId: a0432f5e-c777-4676-adcb-8a2c3a606183
---

Landing page do **APP ADESIVA PRO** — info-produto de figurinhas estratégicas para Stories do Instagram. **É pra cliente externo do usuário**, não produto próprio.

- **Live**: https://adesiva-pro.pages.dev (Cloudflare Pages, projeto `adesiva-pro`)
- **Repo**: https://github.com/ursinho0909-cloud/adesiva-pro-landing (privado, conta ursinho0909-cloud)
- **Pasta local**: `C:\Users\User\Desktop\adesiva-pro-landing\`
- **Oferta**: De R$97,00 por **R$19,90** plano anual
- **Stack**: HTML único + Tailwind CDN + 3 vídeos demo do app + 62 imagens reais (depoimentos, mockups stories, kits temáticos por nicho)
- **Status**: Visual entregue. **Falta**: plugar checkout (Cakto? Lowify? Hotmart?), trocar `href="#"` do botão "QUERO AGORA", adicionar pixel UTMify + Meta CAPI, e-mail/WhatsApp reais no footer/suporte

**Why**: cliente externo (não é do portfólio do usuário) — projetos parecidos dele (Brincadeiras, Caixa Mágica, etc.) seguem padrão Cakto/Lowify + UTMify, mas esse aqui ainda não tem decisão de qual checkout.

**How to apply**: pra atualizar, edita o HTML local e roda `wrangler pages deploy . --project-name=adesiva-pro --commit-dirty=true --branch=main` da pasta. Quando o cliente decidir checkout, plugar no botão "QUERO AGORA" da seção `#oferta` e configurar pixel igual [[project_brincadeiras_landing]].
