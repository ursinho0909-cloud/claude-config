---
name: project-github-sync
description: "Setup multi-PC: 5 repos privados no GitHub pra sincronizar projetos entre 2 PCs do usuário"
metadata: 
  node_type: memory
  type: project
  originSessionId: ee771611-29c7-428f-8237-a58c14834760
---

Em 2026-05-28 montei sync entre os 2 PCs do usuário (mesma conta Google/Microsoft). **Decisão:** código vai pro GitHub (versionado), arquivos pesados/binários vão pro Google Drive Desktop (que o usuário já instalou).

**Conta GitHub:** `ursinho0909-cloud` (email `ursinho0909@gmail.com`). Auth via `gh` CLI (HTTPS+browser, token com scopes `repo, gist, read:org, workflow`). `gh` instalado neste PC via `winget install GitHub.cli` (v2.93.0). git config global: name=`ursinho0909-cloud`, email=`ursinho0909@gmail.com`, defaultBranch=main.

**5 repos PRIVADOS criados (sempre privados — código de info-produto, não open-source):**

| Repo | Pasta local | Conteúdo |
|------|-------------|----------|
| `treino-express-app` | `C:\Users\User\Desktop\treino-express-src` | Next.js webapp (área de membros) — ver [[project-fitness-app]] |
| `treino-express-vendas` | `C:\Users\User\Desktop\SITE FUNCIONAL` | Landing VSL single-file (HTML+webp+mp4 16MB) |
| `treino-meta-capi` | `C:\Users\User\Desktop\treino-meta-capi` | Worker Cloudflare forwarder Meta CAPI |
| `controle-mercadolivre` | `C:\Users\User\controle-mercadolivre` | Dashboard ML (Express) — ver [[project-controle-ml]] |
| `ebook-brincadeiras` | `C:\Users\User\Desktop\ebook-brincadeiras` | E-book HTML single-file +150 brincadeiras mãe e filho (criado 2026-05-30) |
| `arsenal-futsal-landing` | `C:\Users\User\Desktop\arsenal-futsal-landing` | Landing de vendas +200 Dinâmicas de Futsal (HTML/CSS/JS puro, criado 2026-06-05). CONTINUE_AQUI.md dentro do repo |
| `coreano-area-membros` | `C:\Users\User\Desktop\coreano-area-membros` | Área de membros do coreano (entregável) — 4 módulos CEFR + 40 mapas mentais + 4 bônus. Criado 2026-06-19. Repo INCLUI os 40 PNGs (~74MB) pra deploy self-contained. |
| `meta-ads-escala` | `C:\Users\User\Desktop\meta-ads-escala` | Estratégia de escala Meta Ads do Coreano LATAM (não-código). Contém ESTRATEGIA_ESCALA.md (playbook) + LOG_DECISOES.md (histórico diário). Criado 2026-06-27. Workflow: `git pull` antes da sessão de decisão, `git commit/push` depois de aplicar bump do dia. Ver [[project-coreano-meta-ads-latam]]. |

**Gitignores em ordem (importante NÃO vazar):**
- `treino-express-src/.gitignore`: já existia, adicionei `.open-next/` e `.wrangler/` (build artifacts do Cloudflare). Ignora também `node_modules`, `.next`, `.env`, `.env*.local`.
- `controle-mercadolivre/.gitignore`: já existia, adicionei `data/sales.backup.json` (mesma info sensível do sales.json que já ignorava). Continua ignorando `.env` (tem refresh_token do ML!), `data/sales.json`, `data/tokens.json`.
- `treino-meta-capi/.gitignore`: criado do zero (ignora `node_modules`, `.wrangler`, `.env*`, `.dev.vars`).
- `SITE FUNCIONAL/.gitignore`: criado do zero (só OS files + `.wrangler`).

**Arquivos NÃO versionados que precisam estar no outro PC (recriar manualmente lá ou colocar no Drive):**
- `treino-express-src/.env.production.local` — CRÍTICO pro `next build` (Supabase URL/Anon Key inlined). Ver [[project-fitness-app]] linha sobre `.env.production.local` (perda disso quebra prod com `supabaseUrl is required`).
- `controle-mercadolivre/.env` — contém ML refresh_token. Sem isso o dashboard não conecta na API do ML.
- Pastas `data/*.json` (sales/tokens) — estado runtime do controle-ml, não devem ir pro git mesmo.

**Fluxo diário (uma vez ensinado, não tem mistério):**
- Trabalhou aqui → `git add . ; git commit -m "msg" ; git push` (na pasta do projeto)
- Chega no outro PC → `git pull` antes de começar
- Conflito = avisar — não auto-merge

**Setup do outro PC (passos pro usuário):**
1. Instalar `gh`: `winget install GitHub.cli`
2. `gh auth login` (mesmo fluxo: HTTPS, browser, código)
3. `gh repo clone ursinho0909-cloud/<repo-name>` (4 vezes, ou clonar onde quiser)
4. Pros que precisam de `.env`, copiar do Drive antes de rodar

**NÃO confundir nome de pasta com nome de repo:** `treino-express-src` (pasta) = `treino-express-app` (repo). `SITE FUNCIONAL` (pasta, com espaço) = `treino-express-vendas` (repo, kebab-case). Os outros 2 têm nome igual.
