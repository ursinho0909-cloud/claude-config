$ErrorActionPreference = 'SilentlyContinue'

$raw = [Console]::In.ReadToEnd()
try { $j = $raw | ConvertFrom-Json } catch { $j = $null }

$modelName = if ($j.model.display_name) { $j.model.display_name } else { 'Claude' }
$modelId   = "$($j.model.id)"
$cwd       = if ($j.workspace.current_dir) { Split-Path -Leaf $j.workspace.current_dir } else { '' }
$costUsd   = [double]($j.cost.total_cost_usd)

# Limite de contexto por modelo
$ctxLimit = 200000
if ($modelId -match 'sonnet') { $ctxLimit = 1000000 }
if ($modelId -match 'haiku')  { $ctxLimit = 200000 }

# Lê o transcript e soma o uso da última mensagem do assistant
$inTok = 0; $outTok = 0; $cacheRead = 0; $cacheCreate = 0
if ($j.transcript_path -and (Test-Path $j.transcript_path)) {
    $lines = Get-Content -LiteralPath $j.transcript_path -Tail 200 -ErrorAction SilentlyContinue
    for ($i = $lines.Count - 1; $i -ge 0; $i--) {
        try {
            $entry = $lines[$i] | ConvertFrom-Json
            $u = $entry.message.usage
            if ($u) {
                $inTok       = [int]$u.input_tokens
                $outTok      = [int]$u.output_tokens
                $cacheRead   = [int]$u.cache_read_input_tokens
                $cacheCreate = [int]$u.cache_creation_input_tokens
                break
            }
        } catch { }
    }
}

$ctxUsed = $inTok + $cacheRead + $cacheCreate
$pct = if ($ctxLimit -gt 0) { [math]::Round(($ctxUsed / $ctxLimit) * 100, 1) } else { 0 }

function Fmt-K($n) {
    if ($n -ge 1000) { return ("{0:N1}k" -f ($n / 1000.0)) }
    return "$n"
}

# Cores ANSI
$cyan = "`e[36m"; $green = "`e[32m"; $yellow = "`e[33m"; $red = "`e[31m"; $gray = "`e[90m"; $reset = "`e[0m"
$pctColor = $green
if ($pct -ge 60) { $pctColor = $yellow }
if ($pct -ge 85) { $pctColor = $red }

$ctxStr  = "$(Fmt-K $ctxUsed)/$(Fmt-K $ctxLimit)"
$tokStr  = "in $(Fmt-K $inTok) | out $(Fmt-K $outTok)"
$costStr = "{0:N4}" -f $costUsd

"$cyan$modelName$reset $gray|$reset $cwd $gray|$reset ctx $pctColor$ctxStr ($pct%)$reset $gray|$reset $tokStr $gray|$reset `$$costStr"
