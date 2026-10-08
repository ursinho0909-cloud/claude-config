---
name: project-codice-prehistorico
description: "Info-produto LATAM \"El Códice de las Criaturas Prehistóricas\" — 2º da série Códice, 100 expedientes em 5 módulos, landing pronta e sem imagens"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4d399978-86c5-41e2-aaf5-f90422f287cb
  modified: 2026-08-07T17:29:14.676Z
---

Segundo produto da série **Códice**, decidido em 07/08/2026 depois que o [[project-codice-mitologia]] validou o molde vendendo desde o 1º dia. Escolhido sobre "Gigantes de la Tierra" (título ambíguo) e sobre folclore latino-americano (fragmentação regional + tom de terror choca com a compradora-mãe).

**Oferta:** US$ 9,90 (antes US$ 29,90), pagamento único, 3 bônus. Mesmo padrão do Grego.

**Landing:** `Desktop\codice-prehistorico-landing\` — clone estrutural de `codice-mitologia-landing`. Paleta **âmbar-fóssil**: hueso #FBF8F2 · arena #F3ECE0 · pizarra #1E2A2E · âmbar #B0691C · CTA lava #C0442B. Meandro grego trocado por divisória de **estratos** (SVG) e as listras de coluna do hero por **camadas sedimentares**. Preview: `python dev_server.py` → localhost:**8767**. Sem imagens (usuário gera).

**Headline:** "Tyrannosaurus. Megalodón. Mamut. Titanoboa. Y otras 96."

**5 módulos × 20** (por TIPO, não por era — se dividir por era o Módulo 1 = Triássico só tem nomes que ninguém conhece): Depredadores #C0442B · Gigantes Herbívoros #4E8C4A · Monstruos de los Mares #1F6F8B · Señores del Cielo #2FA0A8 · Megafauna del Hielo #7B8FA8.

**Duas adaptações obrigatórias do molde grego** (a lâmina grega vive do painel FAMILIA, e dinossauro não tem família — sem isso a ficha fica com buraco no meio):
1. **COMPARACIÓN DE TAMAÑO** no lugar de FAMILIA — silhueta ao lado de pessoa/auto/ônibus. É o painel mais viciante do nicho e o que justifica o preço.
2. **EL DESCUBRIMIENTO** no lugar de PRINCIPALES HISTORIAS — quem achou o fóssil, quando, o que o esqueleto revelou.

**"EL DATO REAL"** — campo fixo que corrige o que o cinema mostrou errado (Velociraptor tinha penas e media menos que um cachorro grande). Resolve o risco de comentário técnico negativo no anúncio e virou pilar de copy.

**Ângulo LATAM (seção própria na landing):** "Los dinosaurios más grandes del planeta no se encontraron en Estados Unidos." Argentinosaurus, Giganotosaurus, Carnotaurus, Titanoboa, Megaterio, Amargasaurus, Gliptodonte, Argentavis, Macrauchenia, Patagotitan. Dá o orgulho identitário sem os problemas do folclore.

**Bônus:** #1 El Póster de los Tamaños (as 100 a escala) · #2 La Línea del Tiempo de la Vida · #3 El Mapa de los Gigantes de América.

**Risco de marca:** "Jurassic", "Jurassic World", "Ice Age", "Dino Rey" fora do título, da URL e dos criativos (Universal derruba anúncio). No corpo do texto "era jurásica" e "edad de hielo" passam — são termos científicos.

**Área de membros:** `Desktop\codice-prehistorico-area-miembros\` — clone estrutural da área do Grego (que estava idêntica local↔live, ao contrário da landing). Gerada por `build-pages.py` (mesmo gerador, só trocaram FICHAS/MODULES/BONOS). Preview: `python dev_server.py` → localhost:**8768** (atenção: o `dev_server.py` da ÁREA vem com PORT 8765, não 8766 como o da landing). Paleta dark **âmbar sobre piedra** (tokens renomeados navy→piedra, gold→ambar no CSS e nas classes do gerador). 100 fichas nomeadas, 5 páginas de módulo geradas. `arte.html` não é gerado ainda — o gerador só cria quando existir lâmina nas DUAS edições (clara+escura), mecanismo mantido intacto.

**Direção de arte da lâmina (VALIDADA 07/08 com o T-Rex):** prancha de história natural do séc. XIX, papel osso envelhecido, paleta âmbar/osso/sépia/ardósia — **edição única CLARA**, sem edição escura (no Grego a clara já tinha ganhado em legibilidade; fazer as duas dobraria a produção pra 200 imagens). Moldura = **camadas de estrato rochoso** + 4 medalhões de canto DIFERENTES (amonite, corte de osso, pegada de 3 dedos, samambaia). O NEGATIVE tem que proibir explicitamente meandro/elmo/louro/coluna/azul — sem isso o gerador volta pro grego sozinho. Lâmina clara dentro da área escura = efeito galeria, é proposital. Prompt mestre em `Desktop\codice-prehistorico\prompts\`.

**Painéis da lâmina:** 1 ¿QUÉ ERA? · 2 ARMAS Y DEFENSAS · 3 DATOS CLAVE · [ilustração] · 4 FICHA TÉCNICA · 5 COMPARACIÓN DE TAMAÑO (3 silhuetas com medida escrita) · 6 CURIOSIDADES · faixa EL DESCUBRIMIENTO (5 cards) · faixa EL DATO REAL (largura total, fundo ardósia, lupa) · frase.

**Pipeline de imagem:** `scripts/procesar_laminas.py` na área — dropa o PNG em `_entrada/` com o nome exato da ficha (`DEPREDADORES_01_TyrannosaurusRex.png`) e roda; sai JPG q88 + thumb WebP 520px nas pastas certas. Edição única vai em `modulos-content/`, NÃO em `modulos-content-print/`. ChatGPT entrega 1024×1536 e o texto sai legível; Manus só entrega 1536×2304 em tanda de 10.

**Placeholder de imagem na área:** `app.js` troca imagem quebrada por um SVG inline "PENDIENTE + caminho do arquivo". Não cria arquivo falso e some sozinho quando o real entra na pasta.

**Pendente:** imagens (landing: hero, mockup, 3 bônus, premium-cover, 10 lâminas do carrossel · área: banner, bonus-cover, 5 capas de módulo, 100 lâminas + thumbs), prompts das lâminas, checkout, pixel, deploy CF Pages.

**Sync:** em 07/08 a pasta local da landing do GREGO estava 2 gerações atrás do deploy (faltavam os 2 pixels e o link do checkout `pay.hotmart.com/N107038061T?checkoutMode=10`). Sempre diffar contra o LIVE antes de clonar — ver [[feedback-landing-sync-before-edit]].

Relacionado: [[project-codice-mitologia]], [[feedback-oferta-ancora-unidade]], [[feedback-imagens-peso-landing]], [[feedback-manus-prompt-order]]
