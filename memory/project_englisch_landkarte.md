---
name: project-englisch-landkarte
description: "Mapa mental de inglês p/ Alemanha — usuário já tem mapas PT-BR (marca d'água \"ACERVO EDUCATIVO\"); tradução direta na imagem via Python (inpaint + Ink Free) funcionou no teste 06/10/2026"
metadata:
  node_type: memory
  type: project
  originSessionId: af1d7199-4dbf-49e7-b14f-b7692b599713
  modified: 2026-10-06T17:51:40.997Z
---

Escolhido 06/10/2026 como oferta de mapa mental: inglês para alemães (adulto geral, NÃO focar 50+). Concorrência DE só Sprachfluss-Karten (7d); FR tem academyaxon escalando. Ver [[project-varredura-europa-2026-10-06]].

Usuário JÁ TEM o material em PT-BR (ex.: Downloads\mapa_familia.webp, 1400×933, "Nível A1 · Mapa 12", marca d'água ACERVO EDUCATIVO = mesmo nome do "Acervo Educa" que anuncia na ES → confirmar direito de revenda e trocar marca).

Pipeline testado: `Desktop\PROJETOS\englisch-landkarte\traduz_mapa.py` — lista de caixas (coordenadas manuais) → máscara adaptativa + cv2.inpaint apaga o PT → escreve DE com Inkfree.ttf (stroke 1 ≥18px) e Segoe Script bold nos títulos, compressão horizontal até 0.80 antes de reduzir fonte. Resultado em englisch-landkarte\teste\mapa_familia_DE.png.

**Why:** reaproveitar material pronto evita regerar 300+ mapas no ChatGPT.
**How to apply:** gargalo é achar as coordenadas de cada mapa; p/ escalar, instalar OCR (easyocr/tesseract) p/ detectar caixas automático + revisão visual. Trocar referências BR (Bahia→Mallorca). Inglês fica igual, só muda a explicação PT→DE.

Marca d'água/marca da operação fora do país = **DIGITAL.PRIME** (usuário pediu 06/10; não usar ENGLISCH-LANDKARTE na marca d'água).

**Plano decidido 06/10/2026:** inglês DE é a oferta. Usuário vai mandar o material; traduzir só ~50 mapas p/ começar. Amanhã (07/10): terminar tradução + página de vendas + criativos + checkout. Antes, usuário quis ver concorrentes FR abertos (academyaxon "La Carte de l'Anglais", "Cartes de Fluidité").

**ALERTA 06/10 (busca com inativos, "Englisch-Mindmap" DE):** Alemanha JÁ FOI TESTADA e abandonada por 3 operadores:
- academyaxon ("Karin Meyer", 520 mapas A1-C2, ângulo "dein Englisch ist nur eingerostet") rodou só 30-31/ago (17h) e desligou — enquanto na FR segue 30d+.
- "Englisch Startklar / Sprachen Startklar" (+500 mapas ilustrados, 4 bônus) rodou 05-22/ago e parou.
- Sprachfluss-Karten: anúncio 17/jul-28/set de página DESATIVADA pela Meta por política; o atual (17 €) tem <100 impressões e restrição.
Leitura: DE vazio porque testaram e saíram, não por falta de ideia. FR é o mercado validado (academyaxon persistindo). Sempre checar active_status=all antes de chamar mercado de "vazio".
