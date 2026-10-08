---
name: project-treinos-futsal
description: "Arsenal do Treinador de Futsal — área de membros (capa+links Drive) em treinos-futsalpremium.pages.dev, info-produto R$24,90"
metadata: 
  node_type: memory
  type: project
  originSessionId: 532f4149-bdb2-4d21-a3f4-b6dc74625a07
---

Info-produto de futsal: webapp tipo "ebook premium" que entrega vídeos via link Drive por categoria.

**Live (área de membros / entregável):** https://arsenal-futsal-area.pages.dev/ (CF Pages, projeto `arsenal-futsal-area`, criado 2026-06-06 — esse é o link que o COMPRADOR recebe)

**Live (página de vendas):** https://treinos-futsalpremium.pages.dev/ (CF Pages, projeto `treinos-futsalpremium`, originalmente era a área de membros mas foi sobrescrito pela sales page em 2026-06-06)

**Pasta local:** `C:\Users\User\Desktop\arsenal-futsal\` — HTML puro (sem build), 1 index + 7 páginas de categoria + style.css + assets/. Essa pasta = código-fonte da ÁREA DE MEMBROS, não da sales page.

**Estrutura de produto:**
- Preço alvo: R$24,90 (ticket de impulso)
- Order bump previsto: +R$9,90 (Pack Avançado Sistemas Táticos)
- 7 categorias ativas: Dinâmicas · Finalização · Fundamentos · Preparo Físico · Marcação · Sistemas Táticos · Treinos Premium
- DRIBLES removido (era 03, renumerei tudo)
- Cada categoria tem botão "Acessar todos os treinos de X" → abre folder Drive em nova aba

**Visual:** dark navy + amarelo + preto. Banner compacto com ícone+número+título em vez de capa gigante (user reclamou que ficou feio). Mobile-first com breakpoints em 520px e 360px.

**Why deste formato (vs webapp asvitrine completo):** custo R$0 de infra (Drive já hospeda vídeo), lançamento rápido, mesma defensibilidade dos megapacks do usuário. Se vender bem, migra pra Bunny Stream depois.

**How to apply:**
- Pra atualizar área de membros: edita HTML local e `npx wrangler pages deploy . --project-name=arsenal-futsal-area --branch=main --commit-dirty=true` da pasta arsenal-futsal
- CUIDADO: NÃO fazer deploy da pasta arsenal-futsal pro projeto `treinos-futsalpremium` (esse agora é só sales page)
- Pra novo link Drive: edita o `href` do botão `btn-drive` na página da categoria
- Pra nova capa do TREINOS PREMIUM: substituir `assets/cat-premium.png` (hoje usa a capa principal como placeholder)
- DRIBLES e suas dependências foram deletadas — se quiser voltar, criar nova página e gerar capa

**Risco IP:** vídeos são de fonte terceira (Drive externo, possivelmente gray). Mitigação típica: migrar pro Drive próprio do usuário, marca d'água, evitar publicar URL fora do funil pago. NÃO está no GitHub sync ainda — se for usar no outro PC, criar repo ou copiar via Drive Desktop.
