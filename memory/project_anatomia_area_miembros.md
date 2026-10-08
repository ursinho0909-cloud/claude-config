---
name: project-anatomia-area-miembros
description: "Area de membros do info-produto Anatomia Sin Complicaciones (LATAM, ES) · 10 sistemas · LIVE"
metadata: 
  node_type: memory
  type: project
  originSessionId: c8239071-ad35-4ce1-947e-85e80a7f9d33
---

Area de membros do info-produto **"Anatomía Sin Complicaciones · +100 Mapas Mentales Visuales"** pra LATAM (espanhol).

**Stack:**
- Pasta local: `C:\Users\User\Desktop\anatomia-area-miembros\`
- Repo: `github.com/ursinho0909-cloud/anatomia-area-miembros` (privado)
- LIVE: **https://anatomia-area-miembros.pages.dev** (CF Pages project name `anatomia-area-miembros`)
- Sales page par: `anatomia-sin-complicaciones.pages.dev` (em `Desktop\anatomia-sin-complicaciones-landing\`)
- Paleta: teal-petróleo `#0B4F6C` + vermelho médico `#D32F2F` + cream `#FAF4E8`

**Estrutura:** 10 módulos (sistemas) × 10 mapas mentais cada = 100 mapas. Cada slot é um JPG em `modulos-content/<SISTEMA>/<SISTEMA>_NN_<key>.jpg`.

**Status mapas: 100/100 ✅ COMPLETO (fechado 2026-07-01)**
- Todos 10 sistemas em 10/10
- Reproductor + Endocrino + Digestivo + Urinario: batch premium via Manus (2026-07-01)
- Esqueleto 08+09 (HuesosMano/Pie): via ChatGPT em resolução alta 1400x2488 (Manus caiu pra 768x1344 nos batches grandes — ChatGPT é melhor pra premium single-shot)

**Bônus:**
- ✅ Bono 3 · Flashcards: `bonus/bonus-3.pdf` (Anki) + NOVO (2026-07-04) **200 Flashcards Visuais** (5 láminas Q&A PNG 1080x1920) em `bonus/flashcards-premium/` + viewer `flashcards-premium.html`. Bono 3 no index tem 2 botões agora (Acceder PDF + "Flashcards Visuales"). CSS `.bonus-actions`/`.bonus-btn-alt`.
  - ⚠️ DEFEITOS nas imagens de origem a corrigir: flashcards-03 (Nervioso) tem marca d'água shutterstock + barra preta cobrindo resposta Q111; flashcards-05 (Urinario) tem texto vazado "Perfeito, mas pode melhorar:" na resposta Q193 + marca d'água dreamstime. Usuário avisado 2026-07-04.
- ⏳ Bono 1 · Atlas Palpación, Bono 2 · 500 Preguntas, Bono 4 · Glosario ES-Latín

**Pipeline pra integrar novos mapas/bônus do Manus:**
1. User manda ZIP de PNGs com nomes corretos (ex: `SISTEMA_NN_Key.png`)
2. Comprimir: `PIL` resize max 1400px wide + JPG q=82 optimize progressive
3. Salvar em `modulos-content/<SISTEMA>/<SISTEMA>_NN_<key>.jpg`
4. Bump cache: `?v=N+1` em `build-pages.py` (replace_all `?v=N` → `?v=N+1`)
5. Rebuild: `py build-pages.py`
6. Commit + push + `wrangler pages deploy . --project-name anatomia-area-miembros`

**Arquivos chave:**
- `build-pages.py` — gera index + 10 modulo-*.html a partir de TITLES dict
- `PROMPTS_PENDIENTES.md` — todos os prompts pra gerar o que falta (acessível de qualquer PC via repo)
- `BANNER_PROMPT_MANUS.md` + `CAPAS_PROMPT_MANUS.md` — referência das gerações já feitas
- `scripts/place_real_mapas.py` — pipeline compressão+placeholders
- `scripts/build_placeholders.py` — gera placeholders pros slots vazios
- `scripts/compress_capas.py` — comprime capas

**Cache busting:** versão atual `?v=6` (bumpa toda vez que substituir mapa pra forçar reload no browser). Fica no `build-pages.py` linha ~236.

Link com [[project_coreano_area_miembros_es]] — clonado dessa área. Padrão template seguindo [[project_biopremium_template_pattern]] pra info-produtos LATAM.
