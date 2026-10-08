---
name: project-parabolas-jesus
description: "Landing info-produto \"As 40 Parábolas de Jesus Explicadas\" (R$5,90/R$14,90 com upsell R$9,90), live em parabolas-jesus.pages.dev"
metadata: 
  node_type: memory
  type: project
  originSessionId: 236d8358-e854-4906-bdc3-af9be6026728
---

Landing de info-produto cristão criada em 2026-06-11. Vende ebook "As 40 Parábolas de Jesus Explicadas".

**Stack:** HTML/CSS/JS single-file, sem build, deployada via wrangler em Cloudflare Pages.

**URLs:**
- Landing live: https://parabolas-jesus.pages.dev
- **Área de membros (entregável) live:** https://parabolas-jesus-area.pages.dev (deployada 2026-06-12, CF Pages projeto `parabolas-jesus-area`)
- Repo landing: github.com/ursinho0909-cloud/parabolas-jesus-landing (privado)
- Pasta local landing: `C:\Users\User\Desktop\40-parabolas-jesus\`
- Pasta local área: `C:\Users\User\Desktop\parabolas-jesus-area\` (com `audio/` e `index.html`)

**Áudios adicionados na landing (2026-06-12):** 3 players MP3 abaixo do sumário "O que você recebe hoje" — A Parábola da Figueira, do Semeador e do Filho Pródigo. Arquivos em `audio/figueira.mp3`, `audio/semeador.mp3`, `audio/filho-prodigo.mp3` (ainda não deployado — falta `wrangler pages deploy` na pasta da landing).

**Área de membros:** single-file HTML com sidebar TOC sticky das 40 parábolas, cada uma com 5 seções (I texto bíblico, II ensinamento, III significado, IV aplicação, V oração). Mesma paleta da landing. Print-friendly. Navegação JS com IntersectionObserver pra highlight do item ativo.

**Ofertas:**
- Essencial R$ 5,90 (só ebook)
- Premium R$ 14,90 (ebook + 4 bônus: 30 Dias com Jesus, 100 frases, diário de oração, guia de reflexão)
- **Upsell R$ 9,90** (modal abre ao clicar Essencial) — mesma oferta da Premium com R$ 5 desconto, "só nesta tela"

**Autora/persona:** Conceição Almeida — católica, 40+ anos de fé, formada em Teologia, catequista (não é pessoa real, persona de copy).

**Pendente plugar checkouts** quando criar links Cakto/Lowify:
- `.cta-offer` da Essencial (atual: `<button data-open-upsell>` que abre modal) — botão "Não, prefiro a Essencial" do modal vai pro checkout R$5,90
- `.cta-offer` da Premium (atual: `href="#"`) — checkout Premium R$14,90
- `#upsellAccept` no modal — checkout R$9,90 (precisa criar essa oferta)

**Imagens:** 6 WebP em `img/` totalizando ~1MB (originais PNG eram 13MB, comprimidas com Pillow q=82-85). Imagens prontas que vieram do ChatGPT: capa, capa-premium, jornada, autora, recebe-hoje. Tudo no fluxo creme/dourado/azul-marinho.

**Não usa:** tracking pixel (sem UTMify/Meta CAPI ainda), checkout, analytics. Tudo a plugar.
