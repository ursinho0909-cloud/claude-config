---
name: project-farmacologia-sin-complicaciones
description: "Info-produto LATAM \"+100 Mapas Mentales de Farmacología\" (ES), área de membros pronta, lançamento pré-venda mai/jul 2026"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2f1cfb39-0633-4f57-a899-36b0508b98c7
---

Info-produto de saúde pra LATAM (ES): **"Farmacología Sin Complicaciones — +100 Mapas Mentales de Farmacología"**. Parte do cluster saúde junto com [[project_anatomia_area_miembros]] (mesma marca "Sin Complicaciones", mesmo público estudante de saúde → cross-sell). Decidido 2026-07-10 após validar concorrência no Meta Ad Library (~85 ads ativos "mapas mentales de farmacología") e mercado Hotmart (Paolo López +300 mapas mas 2 estrelas = brecha de qualidade).

**ÁREA DE MEMBROS** (entregável) em `C:\Users\User\Desktop\farmacologia-area-miembros\` — clonada do esqueleto de [[project_coreano_area_miembros_es]] (HTML estático + gerador `build-pages.py`, lightbox, galeria zoom/download). Git re-inicializado (desconectado do coreano). Servidor local de teste: `python -m http.server 8899`.

**ESTRUTURA:** 10 módulos por sistema, 104 mapas total. Cores por grupo: Módulo 1 (Principios) neutro/branco, 2-4 (SNA/SNC/Cardio) marinho, 5-7 (ATB/Endo/Resp) verde, 8-10 (Dig/Dolor/Urg) roxo. Tema CSS trocado de vermelho→paleta creme+marinho+verde+roxo(bônus amarelo). Classes `.mtheme-navy/green/purple/white` fazem override local de `--korea-red*`.

**MAPAS:** gerados no **Manus** com prompts padronizados (template 6 blocos de fármaco OU conceitual; ilustração central; estruturas variadas A-G intercaladas pra não enjoar; cor de acento própria por mapa). Fluxo: user gera → zipa → eu renomeio pro padrão `FOLDER_NN_Nome.png` → converto PNG→WebP (Pillow quality 82, ~8% do peso) → `build-pages.py`. Status 2026-07-10: 98/104 plugados + 10 capas (mockup de livro). **Faltam 6:** Cardio (Espironolactona, Digoxina, Heparina, Warfarina, Antiagregantes) + Respiratorio (Ipratropio).

**PENDENTE:** 6 mapas restantes, landing de vendas + checkout + pixel, deploy (Cloudflare Pages provável), git commit/push. Plano de lançamento: pré-venda segunda com módulos prontos, resto progressivo. Timing LATAM: julho é vale (férias 2 blocos), escalar ago-nov.
