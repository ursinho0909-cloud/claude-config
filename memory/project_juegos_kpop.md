---
name: project_juegos_kpop
description: "Info-produto UNO K-Pop imprimível (LATAM/ES), live em juegos-kpop.pages.dev, RODANDO TRÁFEGO a $7,90 — tracking sem UTMify (Hotmart CAPI + src/sck manual)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 94200492-0cde-43e7-b6ad-343e4df58fca
  modified: 2026-07-21T18:08:12.877Z
---

Info-produto **"UNO K-Pop"** pra LATAM (ES): jogo de cartas estilo UNO imprimível, **7 grupos** cada um com SEU próprio jogo (BTS, BLACKPINK, Stray Kids, SEVENTEEN, TWICE, ENHYPEN, aespa). Oferta única **$9,90 USD** (âncora $59,90), 3 bônus ($40,70): Nuevos Grupos Gratis + Guía de Impresión + Derecho de Reventa.

**Estratégia de risco (decidida):** "UNO" NÃO aparece no nome do produto/URL (marca Mattel) — só no criativo do anúncio, formato UGC. URL/repo limpos de propósito. Fotos de idols "sem reproduzir rostos com exatidão".

**Onde está:**
- Pasta: `C:\Users\User\Desktop\cartas-kpop-latam\` (nome da pasta ≠ nome do projeto)
- Live: **juegos-kpop.pages.dev** (Cloudflare Pages, projeto `juegos-kpop`), deploy via `wrangler pages deploy .`
- Repo: github.com/ursinho0909-cloud/juegos-kpop (privado), criado 2026-07-16
- Tema claro (branco creme + vermelho/rosa kpop), faixa 4 cores UNO. Fontes Fredoka+Nunito+Luckiest Guy.

**Arte:** tudo WebP comprimido via ffmpeg (não tem cwebp/magick na máquina, usar ffmpeg -c:v libwebp). Hero + 7 boxes (carrossel) + 3 bônus + 5 depoimentos (3 wpp + 2 ig, prints realistas com foto do material) + mockup oferta (7 boxes juntas). Imagens geradas no Manus/ChatGPT.

**Status 2026-07-21:** LANÇADO e rodando tráfego. Preço mexido 2x no mesmo dia: $9,90 → $7,90 → **$8,90 USD** (âncora $59,90 mantida). Checkout Hotmart `pay.hotmart.com/F106811559O`. ⚠️ Dado do dia 21/07 é inanalisável por preço (3 preços + mudança de tracking no mesmo dia). Preço se testa em degrau grande ($8,90 vs $12,90), nunca em R$1 — volume dele (27 ICs) não distingue.

**Tracking — este projeto é a EXCEÇÃO do padrão (não tem UTMify):**
Estourou o limite de slots da UTMify (ocupados por anatomia, coreano ES, photocards, matematicabloques + 3 BR parados). Montado à mão:
- Pixel Meta `1051155734276688` na landing → PageView + InitiateCheckout (IC só no `#cta-oferta`).
- Pixel cadastrado na **Hotmart** (Ferramentas → Pixel de Rastreamento), evento **só "Vendas realizadas"**. IC NÃO marcado lá de propósito — dobraria o IC da landing.
- Envio **só via API de Conversão** (token configurado), WEB desligada por escolha do usuário.
- Atribuição de criativo: script no fim do `index.html` captura UTM+fbclid, guarda em `sessionStorage` e injeta na URL da Hotmart como `src`=campanha e `sck`=criativo. **É o `sck` no relatório de vendas da Hotmart que diz qual CTV vendeu.** Parâmetros de URL já configurados nos 4 anúncios do Meta (`{{ad.name}}` etc).

**Aprendizados da campanha (dia 1):** campanha "CAMPANHA UNO", 4 conjuntos. Otimizava por **Comprar** com o evento nunca tendo disparado (pixel Hotmart só entrou em 21/07) — vendeu mesmo assim. Métricas com o algoritmo cego: CTR 3,38%, CPC R$0,42, CPM R$14,23, conversão de página 20,45%, 27 ICs. Meta de desempenho **não pode ser trocada** depois de publicada.

**Pendente:** confirmar que o conjunto de dados "PIXEL-UNO" da campanha == pixel `1051155734276688`; validar `Purchase` no Gerenciador de Eventos e `sck` no relatório Hotmart (teste com cupom 100%); fechar ROAS real com gasto × vendas Hotmart.

Relacionado: [[project_coreano_launch_latam]] (mesmo playbook LATAM), [[feedback_orderbump_playbook]], [[project_photocards_latam]] (mesma pasta-mãe de nicho kpop).
