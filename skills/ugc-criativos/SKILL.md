---
name: ugc-criativos
description: Monta CTVs/UGC de info-produto (crochê Natal FR/IT/DE, crochê casa FR/DE e ofertas parecidas) no formato VALIDADO em out/2026 — abertura de b-roll já narrada com a apresentadora recortada apontando + faixa vermelha, ela entra, capa, fichas, câmera guiada na ficha, filmagens do material, seta no CTA, efeitos sonoros. Gera as falas no HeyGen pelo Chrome. Use quando o usuário pedir "faz mais CTV", "criativo UGC", "variação do vencedor", "gera no HeyGen", "CTV pra França/Itália/Alemanha".
---

# UGC criativos — pipeline validado (10/10/2026)

Vendas que validaram (10/10): Natal FR 34 > Maison FR 17 > MEGA PACK 15 = Natal IT 15 > Häkelideen DE 12.
Entregar SEMPRE **sem legenda e sem música** (o usuário põe no CapCut), a não ser que ele peça.

## Formato que vende (não mudar sem pedir)
1. **0–3/7 s — gancho**: b-roll em tela cheia trocando a cada 1,2–2 s, a VOZ dela já narrando, **ela recortada (rembg) no canto inferior apontando pro b-roll** (PIP) + **faixa** no topo: 2 linhas pretas em placa branca + linha vermelha "100% AU CROCHET / ALL'UNCINETTO / GEHÄKELT".
   - O usuário reprovou: curto sem apresentadora (muito rápido), abrir sem a mulher (V9). Ele aprovou: timelapse da mesa sendo montada (tm_luiza acelerado) e enfeites de árvore / bonecos de neve espiral.
   - Faixa nunca cobre o rosto: topo (y=230) no b-roll; se ela estiver inteira na tela, descer pra y=1250 (HOOKTXT2).
2. Ela em tela cheia → b-roll casado com cada palavra (paniers→cestos, tapis→tapetes, coussins→ficha almofada…).
3. **Capa** com flash branco → 4–7 **fichas** trocando no ritmo dos nomes falados.
4. **Câmera guiada** (fpush.py) numa ficha real: Matériel → Couleurs → Étapes, moldura vermelha + pop.
5. Filmagens reais do material no idioma: PDF no celular, notebook, folhas impressas.
6. CTA com **seta vermelha** quicando + SFX.
SFX (sfx.py): pop na abertura, whoosh nos cortes, flash da capa, pops nas molduras, seta; Natal ganha **sino** ('bell'/'bell2') e **guizo** ('jingle').

## Pastas e arquivos (PC principal)
- Scripts: `Desktop\UGC CROCHE NATAL\_src_edicao\` (cópia em `scripts/` desta skill). `compose.py <config>` monta; `sfx.py <config>` grava `*_SFX.mp4`.
- Trabalho/temporários: `C:\tmp\ugcn\` (ROOT). B-roll normalizado 1080x1920/25fps em `C:\tmp\ugcn\src\` (backup no Google Drive `G:\Meu Drive\_ugc-kit\src`). Recortes rembg em `C:\tmp\ugcn\cut\<nome>\%04d.png`.
- B-roll Natal: tm_* (mesas postas), tk_mario/tk_igru/tk_snow (enfeites/amigurumi/bonecos de neve espiral — tk_snow só tem 10 s!), tt2/tt3 (caixa de amigurumis). Casa: cs_ayara (sousplats verdes), cs_neri (tapetes), cs_wow (cestos rosa), cs_eleno (caixas), cs_usec (cesto cinza/lã grossa). Material: img3008/3012/3013 (FR Natal), it3018/3020/3021 (IT), de2954/2955/2958 (DE casa), fr2951/2952/2953 (FR casa).
- Finais: `Desktop\UGC CROCHE NATAL\{FR,IT,DE}\3-final`, `Desktop\UGC CROCHE CASA DE\3-final`, `Desktop\UGC CROCHE CASA FR\3-final`.
- Fichas Natal: `Desktop\CROCHE NATAL {FRANÇA,ITALIA,ALEMANHA}\<módulo>\Model*_NN.png`. Casa: páginas `CRIATIVOS CROCHE EUROPA\CROCHE {FRANÇA,ALEMANHA}\_quellen\out_{fr,de}\main\pNNN.png` (config usa `FICHA_DIR`).

## Como fazer um CTV novo
1. Ver na Ad Library qual ângulo novo usar (BR "crochê natal" vídeo por impressões; país-alvo idem). Página do usuário na FR = "Helena González" (não é concorrente).
2. Roteiro na estrutura acima (FR "vous", DE "du", IT "voi"). CTA: "touchez En savoir plus juste en dessous" / "tipp unten auf Mehr dazu" / "tocca Scopri di più".
3. **HeyGen** (conta do usuário, Chrome logado): `app.heygen.com/home/photo-to-video` ("Cena única"), avatar **"Croche Natal"**.
   - Looks: parede cinza apontando (neutro), 2× "in green crochet" (sala clara, apontando — crochê casa), mesa posta, sofá, novelo ("with festive crafts"), em pé na mesa, guirlanda… Pra PIP precisa de look **apontando**.
   - Voz: Chloe (FR), Linda Fiore (IT), Susi (DE). Trocar em "Trocar voz" → "Definir padrão" (vira padrão do avatar).
   - **Resolução volta sozinha pra 720p — conferir 1080p.**
   - Texto: a caixa é textarea React. NÃO clicar no placeholder (abre modal "Gravar Áudio" que empilha). Preencher via JS: `Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype,'value').set.call(el,t); el.dispatchEvent(new Event('input',{bubbles:true}))`.
   - Look novo: avatar → "Adicionar visuais" → "Criar com IA" → descrever a edição (manter rosto/regata/pose apontando; "No Christmas decorations" se for casa). Sai em ~20 s, 2 variações.
   - Baixar: abrir o vídeo em Projetos, pegar `video.currentSrc` → trocar `720x1280_nocap` por `1080x1920_nocap` e baixar com curl. Se o src for `files2.heygen.ai` assinado, baixar via `fetch(src)→blob→<a download>` na página.
4. Transcrever com faster-whisper (decodificar com ffmpeg pra wav 16k e passar numpy; passar o path direto dá erro) → tempos de cada palavra.
5. Recortar ela pro PIP: `python cut2.py <primeiros_segundos.mp4> C:/tmp/ugcn/cut/<nome> u2net` (u2net + threshold; u2net_human_seg pega o sofá junto). Parede lisa: cut.py serve.
6. Criar config em compose.py (copiar `de1`/`frc1` pro formato PIP, `v11`/`v12`/`it5`/`it6` pros Natal): `MESA` = clipe(s) HeyGen (concatenar com ffmpeg se forem 2), `M` = lista (tempo, tipo, args) com tipos `broll`, `aroll`(zoom), `cover`, `ficha`, `clip`(fpush), `speed`(timelapse); `HOOKTXT`/`HOOKTXT2`, `PIP=(pasta, t0, t1, 1250[, 'L'])`, `ARROW`.
7. Adicionar a lista de SFX em sfx.py (`PTS['NOME']` + caminho em `VIDS` + chave no seletor) e rodar `python compose.py X && python sfx.py X`.
8. **Conferir**: grade de frames (ffmpeg select+tile) e `freezedetect=n=0.0005:d=0.6` — b-roll curto com ss+duração além do fim CONGELA (aconteceu com tk_snow).
9. fpush preset novo: medir as caixas da ficha com grade (PIL) e adicionar `CAM`/`HL` em fpush.py (presets existentes: 11, 23, 24, 31, 53 Natal; de54 casa — páginas FR/DE casa têm a mesma numeração).

## Outro PC — o que precisa além desta skill
- `winget install Gyan.FFmpeg yt-dlp.yt-dlp` ; `pip install faster-whisper rembg onnxruntime opencv-python pillow numpy`
- Copiar `G:\Meu Drive\_ugc-kit\src` → `C:\tmp\ugcn\src` (b-roll) e os `*.words.json`; os scripts usam caminhos fixos `C:/tmp/ugcn` e `C:/Users/User/Desktop/...` — se o usuário do Windows tiver outro nome, ajustar `DESK`/`ROOT` no topo de compose.py e sfx.py.
- Extensão Claude in Chrome + HeyGen logado no Chrome.
