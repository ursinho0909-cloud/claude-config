# Sincroniza o "cerebro" do Claude Code entre os PCs (memoria, skills, settings).
# Uso: clique direito > Executar com PowerShell  (ou: powershell -ExecutionPolicy Bypass -File sync-claude.ps1)
# Roda nos dois sentidos: baixa o que o outro PC mandou e envia o que este PC aprendeu.
$ErrorActionPreference = 'Stop'
$repo   = $PSScriptRoot
$claude = Join-Path $env:USERPROFILE '.claude'
# a pasta de memoria tem o nome da pasta onde o claude e aberto (ex.: C:\Users\User -> C--Users-User)
$key    = ($env:USERPROFILE -replace '[:\\/ ]', '-')
$memLocal = Join-Path $claude "projects\$key\memory"
New-Item -ItemType Directory -Force $memLocal | Out-Null

Set-Location $repo
git pull --quiet --rebase origin main 2>$null

# pares: pasta do repo <-> pasta local. /XO = so copia o que for mais novo; nunca apaga nada.
$pares = @(
    @{ repo = "$repo\memory";   local = $memLocal },
    @{ repo = "$repo\skills";   local = "$claude\skills" },
    @{ repo = "$repo\agents";   local = "$claude\agents" },
    @{ repo = "$repo\commands"; local = "$claude\commands" }
)
foreach ($p in $pares) {
    New-Item -ItemType Directory -Force $p.repo, $p.local | Out-Null
    robocopy $p.repo  $p.local /E /XO /NJH /NJS /NFL /NDL /NP | Out-Null   # repo -> PC
    robocopy $p.local $p.repo  /E /XO /NJH /NJS /NFL /NDL /NP | Out-Null   # PC -> repo
}
foreach ($f in 'settings.json', 'statusline.ps1') {
    $r = Join-Path $repo $f; $l = Join-Path $claude $f
    if ((Test-Path $r) -and (-not (Test-Path $l) -or (Get-Item $r).LastWriteTime -gt (Get-Item $l).LastWriteTime)) { Copy-Item $r $l -Force }
    elseif (Test-Path $l) { Copy-Item $l $r -Force }
}

git add -A
$mudou = git status --porcelain
if ($mudou) {
    git commit --quiet -m "sync $env:COMPUTERNAME $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    git push --quiet origin main
    Write-Host "Enviado: $(@($mudou).Count) arquivo(s) atualizados." -ForegroundColor Green
} else {
    Write-Host "Tudo igual, nada pra enviar." -ForegroundColor Green
}
Write-Host "Memoria em: $memLocal"
