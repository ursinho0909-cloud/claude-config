---
name: feedback-landing-sync-before-edit
description: "Antes de editar QUALQUER landing/site multi-PC, baixar o HTML/assets do deploy LIVE primeiro pra comparar com a pasta local — pode estar dessincronizado"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 07f686e6-cc47-4710-b2e6-3fde8a2b7085
---

Antes de editar arquivos de uma landing/site que tem deploy no Cloudflare Pages (ou Vercel/Workers), SEMPRE baixar o último deploy live e comparar com a pasta local antes de tocar em qualquer coisa.

**Why:** Aconteceu 2x e queimou ciclos do usuário pra resolver.
- 2026-06-06: quebrei a sales page de futsal (`treinos-futsalpremium.pages.dev`) sobrescrevendo VSL, selo de garantia, benefit-cards. A versão boa tinha sido deployada do outro PC, Google Drive Desktop atrasado. Rodei `wrangler pages deploy .` com o estado VELHO da pasta, apagando trabalho recente.
- 2026-06-25: deployei `coreano-descomplicado` e apaguei o pixel Lowtrack `lt_px_279e4369ef31`. Causa diferente: o pixel tinha sido adicionado via DEPLOY DIRETO no live (sem commit no git), então mesmo com repo sincronizado o `index.html` local não tinha. Detectei via `wrangler pages deployment list` (deploy anterior com "Source" vazio = deploy direto sem git).

**How to apply:**
- Antes do primeiro Edit/Write em um projeto de landing: `curl -s https://<projeto>.pages.dev/ | grep -iE "pixel|utmify|fbq|lowtrack|gtag|<script"` pra ver se tem scripts de tracking que o repo pode não ter
- `diff <(curl -s LIVE_URL) index.html` pra ver diferença geral
- `wrangler pages deployment list --project-name=X` — se algum deploy recente tiver "Source" vazio, foi deploy direto sem git → arquivos live podem ter conteúdo que o repo não tem (pixel, hotfix, etc)
- Padrão de projetos com risco multi-PC: `arsenal-futsal-landing`, `caixamagica`, `brincadeiras-sem-tela-deploy`, `treino-express-vendas`
- Memory [[project-github-sync]] lista quais já estão em GitHub. Os que NÃO estão são os de maior risco do tipo "Drive atrasado"
