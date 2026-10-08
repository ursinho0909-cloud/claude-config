---
name: project-anatomia-alemanha
description: "Anatomia DE — PDF PLR (202 págs, ex-SketchMED) traduzido pro alemão em 2026-09-25, em Desktop\\PROJETOS\\anatomie-DE; mercado DE sem concorrente de mapas baratos"
metadata:
  node_type: memory
  type: project
  originSessionId: 2fdc437a-d748-41ef-8a8d-8638f68c1d73
  modified: 2026-09-25T12:31:24.067Z
---

**Entregável (2026-09-25):** `Desktop\PROJETOS\anatomie-DE\ANATOMIE_ILLUSTRIERT_DE.pdf` — 202 págs, tradução do `Downloads\ANATOMIA_ILUSTRADA_PT2.pdf` (material PLR; usuário confirmou licença). Logo "SketchMED" + assinatura "Paola Rios" removidos (estavam só nas págs 28, 55, 63, 89, 101, 103, 112, 132, 134, 201).
- Padrão: títulos em latim (OS SACRUM, SCAPULA, CUBITUS...), legendas com nomenclatura latina + explicação em alemão; vistas "Ansicht von vorne/hinten/lateral/medial/oben/unten". Texto alemão é vetorial (nítido, pesquisável).
- Pra corrigir uma página: editar `_traducao\tr\<pág>.txt` (formato `id| linha1 / linha2`; `T x0,y0,x1,y1|` título manual; `E x0,y0,x1,y1| texto` apaga área e escreve) e rodar `render.py <pág>` na pasta `_traducao` — precisa de `src/` e `x2/` regenerados via `ocr_all.py` a partir do PDF PT.
- Fonte PT tem erros de anatomia/tradução (ex.: pág 74 rotula faces do osso como "Osso trapezoide"); corrigi no alemão onde o contexto era claro.

**Pesquisa de mercado (2026-09-24)** pra levar [[project-anatomia-area-miembros]] pra Alemanha:
- "Anatomie Mindmaps": 1 anúncio (Thieme). "Anatomie Lernkarten" ~7: Medi Know, Thieme, Elsevier.
- Concorrente mais próximo: Medi Know (medi-know.org), skripte digitais, bundle 199 €.
- Ninguém rodando o formato BR (mapas visuais PDF, preço baixo) em alemão.
- Público: Pflegeausbildung, Heilpraktiker, Physio, Medizinstudium.
