---
name: project_matematicabloques_area
description: "Área de miembros de Matemáticas con Minecraft (LATAM), clone estrutural do coreano re-tematizado, placeholders esperando conteúdo"
metadata: 
  node_type: memory
  type: project
  originSessionId: d5d099e3-97cd-4eb8-bfa0-999b2d8974ce
  modified: 2026-07-31T18:00:26.537Z
---

Área de membros (entregável) do info-produto **Matemáticas con Minecraft** — +100 atividades matemáticas imprimíveis estilo Minecraft, 1.º a 5.º de Primária, LATAM/ES, US$9,90 (Cakto). Landing: matematicabloques.pages.dev (repo [[project_megapacks]]-style, ver `matematicabloques-landing`).

Criado 2026-07-18 clonando a estrutura de `coreano-area-miembros-es` (HTML/CSS/JS estático), re-tematizado pra paleta Minecraft (verde grama `#5b9d33` + madeira `#8a5a2b`; variáveis CSS `--korea-*` mantidas com valores novos). Marca "＋", sem nenhuma imagem/resíduo coreano.

- Pasta: `Desktop\matematicabloques-area\`
- Repo: github.com/ursinho0909-cloud/matematicabloques-area (**private**), branch main
- Páginas: index.html + modulo-1..5 (um por série), modulo-problemas (100 Problemas / 10 misiones), modulo-tablas (Tabla de Multiplicar 1–10). Bônus (3): Mapa de Progreso, Tarjetas de Recompensa, Guía para Padres.
- **Progresso conteúdo (2026-07-31): CONTEÚDO COMPLETO.** Os 7 módulos têm 10 fichas reais cada (M1..M5, PROBLEMAS, TABLAS), ~2,5 MB por pasta. Não é mais placeholder.
- **Download do módulo inteiro em PDF**: cada `modulo-*.html` tem um botão `.modulo-dl` no hero (irmão do `.module-stats`) apontando pra `descargas/<slug>.pdf` — A4 595×842 pt, uma ficha por página. **Cor fixa `var(--korea-red)` verde #5b9d33 nos 7** — decisão do usuário de não variar por módulo (diferente do caligrafia, que herda `--c`). Gerados com Python/PIL: `Image.init()` é obrigatório senão dá `KeyError: 'JPEG'`, e ordenar pelo ÚLTIMO número do nome (`M1_Actividad07`→7, senão o "1" de M1 confunde). Regerar quando entrar ficha nova. Deploy no Pages leva ~1 min pra propagar os PDFs — testar duas vezes antes de achar que falhou.
- **Fichas geradas via Manus** estilo Minecraft worksheet (validado). Prompt kit reusável em `PROMPTS_MANUS_MODULO1.md` + referência de estilo `_referencia_estilo_M1.png`. Fluxo: gerar PNG na Manus → converter PNG→WebP (Pillow q85, ~250KB cada, -92%) → nomear `M{n}_Actividad0N.webp` → plugar card real (img+data-src ativa lightbox).
- **Falta**: fechar conteúdo módulos, deploy Cloudflare Pages, plugar checkout Cakto.

Segue o padrão de [[project_coreano_area_miembros_es]] / [[project_coreano_template_pattern]].
