---
name: Setup Multi-PC (2 PCs sincronizados via GitHub + Drive)
description: Usuário tem 2 PCs sincronizados — repos no GitHub privado + backups no Google Drive. Conta ursinho0909-cloud. Guia completo em CONTINUE_AQUI.md
type: reference
originSessionId: 0f11b19e-a543-4fc7-a16d-84b252059897
---
# Os 2 PCs

| Identificador | Caminho home | Status (2026-05-28) |
|---|---|---|
| **PC "User"** (principal) | `C:\Users\User\` | Setup completo: tem todos os repos, Drive Desktop, gh CLI, bat de backup |
| **PC "Pc"** (este) | `C:\Users\Pc\` | Setup INCOMPLETO: tem projetos locais mas NÃO como repos git, sem Drive Desktop, sem gh CLI |

# Conta GitHub
- Username: **ursinho0909-cloud**
- Email: ursinho0909@gmail.com
- Login via HTTPS web browser (`gh auth login`)

# Repos privados e paths esperados

| Pasta no PC User | Repo GitHub |
|---|---|
| `Desktop\treino-express-src` | `ursinho0909-cloud/treino-express-app` |
| `Desktop\SITE FUNCIONAL` | `ursinho0909-cloud/treino-express-vendas` |
| `Desktop\treino-meta-capi` | `ursinho0909-cloud/treino-meta-capi` |
| `controle-mercadolivre` (em `C:\Users\User\`) | `ursinho0909-cloud/controle-mercadolivre` |

**No PC "Pc" (este)**: o `Desktop\appfuncional[` parece ser equivalente ao `treino-express-src` do PC User (mesmo projeto Treino Express da memória), mas não é repo git ainda.

# Backups no Drive (`G:\Meu Drive\_backup-pc\`)
Só existe no PC User. Arquivos:
- `controle-mercadolivre\.env` — credenciais ML
- `controle-mercadolivre\data\tokens.json` — refresh_token ML (renova a cada 6h)
- `controle-mercadolivre\data\sales.json` + backup
- `claude-memory\` — memória do Claude inteira

Atualizar backup: `C:\Users\User\Desktop\ATUALIZAR_BACKUP_DRIVE.bat`

# Guia completo
`c:\Users\Pc\Downloads\CONTINUE_AQUI.md` (cópia também no Drive e Desktop do PC User)

# Rotina obrigatória
- **Antes de mexer:** `git pull` na pasta do projeto
- **Depois de mexer:** `git add . && git commit -m "..." && git push`
- **Se mexeu em controle-mercadolivre:** rodar `ATUALIZAR_BACKUP_DRIVE.bat`
