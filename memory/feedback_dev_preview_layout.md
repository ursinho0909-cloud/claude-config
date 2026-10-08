---
name: feedback-dev-preview-layout
description: "Sempre que for editar landing/frontend, montar split VSCode (esquerda 1020px) + janela navegador modo app em viewport mobile 420x900 (direita) servindo localhost"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2fa6b940-8dd2-42d0-bd03-a6c57309c74f
---

Quando o usuário for editar landing page, site, frontend ou qualquer coisa servida por localhost, montar este layout sem precisar perguntar:

1. Subir servidor estático na pasta do projeto (`python -m http.server <porta>` em background).
2. Abrir janela **Edge em modo `--app=`** apontando pro localhost — isso dá janela limpa (sem abas, sem barra de URL), parece app nativo.
3. Posicionar via Win32 `MoveWindow`:
   - **VSCode (chat Claude Code)**: `(0, 0, 1020, 900)` — ocupa esquerda, mensagens do chat respiram, não cortam.
   - **Browser app (preview)**: `(1020, 0, 420, 900)` — formato mobile (iPhone-ish), à direita do VSCode.
4. Resolução base assumida: 1440x900. Se for outra, recalcular mantendo proporção (browser ~30% da largura, mobile portrait).

**Why:** Usuário quer fluxo tipo Lovable/v0 — editar código e ver mudança ao vivo do lado, sem ter que abrir/alternar navegador. Recusou Simple Browser do VSCode (não testou direito) e prefere janela `--app` posicionada. Mobile portrait porque 80%+ do tráfego dos info-produtos dele ([[project-caixa-magica]], [[project-fitness-app]], [[project-megapacks]], [[project-biopremium]]) vem de Meta Ads mobile.

**How to apply:** No início de qualquer sessão de edição de landing/site (Caixa Mágica, Treino Express, Megapacks, BioPremium, template nutricionista, ou novos), montar esse layout antes de perguntar quais mudanças fazer. NÃO usar Simple Browser do VSCode (sendkeys frágeis); usar `msedge --app=` + MoveWindow. NÃO abrir página em aba normal do Opera/Chrome — sempre janela `--app` dedicada.
