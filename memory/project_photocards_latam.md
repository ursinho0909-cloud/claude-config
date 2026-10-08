---
name: project_photocards_latam
description: "Info-produto photocards K-pop/K-drama (LATAM, ES) — landing live em photocardspremium.pages.dev, repo photocards-latam"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4d269cb2-6ca0-42b8-aa39-ed64623206e1
---

Info-produto de photocards (K-pop + K-drama, ES/LATAM).

- **Landing LIVE:** photocardspremium.pages.dev (Cloudflare Pages, projeto `photocardspremium`)
- **Repo:** github.com/ursinho0909-cloud/photocards-latam (público, branch `main`)
- **Pasta local:** `C:\Users\User\Desktop\photocards-latam` (clonada em 2026-07-13 neste PC; o projeto nasceu no outro PC)
- **Stack:** HTML/CSS/JS puro (index.html + style.css + script.js) + assets .webp (hero, oferta, 4 bônus, 4 depoimentos, 16 photocards)
- **Estado em 2026-07-13:** deploy no ar == HEAD do repo (commit 38d3ad1). Site em fase de ajustes de landing.

Conteúdo dos 16 photocards: BTS, BLACKPINK, Stray Kids, TWICE, NewJeans, SEVENTEEN, ATEEZ, LE SSERAFIM + K-dramas (Queen of Tears, Squid Game, Business Proposal, Vincenzo, Goblin, Crash Landing, True Beauty, Hospital Playlist).

**Preço local por IP (add 2026-07-17):** a oferta mostra o preço na moeda do país do visitante, detectado via Cloudflare `/cdn-cgi/trace` (sem API externa). Config no topo do `script.js` (`COUNTRIES`, campo `rate` = 1 USD ≈ X). Cobre AR/MX/CL/CO/PE/UY/ES/BR; fallback `$8,90 USD`. Câmbio hardcoded — revisar Argentina a cada ~2-3 semanas (peso volátil). Checkout = Hotmart Intl `pay.hotmart.com/W106721659I` ($8,90 USD, converte sozinho no checkout).

Segue o padrão de landing do [[project_coreano_template_pattern]] e vale a regra de [[feedback_landing_sync_before_edit]] (conferir deploy live antes de editar, PC duplo).
