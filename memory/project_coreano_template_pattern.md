---
name: project-coreano-template-pattern
description: "Playbook do esqueleto da landing Coreano Descomplicado, modelo padrão pra próximos sites de info-produto. Quando user pedir \"modelo-<nicho>\" seguir esse padrão direto sem perguntar."
metadata: 
  node_type: memory
  type: project
  originSessionId: 1bb03cf4-82df-43ff-ae87-0ad84a0e0327
---

Esqueleto reutilizável de info-produto landing, validado em [[project-coreano-descomplicado]]. Quando o user pedir "modelo-<nicho>" ou referenciar "modelo da coreia" / "modelo Coreano Descomplicado", seguir isso sem perguntar.

## Estrutura HTML (ordem das seções)
1. Top bar countdown (gradient azul-bandeira ou cor temática)
2. Hero: brand + kicker badge + h1 com `<span class="hl">` + sub + img mockup + CTA + social proof + trust row
3. Marquee `Veja o material por dentro` (carrossel infinito CSS, 26s, imparável, fade mask nas pontas)
4. Section dor: pain-list (5 itens) + pain-resolver
5. Marquee de depoimentos (screenshots WhatsApp/Instagram, 38s, imparável)
6. `O que tem dentro` learn-grid (6 cards com emoji + título + descrição específica — sem AI-speak)
7. Countdown grande (urgency)
8. `Você se reconhece em alguma?` ideal-grid-v2 (6 personas reconhecíveis com problema concreto + produto/marca nominado)
9. CTA block fechando a seção ideal
10. `O que você recebe` receive-split (split image+checklist com 7 bullets)
11. Bônus grid (4 cards com 1ª destacada como `hot` + tag "🔥 Mais cobiçado")
12. Pricing 2 colunas:
    - Básico: cover img smaller + lista (3 ok + 2 locked) + preço + nudge "92% prefere os bônus na oferta abaixo" com seta ↓ pulsante
    - Premium: ribbon "⭐ MAIS ESCOLHIDO" + cover img big + título + 5 bullets + bonus-list-mini + preço centralizado com strike no original + parcelado destacado + CTA
13. FAQ accordion (8 details)
14. Footer com brand + tagline + legal + copy

## Paleta padrão (taegukgi — bandeira coreana)
Reutilizar essa pra qualquer nicho. Pra nichos específicos trocar `--korea-red/--korea-blue` por cores da bandeira/identidade do nicho mantendo a relação.
- `--korea-red:#CD2E3A` (CTA, ribbon, urgency, kicker, savings, prices premium)
- `--korea-blue:#0047A0` (brand, top-bar, footer, checks, badges secundários)
- `--bg-white/--bg-cream/--bg-soft/--bg-blue-tint/--bg-red-tint` (rotação dos fundos pastéis claros)
- CTA pulsa, gradient vermelho, com `animation:pulse`

## Tipografia
- Inter 400/700/800/900 + Black Han Sans pro brand/footer

## JS
- Countdown 29:43 com reset (mantém urgência infinita)
- Sem JS de carrossel (puro CSS marquee)
- CTAs stub com `data-plan="basico|premium"` esperando link checkout

## Performance (sempre aplicar)
- `<link rel="preload" as="image" fetchpriority="high">` no hero
- `width/height` explícitos no hero img (zero CLS)
- `loading="lazy" decoding="async"` em todo resto
- PNGs com transparência: max 720px, optimize=True, palette quantize 128 cores no hero
- Screenshots: convert pra JPG q=78 (sem transparência), max 800px wide
- MMs JPGs: q=78, max 1000px wide
- Pillow `_compress_all.py` em `C:\Users\User\Desktop\koreia\` faz tudo

## Scripts auxiliares (em Desktop\koreia\)
- `_remove_white_bg.py` / `_remove_bg_v2.py`: corner-color floodfill bg removal
- `_mask_watermark.py`: cobre marca d'água ✦ do Gemini no canto inferior direito
- `_upscale_dep4.py`: Lanczos 4x + unsharp mask pra fontes ruins
- `_compress_all.py`: pipeline completo de otimização

## Cache busting
Sempre `?v=N` nos imgs trocados pra forçar reload no mobile sem precisar Ctrl+Shift+R.

## Deploy
- CF Pages via wrangler (`wrangler pages deploy . --project-name <slug> --branch main --commit-dirty=true`)
- Conta ursinho0909@gmail.com
- Slug do projeto = `<nicho>-descomplicado` ou similar

## Assets necessários do user (brief padrão)
Ver `project_coreano_template_brief.md` (template em branco que o user preenche).

## Why
Esse padrão converte porque: countdown insistente + CTA vermelho + mockups limpos + depoimentos screenshot reais (chat) + nudge no básico forçando upsell pro premium. Já vendido 3.000+ alunos no original (claim).

## How to apply
Quando user mandar "modelo-<nicho>" ou referenciar esse template:
1. Pedir os assets do brief
2. Copiar pasta `Desktop\coreano-descomplicado-landing\` pra nova pasta `Desktop\<nicho>-landing\`
3. Trocar todos assets em `assets/`
4. Rodar `_remove_white_bg.py` adaptado pro novo set
5. Substituir copy nos pontos certos (h1, sub, learn-cards, ideal-cards, faq)
6. Trocar nome do projeto + brand color se nicho exigir
7. Rodar `_compress_all.py`
8. Deploy CF
