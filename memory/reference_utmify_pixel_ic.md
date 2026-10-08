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
