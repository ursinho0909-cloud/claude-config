---
name: reference-utmify-pixel-ic
description: "Como o pixel.js da UTMify decide disparar InitiateCheckout, e por que não dá pra testar em localhost"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 608b577b-fc34-43d0-af3f-a2fe5970b380
  modified: 2026-08-18T14:21:16.294Z
---

Lido direto do fonte de `https://cdn.utmify.com.br/scripts/pixel/pixel.js` em 18/08/2026,
depurando o [[project-codice-santos]].

**IC é 100% front-end.** Webhook (plataforma → UTMify) é servidor→servidor e só traz
Purchase. Trocar de painel ou criar webhook novo nunca conserta IC — não gastar limite com isso.

**A cascata do `isCheckoutLink(href, texto, classes)` tem curto-circuito:**

```
if (icURLMatch)  return href.includes(icURLMatch);   // sai aqui
if (icTextMatch) { ...testa o texto do link... }     // ou aqui
if (icCSSMatch)  return classes.contains(...)        // ou aqui
for (kw of checkoutLinkKeywords) ...                 // só chega se o painel estiver VAZIO
```

Ou seja: **qualquer regra configurada no painel desliga a lista padrão.** Se a regra não
casar, o IC simplesmente não sai.

Lista embutida (`checkoutLinkKeywords`): checkout, pagamento, payment, pay, kiwify,
**hotmart**, eduzz, monetizze, vindi, pague, comprar, finalizar, compra, cart, carrinho,
order, pedido, confirmar, adoorei, vega, buygoods, octuspay, perfect, payt, guru, green,
yampi, appmax, pepper.

**Preferir sempre regra por URL, nunca por texto de botão.** Numa landing onde só um botão
sai pro checkout e os outros são âncora pro preço, regra por texto dispara IC em quem nem
saiu da página e infla o número que o Meta usa pra otimizar.

**Gotcha de idioma:** regra "QUERO" copiada de projeto PT não casa com landing ES, que diz
"QUIERO". Uma letra derruba o IC inteiro.

**Não dá pra testar em localhost:** o script faz
`hostname === "localhost" || "127.0.0.1" ? "http://localhost:3001/tracking/v1" : "https://tracking.utmify.com.br/tracking/v1"`.
Em localhost ele tenta a porta 3001 e nada é enviado. Testar pelo IP da LAN ou no domínio publicado.

**Como depurar:** o script é falante, loga tudo com `console.log`. Clicar no botão com o
console aberto mostra `check is checkout link: <href>` e depois `canSendIc true/false`.
Dá pra automatizar com
`msedge --headless=new --enable-logging=stderr --v=0 --virtual-time-budget=20000 --dump-dom <url>`
e filtrar o stderr.

O script `utms/latest.js` reescreve sozinho o link do checkout com utm_*, `xcod` e `sck` —
não precisa injetar `src`/`sck` na mão.

**Checagem 26/09/2026 (DASH-EUROPA):** as 6 landings (pilates-visual-de/fr/es/it, actividades-tea, activites-tsa) têm `icURLMatch = "https://pay.hotmart.com"` e `canSendIc true` no clique → front OK.
Config fica no localStorage `lead` da landing (icURLMatch/icTextMatch/icCSSMatch/metaPixelIds) — ler isso é o jeito rápido de auditar.
Testar clique sem sair da página: adicionar classe `link_interno` no `<a>` antes do `.click()` (o pixel não navega).
CONFIRMADO 26/09: UTMify conta cada order bump como venda separada (ESCALA GER: 23 "vendas" = 12 compradores). Pra comprador real, filtrar Produto = só o principal (param `products=` na URL aceita lista de nomes). CPA por comprador GER ~R$55, TEA ES ~R$46, ITA ~R$18. Mesmo assim IC ≈ compradores na Alemanha = IC ainda subnotificado lá (causa não achada; landing OK).
Extensão Claude-in-Chrome no Opera GX NÃO funciona (sem tab groups) — usar o Chrome.
**08/10/2026 — pedido do suporte UTMify (Filipe):** pixel deve ficar EXATAMENTE como gerado em Integrações→Pixel (não dentro de função/IIFE) e botões SEM animação pulsante ("atrapalha o IC"). Aplicado e no ar em haekel-weihnacht, crochet-noel, haekeln-zuhause, crochet-maison (snippet top-level `window.pixelId=...; var a=document.createElement("script")...`; build_fr.py e build_lang.py também atualizados). Teste no ar: canSendIc true. Obs.: 1 clique gera ~6 "link clicked/canSendIc" no console (listener duplicado do próprio pixel.js). Teste A/B: comparar IC/visita de antes x 2 dias depois. Minha hipótese p/ IC subnotificado = navegação in-app (Instagram/FB) sai antes do envio, não a pulsação. Ainda com IIFE/pulse: croche-casa-pt, aktivitaeten-tea-de, pilates-pt (só pulse).
**08/10 tarde:** o código do painel (Integrações→Pixel) é OFUSCADO e também é IIFE (`(function(){var x=atob("...")...` = XOR c/ chave no 1º byte → JSON {globals:[{pixelId}], url}). Decodificar com base64+xor p/ auditar. Pilates IT/ES/DE, anatomie-visuell/visuelle, atlas-anatomia-pt já tinham o código exato do painel → só removida pulsação (btn-pulse / .btn-teal animation:pulsar) e redeploy via espelho do site no ar (C:\tmp\mirror.py; anatomia carrega assets/pagina-01..16.webp via JS, crawler não pega sozinho). As 4 de crochê (manhã) ficaram com snippet legível escrito por mim, não o ofuscado do painel — funcionalmente igual.
