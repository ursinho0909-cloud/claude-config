---
name: Projeto Treino Express — app de membros (Next.js)
description: App fitness premium (área de membros pós-compra), em C:\Users\Pc\Desktop\appfuncional[, Next 14 + Supabase + Cloudflare Workers
type: project
originSessionId: 01cd5745-3510-44a8-9c45-fe8fb55a931c
---
Treino Express é a área de membros pós-compra de um produto fitness high-ticket. O site de vendas (VSL) é um projeto separado.

**Localização:** `C:\Users\Pc\Desktop\appfuncional[` (a pasta tem `[` no nome — em PowerShell sempre usar `-LiteralPath`, e no Bash usar aspas e o globbing pode confundir).

**Stack:** Next.js 14 (App Router) + TypeScript + Tailwind + shadcn/ui + Framer Motion + Supabase + Resend + Cakto (pagamento). Deploy em Cloudflare Workers via `@opennextjs/cloudflare`. Identidade visual: vermelho `#e10600` em fundo escuro.

**Decisão de autenticação (2026-05-20):** Magic link via Supabase, **Opção A** — o Supabase envia o e-mail com template customizado no painel (Authentication → Email Templates), não usamos Resend pra esse e-mail. A pessoa compra na Cakto → webhook cria user no Supabase → Supabase manda magic link → ela clica → cai em `/auth/callback` → vai pro onboarding `/bem-vindo`.

**Onboarding (`/bem-vindo`):** primeira tela pós-magic-link. Tela cheia com "BORA TREINAR!" em gradiente vermelho + input pedindo o nome ("Coloque seu nome para acessar os treinos"). Esse nome é persistido (hoje em localStorage via `lib/session.ts`, depois vai pra `profiles.name` no Supabase) e aparece automaticamente no Hero do dashboard ("Bora suar hoje, {nome}!") e no avatar/sidebar do AppShell. O `AppShell` tem um gate: se nome estiver vazio e a rota for privada, redireciona pra `/bem-vindo`. Rotas públicas (sem chrome e sem gate): `/login`, `/bem-vindo`, `/auth/*`.

**Estado por localStorage (vai migrar pro Supabase depois):**
- `te_user_v1` — `{name}` do usuário
- `te_first_seen_v1` — `{date}` da primeira visita ao app (usado em "Membro desde" no perfil; setado no AppShell via `ensureFirstSeen()`)
- `te_stats_v1` — `{entries: [{date, minutes, kcal}]}` somados em `useUserStats()`
- `te_recent_v1` + `te_completed_v1` — treinos em andamento e concluídos (alimentam o hero dinâmico e o "Continuar treinando")
- `te_checkin_v2` — check-in semanal
- `te_challenge21_v1` — `{enabled, days[21]}` do Desafio 21 Dias (toggle "Começar o desafio"/"Deixar pra uma próxima" no bonus b3 → mostra/esconde `Challenge21Card` no dashboard, abaixo do check-in semanal)

**Como rodar dev:** `npm run dev -- -p 3010` (com `Set-Location -LiteralPath` em PowerShell). NÃO usar `npx next dev` direto — pega Next 16 da internet em vez do 14 local por causa de outro `package-lock.json` em `C:\Users\Pc`. **Why:** `npx` resolve `next` global vs local errado quando o cwd não tem o `next` instalado. **How to apply:** sempre rodar via `npm run dev` dentro do projeto.

**Status Supabase Auth (2026-05-20): LIGADO E FUNCIONANDO em dev.**
- Projeto: `ychvetyfoofzsrumnupb.supabase.co` (creds em `.env.local`, protegido pelo .gitignore)
- Schema rodado: 8 tabelas + RLS
- Implementado: `app/login/page.tsx` (magic link via `signInWithOtp`, `shouldCreateUser: false`), `app/auth/callback/route.ts`, `middleware.ts` (público: `/login`, `/auth`, `/bem-vindo`, `/api/webhooks`; resto exige sessão; raiz `/` redireciona conforme estado), webhook Cakto `app/api/webhooks/cakto/route.ts` reescrito pra criar user + disparar magic link sem senha, botão Sair no perfil chama `supabase.auth.signOut()` antes de limpar.
- Site URL + Redirect URL configurados no painel: `http://localhost:3010/auth/callback`

**Domínio (2026-05-20):** comprou `meutreinoexpress.com.br` no Registro.br (R$40/ano). Nameservers já trocados pra Cloudflare (`arnold.ns.cloudflare.com` + `paislee.ns.cloudflare.com`). Aguardando propagação (~1-2h). Cloudflare em status "Pending Nameserver Update".

**Arquitetura de URLs definida:**
- `meutreinoexpress.com.br` → site de vendas (HTML estático que ele tem em OUTRO PC, vai subir no Cloudflare Pages)
- `app.meutreinoexpress.com.br` → app de membros (Cloudflare Workers via `npm run cf:deploy`)

**Template magic link no Supabase JÁ CUSTOMIZADO** com identidade Treino Express (HTML em `supabase/email-template-magic-link.html`). Mas ainda usando SMTP padrão (limite 3 e-mails/h) — vai melhorar quando plugar Resend.

**Resend:** conta criada, NÃO adicionou domínio ainda (precisa esperar Cloudflare ativar). Plano grátis: 3000 emails/mês.

**Cakto:** conta existente, parou no meio da criação do produto na escolha do tipo de entrega — orientado a escolher **"Área de membros Externa"**. Webhook vai apontar pra `https://app.meutreinoexpress.com.br/api/webhooks/cakto`.

**Próximos passos quando voltar (em ordem):**
1. ⏳ Confirmar Cloudflare ativou (email "is now active")
2. 🔧 Adicionar domínio no painel da Resend → vai dar 3 records DNS (SPF/DKIM/DMARC) → colar no DNS da Cloudflare
3. 🔧 Pegar API key da Resend → configurar SMTP no Supabase (Project Settings → Auth → SMTP Settings) + trocar `EMAIL_FROM` no `.env.local`
4. 🔧 Testar magic link agora saindo do domínio próprio
5. 🔧 Subir site de vendas (HTML que está em OUTRO PC do usuário) no Cloudflare Pages
6. 🔧 Configurar DNS: `meutreinoexpress.com.br` → Pages | `app.meutreinoexpress.com.br` → Workers
7. 🔧 Deploy do app no Cloudflare Workers
8. 🔧 Atualizar Site URL + Redirect URL no Supabase pro domínio de produção + `NEXT_PUBLIC_APP_URL`
9. 🔧 Voltar na Cakto, terminar produto, configurar webhook com URL de produção + `CAKTO_WEBHOOK_SECRET`
10. 🔧 Testar compra real (PIX de R$1)
11. (depois) Migrar `name`, stats, recents, desafio21, check-in do localStorage pro Supabase

**Status atual da migração entre PCs (2026-05-20 noite):** usuário vai dormir, vai retomar AMANHÃ CEDO em outro PC. Foi orientado a zipar a pasta `appfuncional[` (com `.env.local` incluído, que é secreto) e mover via Google Drive ou pendrive. No outro PC: descompactar → `npm install` → `npm run dev -- -p 3010`.

**Não usar Stripe** — Cakto cobre LATAM melhor (PIX, BRL, aprovação fácil). Stripe só faria sentido se vender em USD pra fora do LATAM, que não é o caso.

**Modelo de oferta (2026-05-27):** pagamento ÚNICO via Cakto = **acesso VITALÍCIO ao app** (não é assinatura/mensalidade). **Why:** é o gancho comercial principal contra academias e apps com mensalidade — destaca-se nas copies de ads. **How to apply:** em toda copy/ad/landing do Treino Express, deixar explícito "Acesso vitalício" ou "Pagamento único, sem mensalidade". Nunca chamar de mensal ou assinatura.
