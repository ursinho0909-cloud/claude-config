---
name: project-atividades-autismo-alemanha
description: "Atividades Autismo DE — pacote completo traduzido pro alemão em 25/09/2026 (Desktop\\AKTIVITAETEN-AUTISMUS-DE), clone da França; falta landing/checkout/pixel"
metadata:
  node_type: memory
  type: project
  originSessionId: 2fdc437a-d748-41ef-8a8d-8638f68c1d73
  modified: 2026-09-25T19:33:11.684Z
---

Clone alemão de [[project-atividades-autismo-franca]], decidido após varredura DE de 25/09 (ver [[project-atividades-autismo-it-de]]).

**Entregável:** `Desktop\AKTIVITAETEN-AUTISMUS-DE\` (mesma estrutura do ACTIVITES-TSA-FR):
- 1-HAUPTHEFT: Angepasste_Aktivitaeten_-_Autismus.pdf (98 págs)
- Aktivitaeten_Plus_-_Autismus.pdf (30 fichas 100–129)
- 2-BONUS: Urkunde, Quiz 30, Wochenplan, Bildkarten (4 PDFs)
- 3-ORDER-BUMPS: Ruhe-Kit (14p), Spiele (21p), 10 Berufe gegen die Angst (3p)

**Pipeline:** `Desktop\PROJETOS\aktivitaeten-tea-de\_trabalho\` — dicionários de.py (+de_plus.py p/ 100–129), deb.py, dej.py, dep.py, tr_vec_de.py; scripts batch/bbatch/jbatch/pbatch/vec.py saem de_*.png. As 30 extras usam como fonte as fichas FR (novas-30-fr/img) com OCR próprio.
- Convenções: "du" nas consignas ao kind, "Sie" nas instruções ao adulto; "Ziel:", "Anpassungen:", "Aktivität N".

**Landing (25/09, NÃO publicada — usuário pediu só salvar):** pasta aktivitaeten-tea-de\site\index.html em Desktop\PROJETOS — `Desktop\PROJETOSktivitaeten-tea-de\site\index.html` + assets gerados das páginas DE reais (site_build/mk_assets.py). Escada: Basis 9,90 (98 ativ.) / Plus 19,90 (128 + 4 boni) / Komplett 29,90 ★ (tudo + Ruhe-Kit, Spiele, Berufe). Claim honesto "128 Aktivitäten" (não +250).
**Falta:** 3 links de checkout (placeholders #TODO-CHECKOUT-*), pixel, e-mail suporte, dados do Impressum.

**Concorrência DE re-checada 01/10/2026:**
- autismusfoerderheft.com/page (Isabel Rodrigues + página "Flux Up" com a mesma copy, ~11 anúncios, desde 22/09): "Autismus Förderheft +120 Fertige Vorlagen PDF", TEACCH, p/ pais (autismo + fala), 29 € (de 39), bundle até 49,90 €, 14 dias garantia, alega "20.000 mães". = concorrente direto quase igual ao nosso (128 fichas).
- routine-cards.online/de (Therapy Toolkit, desde 28/09): 214 cartões de rotina ilustrados p/ autismo/TDAH/T21, 9 €, 7 bônus, 15 dias. Mesma oferta "Carte delle Routine" que tinha 63 anúncios na IT desde 07/09.
- ptp.abatools.pro/de (Therapy Toolkit, desde 26/08): +80 materiais p/ terapeuta infantil, 27 € (âncora 114 €), upsells 17–77 €. B2B.
Conclusão: DE deixou de ser vazio; preço de referência p/ pais 29 €. Diferencial possível: adaptações por ficha + 4 bônus + Rotina como bump.

**Landing 2 pacotes (01/10/2026, decisão do usuário):** site/index.html agora tem só Basis 17 € (98 ativ., sem boni; âncora 29 €) e Komplett 24 € ★ (128 ativ. + 4 boni; âncora 69 €; "Nur 7 € mehr"). Ruhe-Kit / Spiele / Berufe saíram da página → viram order bumps no checkout. Versão de 3 pacotes salva em aktivitaeten-tea-de\index_3pakete_backup.html. Preview local: `python -m http.server 8798` dentro de site\. Placeholders: #TODO-CHECKOUT-BASIS, #TODO-CHECKOUT-KOMPLETT, pixel, e-mail, Impressum.
**Gancho 250 (01/10, pedido do usuário "igual ES/FR"):** DE usa "+250 Übungen" (exercícios), não "+250 Aktivitäten" — amostra de 12 páginas deu ~4,5 exercícios/página (≈550 no total, ≈440 nas 98). Basis 17 € = "+150 Übungen in 98 Aktivitäten"; pacote de 24 € renomeado p/ **Premium** = "+250 Übungen in 128 Aktivitäten + 4 Boni". Banner do hero trocado p/ "+250 ÜBUNGEN · DRUCKFERTIG" (original em site_build\hero_128_orig.webp). Checkout placeholders: #TODO-CHECKOUT-BASIS / #TODO-CHECKOUT-PREMIUM.
**Imagem ChatGPT (01/10):** hero + card Premium agora usam a arte do usuário (Downloads\ChatGPT_Image_1_de_out._de_2026,_10_39_34.png → assets/hero.webp, hero-640.webp, premium.webp). Card Basis usa assets/basis.webp (leque de fichas antigo). Hero anterior em site_build\hero_250uebungen.webp. Arte tem defeitos a corrigir antes do ar: diz "+250 AKTIVITÄTEN" e "MIT ASS", caixa "Geschichten und Abfolgen" duplicada (com "mördeen"), e categorias que o material não tem (Hygiene, Sicherheit, Technologie).
**Igualado ao site PT (01/10):** estrutura segue atividades-adaptadas.pages.dev seção por seção (só a oferta é 2 pacotes). Adicionada seção "Was Sie erhalten" (assets/paket.webp = leque de fichas c/ faixa "+250 ÜBUNGEN"). Cards dos bônus agora são as capas-arte traduzidas como no PT/FR: script `_trabalho\site_bonus_de.py` (clone do site_bonus.py FR, fontes do ES em `_trabalho\site_img\`) gera rotina-de/quiz-de/cert-de; Bildkarten = topo de de_cart_01.png. Antigos em site_build\bonus_old\.
**Imagens (01/10, 2ª rodada):** card Premium = assets/oferta-premium.webp (ChatGPT_Image_..._10_57_57.png, mockup caixa 4:3); "Was Sie erhalten" = assets/erhalten.webp (= arte do hero). Bônus refeitos sem artefatos: site_bonus_de.py usa borracha seletiva no Wochenplan (mantém fita verde/selo/prancheta, preenche c/ fundo real) e bg creme explícito na Urkunde; Bildkarten = página inteira de de_cart_01 centralizada (site_img/karten-de.png). Mockup Premium tem defeitos: "ASS", "+250 Aktivitäten", caixas "Sicherheit"/"Technologie" e texto quebrado "TAUNRNO" em "Exklusive Boni".
**Vídeo do celular (01/10):** material.mp4 agora é rolagem contínua (igual FR): faixa `_trabalho\vid\strip_de.png` com 13 páginas (01,02,11,20,21,33,37,47,60,64,79,104,123) + 2 repetidas p/ loop sem pulo; `ffmpeg -loop 1 -framerate 30 -i strip_de.png -t P/115 -vf "crop=520:760:0:'mod(t*115,P)'"` crf 33 tune stillimage → 1,8 MB. Slideshow antigo em site_build\material_slides_old.mp4.
**Hotmart DE (01/10, em andamento):** modelo = FR (8548536): idioma "Português (Brasil)", país Brasil, eBook, Educacional, Euro, 7 dias, à vista, "Incluir impostos no preço" marcado, área de membros "Thiago Lima", impostos ESS (padrão), página de vendas = Marketplace automática. Arquivos de upload (<10 MB) em aktivitaeten-tea-de\_hotmart\upload (Arbeitsheft em 3 partes). Capas bumps vieram de Downloads\images (10).zip → _hotmart\capas.
- Premium 24 € = ID 8636164, enviado p/ aprovação.
Bumps FR reais (p/ copiar texto): +30 Jeux 8548606, Kit Calme 8548636, +50 Guides 8548684 (duplicatas 8548595/633/678 = rascunhos). FR checkout Y107666342V tem descrição do bump Jeux em ESPANHOL + "traduza pro frances" (erro no ar).
PDFs certos dos bumps "30 Spiele" e "50 Guides" não existem em DE; usuário vai trocar os arquivos depois (por ora Spiele DE + 10 Berufe).
- Bumps DE criados e enviados p/ aprovação (01/10): +30 Spiele zum Ausdrucken 7,90 € = 8636999 (PDF Spiele DE provisório) · Ruhe-Kit – Emotionale Regulation 9,90 € = 8637021 · +50 illustrierte Guides für unterwegs 11,90 € = 8637034 (PDF 10 Berufe PROVISÓRIO) · SUPERPACK: Alle 3 zum Preis von 1! 12,90 € = 8637050 (os 3 PDFs). Basis 17 € foi criado pelo usuário.
- **Checkouts DE publicados (01/10):** Premium 24 € = https://pay.hotmart.com/I107847425I?checkoutMode=10 (contador 15 min #f44747 "Countdown läuft" + banner + 4 bumps) · Basis 17 € (produto 8636239, criado pelo usuário) = https://pay.hotmart.com/Q107847551O?checkoutMode=10 (contador + 4 bumps, SEM banner). Bumps com descrição DE; Superpack com "De 29,70 €" (-57%). Links já plugados no site/index.html. Logo após publicar, contador/banner não apareciam no link público (bumps sim) — conferir propagação.
- **LIVE (01/10/2026):** https://aktivitaeten-autismus.pages.dev (CF Pages projeto aktivitaeten-autismus). Deploy: `npx wrangler pages deploy site --project-name aktivitaeten-autismus --branch main` a partir de Desktop\PROJETOS\aktivitaeten-tea-de. E-mail suporte = apoio@mundovisual.pt (igual FR/ES). Impressum só com "Mundo Visual + e-mail" — FALTA nome completo e endereço (§ 5 DDG). Pixel UTMify 6abe999d697775e0d49d371c LIVE (01/10, forma legível no head).
- **01/10 ajuste:** no mobile Basis aparece primeiro (removido order:-1), Premium segue destacado (selo/borda/botão verde). Outros CTAs (hero, meio, FAQ) rolam até o card Premium (#premium), NÃO vão ao checkout — só os botões dos 2 cards levam ao checkout. Cards sem "in 98/128 Aktivitäten" (só "Über 150/250 Übungen").
- **CTV impresso (01/10):** Desktop\AKTIVITAETEN-AUTISMUS-DE\CTV-AUTISMUS-DE.pdf (7 págs A4): capa ChatGPT_Image_..._14_51_12.png + de_125 (Straße/Ampel = "o do semáforo"), de_122 Klebepunkte, de_110 Finger zählen, de_52 Tierlaute, de_126 Freund spielen, de_62 Reihe fortsetzen. Obs: nº do arquivo de_N ≠ nº da Aktivität impressa.
