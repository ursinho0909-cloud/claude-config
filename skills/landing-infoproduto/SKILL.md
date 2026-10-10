---
name: landing-infoproduto
description: Criar/clonar/traduzir landing de info-produto e publicar no Cloudflare Pages com checkout Hotmart e pixel UTMify — o fluxo padrão do Thiago (PT/FR/DE/IT/ES). Use em "faz a landing", "clona pra alemão", "sobe no ar", "pluga o checkout/pixel", "cadastra na Hotmart".
---

# Landing de info-produto → Cloudflare Pages

## Estrutura que ele usa (HTML único + assets)
hero (capa/mockup) → carrossel de fichas reais → celular folheando o PDF → grade de categorias → "ideal para" → CTA → contador → entregável → bônus com valor riscado → oferta (âncora "De X") → garantia 7 dias → como funciona → FAQ → fecho. Preço Europa típico 13,90–17,90 €. `CHECKOUT_URL` e pixel ficam no topo do script/HTML.
Antes de criar do zero, procure na memória a landing mais parecida e CLONE (ex.: haekeln-zuhause, crochet-noel-fr, crochet-natale-it). Tradução por script de pares (build_lang.py / build_fr.py / build_it.py): rodar de novo sempre que mexer na base.

## Imagens
Medir a largura exibida no CSS e gerar 2× em WebP. Nunca `display:none` em img pesada. Placeholders `img[data-ph]` até o usuário mandar as definitivas.

## Publicar
1. Copiar só `index.html` + `assets/` pra pasta temporária (ex.: `C:\tmp\dep_<proj>`). Não subir scripts de build.
2. `npx wrangler pages deploy C:\tmp\dep_<proj> --project-name <proj> --branch main` (primeira vez cria o projeto; URL = `<proj>.pages.dev`).
3. Conferir no navegador (mobile 420px) e no console.

## Hotmart
- Produto: eBook, preço com impostos, garantia 7 dias; entregável em partes < 10 MB (upload não aceita maior) + bônus. "Cadastrar eBook" = navegar direto em `/products/add/4/info`.
- Checkout `…?checkoutMode=10`, modelo "Em Branco" com contador e banner no idioma, 3 bumps + combo "leve todos" (o combo é o que mais vende). Desktop = cópia do celular.
- Campos que travam com teclado: setter nativo via JS.

## Pixel UTMify
Colar o código EXATO do painel (ofuscado) no `<head>` (+ `utms/latest.js`). Testar `canSendIc`. Cada país tem pixel próprio. Regra do painel controla o IC (webhook não tem a ver).

## Depois
Salvar na memória: URL, projeto CF, checkout, pixel, pasta local, o que falta. Lembrar de commit/push (repo privado no GitHub do usuário) e de rodar o sync do claude-config.
