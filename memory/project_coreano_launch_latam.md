---
name: project-coreano-launch-latam
description: "Estrategia de launch do Coreano Sin Complicaciones pra LATAM via Hotmart Internacional, ticket US$ 9,90 + back US$ 5,90, area de miembros publica sem auth"
metadata: 
  node_type: memory
  type: project
  originSessionId: c218ea9e-ee38-4766-9e9f-c7be2b31e5ab
---

# Coreano Sin Complicaciones · Launch LATAM

## Stack de venda
- **Checkout**: Hotmart Internacional (suporta moeda local MX/AR/CO/CL/PE, OXXO, Mercado Pago, PayPal). Taxa ~10% + IOF, liquido ~US$ 7-8 por venda.
- **Oferta principal**: US$ 9,90 pago unico
- **Back/exit-intent**: US$ 5,90 (40% OFF)
- **Anchor price**: US$ 67,00 riscado
- **Garantia**: 7 dias

## Entrega
- **Landing**: coreano-descomplicado-landing-es (sem repo ainda, pasta Desktop\coreano-descomplicado-landing-es)
- **Area de miembros**: coreano-area-miembros.pages.dev (live, repo github.com/ursinho0909-cloud/coreano-area-miembros)
- **Modelo de acesso**: LINK DIRETO PUBLICO via email padrao da Hotmart, sem auth. Decisao consciente — risco de pirataria em ticket US$ 9,90 nao compensa o custo de setup do webhook+magic-link. Setup de auth fica pra depois caso pirataria se prove problema.

**Why:** Hotmart e a unica plataforma com cobertura LATAM real (moedas locais + metodos de pagamento por pais + tax compliance). Ticket US$ 9,90 e' baixo demais pra justificar arquitetura complexa de auth tipo a do [[project-fitness-app]]. Link publico reduz friccao do comprador.

**How to apply:** Quando o user perguntar "como conectar Hotmart com area de membros" pra esse projeto, NAO sugerir webhook + Supabase + magic link. Manter simples: link publico no email padrao da Hotmart. Reavaliar se ele decidir mudar.

## Status atual (2026-06-23)
- **Landing ES LIVE**: https://coreano-sin-complicaciones.pages.dev (CF Pages, projeto coreano-sin-complicaciones). Repo github.com/ursinho0909-cloud/coreano-sin-complicaciones-landing (privado, criado 2026-06-23). Deploy manual via wrangler pages deploy (sem auto-deploy GitHub→CF ainda). Pasta Desktop\coreano-descomplicado-landing-es\
- **Area de miembros LIVE**: https://coreano-area-miembros.pages.dev (CF Pages, projeto coreano-area-miembros, repo github.com/ursinho0909-cloud/coreano-area-miembros). Modulos A1-C2 + modulo K-Pop & K-Drama Premium (10 mapas), todos com 10 mapas cada. Tem secao "Proximamente" entre modulos e bonos.
- **Pixel UTMify**: `6a3ac9f17e9d08cd3110782d` ja instalado no head da landing ES (2026-06-23). IC configurado por URL "pay.hotmart" no dashboard UTMify
- **Checkout Hotmart**: https://pay.hotmart.com/O106456604M?off=st21vl96&checkoutMode=10 ja plugado no botao da landing
- **PDF de boas-vindas**: gerado em Desktop\Coreano-Sin-Complicaciones-Bienvenida.pdf com link clicavel pra area de miembros. Script make_pdf_capa.py em scripts/
- Pendente: criar produto formal na Hotmart subindo o PDF, configurar IC no UTMify, conectar GitHub→CF auto-deploy
