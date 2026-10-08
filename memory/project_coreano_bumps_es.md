---
name: project-coreano-bumps-es
description: "Área de Bonos ES (LATAM) do Coreano — clone do bumps PT, marca \"Coreano Sin Complicaciones\""
metadata: 
  node_type: memory
  type: project
  originSessionId: e65e8713-e70c-4fc7-a3fe-af666891c91f
---

Versão ES (LATAM) da área de bônus (orderbumps) do Coreano, clone do BR `coreano-area-bumps.pages.dev`.

**Marca em ES:** "Coreano Sin Complicaciones" (mesma marca da [[project-coreano-area-miembros-es]]).

**Pasta local:** `C:\Users\User\Desktop\coreano-area-bumps-es\`
**Repo GitHub:** `github.com/ursinho0909-cloud/coreano-area-bumps-es` (private, criado 2026-06-24)
**Live (CF Pages):** https://coreano-area-bumps-es.pages.dev (projeto `coreano-area-bumps-es`)
**Live equivalente PT:** https://coreano-area-bumps.pages.dev (PT existe só no CF, sem GitHub — baixei via curl)

**Estrutura (4 HTMLs + assets):**
- `index.html` — home com 3 cards de bono
- `bump-exercicios.html` — Bono 1 · 100 Ejercicios
- `bump-desafio.html` — Bono 2 · Desafío de 30 Días
- `bump-flashcards.html` — Bono 3 · Flashcards de Coreano
- `bumps/` — 3 PDFs (100-ejercicios.pdf JÁ ES; desafio-30-dias.pdf e flashcards.pdf AINDA PT)
- `bumps-capas/` — capas + 3 páginas revista desafio + 4 láminas flashcards (TUDO ES)
- `assets/banner.png` — banner herdado do área de membros ES

**Estado conteúdo:**
- HTMLs: 100% traduzidos PT→ES
- 3 capas de bono: ES (geradas ChatGPT 24/06)
- 3 páginas revista desafio (dias 1-6, 13-18, 25-30): ES (Manus 24/06)
- 4 láminas flashcards (día a día, comida, viaje, expresiones): ES (Manus 24/06)
- Bono 1 PDF (100 ejercicios): ES — gerado via Chrome headless de HTML custom (64 páginas, 1.2 MB)
- Bono 2 PDF (desafio 30 días): ES — gerado via Chrome headless usando 3 imagens ES + cards inline (5 MB, era 17MB em PT)
- Bono 3 PDF (flashcards): ES — gerado via Chrome headless (capa + intro com 3 tips + 4 láminas full-page + cierre, 6.5 MB)
- Dias 7-12 e 19-24 do desafío: renderizados inline em HTML cards, já em ES

**How to apply:** quando user pedir pra mexer no bumps ES, usar essa pasta e repo. PDFs Bonos 2/3 ainda pendentes de tradução — quando solicitar, usar mesmo padrão do Bono 1 (extrair texto do PDF PT via pypdf, traduzir manualmente, gerar HTML custom, renderizar via Chrome headless `--print-to-pdf`).

**Deploy:** `wrangler pages deploy . --project-name coreano-area-bumps-es --branch main --commit-dirty=true`
