---
name: project-anatomie-fr
description: "Bônus de anatomia traduzidos DE→FR em 05/10/2026 (200 flashcards, récapitulatif express, plan 30 jours); gerador Python+Chrome em Desktop\\PROJETOS\\anatomie-FR\\src"
metadata:
  node_type: memory
  type: project
  originSessionId: df30c755-fde9-4e2c-9c48-3d6013e099d9
  modified: 2026-10-05T16:12:31.010Z
---

Três PDFs franceses criados a partir dos alemães (Downloads): 200_Flashcards_Anatomie_Francais.pdf (52 p), Recapitulatif_Express_Anatomie_Humaine_FR.pdf (8 p), Anatomie_Plan_Etude_30_Jours_FR.pdf (5 p). Pasta Desktop\PROJETOS\anatomie-FR; dados em src\fc_data.py, layout+textos em src\gen.py (`python gen.py fc|re|lp` regenera via Chrome headless).

O "Revisão Express" alemão original tinha bugs (setas viraram "?", texto PT sobreposto, sistema 10 sem texto, resposta 08 vazia) — a versão FR foi reconstruída em HTML e corrigida; o DE continua com os bugs.

**How to apply:** para outro idioma (IT/ES/PT), copiar gen.py + fc_data.py e traduzir os textos; não reaproveitar o PDF alemão do Revisão Express.
