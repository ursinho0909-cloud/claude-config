---
name: feedback-checar-anuncios-inativos
description: Antes de declarar um país "vazio" numa varredura, buscar também anúncios INATIVOS (active_status=all) — concorrente pode ter testado e desistido
metadata:
  type: feedback
---

Ao avaliar lacuna de mercado na Biblioteca de Anúncios, rodar a busca com `active_status=all`, não só `active`.

**Why:** 06/10/2026 eu disse que inglês em mapa mental na Alemanha estava "quase vazio"; o usuário achou sozinho os inativos: 3 operadores (academyaxon, Englisch Startklar, Sprachfluss-Karten) já tinham testado DE e saído. Isso inverte a leitura (vazio = não converteu). Ver [[project-englisch-landkarte]].

**How to apply:** em toda nota de "lacuna", olhar inativos dos últimos 90 dias: anúncio que rodou poucos dias e parou = teste que falhou; que rodou semanas = validado; página desativada = risco de política. Comparar com o mesmo operador em outros países.

**Reincidência 06/10:** dei nota 9 ao Elástico sem checar inativos; IT tinha 2 operadores que testaram e largaram. Usuário: "então nenhuma nota 9 hoje, parabéns". REGRA: nota 9 só sai DEPOIS de active_status=all nos países-alvo E nos vizinhos (IT antecipa FR). Sem isso, a nota máxima é "8 provisório".
