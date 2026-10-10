# claude-config — o "cérebro" do Claude Code nos 2 PCs

Tudo que o Claude sabe fazer aqui: **memória** (todos os projetos e decisões), **skills** (marketing, ugc-criativos,
ad-library-pesquisa, landing-infoproduto…), **manual de operação** (`CLAUDE.md`: como agir — navegar no Chrome,
pesquisar, baixar e editar vídeo, publicar landing), settings e statusline. Login (`.credentials.json`) e `.env` **não** vêm pra cá.

## PC novo (uma vez só)
```
winget install GitHub.cli
gh auth login
gh repo clone ursinho0909-cloud/claude-config $env:USERPROFILE\claude-config
powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\claude-config\instalar-claude.ps1
```
O instalador põe git, node, python, ffmpeg, yt-dlp, as bibliotecas (whisper, rembg…), wrangler, copia o cérebro
e o kit de b-roll do Google Drive (`G:\Meu Drive\_ugc-kit`). No fim ele mostra os 5 passos manuais
(logins, extensão Claude in Chrome, /model opus, modo auto).

## Dia a dia (nos dois PCs)
Rode `sync-claude.ps1` **ao começar** (puxa o que o outro PC aprendeu) e **ao terminar** (envia o que este aprendeu):
`! powershell -ExecutionPolicy Bypass -File C:/Users/User/claude-config/sync-claude.ps1`

Abra o Claude sempre a partir da pasta do usuário (`C:\Users\<usuario>`), senão ele procura a memória em outra pasta.
