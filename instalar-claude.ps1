# Prepara um PC novo pra ficar IGUAL ao principal: programas, bibliotecas, cerebro do Claude (memoria, skills,
# manual CLAUDE.md, settings) e o kit de b-roll dos criativos.
# Uso (uma vez):  powershell -ExecutionPolicy Bypass -File C:\Users\<voce>\claude-config\instalar-claude.ps1
$ErrorActionPreference = 'Continue'
$repo   = $PSScriptRoot
$claude = Join-Path $env:USERPROFILE '.claude'

function Passo($t) { Write-Host "`n== $t" -ForegroundColor Cyan }

Passo '1/6 Programas (winget)'
$pkgs = 'Git.Git', 'GitHub.cli', 'OpenJS.NodeJS.LTS', 'Python.Python.3.12', 'Gyan.FFmpeg', 'yt-dlp.yt-dlp'
foreach ($p in $pkgs) {
    winget list --id $p -e 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) { winget install --id $p -e --silent --accept-package-agreements --accept-source-agreements }
    else { Write-Host "ok $p" }
}
# recarrega o PATH desta janela
$env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')

Passo '2/6 Bibliotecas Python'
$py = (Get-Command python -ErrorAction SilentlyContinue).Source
if ($py) {
    & python -m pip install --upgrade pip
    & python -m pip install faster-whisper rembg onnxruntime opencv-python pillow numpy yt-dlp pymupdf rapidocr-onnxruntime
} else { Write-Host 'Python nao encontrado no PATH: feche e abra o PowerShell e rode este script de novo.' -ForegroundColor Yellow }

Passo '3/6 Node (wrangler pro Cloudflare Pages)'
if (Get-Command npm -ErrorAction SilentlyContinue) { npm install -g wrangler } else { Write-Host 'npm ainda nao esta no PATH: reabra o PowerShell e rode de novo.' -ForegroundColor Yellow }

Passo '4/6 Cerebro do Claude (memoria, skills, manual, settings)'
& powershell -ExecutionPolicy Bypass -File (Join-Path $repo 'sync-claude.ps1')
Copy-Item (Join-Path $repo 'CLAUDE.md') (Join-Path $claude 'CLAUDE.md') -Force
Write-Host "Manual copiado para $claude\CLAUDE.md"

Passo '5/6 Kit de b-roll dos criativos (Google Drive)'
$kit = 'G:\Meu Drive\_ugc-kit'
if (Test-Path $kit) {
    New-Item -ItemType Directory -Force 'C:\tmp\ugcn\src' | Out-Null
    robocopy "$kit\src" 'C:\tmp\ugcn\src' /E /XO /NJH /NJS /NFL /NDL /NP | Out-Null
    robocopy "$kit\words" 'C:\tmp\ugcn' *.json /XO /NJH /NJS /NFL /NDL /NP | Out-Null
    Write-Host 'b-roll copiado para C:\tmp\ugcn\src'
} else { Write-Host 'Google Drive (G:) nao encontrado: instale o Google Drive para computador, faca login e rode de novo.' -ForegroundColor Yellow }

Passo '6/6 Falta fazer na mao (1 vez)'
Write-Host @'
  1. gh auth login                (GitHub - pra clonar os projetos e sincronizar)
  2. npx wrangler login           (Cloudflare - pra publicar landings)
  3. Chrome: instalar a extensao "Claude in Chrome" e logar em HeyGen, Hotmart, Meta (Ad Library), ChatGPT
  4. Abrir o Claude SEMPRE em C:\Users\<voce>, rodar /model opus e Shift+Tab ate ficar em "auto"
  5. Se o usuario do Windows NAO for "User": peca ao Claude "ajusta os caminhos dos scripts da skill ugc-criativos pro meu usuario"
Pronto. Dia a dia: rode sync-claude.ps1 ao comecar e ao terminar.
'@ -ForegroundColor Green
