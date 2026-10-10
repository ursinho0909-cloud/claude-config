---
name: Deploy para Cloudflare Pages via Wrangler
description: Como fazer deploy automático em sites Cloudflare Pages do usuário (caixamagica, treino-express-vendas, brincadeiras-sem-tela) usando Wrangler CLI
type: reference
originSessionId: beba8c1e-5a5c-49c9-9df6-ef96138fb080
---
Wrangler CLI 4.x instalado globalmente. Login OAuth via `wrangler login` salva token em:
`C:\Users\Pc\.wrangler\config\default.toml` (validado 2026-05-31 com wrangler 4.95.0)

**Path legacy (NÃO usar — fica desatualizado):** `C:\Users\Pc\AppData\Roaming\xdg.config\.wrangler\config\default.toml` — existe de install antigo mas `wrangler login` novo grava no path acima.

**Bug conhecido:** `wrangler pages deploy` rodado pelo Claude (ambiente não-interativo) ignora o OAuth token e exige `CLOUDFLARE_API_TOKEN`. Workaround: extrair o `oauth_token` do `default.toml` e exportar como env var no mesmo comando:

```bash
TOKEN=$(grep oauth_token /c/Users/Pc/.wrangler/config/default.toml | head -1 | awk -F'"' '{print $2}') && \
export CLOUDFLARE_API_TOKEN="$TOKEN" && \
npx wrangler pages deploy <pasta> --project-name=<projeto> --branch=main --commit-message="<msg>"
```

**Projetos Pages do usuário:**
- `caixamagica` → caixamagica.pages.dev (pasta local: `C:\Users\Pc\Desktop\CAIXA MAGICA - NETLIFY` — nome legacy, é Cloudflare agora)
- `treino-express-vendas` → treino-express-vendas.pages.dev, meutreinoexpress.com.br
- `brincadeiras-sem-tela` → brincadeiras-sem-tela.pages.dev (criado 2026-05-31, pasta local: `C:\Users\Pc\Desktop\brincadeiras-sem-tela`)
- `coreano-area-miembros` → coreano-area-miembros.pages.dev (pasta local: `C:\Users\Pc\Desktop\coreano-area-miembros`, area de membros ES do curso de coreano)
- `caligrafia-en-casa` → caligrafia-en-casa.pages.dev (pasta local: `C:\Users\Pc\Desktop\caligrafia-en-casa-landing`, landing ES de caligrafia Bluey). **NÃO tem integração GitHub→CF** — push no repo `ursinho0909-cloud/caligrafia-en-casa-landing` NÃO dispara deploy. Deploy só via `wrangler pages deploy` manual.
- `caligrafia-area-miembros` → caligrafia-area-miembros.pages.dev (área de membros do produto caligrafia Bluey)
- `codice-prehistorico-miembros` → codice-prehistorico-miembros.pages.dev (área de membros @mitologiavisual, 100 láminas, deploy manual via wrangler — sem integração GitHub→CF). NOME DO PROJETO É "codice-prehistorico-miembros" SEM "area" (a pasta local se chama codice-prehistorico-area-miembros, mas o projeto CF não). Cuidado pra não criar duplicado.
- Outros codice do usuário no CF: `codice-prehistorico` (landing), `codice-mitologia` (landing), `codice-mitologia-miembros` (área de membros da mitologia)

**Path com espaços:** copiar pra `/tmp/<nome>` antes de deployar — wrangler tem issues com paths com espaço no Windows.

**Criar projeto novo:** se der "Project not found" no deploy, rodar antes:
```bash
npx wrangler pages project create <nome> --production-branch=main
```

**OAuth token expira em 1h**, mas tem refresh_token. Se der "Not logged in" ou "Invalid access token [code: 9109]" mesmo com config preenchido, pedir ao usuário pra rodar `! npx wrangler login` (o `!` faz o Claude Code rodar interativo, abrindo o navegador). Validado em 2026-05-31: refresh automático às vezes falha — login interativo resolve.
