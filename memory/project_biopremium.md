---
name: project-biopremium
description: "Link-in-bio premium nichado pra profissionais (saúde+imobiliário), com sócio, mensalidade, em aquecimento. Workspace em Desktop\\BIOPREMIUM. 1º template corretor LIVE em biopremium-corretora.pages.dev"
metadata: 
  node_type: memory
  type: project
  originSessionId: ee771611-29c7-428f-8237-a58c14834760
---

## ESTRUTURA WORKSPACE (criada 2026-05-28)

Raiz da empresa: `C:\Users\User\Desktop\BIOPREMIUM\` (aberta no VS Code).

```
BIOPREMIUM/
├── README.md           ← overview empresa, preços, decisões pendentes
└── corretor/           ← 1º nicho/template
    ├── README.md       ← specs deste template + placeholders pra trocar
    ├── index.html      ← source editável
    ├── EMPACOTAR.bat   ← gera index-completo.html single-file (~2MB) offline
    ├── ATUALIZAR_ONLINE.bat ← refresh OAuth CF + deploy automático Pages
    ├── _deploy/        ← pasta usada pelo wrangler pra upload
    ├── VSL.mp4 + VSL-mini.mp4 + casa1-mini.jpg + 3 imgs originais
    └── index-completo.html (gerado, ~2 MB single-file)
```

## DEPLOY CORRETOR LIVE (2026-05-28)

- **URL:** https://biopremium-corretora.pages.dev
- **Projeto CF Pages:** `biopremium-corretora` (account 3efe40850575dec18923b50db72942fc)
- **Branch:** main
- **Tamanho deploy:** ~1.3 MB total (VSL 1.1MB + 4 imagens + HTML)
- **OAuth token CF gotcha:** expira ~16h. `ATUALIZAR_ONLINE.bat` renova automático via `POST dash.cloudflare.com/oauth2/token` grant_type=refresh_token + regrava default.toml (mesmo pattern de [[project-fitness-app]]).
- **Compressão de mídia:** ffmpeg em `C:\Users\User\.media-tools\node_modules\ffmpeg-static\ffmpeg.exe`. VSL: scale=540 CRF 30 audio 56k mono → 2.5MB vira 1.1MB. Foto grande: scale=720 q:v 6 → 545KB vira 63KB.
- **Video no single-file usa Blob URL via JS** (não data: URI) — iOS Safari refusa autoplay com data: URI grande, Blob URL funciona 100%.

## DETALHES DA PÁGINA CORRETOR (template 1)

- **Nicho:** corretor MCMV em São Bernardo do Campo. Hook atual: "Pare de pagar aluguel. Comece a pagar o que é seu."
- **Paleta:** azul marinho `#1a3a5c` + dourado fosco `#c9a961` + off-white `#fafaf7`. Playfair Display + Inter.
- **Estrutura:** hero com hook + sub + grid [video VSL 320px vertical] + [quiz 6 steps], stats persuasivas em linha (+200 famílias / +10 anos / 98% aprovação), marquee infinito de casas vendidas, sobre minimal, footer.
- **Quiz:** 6 steps (Objetivo, FGTS, Renda família MCMV, Tipo imóvel, Prazo, Nome+WhatsApp). Auto-avança no clique. Submit abre `wa.me/<numero>?text=<msg-formatada-1a-pessoa-do-lead>` — lead chama corretora (não corretora chama lead).
- **Placeholders pra trocar quando tiver dados reais:** `CRECI 00000` (3x), `5511999999999` (2x no JS), `VocêImóveis` (3x), `YI` na foto placeholder.

## PARA NOVOS NICHOS

Replicar pattern `BIOPREMIUM/<nicho>/` com index.html + EMPACOTAR.bat + ATUALIZAR_ONLINE.bat. Cada nicho tem seu projeto CF Pages separado (`biopremium-<nicho>.pages.dev`). Templates pendentes (por ordem de ticket): personal trainer, dentista, psicólogo, nutricionista (já tinha protótipo em projeto antigo).

**BioPremium** = SaaS/serviço de **link-in-bio premium** competindo com Linktree, mas nichado e bem mais profissional. Diferente dos outros projetos do usuário ([[project-megapacks]], [[project-fitness-app]], [[project-caixa-magica]], [[project-controle-ml]]) por ser **com sócio** (não é solo) e por ser **B2B/serviço com mensalidade** (não info-produto one-shot).

**Hospedagem confirmada:** Vercel (subdomínio `*.vercel.app` por enquanto, sem domínio próprio ainda). Exemplo de template ao vivo: `https://template-nutricionista-biopremium.vercel.app`. SPA (React/Next), HTML inicial vazio — WebFetch não pega conteúdo, só print mesmo.

**O que a página entrega (visto no template nutricionista):**
- Hero: foto profissional + nome + credencial (ex: CRN 12345) + tagline
- **Social proof live:** "X pessoas online agora" (estilo Hotmart)
- **Form de agendamento embutido em 4 steps** (nome, idade, etc) — captura lead direto na bio
- Cards de especialidades (4 cards com ícone + título + subtítulo, ex: Endurance, Hipertrofia, Alto Rendimento, Reabilitação)
- Identidade visual personalizada por cliente (no template = verde clean estilo clínico)

**Diferencial vs Linktree:**
- Design 1000% mais profissional que botões empilhados
- **Captura de lead direto** (form de agendamento, não só link de saída)
- Social proof ao vivo gera escassez/urgência
- Nichado: template por categoria profissional (nutricionista é o primeiro feito)

**Modelo de negócio:**
- **Mensalidade** (não one-shot) — justificada por hosting + atualizações
- **Estratégia de aquecimento atual (2026-05-28):** primeiras **10 pessoas grátis** em troca de divulgação dos profissionais (classic seed para B2B). Não confundir com "freemium permanente".

**Pontos em aberto que ainda não confirmei com o usuário (perguntar quando voltar ao assunto):**
- Modelo de entrega: full-service (eles criam tudo) vs self-service (cliente edita sozinho via painel)? O fato de cobrarem mensalidade + estarem fazendo template-por-template sugere full-service.
- Quem é o sócio (papel: dev / vendas / design / capital)?
- ICP final escolhido: só saúde ou aberto pra liberais em geral?
- Preço da mensalidade pós-aquecimento?
- Domínio próprio planejado?

**Como tratar pedidos do usuário sobre esse projeto:** sempre lembrar que tem sócio — decisões de copy/preço/posicionamento podem precisar de alinhamento. Não assumir que ele decide sozinho como nos outros projetos.
