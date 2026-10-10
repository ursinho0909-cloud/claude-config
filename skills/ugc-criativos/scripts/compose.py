"""Monta o UGC Natal (modelo Carolina Gonçalves BR) para DE ou FR.
uso: python compose.py de|fr
Sem legenda e sem música (usuário coloca). Saída em Desktop/UGC CROCHE NATAL/<LANG>/3-final.
"""
import sys, os, subprocess, glob, json

LANG = sys.argv[1]
FR2_M = []
ARROW = None
W, H, FPS, T = 1080, 1920, 25, 0.22
ROOT = 'C:/tmp/ugcn'
TMP = f'{ROOT}/seg_{LANG}'
os.makedirs(TMP, exist_ok=True)
DESK = 'C:/Users/User/Desktop'
S = f'{ROOT}/src'

def dur(f):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))

if LANG == 'de':
    FOLDER = f'{DESK}/CROCHE NATAL ALEMANHA'
    COVER = f'{FOLDER}/_capa_DE.png'
    PAPER, PHONE, LAPTOP = f'{S}/img3010.mp4', f'{S}/img3014.mp4', f'{S}/img3011.mp4'
    HOOK, MESA, HOOKCUT, HOOK_END = f'{ROOT}/hook_de.mp4', f'{ROOT}/mesa_de.mp4', f'{ROOT}/cut/de', 3.45
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/DE/3-final'
    # tempos em segundos do clipe da mesa (m-time); cada item = (inicio, tipo, args)
    M = [
        (0.0, 'broll', (f'{S}/tt2.mp4', 1.4)),
        (2.2, 'broll', (f'{S}/tt2.mp4', 5.0)),
        (3.5, 'broll', (f'{S}/tt3.mp4', 0.2)),
        (5.0, 'broll', (f'{S}/tt3.mp4', 11.4)),
        (6.9, 'aroll', (1.0,)),
        (10.6, 'cover', ()),
        (13.1, 'ficha', ('11',)),
        (14.4, 'ficha', ('53',)),
        (15.6, 'ficha', ('31',)),
        (16.9, 'ficha', ('23',)),
        (17.8, 'ficha', ('22',)),
        (18.7, 'broll', (PAPER, 4.6)),
        (20.2, 'broll', (PHONE, 4.0)),
        (21.9, 'broll', (LAPTOP, 8.6)),
        (23.1, 'aroll', (1.12,)),
        (25.0, 'broll', (f'{S}/tt3.mp4', 18.5)),
        (26.6, 'aroll', (1.0,)),
        (28.4, 'aroll', (1.16,)),
        (30.2, 'aroll', (1.0,)),
        (31.9, 'aroll', (1.25,)),
    ]
elif LANG == 'fr2':
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/ref2_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR2_novelo.mp4'
    M = [
        (0.0, 'aroll', (1.0,)),
        (2.4, 'aroll', (1.14,)),
        (5.1, 'broll', (f'{S}/tt2.mp4', 1.4)),
        (6.8, 'broll', (f'{S}/tt2.mp4', 5.0)),
        (8.2, 'broll', (f'{S}/tt3.mp4', 0.2)),
        (9.9, 'broll', (f'{S}/tt3.mp4', 11.4)),
        (11.8, 'aroll', (1.0,)),
        (13.1, 'cover', ()),
        (16.0, 'ficha', ('23',)),
        (16.95, 'ficha', ('24',)),
        (17.94, 'ficha', ('22',)),
        (19.22, 'ficha', ('32',)),
        (20.14, 'ficha', ('21',)),
        (20.98, 'ficha', ('11',)),
        (22.08, 'ficha', ('51',)),
        (22.68, 'broll', (f'{S}/scroll_fr.mp4', 0.0)),
        (24.38, 'aroll', (1.14,)),
        (25.98, 'broll', (f'{S}/img3008.mp4', 4.6)),
        (28.68, 'broll', (f'{S}/img3013.mp4', 4.0)),
        (29.36, 'broll', (f'{S}/img3012.mp4', 10.0)),
        (31.6, 'broll', (f'{S}/img3008.mp4', 0.2)),
        (34.4, 'broll', (f'{S}/tt2.mp4', 7.2)),
        (36.38, 'aroll', (1.0,)),
        (38.9, 'broll', (f'{S}/tt3.mp4', 18.5)),
        (41.2, 'aroll', (1.0,)),
        (42.3, 'aroll', (1.18,)),
        (44.4, 'aroll', (1.3,)),
    ]
    ARROW = (42.3, 47.0)
elif LANG == 'fr2b':
    # FR2 novelo com o trecho do material refeito: câmera guiada na ficha real (fpush.py) + filmagens reais
    # sincronizadas palavra a palavra (PDF -> celular, imprimez -> papel, accès à vie -> notebook)
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/ref2_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR2B_material.mp4'
    M = [
        (0.0, 'aroll', (1.0,)),
        (2.4, 'aroll', (1.14,)),
        (5.1, 'broll', (f'{S}/tt2.mp4', 1.4)),
        (6.8, 'broll', (f'{S}/tt2.mp4', 5.0)),
        (8.2, 'broll', (f'{S}/tt3.mp4', 0.2)),
        (9.9, 'broll', (f'{S}/tt3.mp4', 11.4)),
        (11.8, 'aroll', (1.0,)),
        (13.1, 'cover', ()),
        (16.0, 'ficha', ('23',)),
        (16.95, 'ficha', ('24',)),
        (17.94, 'ficha', ('22',)),
        (19.22, 'ficha', ('32',)),
        (20.14, 'ficha', ('21',)),
        (20.98, 'ficha', ('11',)),
        (22.08, 'ficha', ('51',)),
        (22.68, 'broll', (f'{S}/scroll_fr.mp4', 0.0)),
        (24.38, 'aroll', (1.14,)),
        (25.98, 'clip', (f'{S}/fpush_fr24.mp4', 0.0)),
        (31.6, 'broll', (f'{S}/img3013.mp4', 4.0)),
        (32.92, 'broll', (f'{S}/img3008.mp4', 4.6)),
        (34.72, 'broll', (f'{S}/img3012.mp4', 10.0)),
        (36.38, 'aroll', (1.0,)),
        (38.9, 'broll', (f'{S}/tt3.mp4', 18.5)),
        (41.2, 'aroll', (1.0,)),
        (42.3, 'aroll', (1.18,)),
        (44.4, 'aroll', (1.3,)),
    ]
    ARROW = (42.3, 47.0)
elif LANG == 'v6':
    # V6 "La couronne" (modelo O Mapa do Aprovado BR): porta c/ guirlanda -> enfeite -> sofá.
    # MESA = c1_porta (0-7.2) + c2_enfeite (7.2-13.2) + c3_sofa (13.2-53.25), concatenados em v6_fr.mp4
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v6_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR6_couronne.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/FR/v6_couronne/hook_text.png', 1080, 0.0, 3.2)
    M = [
        (0.0, 'aroll', (1.0,)),
        (3.26, 'aroll', (1.12,)),     # "que je viens de terminer"
        (5.66, 'aroll', (1.0,)),      # "elle est vraiment magnifique"
        (7.2, 'aroll', (1.0,)),       # enfeite
        (11.16, 'aroll', (1.15,)),    # "Regardez… un vrai charme"
        (13.2, 'aroll', (1.0,)),      # sofá
        (18.22, 'aroll', (1.12,)),    # "Alors j'ai trouvé"
        (19.26, 'cover', ()),         # "une collection de plus de 100 modèles"
        (22.52, 'aroll', (1.0,)),     # "et j'ai choisi"
        (25.06, 'ficha', ('51',)),    # couronnes
        (25.90, 'ficha', ('31',)),    # décorations pour le sapin
        (27.62, 'ficha', ('11',)),    # sets de table
        (28.88, 'ficha', ('23',)),    # amigurumis
        (30.04, 'ficha', ('41',)),    # petits cadeaux
        (31.30, 'broll', (f'{S}/scroll_fr.mp4', 0.0)),  # "il y a vraiment de tout"
        (32.90, 'aroll', (1.14,)),    # "Et le mieux"
        (34.29, 'clip', (f'{S}/fpush_fr53.mp4', 0.0)),  # matériel 36.04 / couleurs 37.04 / étapes 37.94
        (39.62, 'aroll', (1.0,)),     # "Plus besoin de chercher"
        (41.72, 'broll', (f'{S}/img3013.mp4', 4.0)),    # "Tout est en PDF"
        (43.90, 'broll', (f'{S}/img3012.mp4', 10.0)),   # "l'accès est à vie"
        (45.48, 'aroll', (1.0,)),     # "Si vous aussi"
        (46.64, 'broll', (f'{S}/tt3.mp4', 18.5)),       # "jolies décorations de Noël"
        (49.68, 'aroll', (1.18,)),    # "touchez En savoir plus"
    ]
    ARROW = (49.68, 53.2)
elif LANG == 'v7':
    # V7: gancho do criativo 05 (ref2_fr 0-11.5) + corpo do sofá da V6 (c3_sofa 5.30-40.0, offset +6.2) em v7_fr.mp4
    # b-roll do TikTok (tk_*.mp4) no gancho e no "il y a vraiment de tout"; câmera na ficha Père Noël (fpush preset 23)
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v7_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR7_hook05.mp4'
    M = [
        (0.0, 'aroll', (1.0,)),
        (2.4, 'aroll', (1.14,)),
        (5.1, 'broll', (f'{S}/tk_mario.mp4', 6.0)),    # "les décorations au crochet"
        (6.8, 'broll', (f'{S}/tk_igru.mp4', 2.0)),
        (8.2, 'broll', (f'{S}/tk_snow.mp4', 7.0)),     # "ce cadeau fait main"
        (9.9, 'broll', (f'{S}/tk_igru.mp4', 10.0)),
        (11.5, 'aroll', (1.0,)),      # sofá: "j'ai trouvé"
        (12.26, 'cover', ()),         # "une collection de plus de 100 modèles"
        (15.52, 'aroll', (1.12,)),    # "et j'ai choisi"
        (18.06, 'ficha', ('53',)),    # couronnes (Couronne de l'Avent)
        (18.90, 'ficha', ('33',)),    # sapin
        (20.62, 'ficha', ('13',)),    # sets de table
        (21.88, 'ficha', ('21',)),    # amigurumis
        (23.04, 'ficha', ('44',)),    # petits cadeaux
        (24.30, 'broll', (f'{S}/tk_mario.mp4', 15.0)), # "il y a vraiment de tout"
        (25.90, 'aroll', (1.14,)),    # "Et le mieux"
        (27.29, 'clip', (f'{S}/fpush_fr23.mp4', 0.0)), # matériel 29.04 / couleurs 30.04 / étapes 30.94
        (32.62, 'aroll', (1.0,)),     # "Plus besoin de chercher"
        (34.72, 'broll', (f'{S}/img3013.mp4', 4.0)),   # "Tout est en PDF"
        (36.90, 'broll', (f'{S}/img3012.mp4', 10.0)),  # "l'accès est à vie"
        (38.48, 'aroll', (1.0,)),     # "Si vous aussi"
        (39.64, 'broll', (f'{S}/tk_igru.mp4', 12.5)),  # "jolies décorations de Noël"
        (42.68, 'aroll', (1.18,)),    # "touchez En savoir plus"
    ]
    ARROW = (42.68, 46.2)
elif LANG == 'v8':
    # V8 = V7 com foco em MESA POSTA: b-roll de mesas natalinas do TikTok (tm_*.mp4) no gancho/"il y a de tout"/CTA,
    # ficha e câmera guiada no Set de table rond (fpush preset 11)
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v7_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR8_mesa.mp4'
    M = [
        (0.0, 'aroll', (1.0,)),
        (2.4, 'aroll', (1.14,)),
        (5.1, 'broll', (f'{S}/tm_casinha.mp4', 19.0)),  # "les décorations au crochet" (mesa com bolo)
        (6.8, 'broll', (f'{S}/tm_jessi.mp4', 31.0)),    # mão colocando a xícara no sousplat
        (8.2, 'broll', (f'{S}/tm_aless.mp4', 36.0)),    # "ce cadeau fait main" (sousplats)
        (9.9, 'broll', (f'{S}/tm_jessi.mp4', 50.0)),    # xícara + garfo dourado
        (11.5, 'aroll', (1.0,)),      # sofá: "j'ai trouvé"
        (12.26, 'cover', ()),
        (15.52, 'aroll', (1.12,)),
        (18.06, 'ficha', ('53',)),    # couronnes
        (18.90, 'ficha', ('33',)),    # sapin
        (20.62, 'ficha', ('11',)),    # sets de table
        (21.88, 'ficha', ('21',)),    # amigurumis
        (23.04, 'ficha', ('44',)),    # petits cadeaux
        (24.30, 'broll', (f'{S}/tm_casinha.mp4', 23.0)), # "il y a vraiment de tout"
        (25.90, 'aroll', (1.14,)),
        (27.29, 'clip', (f'{S}/fpush_fr11.mp4', 0.0)),  # matériel / couleurs / étapes no Set de table
        (32.62, 'aroll', (1.0,)),
        (34.72, 'broll', (f'{S}/img3013.mp4', 4.0)),
        (36.90, 'broll', (f'{S}/img3012.mp4', 10.0)),
        (38.48, 'aroll', (1.0,)),
        (39.64, 'broll', (f'{S}/tm_luiza.mp4', 44.0)),  # "jolies décorations de Noël… pour votre maison" (mesa longa)
        (42.68, 'aroll', (1.18,)),
    ]
    ARROW = (42.68, 46.2)
elif LANG == 'v9':
    # V9 = V8 com gancho VISUAL novo: abre em mesa posta tela cheia (sem a apresentadora) + faixa de texto;
    # áudio do gancho do 05 vira narração. Ela só aparece no sofá ("j'ai trouvé").
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v7_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR9_mesa_hook.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/FR/v9_mesa/hook_text.png', 700, 0.0, 5.0)
    M = [
        (0.0, 'broll', (f'{S}/tm_luiza.mp4', 36.0)),    # mesa com velas
        (1.6, 'broll', (f'{S}/tm_casinha.mp4', 3.0)),   # mãos colocando o sousplat
        (3.3, 'broll', (f'{S}/tm_jessi.mp4', 40.0)),    # xícara no sousplat
        (5.1, 'broll', (f'{S}/tm_casinha.mp4', 27.0)),  # mesa com bolo
        (6.8, 'broll', (f'{S}/tm_aless.mp4', 36.0)),    # pilha de sousplats
        (8.2, 'broll', (f'{S}/tm_alana.mp4', 6.0)),     # close sousplat vermelho
        (9.9, 'broll', (f'{S}/tm_jessi.mp4', 50.0)),    # xícara + garfo dourado
        (11.5, 'aroll', (1.0,)),      # sofá: "j'ai trouvé"
        (12.26, 'cover', ()),
        (15.52, 'aroll', (1.12,)),
        (18.06, 'ficha', ('53',)),
        (18.90, 'ficha', ('33',)),
        (20.62, 'ficha', ('11',)),
        (21.88, 'ficha', ('21',)),
        (23.04, 'ficha', ('44',)),
        (24.30, 'broll', (f'{S}/tm_aless.mp4', 44.0)),  # "il y a vraiment de tout"
        (25.90, 'aroll', (1.14,)),
        (27.29, 'clip', (f'{S}/fpush_fr11.mp4', 0.0)),
        (32.62, 'aroll', (1.0,)),
        (34.72, 'broll', (f'{S}/img3013.mp4', 4.0)),
        (36.90, 'broll', (f'{S}/img3012.mp4', 10.0)),
        (38.48, 'aroll', (1.0,)),
        (39.64, 'broll', (f'{S}/tm_luiza.mp4', 44.0)),
        (42.68, 'aroll', (1.18,)),
    ]
    ARROW = (42.68, 46.2)
elif LANG == 'v10':
    # V10: gancho NOVO na HeyGen (ela sentada na mesa posta, hook_mesa_fr 0-5.655) + ref2_fr 5.0-11.5 + c3_sofa 5.30-40.0
    # = v10_fr.mp4. Corpo = V8 deslocado +0.655 s.
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v10_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR10_table.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/FR/v9_mesa/hook_text_v10.png', 1250, 0.0, 4.4)
    D = 0.655
    M = [
        (0.0, 'aroll', (1.0,)),
        (2.94, 'aroll', (1.12,)),     # "que j'ai préparée cette année"
        (4.50, 'aroll', (1.0,)),      # "tout est au crochet !"
        (5.655, 'broll', (f'{S}/tm_casinha.mp4', 19.0)),  # "les décorations au crochet"
        (6.8 + D, 'broll', (f'{S}/tm_jessi.mp4', 31.0)),
        (8.2 + D, 'broll', (f'{S}/tm_aless.mp4', 36.0)),
        (9.9 + D, 'broll', (f'{S}/tm_jessi.mp4', 50.0)),
        (11.5 + D, 'aroll', (1.0,)),
        (12.26 + D, 'cover', ()),
        (15.52 + D, 'aroll', (1.12,)),
        (18.06 + D, 'ficha', ('53',)),
        (18.90 + D, 'ficha', ('33',)),
        (20.62 + D, 'ficha', ('11',)),
        (21.88 + D, 'ficha', ('21',)),
        (23.04 + D, 'ficha', ('44',)),
        (24.30 + D, 'broll', (f'{S}/tm_casinha.mp4', 23.0)),
        (25.90 + D, 'aroll', (1.14,)),
        (27.29 + D, 'clip', (f'{S}/fpush_fr11.mp4', 0.0)),
        (32.62 + D, 'aroll', (1.0,)),
        (34.72 + D, 'broll', (f'{S}/img3013.mp4', 4.0)),
        (36.90 + D, 'broll', (f'{S}/img3012.mp4', 10.0)),
        (38.48 + D, 'aroll', (1.0,)),
        (39.64 + D, 'broll', (f'{S}/tm_luiza.mp4', 44.0)),
        (42.68 + D, 'aroll', (1.18,)),
    ]
    ARROW = (42.68 + D, 46.9)
elif LANG == 'v11':
    # V11 = CTV01 10/10: abre com TIMELAPSE da mesa sendo montada (tm_luiza 1-45.5 acelerado) com a voz dela narrando
    # o gancho da V10 + faixa vermelha; ela entra em "que j'ai préparée cette année". Corpo = V10 c/ b-roll TikTok (tk_*).
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v10_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR11_CTV01_timelapse.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/FR/v9_mesa/hook_text_v10.png', 230, 0.0, 2.94)
    HOOKTXT2 = (f'{DESK}/UGC CROCHE NATAL/FR/v9_mesa/hook_text_v10.png', 1250, 2.94, 5.0)
    D = 0.655
    M = [
        (0.0, 'speed', (f'{S}/tm_luiza.mp4', 1.0, 45.5)),  # timelapse mesa vazia -> mesa posta
        (2.94, 'aroll', (1.0,)),      # ela entra: "que j'ai préparée cette année"
        (4.50, 'aroll', (1.12,)),     # "tout est au crochet !"
        (5.655, 'broll', (f'{S}/tk_mario.mp4', 8.0)),     # "les décorations au crochet"
        (6.8 + D, 'broll', (f'{S}/tk_igru.mp4', 2.0)),
        (8.2 + D, 'broll', (f'{S}/tk_snow.mp4', 7.0)),    # "ce cadeau fait main"
        (9.9 + D, 'broll', (f'{S}/tt3.mp4', 10.0)),
        (11.5 + D, 'aroll', (1.0,)),
        (12.26 + D, 'cover', ()),
        (15.52 + D, 'aroll', (1.12,)),
        (18.06 + D, 'ficha', ('53',)),
        (18.90 + D, 'ficha', ('33',)),
        (20.62 + D, 'ficha', ('11',)),
        (21.88 + D, 'ficha', ('21',)),
        (23.04 + D, 'ficha', ('44',)),
        (24.30 + D, 'broll', (f'{S}/tm_casinha.mp4', 23.0)),
        (25.90 + D, 'aroll', (1.14,)),
        (27.29 + D, 'clip', (f'{S}/fpush_fr11.mp4', 0.0)),
        (32.62 + D, 'aroll', (1.0,)),
        (34.72 + D, 'broll', (f'{S}/img3013.mp4', 4.0)),
        (36.90 + D, 'broll', (f'{S}/img3012.mp4', 10.0)),
        (38.48 + D, 'aroll', (1.0,)),
        (39.64 + D, 'broll', (f'{S}/tm_luiza.mp4', 44.0)),
        (42.68 + D, 'aroll', (1.18,)),
    ]
    ARROW = (42.68 + D, 46.9)
elif LANG == 'v12':
    # V12 = CTV02 10/10: abre com ENFEITES DE ÁRVORE (tk_mario) narrado pelo gancho do 05 + faixa "décos de mon sapin";
    # ela (look novelo) entra em "vous pouvez commencer". Corpo = V7 (sofá), fichas de sapin, câmera guiada na Étoile (fpush 31).
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{ROOT}/src/capa_fr.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v7_fr.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    OUTNAME = 'UGC_NATAL_FR12_CTV02_sapin.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/FR/v12_sapin/hook_text_v12.png', 230, 0.0, 2.4)
    HOOKTXT2 = (f'{DESK}/UGC CROCHE NATAL/FR/v12_sapin/hook_text_v12.png', 1250, 2.4, 5.1)
    M = [
        (0.0, 'broll', (f'{S}/tk_mario.mp4', 8.0)),    # enfeite ursinho na árvore
        (1.2, 'broll', (f'{S}/tk_mario.mp4', 17.5)),   # sininhos dourados
        (2.4, 'aroll', (1.0,)),       # ela entra: "vous pouvez commencer à faire"
        (3.64, 'aroll', (1.14,)),     # "dès maintenant pour Noël"
        (5.1, 'broll', (f'{S}/tk_snow.mp4', 0.0)),     # "les décorations au crochet" (espirais penduradas)
        (6.6, 'broll', (f'{S}/tk_snow.mp4', 6.5)),
        (8.2, 'broll', (f'{S}/tt3.mp4', 0.5)),         # "ce cadeau fait main" (caixa de presente)
        (9.9, 'broll', (f'{S}/tk_igru.mp4', 10.0)),
        (11.5, 'aroll', (1.0,)),
        (12.26, 'cover', ()),
        (15.52, 'aroll', (1.12,)),
        (18.06, 'ficha', ('53',)),    # couronnes
        (18.90, 'ficha', ('36',)),    # sapin
        (20.62, 'ficha', ('12',)),    # sets de table
        (21.88, 'ficha', ('22',)),    # amigurumis
        (23.04, 'ficha', ('45',)),    # petits cadeaux
        (24.30, 'broll', (f'{S}/tk_mario.mp4', 21.0)), # "il y a vraiment de tout" (meia/luva)
        (25.90, 'aroll', (1.14,)),
        (27.29, 'clip', (f'{S}/fpush_fr31.mp4', 0.0)), # matériel / couleurs / étapes na Étoile
        (32.62, 'aroll', (1.0,)),
        (34.72, 'broll', (f'{S}/img3013.mp4', 4.0)),
        (36.90, 'broll', (f'{S}/img3012.mp4', 10.0)),
        (38.48, 'aroll', (1.0,)),
        (39.64, 'broll', (f'{S}/tk_snow.mp4', 6.6)),   # "jolies décorations de Noël"
        (42.68, 'aroll', (1.18,)),
    ]
    ARROW = (42.68, 46.2)
elif LANG == 'it5':
    # IT5 = CTV01 IT 10/10: timelapse da mesa (tm_luiza acelerado) narrado pelo gancho IT3 + faixa no topo; ela entra em
    # "che ho preparato quest'anno" e a faixa desce. Corpo = IT3 c/ b-roll TikTok (tk_*) no lugar das mesas.
    FOLDER = f'{DESK}/CROCHE NATAL ITALIA'
    COVER = f'{FOLDER}/_capa_IT.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v3_it.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/IT/3-final'
    OUTNAME = 'UGC_NATAL_IT5_CTV01_timelapse.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/IT/v5_v6/hook_text_it5.png', 230, 0.0, 3.2)
    HOOKTXT2 = (f'{DESK}/UGC CROCHE NATAL/IT/v5_v6/hook_text_it5.png', 1250, 3.2, 6.35)
    M = [
        (0.0, 'speed', (f'{S}/tm_luiza.mp4', 1.0, 45.5)),
        (3.2, 'aroll', (1.0,)),       # ela entra: "che ho preparato quest'anno"
        (4.9, 'aroll', (1.12,)),      # "è tutta all'uncinetto!"
        (6.35, 'broll', (f'{S}/tk_mario.mp4', 8.0)),   # "le decorazioni all'uncinetto"
        (8.45, 'broll', (f'{S}/tk_igru.mp4', 2.0)),
        (10.45, 'broll', (f'{S}/tt3.mp4', 0.5)),       # "quel regalo fatto a mano"
        (12.45, 'broll', (f'{S}/tk_igru.mp4', 10.0)),
        (14.85, 'aroll', (1.0,)),
        (16.1, 'cover', ()),
        (19.75, 'ficha', ('23',)),
        (20.85, 'ficha', ('24',)),
        (21.65, 'ficha', ('22',)),
        (22.95, 'ficha', ('32',)),
        (23.45, 'ficha', ('21',)),
        (24.65, 'ficha', ('11',)),
        (25.65, 'ficha', ('51',)),
        (26.4, 'broll', (f'{S}/tm_aless.mp4', 44.0)),
        (28.55, 'aroll', (1.14,)),
        (29.85, 'clip', (f'{S}/fpush_it11.mp4', 0.0)),
        (35.5, 'broll', (f'{S}/it3021.mp4', 4.0)),
        (37.7, 'broll', (f'{S}/it3018.mp4', 7.0)),
        (39.6, 'aroll', (1.0,)),
        (42.1, 'broll', (f'{S}/tm_luiza.mp4', 44.0)),
        (45.4, 'broll', (f'{S}/tm_casinha.mp4', 23.0)),
        (48.25, 'aroll', (1.18,)),
    ]
    ARROW = (48.25, 51.76)
elif LANG == 'it6':
    # IT6 = CTV02 IT 10/10: abre com os BONECOS DE NEVE ESPIRAL (tk_snow) narrado pelo gancho do 05 IT + faixa nova;
    # ela (novelo) entra em "cosa potete iniziare". Corpo = IT4, fichas de árvore, câmera guiada na Stella (fpush_it31).
    FOLDER = f'{DESK}/CROCHE NATAL ITALIA'
    COVER = f'{FOLDER}/_capa_IT.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v4_it.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/IT/3-final'
    OUTNAME = 'UGC_NATAL_IT6_CTV02_albero.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/IT/v5_v6/hook_text_it6.png', 230, 0.0, 3.1)
    HOOKTXT2 = (f'{DESK}/UGC CROCHE NATAL/IT/v5_v6/hook_text_it6.png', 1250, 3.1, 6.6)
    M = [
        (0.0, 'broll', (f'{S}/tk_snow.mp4', 0.0)),     # bonecos de neve espiral pendurados
        (1.6, 'broll', (f'{S}/tk_snow.mp4', 2.0)),     # bordando o rostinho
        (3.1, 'aroll', (1.0,)),       # ela entra: "cosa potete iniziare a fare"
        (4.94, 'aroll', (1.14,)),     # "per questo Natale"
        (6.6, 'broll', (f'{S}/tk_mario.mp4', 8.0)),    # "le decorazioni all'uncinetto"
        (8.6, 'broll', (f'{S}/tk_mario.mp4', 17.5)),   # "bellissime per la casa"
        (10.6, 'broll', (f'{S}/tt3.mp4', 0.5)),        # "quel regalo fatto a mano" (caixa)
        (12.6, 'broll', (f'{S}/tk_igru.mp4', 10.0)),   # "che tutti adorano ricevere"
        (14.8, 'aroll', (1.0,)),
        (18.75, 'cover', ()),
        (20.5, 'ficha', ('12',)),     # tovagliette
        (21.45, 'ficha', ('53',)),    # decorazioni per la tavola
        (23.0, 'ficha', ('36',)),     # albero
        (24.2, 'ficha', ('22',)),     # amigurumi
        (24.95, 'clip', (f'{S}/fpush_it31.mp4', 0.0)), # materiali / colori / spiegazioni na Stella
        (29.75, 'aroll', (1.14,)),
        (30.85, 'broll', (f'{S}/tk_snow.mp4', 6.6)),   # "pezzi come questi"
        (32.6, 'aroll', (1.0,)),
        (33.8, 'aroll', (1.18,)),
    ]
    ARROW = (33.8, 37.8)
elif LANG == 'de1':
    # CROCHÊ CASA DE · vídeo 1 (formato CTV01): b-roll de mesa c/ sousplats verdes narrado + faixa; ela (parede cinza) entra
    # em "was ihr jetzt"; páginas do PDF DE (FICHA_DIR) e câmera guiada no Kissen (fpush_de54); filmagens reais do material DE.
    FOLDER = f'{DESK}/CRIATIVOS CROCHE EUROPA/CROCHE ALEMANHA'
    FICHA_DIR = f'{FOLDER}/_quellen/out_de/main'
    COVER = f'{FOLDER}/capa_100_receitas_croche_casa_alemao_1x1.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/de1_parede.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE CASA DE/3-final'
    OUTNAME = 'UGC_CASA_DE1_parede.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE CASA DE/hook_text_de1.png', 230, 0.0, 5.02)
    PIP = (f'{ROOT}/cut/de1', 0.0, 5.02, 1250)   # ela recortada apontando pro b-roll do gancho
    M = [
        (0.0, 'broll', (f'{S}/cs_ayara.mp4', 0.0)),     # "Liebe Häklerinnen, schaut mal" (mesa c/ sousplats verdes)
        (2.26, 'broll', (f'{S}/cs_neri.mp4', 6.0)),     # "was ihr jetzt für euer Zuhause"
        (3.62, 'broll', (f'{S}/cs_usec.mp4', 3.0)),     # "häkeln könnt"
        (5.02, 'broll', (f'{S}/cs_wow.mp4', 0.0)),      # Körbe
        (5.86, 'broll', (f'{S}/cs_neri.mp4', 12.0)),    # Teppiche
        (6.76, 'ficha', ('054',)),    # Kissen
        (7.6, 'broll', (f'{S}/cs_ayara.mp4', 8.0)),     # Untersetzer
        (8.94, 'aroll', (1.0,)),      # "selbstgemachte Deko"
        (11.12, 'aroll', (1.14,)),    # "sofort gemütlicher"
        (12.76, 'broll', (f'{S}/cs_eleno.mp4', 14.0)),  # "das schönste Geschenk"
        (15.02, 'aroll', (1.0,)),     # "Ich habe eine Sammlung"
        (16.32, 'cover', ()),         # "mit über 100 Häkelanleitungen"
        (20.76, 'ficha', ('078',)),   # Wohnzimmer
        (22.3, 'ficha', ('003',)),    # Küche
        (23.24, 'ficha', ('055',)),   # Bad
        (24.3, 'ficha', ('079',)),    # Schlafzimmer
        (25.6, 'broll', (f'{S}/de2955.mp4', 4.0)),      # "wirklich alles dabei"
        (27.02, 'aroll', (1.14,)),    # "Und das Beste"
        (28.88, 'clip', (f'{S}/fpush_de54.mp4', 0.0)),  # Material 30.58 / Farben 31.73 / Schritte 32.48
        (34.56, 'aroll', (1.0,)),     # "Kein langes Suchen mehr"
        (36.86, 'broll', (f'{S}/de2954.mp4', 4.0)),     # PDF, Handy
        (39.9, 'broll', (f'{S}/de2958.mp4', 0.5)),      # Tablet
        (40.92, 'broll', (f'{S}/de2955.mp4', 0.5)),     # ausgedruckt
        (43.02, 'aroll', (1.0,)),     # "Zugang ist für immer"
        (45.36, 'broll', (f'{S}/cs_usec.mp4', 8.0)),    # "dein Zuhause dieses Jahr"
        (48.1, 'aroll', (1.0,)),
        (51.18, 'aroll', (1.18,)),    # "tipp unten auf Mehr dazu"
    ]
    ARROW = (51.18, 53.48)
elif LANG == 'de2':
    # CROCHÊ CASA DE · vídeo 2 (formato CTV02): 2 cortes de b-roll narrados + faixa; gancho = clipe parede cinza (de2_gancho_par)
    # recortado apontando; corpo = clipe em pé na mesa. MESA = de2_gancho (0-11.12) + de2_mesa = de2_full.mp4
    FOLDER = f'{DESK}/CRIATIVOS CROCHE EUROPA/CROCHE ALEMANHA'
    FICHA_DIR = f'{FOLDER}/_quellen/out_de/main'
    COVER = f'{FOLDER}/capa_100_receitas_croche_casa_alemao_1x1.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/de2_full.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE CASA DE/3-final'
    OUTNAME = 'UGC_CASA_DE2_gemuetlich.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE CASA DE/hook_text_de2.png', 230, 0.0, 7.08)
    PIP = (f'{ROOT}/cut/de2', 0.0, 7.08, 1250)   # ela (parede cinza) recortada apontando pro b-roll do gancho
    G = 11.12
    M = [
        (0.0, 'broll', (f'{S}/cs_usec.mp4', 0.0)),      # lã grossa cinza ("Liebe Häklerinnen")
        (1.8, 'broll', (f'{S}/cs_wow.mp4', 3.0)),       # cestos rosa ("jetzt, wo es draußen kalt wird")
        (3.74, 'broll', (f'{S}/cs_eleno.mp4', 20.0)),   # "ist die beste Zeit"
        (5.5, 'broll', (f'{S}/cs_ayara.mp4', 0.0)),     # "das Zuhause gemütlich zu machen"
        (7.08, 'broll', (f'{S}/cs_neri.mp4', 12.0)),    # "am schönsten geht das"
        (8.5, 'broll', (f'{S}/cs_ayara.mp4', 4.0)),     # "mit Häkeldeko"
        (9.52, 'aroll', (1.0,)),      # "die man selbst gemacht hat"
        (G + 0.0, 'aroll', (1.0,)),   # mesa: "Ich habe eine Sammlung"
        (G + 1.54, 'cover', ()),      # "mit über 100 Häkelanleitungen"
        (G + 5.44, 'broll', (f'{S}/cs_neri.mp4', 16.0)),  # Teppiche
        (G + 7.24, 'broll', (f'{S}/cs_wow.mp4', 4.5)),    # Körbe
        (G + 9.16, 'ficha', ('054',)),  # Kissen
        (G + 10.9, 'ficha', ('002',)),  # Platzsets
        (G + 11.78, 'ficha', ('085',)), # Tischläufer
        (G + 12.92, 'broll', (f'{S}/cs_ayara.mp4', 10.0)),  # "schön gedeckten Tisch"
        (G + 14.96, 'aroll', (1.12,)),  # "Jede Anleitung"
        (G + 15.82, 'clip', (f'{S}/fpush_de54.mp4', 0.0)),  # Material / Farben / Runde
        (G + 21.5, 'broll', (f'{S}/de2954.mp4', 2.0)),    # PDF, Handy
        (G + 25.08, 'broll', (f'{S}/de2955.mp4', 2.0)),   # ausdrucken
        (G + 26.9, 'aroll', (1.0,)),    # "so oft du willst… für immer"
        (G + 30.58, 'broll', (f'{S}/cs_eleno.mp4', 14.0)),  # "dein Zuhause"
        (G + 32.74, 'aroll', (1.0,)),
        (G + 35.52, 'aroll', (1.18,)),  # "tipp unten auf Mehr dazu"
    ]
    ARROW = (G + 35.52, G + 38.0)
elif LANG == 'frc1':
    # CROCHÊ CASA FR · vídeo 1: look novo "sala clara" A (HeyGen Design com IA), gancho 0-4.08 = b-roll + ela recortada
    # apontando (PIP) + faixa; páginas do PDF FR, câmera guiada no Coussin (fpush_frc54), filmagens reais FR (fr2951-2953).
    FOLDER = f'{DESK}/CRIATIVOS CROCHE EUROPA/CROCHE FRANÇA'
    FICHA_DIR = f'{FOLDER}/_quellen/out_fr/main'
    COVER = f'{FOLDER}/capa_100_receitas_croche_casa_frances_1x1.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/fr1_sala.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE CASA FR/3-final'
    OUTNAME = 'UGC_CASA_FRC1_salon.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE CASA FR/hook_text_fr1.png', 230, 0.0, 4.08)
    PIP = (f'{ROOT}/cut/fr1', 0.0, 4.08, 1250)
    M = [
        (0.0, 'broll', (f'{S}/cs_ayara.mp4', 0.0)),     # "Amies crocheteuses"
        (1.44, 'broll', (f'{S}/cs_neri.mp4', 6.0)),     # "regardez ce que vous pouvez crocheter"
        (2.7, 'broll', (f'{S}/cs_usec.mp4', 3.0)),      # "pour votre maison"
        (4.08, 'broll', (f'{S}/cs_wow.mp4', 0.0)),      # paniers
        (4.82, 'broll', (f'{S}/cs_neri.mp4', 12.0)),    # tapis
        (5.36, 'ficha', ('054',)),    # coussins
        (5.82, 'broll', (f'{S}/cs_ayara.mp4', 8.0)),    # dessous de verre
        (6.88, 'aroll', (1.0,)),      # "la déco faite main"
        (9.46, 'aroll', (1.14,)),     # "et c'est aussi"
        (10.06, 'broll', (f'{S}/cs_eleno.mp4', 14.0)),  # "le plus beau des cadeaux"
        (11.48, 'aroll', (1.0,)),     # "J'ai trouvé"
        (12.5, 'cover', ()),          # "plus de 100 modèles"
        (15.5, 'ficha', ('078',)),    # salon
        (16.44, 'ficha', ('003',)),   # cuisine
        (17.16, 'ficha', ('055',)),   # salle de bain
        (17.86, 'ficha', ('079',)),   # chambre
        (18.7, 'broll', (f'{S}/fr2952.mp4', 4.0)),      # "il y a vraiment de tout"
        (20.26, 'aroll', (1.14,)),    # "Et le mieux"
        (21.18, 'clip', (f'{S}/fpush_frc54.mp4', 0.0)), # matériel 22.88 / couleurs 24.03 / étapes 24.78
        (26.28, 'aroll', (1.0,)),     # "Finis de chercher"
        (28.48, 'broll', (f'{S}/fr2953.mp4', 3.0)),     # PDF, téléphone
        (31.82, 'broll', (f'{S}/fr2951.mp4', 0.5)),     # tablette
        (32.76, 'broll', (f'{S}/fr2952.mp4', 1.0)),     # imprimé
        (35.16, 'aroll', (1.0,)),     # "l'accès est à vie"
        (36.9, 'broll', (f'{S}/cs_usec.mp4', 8.0)),     # "rendre votre maison plus belle"
        (39.18, 'aroll', (1.0,)),
        (40.78, 'aroll', (1.18,)),    # "touchez En savoir plus"
    ]
    ARROW = (40.78, 42.92)
elif LANG == 'frc2':
    # CROCHÊ CASA FR · vídeo 2: look novo "sala clara" B, gancho 0-6.18 = b-roll + ela recortada no canto ESQUERDO
    FOLDER = f'{DESK}/CRIATIVOS CROCHE EUROPA/CROCHE FRANÇA'
    FICHA_DIR = f'{FOLDER}/_quellen/out_fr/main'
    COVER = f'{FOLDER}/capa_100_receitas_croche_casa_frances_1x1.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/fr2_sala.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE CASA FR/3-final'
    OUTNAME = 'UGC_CASA_FRC2_douillette.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE CASA FR/hook_text_fr2.png', 230, 0.0, 6.18)
    PIP = (f'{ROOT}/cut/fr2', 0.0, 6.18, 1250, 'L')
    M = [
        (0.0, 'broll', (f'{S}/cs_usec.mp4', 0.0)),      # "Amies crocheteuses"
        (1.26, 'broll', (f'{S}/cs_wow.mp4', 3.0)),      # "maintenant qu'il commence à faire froid"
        (3.22, 'broll', (f'{S}/cs_eleno.mp4', 20.0)),   # "le meilleur moment"
        (4.72, 'broll', (f'{S}/cs_ayara.mp4', 0.0)),    # "la maison plus douillette"
        (6.18, 'broll', (f'{S}/cs_neri.mp4', 12.0)),    # "et le plus joli"
        (7.64, 'broll', (f'{S}/cs_ayara.mp4', 4.0)),    # "une déco au crochet"
        (9.96, 'aroll', (1.0,)),      # "J'ai trouvé"
        (10.9, 'cover', ()),          # "plus de 100 modèles"
        (14.08, 'broll', (f'{S}/cs_neri.mp4', 16.0)),   # tapis
        (15.14, 'broll', (f'{S}/cs_wow.mp4', 4.5)),     # paniers
        (16.48, 'ficha', ('054',)),   # coussins
        (18.12, 'ficha', ('002',)),   # sets de table
        (19.02, 'ficha', ('085',)),   # chemins de table
        (20.04, 'broll', (f'{S}/cs_ayara.mp4', 10.0)),  # "une jolie table"
        (21.34, 'aroll', (1.12,)),    # "Chaque modèle"
        (22.34, 'clip', (f'{S}/fpush_frc54.mp4', 0.0)), # matériel 24.04 / couleurs 25.19 / rang 25.94
        (27.2, 'broll', (f'{S}/fr2953.mp4', 2.0)),      # PDF, téléphone
        (30.1, 'broll', (f'{S}/fr2952.mp4', 2.0)),      # imprimer
        (32.16, 'aroll', (1.0,)),     # "l'accès est à vie"
        (34.2, 'broll', (f'{S}/cs_eleno.mp4', 14.0)),   # "embellir votre maison"
        (36.22, 'aroll', (1.0,)),
        (37.68, 'aroll', (1.18,)),    # "touchez En savoir plus"
    ]
    ARROW = (37.68, 39.88)
elif LANG == 'it3':
    # IT3: gancho NOVO na HeyGen (ela na mesa posta, hook_mesa_it 0-6.35) + ref2_it 6.5-fim (offset -0.15) = v3_it.mp4
    # b-roll de mesa posta (tm_*), câmera guiada no Set de table (fpush_it11), faixa de texto no gancho e seta no CTA
    FOLDER = f'{DESK}/CROCHE NATAL ITALIA'
    COVER = f'{FOLDER}/_capa_IT.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v3_it.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/IT/3-final'
    OUTNAME = 'UGC_NATAL_IT3_tavola.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/IT/v3_tavola/hook_text_it3.png', 1250, 0.0, 4.8)
    M = [
        (0.0, 'aroll', (1.0,)),
        (3.2, 'aroll', (1.12,)),      # "che ho preparato quest'anno"
        (4.9, 'aroll', (1.0,)),       # "è tutta all'uncinetto!"
        (6.35, 'broll', (f'{S}/tm_casinha.mp4', 19.0)), # "le decorazioni all'uncinetto"
        (8.45, 'broll', (f'{S}/tm_jessi.mp4', 31.0)),
        (10.45, 'broll', (f'{S}/tm_aless.mp4', 36.0)),  # "quel regalo fatto a mano"
        (12.45, 'broll', (f'{S}/tm_jessi.mp4', 50.0)),
        (14.85, 'aroll', (1.0,)),     # novelo: "ho trovato una raccolta"
        (16.1, 'cover', ()),          # "oltre 100 schemi"
        (19.75, 'ficha', ('23',)),    # Babbo Natale
        (20.85, 'ficha', ('24',)),    # renna
        (21.65, 'ficha', ('22',)),    # pupazzo di neve
        (22.95, 'ficha', ('32',)),    # albero
        (23.45, 'ficha', ('21',)),    # gnomi
        (24.65, 'ficha', ('11',)),    # tovagliette
        (25.65, 'ficha', ('51',)),    # ghirlande
        (26.4, 'broll', (f'{S}/tm_aless.mp4', 44.0)),   # "tanti altri progetti"
        (28.55, 'aroll', (1.14,)),    # "e non ricevi solo la foto"
        (29.85, 'clip', (f'{S}/fpush_it11.mp4', 0.0)),  # materiali 31.55 / colori 32.65 / passaggi 33.47
        (35.5, 'broll', (f'{S}/it3021.mp4', 4.0)),      # "è tutto in pdf" (celular)
        (37.7, 'broll', (f'{S}/it3018.mp4', 7.0)),      # "lo stampi quante volte vuoi"
        (39.6, 'aroll', (1.0,)),      # "e l'accesso è per sempre"
        (42.1, 'broll', (f'{S}/tm_luiza.mp4', 44.0)),   # "iniziando adesso... per la casa"
        (45.4, 'broll', (f'{S}/tm_casinha.mp4', 23.0)), # "e per i regali di Natale"
        (48.25, 'aroll', (1.18,)),    # "tocca, scopri di più"
    ]
    ARROW = (48.25, 51.76)
elif LANG == 'it4':
    # IT4: gancho do 05 em italiano (ref2_it 0-14.8, novelo) + corpo da mesa (mesa_it 5.95-fim, offset +8.85) = v4_it.mp4
    # b-roll TikTok (tk_*), câmera guiada na ficha Babbo Natale (fpush_it23), faixa de texto no gancho e seta no CTA
    FOLDER = f'{DESK}/CROCHE NATAL ITALIA'
    COVER = f'{FOLDER}/_capa_IT.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/v4_it.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/IT/3-final'
    OUTNAME = 'UGC_NATAL_IT4_amigurumi.mp4'
    HOOKTXT = (f'{DESK}/UGC CROCHE NATAL/IT/v3_tavola/hook_text_it4.png', 1250, 0.0, 6.4)
    M = [
        (0.0, 'aroll', (1.0,)),
        (3.1, 'aroll', (1.14,)),      # "cosa potete iniziare a fare"
        (6.6, 'broll', (f'{S}/tk_mario.mp4', 6.0)),    # "le decorazioni all'uncinetto"
        (8.6, 'broll', (f'{S}/tk_igru.mp4', 2.0)),     # "bellissime per la casa"
        (10.6, 'broll', (f'{S}/tk_snow.mp4', 7.0)),    # "quel regalo fatto a mano"
        (12.6, 'broll', (f'{S}/tk_igru.mp4', 10.0)),   # "che tutti adorano ricevere"
        (14.8, 'aroll', (1.0,)),      # mesa: "e puoi realizzare questa collezione"
        (18.75, 'cover', ()),         # "ci trovi oltre 100 schemi"
        (20.5, 'ficha', ('11',)),     # tovagliette
        (21.45, 'ficha', ('03',)),    # decorazioni per la tavola
        (23.0, 'ficha', ('33',)),     # albero
        (24.2, 'ficha', ('21',)),     # amigurumi
        (24.95, 'clip', (f'{S}/fpush_it23.mp4', 0.0)), # materiali 26.49 / colori 27.37 / spiegazioni 28.03
        (29.75, 'aroll', (1.14,)),    # "se ami l'uncinetto"
        (30.85, 'broll', (f'{S}/tk_mario.mp4', 15.0)), # "pezzi come questi"
        (32.6, 'aroll', (1.0,)),      # "questo è il momento giusto"
        (33.8, 'aroll', (1.18,)),     # "tocca, scopri di più"
    ]
    ARROW = (33.8, 37.8)
elif LANG == 'it2':
    FOLDER = f'{DESK}/CROCHE NATAL ITALIA'
    COVER = f'{FOLDER}/_capa_IT.png'
    HOOK, MESA, HOOKCUT, HOOK_END = None, f'{ROOT}/ref2_it.mp4', None, 0.0
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/IT/3-final'
    OUTNAME = 'UGC_NATAL_IT2_novelo.mp4'
    M = [
        (0.0, 'aroll', (1.0,)),
        (3.1, 'aroll', (1.14,)),
        (6.6, 'broll', (f'{S}/tt2.mp4', 1.4)),
        (8.5, 'broll', (f'{S}/tt2.mp4', 5.0)),
        (10.6, 'broll', (f'{S}/tt3.mp4', 0.2)),
        (12.7, 'broll', (f'{S}/tt3.mp4', 11.4)),
        (14.9, 'aroll', (1.0,)),
        (16.8, 'cover', ()),
        (19.9, 'ficha', ('23',)),
        (21.0, 'ficha', ('24',)),
        (21.8, 'ficha', ('22',)),
        (23.1, 'ficha', ('32',)),
        (23.6, 'ficha', ('21',)),
        (24.8, 'ficha', ('11',)),
        (25.8, 'ficha', ('51',)),
        (26.5, 'broll', (f'{S}/scroll_it.mp4', 0.0)),
        (28.7, 'aroll', (1.14,)),
        (30.5, 'broll', (f'{S}/it3018.mp4', 7.0)),
        (32.8, 'broll', (f'{S}/it3021.mp4', 4.0)),
        (33.6, 'broll', (f'{S}/it3020.mp4', 9.3)),
        (36.1, 'broll', (f'{S}/it3018.mp4', 0.3)),
        (39.8, 'broll', (f'{S}/tt2.mp4', 7.2)),
        (42.3, 'aroll', (1.0,)),
        (44.6, 'broll', (f'{S}/tt3.mp4', 18.5)),
        (47.5, 'aroll', (1.0,)),
        (48.5, 'aroll', (1.18,)),
        (50.0, 'aroll', (1.3,)),
    ]
elif LANG == 'it':
    FOLDER = f'{DESK}/CROCHE NATAL ITALIA'
    COVER = f'{FOLDER}/_capa_IT.png'
    HOOK, MESA, HOOKCUT, HOOK_END = f'{ROOT}/hook_it.mp4', f'{ROOT}/mesa_it.mp4', f'{ROOT}/cut/it', 3.4
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/IT/3-final'
    M = [
        (0.0, 'broll', (f'{S}/tt2.mp4', 1.4)),
        (2.0, 'broll', (f'{S}/tt2.mp4', 5.0)),
        (3.1, 'broll', (f'{S}/tt3.mp4', 0.2)),
        (4.6, 'broll', (f'{S}/tt3.mp4', 11.4)),
        (6.1, 'aroll', (1.0,)),
        (10.0, 'cover', ()),
        (11.8, 'ficha', ('11',)),
        (12.7, 'ficha', ('53',)),
        (14.2, 'ficha', ('31',)),
        (15.4, 'ficha', ('23',)),
        (16.3, 'ficha', ('22',)),
        (17.1, 'broll', (f'{S}/it3018.mp4', 7.0)),
        (18.5, 'broll', (f'{S}/it3021.mp4', 4.0)),
        (19.7, 'broll', (f'{S}/it3020.mp4', 9.3)),
        (21.0, 'aroll', (1.12,)),
        (22.5, 'broll', (f'{S}/tt3.mp4', 18.5)),
        (23.8, 'aroll', (1.0,)),
        (25.0, 'aroll', (1.16,)),
        (27.4, 'aroll', (1.27,)),
    ]
else:
    FOLDER = f'{DESK}/CROCHE NATAL FRANÇA'
    COVER = f'{DESK}/PROJETOS/crochet-noel-fr/assets/img/capa.webp'
    PAPER, PHONE, LAPTOP = f'{S}/img3008.mp4', f'{S}/img3013.mp4', f'{S}/img3012.mp4'
    HOOK, MESA, HOOKCUT, HOOK_END = f'{ROOT}/hook_fr.mp4', f'{ROOT}/mesa_fr.mp4', f'{ROOT}/cut/fr', 3.15
    OUTDIR = f'{DESK}/UGC CROCHE NATAL/FR/3-final'
    M = [
        (0.0, 'broll', (f'{S}/tt2.mp4', 1.4)),
        (1.6, 'broll', (f'{S}/tt2.mp4', 5.0)),
        (3.0, 'broll', (f'{S}/tt3.mp4', 0.2)),
        (4.5, 'broll', (f'{S}/tt3.mp4', 11.4)),
        (6.1, 'aroll', (1.0,)),
        (9.0, 'cover', ()),
        (11.1, 'ficha', ('11',)),
        (12.1, 'ficha', ('53',)),
        (13.2, 'ficha', ('31',)),
        (14.6, 'ficha', ('23',)),
        (15.4, 'ficha', ('22',)),
        (16.2, 'broll', (PAPER, 4.4)),
        (17.9, 'broll', (PHONE, 4.0)),
        (19.4, 'broll', (LAPTOP, 10.0)),
        (20.8, 'aroll', (1.12,)),
        (22.6, 'broll', (f'{S}/tt3.mp4', 18.5)),
        (24.2, 'aroll', (1.0,)),
        (25.5, 'aroll', (1.16,)),
        (27.6, 'aroll', (1.27,)),
    ]

def ficha(num):
    if globals().get('FICHA_DIR'):   # crochê casa: páginas do PDF (pNNN.png)
        return f'{FICHA_DIR}/p{num}.png'
    return glob.glob(f'{FOLDER}/*/Model*_{num}.png')[0]

# gancho: b-roll de fundo + apresentadora recortada por cima
HOOK_SEGS = [] if HOOK is None else [(0.0, 'broll', (f'{S}/tt4.mp4', 0.0))]

TOTAL = HOOK_END + dur(MESA)
segs = [(t, k, a) for t, k, a in HOOK_SEGS] + [(HOOK_END + t, k, a) for t, k, a in M]

# transições variadas (índice = transição de entrada do segmento i)
TRANS = {}
for i, (t, k, a) in enumerate(segs):
    if i == 0: continue
    pk = segs[i - 1][1]
    if k == 'cover': TRANS[i] = 'fadewhite'
    elif k in ('ficha', 'fzoom'): TRANS[i] = 'slideleft'
    elif k == 'clip': TRANS[i] = 'zoomin'
    elif k == 'aroll' and pk == 'speed': TRANS[i] = 'zoomin'
    elif k == 'aroll' and pk == 'aroll': TRANS[i] = None  # jump-cut seco (punch-in)
    elif k == 'aroll': TRANS[i] = 'zoomin'
    else: TRANS[i] = ['smoothleft', 'slideup', 'circleopen', 'smoothright', 'wipeleft', 'slidedown'][i % 6]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-1500:]); sys.exit(1)

kb = lambda d, z0, z1: f"scale=w='trunc({W}*({z0}+({z1}-{z0})*t/{d})/2)*2':h=-2:eval=frame,crop={W}:{H}"

files = []
for i, (t, k, a) in enumerate(segs):
    end = segs[i + 1][0] if i + 1 < len(segs) else TOTAL
    nxt_t = TRANS.get(i + 1)
    d = end - t + (T if (i + 1 < len(segs) and nxt_t) else 0)
    out = f'{TMP}/{i:02d}.mp4'
    enc = ['-r', str(FPS), '-t', f'{d:.3f}', '-an', '-c:v', 'libx264', '-crf', '17', '-preset', 'fast', '-pix_fmt', 'yuv420p', out]
    if k == 'broll':
        f, ss = a
        z0, z1 = (1.0, 1.08) if i % 2 else (1.08, 1.0)
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', f, '-vf', f'fps={FPS},{kb(d, z0, z1)},setsar=1', *enc])
    elif k == 'speed':
        f, ss, ee = a
        fac = (ee - ss) / (end - t)
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-t', f'{ee - ss + 2:.2f}', '-i', f, '-vf',
             f'setpts=PTS/{fac:.4f},fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1', *enc])
    elif k == 'clip':
        f, ss = a
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', f, '-vf', f'fps={FPS},setsar=1', *enc])
    elif k == 'aroll':
        z = a[0]
        ms = t - HOOK_END
        vf = f'scale={int(W * z) // 2 * 2}:-2,crop={W}:{H}:(iw-{W})/2:(ih-{H})*0.3,setsar=1'
        run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{ms:.3f}', '-i', MESA, '-vf', vf, *enc])
    elif k in ('cover', 'ficha'):
        img = COVER if k == 'cover' else ficha(a[0])
        fw = 860 if k == 'cover' else 1080
        z0, z1 = (1.0, 1.12) if k == 'cover' else (1.0, 1.06)
        fc = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:3,eq=brightness=-0.08[bg];"
              f"[0:v]scale={fw}:-2,format=rgba[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,fps={FPS},{kb(d, z0, z1)},setsar=1")
        run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-i', img, '-filter_complex', fc, *enc])
    elif k == 'fzoom':
        img = ficha(a[0]); x0, y0, x1, y1 = a[1]
        fc = (f"[0:v]crop={x1-x0}:{y1-y0}:{x0}:{y0},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{kb(d, 1.0, 1.10)},setsar=1")
        run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-i', img, '-filter_complex', fc, *enc])
    files.append((out, t, d))
    print(f'{i:02d} {k:6s} t={t:6.2f} d={d:5.2f} trans_in={TRANS.get(i)}')

# encadeia com xfade (offset = início do segmento na linha do tempo => lábios ficam sincronizados)
inputs, fc, last = [], [], '[s0]'
for i, (f, t, d) in enumerate(files):
    inputs += ['-i', f]
    fc.append(f'[{i}:v]settb=AVTB,setpts=PTS-STARTPTS[s{i}]')
cur_concat = []
for i in range(1, len(files)):
    tr = TRANS.get(i)
    t = files[i][1]
    if tr:
        fc.append(f'{last}[s{i}]xfade=transition={tr}:duration={T}:offset={t:.3f}[v{i}]')
    else:
        fc.append(f'{last}[s{i}]concat=n=2:v=1:a=0,settb=AVTB[v{i}]')
    last = f'[v{i}]'

# apresentadora recortada no gancho (entra deslizando da direita), no canto inferior direito
n_in = len(files)
if HOOK is not None:
    inputs += ['-framerate', str(FPS), '-i', f'{HOOKCUT}/%04d.png']
    fc.append(f'[{n_in}:v]scale=-2:1500,trim=duration={HOOK_END},setpts=PTS-STARTPTS[pip]')
    fc.append(f"{last}[pip]overlay=x='W-w*0.80+max(0,0.35-t)*1400':y=H-h+60:eof_action=pass:enable='lt(t,{HOOK_END})'[vout]")
    inputs += ['-i', HOOK, '-i', MESA]
    fc.append(f'[{n_in + 1}:a]atrim=0:{HOOK_END},asetpts=PTS-STARTPTS[a0];[{n_in + 2}:a]asetpts=PTS-STARTPTS[a1];[a0][a1]concat=n=2:v=0:a=1[aout]')
else:
    fc.append(f'{last}null[vout]')
    inputs += ['-i', MESA]
    fc.append(f'[{n_in}:a]asetpts=PTS-STARTPTS[aout]')

BASE_V = '[vout]'
PIP = globals().get('PIP')
if PIP:   # (pasta de PNGs recortados, t0, t1, altura): entra deslizando da direita no canto inferior
    cdir, p0, p1, ph, *side = PIP
    n_i = sum(1 for x in inputs if x == '-i')
    inputs += ['-framerate', str(FPS), '-i', f'{cdir}/%04d.png']
    fc.append(f'[{n_i}:v]scale=-2:{ph},trim=duration={p1},setpts=PTS-STARTPTS[pipc]')
    px = "-w*0.18-max(0,0.30-t)*1500" if side and side[0] == 'L' else "W-w*0.80+max(0,0.30-t)*1500"   # 'L' = canto esquerdo
    fc.append(f"[vout][pipc]overlay=x='{px}':y=H-h+30:eof_action=pass:enable='between(t,{p0},{p1})'[voutp]")
    BASE_V = '[voutp]'

HOOKTXT = globals().get('HOOKTXT')
if HOOKTXT:   # faixa de texto do gancho (entra com "pop")
    png, y, t0, t1 = HOOKTXT
    n_i = sum(1 for x in inputs if x == '-i')
    inputs += ['-loop', '1', '-framerate', str(FPS), '-i', png]
    fc.append(f"[{n_i}:v]format=rgba,scale=w='iw*(1+0.12*max(0,1-t/0.2))':h=-1:eval=frame[htx]")
    fc.append(f"{BASE_V}[htx]overlay=x=(W-w)/2:y={y}-(h-420)/2:shortest=1:enable='between(t,{t0},{t1})'[vout2]")
    last_v = '[vout2]'
    HOOKTXT2 = globals().get('HOOKTXT2')
    if HOOKTXT2:  # mesma faixa reposicionada quando ela entra (sem cobrir o rosto)
        png, y, t0, t1 = HOOKTXT2
        n_i = sum(1 for x in inputs if x == '-i')
        inputs += ['-loop', '1', '-framerate', str(FPS), '-i', png]
        fc.append(f"[{n_i}:v]format=rgba[htx2]")
        fc.append(f"[vout2][htx2]overlay=x=(W-w)/2:y={y}-(h-420)/2:shortest=1:enable='between(t,{t0},{t1})'[vout3]")
        last_v = '[vout3]'
else:
    last_v = BASE_V

if ARROW:
    n_i = sum(1 for x in inputs if x == '-i')
    inputs += ['-loop', '1', '-framerate', str(FPS), '-i', f'{ROOT}/src/seta.png']
    fc.append(f"{last_v}[{n_i}:v]overlay=x=(W-w)/2:y='H-h-150-abs(sin(t*7))*45':shortest=1:enable='between(t,{ARROW[0]},{ARROW[1]})'[vfin]")
    VMAP = '[vfin]'
else:
    VMAP = last_v

os.makedirs(OUTDIR, exist_ok=True)
out = f'{OUTDIR}/' + globals().get('OUTNAME', f'UGC_NATAL_{LANG.upper()}_modelo_BR.mp4')
run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(fc), '-map', VMAP, '-map', '[aout]',
     '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', str(FPS),
     '-c:a', 'aac', '-b:a', '192k', '-t', f'{TOTAL:.3f}', '-movflags', '+faststart', out])
print('OK', out, round(dur(out), 2), 'esperado', round(TOTAL, 2))
