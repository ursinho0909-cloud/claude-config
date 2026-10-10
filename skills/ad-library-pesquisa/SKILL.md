---
name: ad-library-pesquisa
description: Varredura de mercado na Biblioteca de Anúncios da Meta pelo Chrome — achar ofertas validadas no BR, checar lacuna/concorrência em FR/IT/DE/ES/PT/LATAM, achar referências de criativo e baixar os vídeos. Use em "pesquisa", "varredura", "o que tá rodando", "tem concorrência?", "acha referência de criativo", "ideia de oferta nova".
---

# Pesquisa na Ad Library (método do Thiago)

## URL base (navegar direto, sem clicar em filtro)
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=<BR|FR|IT|DE|ES|PT|MX|AR|GB>&media_type=<all|video|image>&q=<termo>&search_type=keyword_unordered&sort_data[direction]=desc&sort_data[mode]=total_impressions`
- Ordenar por impressões = o que mais escala aparece primeiro. Termos no idioma local ("crochet noël", "uncinetto natale", "Weihnachten häkeln", "ganchillo"…).
- **Lacuna**: repetir com `active_status=all` (inativos). Rodou poucos dias e parou = teste que falhou; semanas = validado. Nota 9 só depois de checar inativos no alvo E nos vizinhos (IT antecipa FR).

## Extrair rápido (get_page_text fica gigante)
Rolar até o fim 2–3× e rodar JS que separa por "Identificação da biblioteca: ": id, data de início, anunciante, 60 primeiros caracteres; agrupar por anunciante com contagem (nº de anúncios = escala). Saída do javascript_tool trunca ~1000 caracteres → guardar em `window._rows` e ler em fatias.
Se der "Cannot access a chrome-extension:// URL", outra extensão injetou iframe: usar get_page_text.

## O que olhar
- Exportador BR entrando no país (nome brasileiro, lovable.app/vercel, checkout Hotmart/Kiwify/lastlink) = termômetro de que vende.
- Ângulo (decorar/presentear na Europa vs "faça e venda" no BR/LATAM), preço, formato (nº de receitas/fichas), bônus.
- Página do próprio usuário na FR = "Helena González" (não é concorrente).

## Baixar criativo de referência
`python -m yt_dlp "https://www.facebook.com/ads/library/?id=<ID>"` → salvar em pasta `_referencias_BR` do projeto; transcrever com faster-whisper pra modelar o roteiro.

## Entregar
Ranking com nota (provisória se faltou checar inativos), 1 escolha defendida + 2–3 alternativas, nº de anúncios/anunciantes por país, links/IDs, e salvar um resumo na memória (project_varredura_<tema>_<data>.md).
