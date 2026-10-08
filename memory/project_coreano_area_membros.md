---
name: project-coreano-area-membros
description: "Área de membros (entregável) do produto Coreano Descomplicado, live na Cloudflare Pages, pendente plug do conteúdo dos módulos"
metadata: 
  node_type: memory
  type: project
  originSessionId: b7d6835d-f28e-4b75-8aab-17e05cd95fe3
---

Área de membros do info-produto coreano (par do [[project-coreano-descomplicado]]).

**Live:** https://coreano-area-membros.pages.dev (CF Pages, projeto `coreano-area-membros`)
**Pasta:** `C:\Users\User\Desktop\PROJETOS\coreano-area-membros\` (re-clonada do GitHub em 2026-08-21)
**Repo:** github.com/ursinho0909-cloud/coreano-area-membros (PRIVATE, inclui os 40 PNGs ~74MB)
**Deploy:** `npx wrangler pages deploy . --project-name=coreano-area-membros --commit-dirty=true`

**Estrutura:**
- 4 módulos CEFR (A1/A2/B1/B2) com capas em `modulos-capas/nova_capa_*.png`
- Seção bônus com 4 PDFs em `bonus/bonus-{1..4}.pdf` (vieram de `C:\Users\User\Desktop\KOREIAA\`)
- Sidebar lateral fixa (drawer no mobile com hambúrguer) + scroll spy
- Cada módulo: capa clicável + botão "Acessar Material" que expande/colapsa o painel de conteúdo
- Banner topo (`assets/banner.png`) + capa de bônus (`assets/bonus-cover.png`)

**Paleta:**
- A1+A2 = vermelho coreano `#CD2E3A`
- B1+B2 = azul coreano `#0047A0`
- Bônus = dourado `#efb849`
- Fundo creme `#fbf8f1`

**Status (2026-08-21):** CONTEÚDO PLUGADO e VENDENDO. Oferta PT rodando pra **Portugal** (primeiras 4 vendas em 21/08/2026). Módulos hoje: A1/A2/B1/B2/C1/C2 + Caligrafia (pill "NEW") + Curiosidades + Vídeo. WhatsApp de suporte REMOVIDO (link do sidebar, modal e handler no app.js + template em `build-pages.py`) — não reintroduzir.

**Why:** entregável da oferta coreana (par do [[project-coreano-descomplicado]] que é a sales page). Antes era só sales sem área de membros — agora tem onde entregar.

**How to apply:** quando usuário mandar conteúdo de cada módulo (texto/aulas/vídeos/PDFs), plugar dentro do `<div class="modulo-content" data-content="aN">` correspondente, substituindo o `.empty-placeholder`. Re-deploy via wrangler.
