---
name: project-coreano-descomplicado
description: "Info-produto \"+100 Mapas Mentais Visuais para aprender coreano\" — landing live em coreano-descomplicado.pages.dev, 2 planos R$17,90/R$27,90, 4 bônus. Falta plugar checkout"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1bb03cf4-82df-43ff-ae87-0ad84a0e0327
---

Info-produto: +100 Mapas Mentais Visuais para aprender Coreano. Pago único, acesso vitalício.

- **Live:** https://coreano-descomplicado.pages.dev (CF Pages, projeto `coreano-descomplicado`)
- **Pasta local:** `C:\Users\User\Desktop\coreano-descomplicado-landing\`
- **Assets originais (PSDs, brutos):** `C:\Users\User\Desktop\koreia\` (HERO.png, bonus 1-4.png, 7 WhatsApp_Image_*.jpg mapas mentais)
- **Estrutura:** HTML/CSS/JS puro. CSS marquee pro carrossel de entregáveis (7 mapas) e carrossel de depoimentos (5 prints WhatsApp/Instagram com marca d'água Gemini mascarada).
- **Planos:**
  - Básico R$17,90 (só 50 mapas, sem bônus)
  - Premium R$27,90 ("MAIS ESCOLHIDO", +100 mapas + 4 bônus, economia R$217,10 vs R$245)
- **Bônus (4):** Guia Hangul, 100 Expressões Essenciais, 200 Frases Conversação, Mini Guia Cultura
- **Scripts auxiliares em `Desktop\koreia\`:** `_remove_bg.py` (floodfill bg removal hero+bonus), `_remove_bg_extra.py` (corner-based pra hero-kit+payments), `_mask_watermark.py` (cobre ✦ do Gemini no canto), `_upscale_dep4.py` (Lanczos 4x pra fonte ruim)

**Pendências:**
- Plugar checkout (Cakto provavelmente, 4 CTAs prontos com `data-plan="basico|premium"`)
- Pixel UTMify
- Pixel Meta CAPI se for rodar tráfego

**Why:** info-produto BR→LATAM, mesmo perfil dos outros packs do usuário ([[project_megapacks]], [[project_caixa_magica]], [[project_brincadeiras_landing]]).

**How to apply:** quando o usuário pedir pra editar landing, seguir [[feedback_landing_sync_before_edit]] e [[feedback_dev_preview_layout]]. Carrossel é puro CSS marquee, não tem JS de carrossel.
