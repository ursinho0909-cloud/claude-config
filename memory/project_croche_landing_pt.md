---
name: project_croche_landing_pt
description: Landing PT-PT "+100 Receitas de Croché para a Casa" 14,90 € em Desktop\PROJETOS\croche-casa-pt, base para clonar FR e DE
metadata:
  type: project
---

Landing de vendas do Crochê para Casa ([[project_croche_casa]]) para Portugal, criada 2026-09-29 em `Desktop\PROJETOS\croche-casa-pt\index.html` (HTML único, sem git, preview `python -m http.server 8795`). Estrutura clonada do Pilates PT (pilates-pt-landing) — o usuário quer depois clonar pra FR e DE com a mesma estrutura.

Paleta verde-floresta #1d5a45 + terracota #c0603a + creme; fontes Fraunces + Nunito Sans. Secções: hero (HERO PORTUGAL.png) → carrossel de fichas (páginas do PDF original) → telemóvel folheando o PDF → grelha de 6 categorias por divisão (pedido do usuário, "abaixo do celular") → ideal para → CTA → contador → entregável (capa_…_ptpt_1x1) → 4 bónus com valores 17/12/14/19 € → oferta 14,90 € (âncora "De 39,90 €") → garantia 7 dias → como funciona → FAQ → fecho.

Pendente: CHECKOUT_URL (constante no script, hoje "#oferta"), pixel, deploy CF Pages. Imagens com PT-BR: capa do Bónus 3 diz "Crochê", Planner diz "Autor: [Seu Nome]"; fichas do carrossel são do PDF original em PT-BR.

**FR e DE (2026-09-29):** clones em `Desktop\PROJETOS\croche-casa-fr` (localhost 8796) e `croche-casa-de` (8797), gerados por `croche-casa-pt\build_lang.py` (pares PT→idioma; rodar de novo depois de mexer no PT). Hero = capa 1x1 do idioma (Downloads), fichas/bónus tirados de out_fr/out_de do pipeline de tradução. FR em "vous", DE em "du". Nome usado: FR "+100 Modèles de Crochet pour la Maison", DE "+100 Häkelanleitungen fürs Zuhause" — as capas 1x1 do usuário dizem "recettes de crochet" e "Häkelideen für die Wohnungsdekoration". DE ainda sem Impressum/Datenschutz.

**Hotmart (29/09, INTERROMPIDO pelo usuário):** PT principal 8619698 (+100 Receitas de Croché para a Casa, 14,90 € c/ impostos, 7 dias, livro dividido em 3 partes <10 MB + 4 bónus) e bump1 PT 8619783 (Guia de Acabamentos, 6,90 €) enviados p/ aprovação. Faltam: bump2 PT (+50 Mini Projetos 8,90 — estava no passo de preço, rascunho pode ter ficado), bump3 PT (Natal 9,90), Kit 3 em 1 PT (9,90), todos FR/DE, e os 3 checkouts. Partes do livro e capas 1000px em <pasta idioma>\_hotmart\. Lições: ferramenta de upload só aceita arquivo <10 MB; digitar pelo teclado às vezes se perde (aba congela) → preencher com setter nativo via JS; "Cadastrar eBook" = navegar direto p/ /products/add/4/info.
**CTV impresso (29/09):** CTV-CROCHE-PT/FR/DE.pdf na raiz de cada pasta de idioma (capa + fichas p002, p011, p054, p078, p084). Capa traduzida por ctv_capa.py em CROCHE FRANÇA\_quellen.
**Checkouts e preço (29/09):** PT J107814692M 14,90 € · FR F107815396L 17,00 € · DE D107815643K 17,00 € (todos ?checkoutMode=10). Hotmart todo feito pelo usuário. Preço/URL FR-DE ficam em pares no build_lang.py.
**LIVE (29/09):** PT receitas-croche-casa.pages.dev · FR crochet-maison.pages.dev · DE haekeln-zuhause.pages.dev (CF Pages, projetos com os mesmos nomes). Deploy = copiar index.html + assets p/ pasta temporária e `npx wrangler pages deploy <pasta> --project-name <proj> --branch main` (não subir build_lang.py). Sem pixel ainda.
**Pixel PT (29/09):** UTMify 6abbfb6d185b6483b76731e3 + utms/latest.js no head do PT, em forma legível (o snippet ofuscado só faz window.pixelId + carregar pixel.js). build_lang.py remove o bloco "<!-- UTMify Portugal" antes de gerar FR/DE. LIVE.
**Pixel FR (29/09):** UTMify 6abbfc85839c25614eb6d76f, par no build_lang.py (lista FR). LIVE.
**Pixel DE (29/09):** UTMify 6abbfdf3dd197b176870140c, par no build_lang.py (lista DE). LIVE. Os 3 países têm pixel próprio.
