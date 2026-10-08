---
name: project-ebooks-premium
description: "Bônus premium do Brincadeiras Sem Tela — 3 ebooks (fala, sensorial, sono) hospedados em CF Pages ebooks-premium.pages.dev"
metadata: 
  node_type: memory
  type: project
  originSessionId: 532f4149-bdb2-4d21-a3f4-b6dc74625a07
---

3 ebooks de bônus do produto [[project-brincadeiras-landing]]:
- `fala` — 30 Atividades para Estimular a Fala em Casa
- `sensorial` — 30 Atividades Sensoriais (Hipersensibilidade Tátil)
- `sono` — 30 Brincadeiras Calmas para a Hora de Dormir

**Hospedagem:** Cloudflare Pages, projeto `ebooks-premium`, URL `ebooks-premium.pages.dev` (criado 2026-06-05).

**Pasta local:** `C:\Users\User\Desktop\ebooks-premium\` — index.html + 3x HTML + 3x PDF.

**Estrutura URL servida:**
- `/` → index com cards dos 3 ebooks
- `/fala`, `/sensorial`, `/sono` → versões HTML (CF Pages remove .html)
- `/fala.pdf`, `/sensorial.pdf`, `/sono.pdf` → download direto

**Why:** Usuário reportou que PDFs sozinhos abriam em branco (gerados via Chrome print-to-PDF, bug em alguns visualizadores mobile). Solução foi servir HTML como link principal + PDF como botão de download secundário.

**How to apply:** Pra atualizar, edita arquivos locais e `npx wrangler pages deploy . --project-name=ebooks-premium --branch=main --commit-dirty=true` da pasta. NÃO está no GitHub sync ainda — se for usar no outro PC, criar repo ou copiar via Drive.

**Deploy:** `noindex,nofollow` no meta robots — é bônus de produto pago, não pra indexar.
