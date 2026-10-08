---
name: project-boxe-pro
description: Boxe Pro — info-produto 500 treinos boxe. Sales boxe-pro.pages.dev + área de membros boxe-pro-area.pages.dev. Pasta Desktop\boxe-pro-landing (Next 15) + Desktop\boxe-pro-area (HTML puro)
metadata: 
  node_type: memory
  type: project
  originSessionId: fbadf291-e276-4213-81d6-9b74e3cd2807
---

Info-produto Boxe Pro: 500 treinos em vídeo. Mesmo modelo do Arsenal Futsal (Drive como host de vídeo).

**Live (sales page):** https://boxe-pro.pages.dev (CF Pages, projeto `boxe-pro`)
- Stack: Next.js 15 + TS + Tailwind + Framer Motion, static export
- Pasta local: `C:\Users\User\Desktop\boxe-pro-landing\`
- Repo: https://github.com/ursinho0909-cloud/boxe-pro-landing (privado, criado 2026-06-09)
- Deploy: `npm run build && wrangler pages deploy out --project-name=boxe-pro --branch=main --commit-dirty=true`

**Live (área de membros):** https://boxe-pro-area.pages.dev (CF Pages, projeto `boxe-pro-area`, criado 2026-06-09)
- Stack: HTML puro + CSS, sem build (mesma fórmula Arsenal Futsal)
- Pasta local: `C:\Users\User\Desktop\boxe-pro-area\`
- Repo: https://github.com/ursinho0909-cloud/boxe-pro-area (privado, criado 2026-06-09)
- Deploy: `wrangler pages deploy . --project-name=boxe-pro-area --branch=main --commit-dirty=true` dentro da pasta
- Estrutura: 10 módulos (JAB·DIRETO·CRUZADO·UPPERCUT·DEFESA·ESQUIVAS·MOVIMENTAÇÃO·COMBINAÇÕES·CONDICIONAMENTO·ESTRATÉGIA) + 4 bônus PDF. Cada card é `<a href>` que abre pasta Drive em nova aba (placeholders `#` ainda)
- 3 fotos rotacionadas (jab/direto/movi) intercaladas pra não repetir mesma seguida

**Produto:**
- Preço: R$6,97 (Básico, 12 meses) / R$24,97 (Premium, vitalício)
- Upsell modal: R$14,90 ao clicar Básico
- Checkout: ainda não plugado (botões em `#`)

**VSL:** vídeo real do usuário (`vsl.mp4` 3MB comprimido) em `boxe-pro-landing/public/`, player custom anti-rewind, capa `vsl-poster.webp` ("500 VÍDEOS DE BOXE"), aspect 9:16

**Visual:** preto #0A0A0A + vermelho #D90429. Fundo da landing usa 3 imagens (`bg-1/2/3.webp`) com crossfade em scroll. Sticky bar "Garantir treinos agora" aparece só depois do FAQ.

**How to apply:**
- Atualizar conteúdo da área de membros: editar `index.html` dos `<a href>` dos cards/bônus e fazer deploy de novo
- NÃO confundir os 2 projetos CF Pages: `boxe-pro` (sales) ≠ `boxe-pro-area` (entregável)
- Source images originais ficam em `C:\Users\User\Desktop\BOXE\` (BONUS 1-4, CAPA 1/2/3, VSL.mp4) e `C:\Users\User\Desktop\boxe entregavel\` (hero, jab, direto, movi pra área)

**Falta:**
- Plugar links Drive em 10 módulos + 4 bônus
- Plugar checkout Cakto/Hotmart nos 3 botões da sales (Básico, Premium, upsell R$14,90)
- Setup tracking (UTMify? pixel Meta?) similar ao Caixa Mágica
