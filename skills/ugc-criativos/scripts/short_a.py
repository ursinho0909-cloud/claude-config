"""CTV curto sem apresentadora, formato "Vous crocheteriez ça pour Noël ?" (ref. Essentialglowdesign FR, 06/10).
Peças prontas em cortes rápidos + legenda por peça -> capa/fichas -> celular -> CTA com seta.
uso: python short_a.py fr|it      (sem música: usuário coloca)
"""
import sys, os, glob, subprocess
from PIL import Image, ImageDraw, ImageFont

LANG = sys.argv[1] if len(sys.argv) > 1 else 'fr'
W, H, FPS, T = 1080, 1920, 25, 0.2
ROOT, S, DESK = 'C:/tmp/ugcn', 'C:/tmp/ugcn/src', 'C:/Users/User/Desktop'
TMP = f'{ROOT}/shortA/{LANG}'
os.makedirs(TMP, exist_ok=True)

CFG = {
    'fr': dict(folder=f'{DESK}/CROCHE NATAL FRANÇA', cover=f'{S}/capa_fr.png', scroll=f'{S}/scroll_fr.mp4',
               out=f'{DESK}/UGC CROCHE NATAL/FR/3-final/UGC_NATAL_FR11_short_ca.mp4',
               txt=[('VOUS CROCHETERIEZ ÇA', 'POUR NOËL ?'), ('', 'LES SETS DE TABLE'), ('', 'LES BOULES DU SAPIN'),
                    ('', 'LES AMIGURUMIS'), ('', 'TOUT EST AU CROCHET'), ('EXPLIQUÉS ÉTAPE PAR ÉTAPE', '+100 MODÈLES DE NOËL'),
                    ('MATÉRIEL · COULEURS', 'ÉTAPES EN PHOTO'), ('SUR LE TÉLÉPHONE', 'OU À IMPRIMER'),
                    ('LE LIEN EST', 'JUSTE EN DESSOUS')]),
    'it': dict(folder=f'{DESK}/CROCHE NATAL ITALIA', cover=f'{DESK}/CROCHE NATAL ITALIA/_capa_IT.png', scroll=f'{S}/scroll_it.mp4',
               out=f'{DESK}/UGC CROCHE NATAL/IT/3-final/UGC_NATAL_IT5_short.mp4',
               txt=[('LO FARESTI ALL\'UNCINETTO', 'PER NATALE?'), ('', 'LE TOVAGLIETTE'), ('', 'LE PALLINE DELL\'ALBERO'),
                    ('', 'GLI AMIGURUMI'), ('', 'TUTTO ALL\'UNCINETTO'), ('SPIEGATI PASSO DOPO PASSO', '+100 SCHEMI DI NATALE'),
                    ('MATERIALE · COLORI', 'PASSAGGI IN FOTO'), ('SUL TELEFONO', 'O DA STAMPARE'),
                    ('IL LINK È', 'QUI SOTTO')]),
}[LANG]

def ficha(n):
    return glob.glob(f"{CFG['folder']}/*/Model*_{n}.png")[0]

# (início, tipo, arquivo, ss, índice da legenda)
SEGS = [
    (0.0,  'broll', f'{S}/tm_luiza.mp4', 38.0, 0),
    (2.6,  'broll', f'{S}/tm_casinha.mp4', 19.0, 1),
    (4.0,  'broll', f'{S}/tm_jessi.mp4', 27.0, 1),
    (5.4,  'broll', f'{S}/tk_mario.mp4', 8.0, 2),
    (6.8,  'broll', f'{S}/tt3.mp4', 10.0, 3),
    (8.2,  'broll', f'{S}/tm_aless.mp4', 24.0, 4),
    (9.4,  'cover', CFG['cover'], 0, 5),
    (11.0, 'ficha', ficha('11'), 0, 6),
    (11.6, 'ficha', ficha('23'), 0, 6),
    (12.2, 'ficha', ficha('31'), 0, 6),
    (12.8, 'ficha', ficha('53'), 0, 6),
    (13.4, 'broll', CFG['scroll'], 0.0, 7),
    (14.9, 'broll', f'{S}/tm_luiza.mp4', 44.0, 8),
]
TOTAL = 17.6
ARROW = (14.9, TOTAL)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-1500:]); sys.exit(1)

# ---------- legendas (preto em placa branca + branco em placa vermelha) ----------
FB = 'C:/Windows/Fonts/arialbd.ttf'
def pill(d, xy, fill): d.rounded_rectangle(xy, radius=22, fill=fill)
def caption(top, main, path):
    im = Image.new('RGBA', (W, 420), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    y = 20
    if top:
        f1 = ImageFont.truetype(FB, 62)
        while d.textlength(top, font=f1) > W - 140: f1 = ImageFont.truetype(FB, f1.size - 2)
        tw = d.textlength(top, font=f1)
        pill(d, ((W - tw) / 2 - 30, y, (W + tw) / 2 + 30, y + 96), (255, 255, 255, 255))
        d.text((W / 2, y + 48), top, font=f1, fill=(20, 20, 20), anchor='mm'); y += 120
    f2 = ImageFont.truetype(FB, 88)
    while d.textlength(main, font=f2) > W - 140: f2 = ImageFont.truetype(FB, f2.size - 2)
    tw = d.textlength(main, font=f2)
    pill(d, ((W - tw) / 2 - 36, y, (W + tw) / 2 + 36, y + 128), (200, 24, 36, 255))
    d.text((W / 2, y + 64), main, font=f2, fill=(255, 255, 255), anchor='mm')
    im.save(path)

caps = []
for i, (top, main) in enumerate(CFG['txt']):
    p = f'{TMP}/cap{i}.png'; caption(top, main, p); caps.append(p)

# janelas de cada legenda (agrupa segmentos consecutivos com a mesma legenda)
win = []
for i, s in enumerate(SEGS):
    end = SEGS[i + 1][0] if i + 1 < len(SEGS) else TOTAL
    if win and win[-1][0] == s[4]: win[-1][2] = end
    else: win.append([s[4], s[0], end])

# ---------- segmentos ----------
kb = lambda d, z0, z1: f"scale=w='trunc({W}*({z0}+({z1}-{z0})*t/{d})/2)*2':h=-2:eval=frame,crop={W}:{H}"
files = []
for i, (t, k, f, ss, _) in enumerate(SEGS):
    end = SEGS[i + 1][0] if i + 1 < len(SEGS) else TOTAL
    d = end - t + (T if i + 1 < len(SEGS) else 0)
    out = f'{TMP}/{i:02d}.mp4'
    enc = ['-r', str(FPS), '-t', f'{d:.3f}', '-an', '-c:v', 'libx264', '-crf', '17', '-preset', 'fast', '-pix_fmt', 'yuv420p', out]
    if k == 'broll':
        z0, z1 = (1.0, 1.10) if i % 2 else (1.10, 1.0)
        vf = f'fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{kb(d, z0, z1)},setsar=1'
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', f, '-vf', vf, *enc])
    else:
        fw = 820 if k == 'cover' else 920
        fc = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:3,eq=brightness=-0.08[bg];"
              f"[0:v]scale={fw}:-2,format=rgba[fg];[bg][fg]overlay=(W-w)/2:H-h-70,fps={FPS},{kb(d, 1.0, 1.08)},setsar=1")
        run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-i', f, '-filter_complex', fc, *enc])
    files.append((out, t))

TR = ['slideleft', 'smoothup', 'wipeleft', 'smoothright', 'circleopen', 'fadewhite',
      'slideleft', 'slideleft', 'slideleft', 'slideleft', 'smoothup', 'zoomin']
inputs, fc, last = [], [], '[s0]'
for i, (f, t) in enumerate(files):
    inputs += ['-i', f]; fc.append(f'[{i}:v]settb=AVTB,setpts=PTS-STARTPTS[s{i}]')
for i in range(1, len(files)):
    fc.append(f'{last}[s{i}]xfade=transition={TR[i - 1]}:duration={T}:offset={files[i][1]:.3f}[v{i}]'); last = f'[v{i}]'

n = len(files)
for j, (ci, t0, t1) in enumerate(win):
    inputs += ['-loop', '1', '-framerate', str(FPS), '-i', caps[ci]]
    fc.append(f"[{n}:v]format=rgba,scale=w='iw*(1+0.10*max(0,1-(t-{t0})/0.18))':h=-1:eval=frame[c{j}]")
    fc.append(f"{last}[c{j}]overlay=x=(W-w)/2:y=230:shortest=1:enable='between(t,{t0},{t1})'[o{j}]"); last = f'[o{j}]'; n += 1
inputs += ['-loop', '1', '-framerate', str(FPS), '-i', f'{S}/seta.png']
fc.append(f"{last}[{n}:v]overlay=x=(W-w)/2:y='H-h-150-abs(sin(t*7))*45':shortest=1:enable='between(t,{ARROW[0]},{ARROW[1]})'[vfin]")
inputs += ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']

os.makedirs(os.path.dirname(CFG['out']), exist_ok=True)
run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(fc), '-map', '[vfin]', '-map', f'{n + 1}:a',
     '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', str(FPS),
     '-c:a', 'aac', '-b:a', '128k', '-t', f'{TOTAL:.3f}', '-movflags', '+faststart', CFG['out']])
print('OK', CFG['out'])
