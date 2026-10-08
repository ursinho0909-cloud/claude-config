---
name: feedback_imagens_peso_landing
description: Gerar toda imagem de landing em WebP a 2× da largura de exibição no CSS — e nunca usar display:none em img com loading lazy
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4923dff1-80c3-409e-89bd-abf9fe69423f
  modified: 2026-07-30T15:39:18.902Z
---

Antes de salvar qualquer imagem numa landing, **ler a largura de exibição no CSS** (`max-width` do wrapper, `width` do `.marquee-item`, etc.) e gerar em **2× disso, em WebP**. Nunca subir PNG/JPG direto do gerador de imagem — eles saem com 1,5–7 MB cada.

**Why:** em 2026-07-30 auditei as landings e o `matematicabloques` (rodando tráfego pago) carregava **25,4 MB**, com `hero.png` de 2,46 MB e `fetchpriority="high"` travando o primeiro paint por ~4 s a 5 Mbps. Os bônus tinham 1632px pra aparecer em 200px — 8× a resolução necessária, 4,5 MB cada. Convertido pra WebP no tamanho certo: 25,4 MB → 1,41 MB, sem mudar uma linha de layout. O coreano ES foi 6,81 → 2,82 MB.

**How to apply:**
- Medir o total real da página baixando os assets do domínio live, não estimar pela pasta (tem arquivo órfão que não carrega).
- Distinguir **o que bloqueia o primeiro paint** (imagem sem `loading="lazy"`) do resto. É o único número que decide se a pessoa fica — o total da página engana. Foi por olhar só o total que classifiquei o coreano como pior caso, e ele não era.
- Diagnóstico verificável no Meta: comparar **Cliques no link × Visualizações da página de destino**. Diferença normal é 10–20%; muito acima disso é gente saindo antes da página montar.
- **Nunca `display:none` em imagem com `loading="lazy"`** — fora do layout ela nunca se aproxima da viewport e o lazy jamais dispara. Ocultar por `opacity`.
- `wrangler` não respeita `.gitignore`: pasta de backup dentro do projeto vai pro deploy. Mover pra fora antes.
- Guardar os originais fora do repo e mandar pro Drive — ver [[project_github_sync]].

Aplicado em [[project_caligrafia_bluey]], que já nasceu em 1,35 MB.
