---
name: Projeto Megapacks Amigurumi
description: Lançamento ativo (maio/2026) de pack de receitas de amigurumi em espanhol pra LATAM. Landing page + PDFs prontos. Pendente hospedagem, checkout e compressão de imagens.
type: project
originSessionId: 0e44a3a0-49ce-446c-822c-a1489e0336a0
---
Lançamento em curso de **pack de receitas de amigurumi traduzido pra mercado LATAM hispânico**. Sessão inicial concluída em **2026-05-08**.

**Why:** Usuário precisa de receita rápida; escolheu Opção 1 ("queima e troca") explicitamente após eu explicar os 3 modelos possíveis. Ciclo esperado 6–18 meses antes de takedown ou saturação.

**Estado atual:**
- Landing page em ES pronta (Tailwind + Montserrat, identidade gold/oliva + verde)
- 2 PDFs gerados: `glosario-pt-es.pdf` (5 págs, vai dentro do Drive) e `acceso-pack.pdf` (1 pág, sobe na Hotmart)
- 3 links de Google Drive públicos com o pack (722 PDFs + 1 RTF + 1 XLSX, ~1.2 GB total)
- Versão standalone HTML (12 MB com base64) no Desktop pra envio via WhatsApp
- Resumo completo de tudo em `C:\Users\User\Desktop\RESUMO-PROJETO.md`

**Decisões de produto:**
- Plano Completo US$ 4.90 / Plano Básico US$ 2.90
- 6 bonos na grade (era 10, removeu 4: Cojines, Blusas, Planilla, Guía Promocionar)
- Posicionamento como "patrones bilingües con glosario PT-ES"
- Entrega via Drive (não área de membros) por escolha de simplicidade
- Plataforma de checkout: **Cakto** (não Hotmart) — exige URL pública na config "link de acesso ao produto"
- Suporte: megapacksamigurumi@hotmail.com

**How to apply:** Quando usuário voltar referenciando esse projeto, abrir o `RESUMO-PROJETO.md` no Desktop e a pasta `C:\Users\User\amigurumis-landing\` pra retomar contexto. Pendências principais: hospedar landing (Netlify Drop recomendado), plugar links de checkout reais nos 4 botões `href="#"`, comprimir hero.png 6.6MB → WebP ~400KB.
