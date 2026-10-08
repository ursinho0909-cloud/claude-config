---
name: project_caligrafia_bluey
description: "Info-produto LATAM \"Caligrafía Bluey\" — 10 cadernos / 100 fichas, US$9,90. Landing em Desktop\\caligrafia-bluey-landing"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4923dff1-80c3-409e-89bd-abf9fe69423f
  modified: 2026-08-01T12:30:29.700Z
---

Info-produto LATAM (ES) de caligrafia infantil temática Bluey. Iniciado 2026-07-30.

**Oferta:** 10 cadernos × 10 fichas = 100 fichas / +400 exercícios · US$ 9,90 (antes US$ 29,90) · 3 bônus (tablero de progreso, diplomas, guía para padres) + Calendario de Práctica 30 días. Público: mãe de criança 4-8 anos.

**Os 10 cadernos:** 1 Trazos · 2 Vocales · 3 Mayúsculas · 4 Minúsculas · 5 Sílabas · 6 Palabras · 7 Frases · 8 Escritura Divertida · 9 Repaso General · 10 Desafíos. Cada um tem cor própria (paleta Bluey) e capa `c1..c10.webp`.

**Landing LIVE em https://caligrafia-en-casa.pages.dev** (projeto CF `caligrafia-en-casa`, repo privado `ursinho0909-cloud/caligrafia-en-casa-landing`). Pasta local continua `Desktop\caligrafia-bluey-landing` — não renomeada. Clone estrutural de `matematicabloques-landing`, CSS reescrito na paleta Bluey (Baloo 2 + Nunito, CTA laranja Bingo). Página inteira pesa 1,35 MB.

Headline escolhida: **"Bluey le enseña a escribir. Tú solo imprimes."** — Bluey em linha própria, 1,75× e amarelo.

**Pendente na landing:** as 8 fichas `f1..f8.webp` hoje são a MESMA imagem repetida (só preview); pixel UTMify; link do checkout (botão está com `href="#"`); e-mail real no `politicas.html`.

**ÁREA DE MEMBROS (entregável) LIVE em https://caligrafia-area-miembros.pages.dev** — projeto CF `caligrafia-area-miembros`, repo `ursinho0909-cloud/caligrafia-area-miembros`, pasta `Desktop\caligrafia-area-miembros`. Deploy via `npx wrangler pages deploy .`.

**Progresso das fichas (2026-07-31): 95 de 100.** C1–C6 completos · C7 faltam Ficha01 e Ficha10 · C8 completo · C9 tem 01–07 (faltam 08, 09, 10) · C10 completo.

**C10 saiu com identidade visual diferente das outras 90** (blocos dentro de caixas em grade 2×2, banner redesenhado, pauta escolar ausente nas fichas 05/07/08, numeração duplicada nos títulos). Usuário decidiu subir assim mesmo em 2026-07-31 — não é bug pra corrigir, é decisão tomada.

**Download do cuaderno inteiro:** cada `cuaderno-N.html` tem um botão `.cuaderno-dl` no hero (irmão do `.module-stats`, herda o `--c` da section pra pegar a cor do cuaderno) que baixa `descargas/cuaderno-NN-slug.pdf` — A4 595×842 pt, uma ficha por página. Gerados com Python/PIL a partir de `cuadernos-content/CN/`. **PIL precisa de `Image.init()` senão dá `KeyError: 'JPEG'` ao salvar PDF.** Regerar os PDFs sempre que entrarem fichas novas.

**Originais em alta (1632×2176):** `Desktop\caligrafia-originais\` — `capas\capa_cuadernoN.webp` (10) + `C1..C8`. Os originais do C8 estavam só num scratchpad temporário do Claude e foram recuperados pra cá em 2026-08-01. **C9 e C10 ainda não têm originais salvos** — só a versão comprimida 1100×1467 da área. Sem original em alta não dá pra fazer PDF de impressão decente (a versão da área dá só ~133 DPI).

**PDFs de impressão:** `caligrafia-area-miembros\impressao\CUADERNO-N-...-IMPRIMIR.pdf` — capa + 10 fichas, A4, margem 8 mm, 214 DPI, JPEG q95 4:4:4. Script em scratchpad `montar_pdf_impressao.py`. Diferente dos PDFs de `descargas\` (esses são só entrega digital, sem capa).

**PDF de entrega da Hotmart:** `caligrafia-area-miembros\entrega\acceso-area-de-miembros.pdf` (fonte em `entrega\src\`), clone do modelo do Minecraft na paleta Bluey. **Chrome headless não sobrescreve PDF existente — apagar antes de regerar.**

**Pipeline das fichas:** prompt `PROMPTS_MANUS_CUADERNO{N}.md` no próprio repo → Manus gera 1 ficha por conversa a 1632×2176 → ZIP → eu comprimo com ffmpeg pra WebP **1100×1467 quality 82** (~140 KB/ficha, ~1,4 MB/cuaderno) → `cuadernos-content/C{N}/`. Sempre revisar ficha por ficha antes de subir — ver [[feedback_manus_prompt_order]].

**Por que Bluey e não Patrulha Canina:** ver [[feedback_bluey_vs_patrulha]]. Patrulha Canina fica como bump (~60 fichas) ou produto #2; fila depois: Miraculous, Peppa.

Segue o padrão de área de membros dos outros produtos — ver [[project_matematicabloques_area]] e [[project_coreano_template_pattern]].
