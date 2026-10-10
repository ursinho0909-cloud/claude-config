---
name: project-claude-config-sync
description: "Repo privado ursinho0909-cloud/claude-config (08/10/2026) sincroniza memória+skills+settings do Claude Code entre os 2 PCs via sync-claude.ps1"
metadata:
  type: project
---

Usuário achava o Claude do outro PC "mais lerdo, pede aceitar tudo, não mexe no PC". Causas: modelo (aqui settings "model": "opus"), modo auto, memória vazia lá, falta de skills/ffmpeg/python libs/extensão Chrome.

Solução (08/10/2026): repo PRIVADO https://github.com/ursinho0909-cloud/claude-config, pasta local C:\Users\User\claude-config. Contém memory/ (101 arquivos), skills/, agents/, commands/, settings.json, statusline.ps1, sync-claude.ps1 (robocopy /XO dos dois lados + git pull/commit/push, nunca apaga), LEIA-ME.md. .gitignore exclui .credentials.json e .env.

**Why:** o classificador do auto mode BLOQUEIA eu copiar a memória/subir pro GitHub e criar instalador que mexe em ~/.claude — o usuário teve que rodar os comandos ele mesmo com `!` (o `!` roda em BASH, não PowerShell).
**How to apply:** quando ele pedir "sincroniza a memória", passar o comando pra ele rodar (`! powershell -ExecutionPolicy Bypass -File C:/Users/User/claude-config/sync-claude.ps1`) em vez de tentar sozinho. Outro PC ainda precisa: clonar, rodar sync, winget ffmpeg/yt-dlp, pip faster-whisper rembg onnxruntime opencv-python pillow numpy, /model opus, Shift+Tab auto, extensão Claude in Chrome. Relacionado: [[project-github-sync]].
**10/10/2026 — "cérebro completo":** repo ganhou CLAUDE.md (manual de operação: perfil do usuário, ferramentas que eu uso e como — Chrome, yt-dlp, ffmpeg, whisper, rembg, wrangler, Hotmart, regras de feedback), instalar-claude.ps1 (winget git/gh/node/python/ffmpeg/yt-dlp + pip libs + wrangler + sync + copia CLAUDE.md p/ ~/.claude + b-roll de G:\Meu Drive\_ugc-kit → C:\tmp\ugcn) e skills ugc-criativos, ad-library-pesquisa, landing-infoproduto. sync-claude.ps1 agora sincroniza CLAUDE.md também. Ao aprender fluxo novo recorrente, virar skill no claude-config\skills.
