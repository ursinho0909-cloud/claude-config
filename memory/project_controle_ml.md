---
name: project-controle-ml
description: Webapp de controle financeiro ML do usuário - dashboard de lucro real integrado à API oficial do Mercado Livre via OAuth2
metadata: 
  node_type: memory
  type: project
  originSessionId: 438b2bd4-a8b8-401b-a1b2-c32073d8d497
---

Webapp de controle de vendas/lucro do Mercado Livre, construído em Node.js + Express + HTML/JS + Chart.js.

**Localização:** `C:\Users\User\controle-mercadolivre\`
- `server.js` - backend com OAuth ML, endpoints REST, cron de sync
- `public/index.html` - dashboard (single-page, tema escuro SaaS)
- `data/sales.json` - vendas (preservar manualmente — backup recomendado)
- `data/tokens.json` - tokens OAuth do ML (ver bug do refresh_token abaixo)
- `data/products.json` - catálogo de custos (nome → custo + embalagem)
- `.env` - ML_CLIENT_ID=8946762761125535 + secret + redirect URI
- `iniciar.bat` - atalho na Área de Trabalho ("Controle ML") que sobe servidor + ngrok

**Acesso público:** `https://tableware-unhitched-eternal.ngrok-free.dev` (domínio fixo grátis do ngrok)

**Como rodar:** duplo clique em "Controle ML" na Área de Trabalho → abre 2 PowerShells (npm start + ngrok) + navegador. Pra parar, fecha as 2 janelas pretas.

**Features implementadas (até 2026-05-15):**
- OAuth ML completo (login, refresh automático de token)
- Sync automático a cada 30 min
- Dashboard com seletor de período: Mês / Ano / Personalizado (data início + fim)
- Total Vendido alinhado com site oficial ML (usa order.total_amount, conta inclusive cancelados)
- Detecção automática de devoluções via payments[].status='refunded'
- Campo manual "Prejuízo REAL" pra cada devolução (separado do "valor reembolsado ao cliente")
- Coluna Cliente na tabela com nome do comprador (buyer.first_name + last_name)
- Coluna Lucro destacada com fundo amarelo
- Card "Mais Vendido" ocupa 2 colunas pra caber nome completo
- Export CSV / Excel (SheetJS) / PDF (jsPDF+autotable)
- Catálogo de custos com matching inteligente: tokenização + stemming PT-BR (branca=branco, preta=preto, ignora acento/caso/palavras extras)
- 4 gráficos anuais (lucro, faturamento, taxas ML, fretes)

**Estado atual (2026-05-16):** 44 vendas, todas com custo aplicado. Catálogo populado (34 produtos de esquadrias de alumínio). Logo "Casa das Janelas" no header (`public/logo.png`). Tabela tem scrollbar duplicada (topo + base) + coluna Embalagem dedicada.

**Regra importante de custo (aplicada em `applyCatalogToSale`):**
- `cost` no catálogo é POR UNIDADE → vira `match.cost × qty` na venda
- `packaging` é FLAT por venda (R$ 5,00 padrão, indep. da qtd) — confirmado pelo usuário
- KITs (ex: "Fecho Kit 2 Tranqueta Cromado" custa R$ 9,80 / "Guia Kit 10 Peças" R$ 10,00) são registrados como custo total do kit no catálogo, e cada qty=1 no ML representa 1 kit completo

**Scripts utilitários em `scripts/`:**
- `import-catalog.js` — lê xlsx do desktop e popula products.json + aplica nas vendas
- `add-missing.js` — adiciona entradas manuais ao catálogo e reaplica

**Importante:** sempre rodar `cp data/sales.json data/sales.backup.json` antes de qualquer script que escreva em sales.json.

**Limitações conhecidas:**
- Frete em Mercado Envios Full às vezes vem zerado (limitação da API ML)
- Custo do produto não tem como vir do ML — daí a necessidade do catálogo manual
- Pedidos > 90 dias podem precisar aumentar daysBack na sync (default 90 no auto-sync, 120 quando rodada manualmente)

**Bug histórico (resolvido 2026-05-18) — "Não autenticado" a cada 6h:**
Sync quebrava com `{"error":"Não autenticado no Mercado Livre"}` porque o OAuth devolvia access_token sem `refresh_token` (length 0 em tokens.json). Causa: no devcenter ML, no painel "Fluxos OAuth" do app, o checkbox **"Refresh Token"** estava desmarcado (só Authorization Code estava ligado). **IMPORTANTE: no ML não é o scope `offline_access` do padrão OAuth — é literalmente um checkbox "Refresh Token" no devcenter.** Resolvido marcando esse checkbox + reconectando. A partir daí refresh_token salvou normalmente e o servidor passou a renovar sozinho.

**How to apply:** Se sync voltar a falhar com "Não autenticado", checar nessa ordem: (1) Node de pé em :3000 (curl localhost:3000/api/status) — se não, `npm start` em `C:\Users\User\controle-mercadolivre`; (2) ngrok ativo — se não, `ngrok http --url=tableware-unhitched-eternal.ngrok-free.dev 3000`; (3) inspecionar `data/tokens.json` com node — se `refresh_token` vazio de novo, alguém desmarcou "Refresh Token" no devcenter ML, voltar lá e marcar. Importante: rodar `iniciar.bat` via shell não-interativo (Claude Bash) NÃO funciona, pq `start cmd /k` dentro do .bat não spawna subjanelas — subir Node e ngrok direto em background.

Relacionado: [[user-business]] (negócio secundário do usuário além de [[project-megapacks]])
