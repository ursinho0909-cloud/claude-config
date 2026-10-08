---
name: project-codice-mitologia
description: "Info-produto LATAM \"El Códice de la Mitología Griega\" — 100 expedientes ilustrados em 5 módulos, área de membros com cor por módulo"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4dc2241c-f809-458d-86a7-be176475f811
  modified: 2026-08-07T14:08:18.582Z
---

Info-produto LATAM (ES) iniciado 04-05/08/2026. Nome: **El Códice de la Mitología Griega** (LATAM) / **O Códice da Mitologia Grega** (BR, unidade = "dossiê"). Regra de naming: códice = coleção, expediente/dossiê = unidade. Nunca "100 códices".

**Ângulo:** 100 personagens (elenco), não "mitologia grega" (assunto). Ancorado na dor declarada do concorrente: *"siempre confundo quién es hijo de quién"*. Dois campos exclusivos: "No confundir con…" e "Dónde aparece hoy" (Percy Jackson, God of War, Hades, Kaos) — ambos ficam **só no HTML**, nunca queimados na imagem.

**Concorrentes:** BR "Mitologia Grega Ilustrada" R$17,90/27,90 · MX "Atlas Visual de la Mitología Griega" US$5,90, 50 mapas, 2 criativos.

**Padrão visual VALIDADO** (Zeus + Medusa aprovados): ouro antigo / marfim / azul-meia-noite, moldura art déco com meandro grego, 2:3. Prompt fechado em `Desktop\codice-mitologia-grega\PROMPT_MESTRE.md` com os 3 patches (família batendo em gênero+contagem, legenda legível no celular, zero ícone repetido). Sempre anexar a Medusa como referência de estilo.

**VALIDADO — rodando tráfego e VENDENDO desde ~04/08/2026** (confirmado em 07/08, 3º dia). O molde "Códice" (expediente ilustrado · 5 módulos × 20 · US$ 9,90 · oferta única) está validado comercialmente e pode ser replicado em outros temas. Série em discussão em 07/08: Prehistórico (aquisição, público novo) vs Folclore LATAM (arriscado: fragmentação regional + tom de terror choca com comprador-mãe) vs Nórdico/Azteca (mesma prateleira, cross-sell na base).

**NO AR (2026-08-05):**
- **Landing:** https://codice-mitologia.pages.dev · projeto CF `codice-mitologia` · repo privado `ursinho0909-cloud/codice-mitologia-landing` · pasta `Desktop\codice-mitologia-landing`
- **Área de membros:** https://codice-mitologia-miembros.pages.dev · projeto CF `codice-mitologia-miembros` · repo privado `ursinho0909-cloud/codice-mitologia-area-miembros` PDF de entrega pra Hotmart em `entrega/acceso-area-de-miembros.pdf`, gerado por `scripts/make_entrega_pdf.py` (clone do modelo do anatomia). Cadastro Hotmart pronto em `codice-mitologia-grega\HOTMART_cadastro.md`.

**Área de membros:** `Desktop\codice-mitologia-area-miembros\` — clone estrutural de anatomia-area-miembros, CSS reescrito dark. 5 módulos × 20. **Decisão de design (05/08):** a casca inteira é ouro sobre azul-meia-noite — **quem identifica o módulo é a CAPA**, não a cor da interface. O acento de categoria (Dioses=ouro · Héroes=bronze · Monstruos=esmeralda · Titanes=índigo · Historias=pergaminho) sobrevive só em 3 lugares pequenos: número da sidebar, badge da capa e pílula "MÓDULO X". Motivo: ouro é a cor da marca, e o vocabulário de cor fica reservado pra diferenciar **produto de produto** depois (Códice Nórdico=gelo/prata, Azteca=jade/obsidiana). Gerado por `build-pages.py`. Preview: `python dev_server.py` → localhost:8765.

**Prompts prontos:** `Desktop\codice-mitologia-grega\prompts\` — 1 arquivo por leva de **10 lâminas** (acima disso o Manus pula e inventa). Prontos: DIOSES 01-20 (ES+BR) e HEROES 01-20 (ES). Faltam Monstruos/Titanes/Historias.

**PRODUÇÃO ES: 60/100 no ar** — Dioses 20/20, Héroes 20/20, Monstruos 20/20 (fechado 2026-08-05). Faltam Titanes y Primordiales e Grandes Historias (prompts ainda não escritos).

**DUAS EDIÇÕES DA MESMA LÂMINA (decidido 2026-08-05):**
- **Escura** (ouro sobre azul-meia-noite) = tela. Fica em `modulos-content/`.
- **Clara** (tinta navy + ouro linha fina sobre papel marfim, estilo prancha de enciclopédia do séc. XIX, 6 painéis numerados em terracota) = impressão. Fica em `modulos-content-print/`.

Motivo: a escura impressa fecha as sombras e vira borrão. Não dá pra converter escuro→claro por processamento (o dourado sobre creme fica ilegível): tem que regerar com direção de arte própria. Prompts em `ES_CLARA_DIOSES_impresion.md` e `ES_CLARA_MONSTRUOS_impresion.md` (7 lâminas cada, dados idênticos aos da escura). Referência de estilo aprovada: `_referencia\REFERENCIA_ESTILO_CLARO_Hades.jpg`. **A versão clara ficou melhor que a escura em legibilidade** — cada retrato da família vem com o nome escrito embaixo.

No site: a galeria mostra a escura, o botão "Descargar" entrega a clara.

**Gerador: ChatGPT sai melhor que Manus para lâmina avulsa.** Manus só entrega 1536×2304 em tandas de 10 — em leva de 1 ou 2 cai pra 832×1248 e a lâmina vira lixo. ChatGPT entrega 1024×1536 e o texto sai perfeitamente legível nessa resolução. Escila e Edipo (as duas que o Manus estragou 3×) saíram limpas no ChatGPT de primeira.

**Regras de prompt que resolveram os defeitos** (descobertas na produção, valem pras 100):
1. **Nenhuma linha de FAMILIA com mais de 4 nomes** — o gerador desenha em grade e não consegue 5 nem 7. Foi o que resolveu a contagem errada de retratos.
2. **"LABELS — every row keeps its written label"** — sem isso ele desenha retratos sem legenda.
3. **"TEXT — do not rewrite the short lines"** — sem isso parafraseia símbolos e curiosidades.
4. Módulo Héroes usa campos diferentes no painel: **ORIGEN · ARMA · DESTINO** no lugar de PLANETA/REINO. "DESTINO" (como o herói terminou) é o campo que mais interessa ao leitor.
5. **Defeito aceito, não vale regerar:** ícones do painel CURIOSIDADES saem repetidos. Cosmético.
6. **RESOLUÇÃO É CRÍTICA — exigir 1536×2304 no prompt.** Quando o Manus entrega 832×1248 a lâmina sai com TODO o texto embaralhado e ilegível (não é só nitidez — ele não consegue desenhar as letras pequenas). Lâmina nessa resolução é lixo, tem que regerar. Sempre conferir o tamanho no momento de converter.

**Pipeline de imagem:** PNG do Manus → JPG q88 (full, ~1.1 MB, pro lightbox/download) + thumb WebP 520px (~120 KB, pro grid). 100 fichas dariam 110 MB sem isso. Converter e rodar `python build-pages.py`.

**Oferta (decidida 2026-08-05): OFERTA ÚNICA US$ 9,90**, sem plano básico. 3 bônus (Árbol Genealógico · Mapa del Mundo Griego · Línea del Tiempo) — o 4º (Guía Griego-Romano) foi cortado. Upsell: Códice Azteca. Produto irmão óbvio: Códice Nórdico (mesmo template, elenco diferente).

**Landing:** `Desktop\codice-mitologia-landing\` — estrutura clonada de caligrafia-en-casa-landing, mas **design CLARO** (mármore #FBF9F4 + ouro #B8892B + CTA terracota), ao contrário da área de membros que é escura. Motivo: o comprador entra num lugar mais luxuoso do que aquele onde comprou, e as lâminas douradas viram as únicas peças escuras da página (efeito de galeria). Preview: `python dev_server.py` → localhost:8766. Copy completa em `codice-mitologia-grega\COPY_PV_ES.md`.

**Headline escolhida:** "Zeus. Medusa. Hades. Aquiles. Y otros 96." — nome próprio na headline para o dedo e vira criativo de vídeo direto.

Relacionado: [[project-coreano-area-miembros-es]], [[project-anatomia-area-miembros]], [[feedback-oferta-ancora-unidade]], [[feedback-manus-prompt-order]]
