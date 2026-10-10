"""Adiciona SFX de transição (whoosh / impacto / pop) nos finais DE e FR.
Detecta os cortes no vídeo final (independe do compose.py) e gera os sons sinteticamente.
uso: python sfx.py  -> grava *_SFX.mp4 ao lado do original
"""
import subprocess, re, wave, numpy as np, os

SR = 48000
BASE = 'C:/Users/User/Desktop/UGC CROCHE NATAL'
VIDS = [f'{BASE}/DE/3-final/UGC_NATAL_DE_modelo_BR.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR_modelo_BR.mp4', f'{BASE}/IT/3-final/UGC_NATAL_IT_modelo_BR.mp4', f'{BASE}/IT/3-final/UGC_NATAL_IT2_novelo.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR2_novelo.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR2B_material.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR6_couronne.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR7_hook05.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR8_mesa.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR9_mesa_hook.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR10_table.mp4', f'{BASE}/IT/3-final/UGC_NATAL_IT3_tavola.mp4', f'{BASE}/IT/3-final/UGC_NATAL_IT4_amigurumi.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR11_CTV01_timelapse.mp4', f'{BASE}/FR/3-final/UGC_NATAL_FR12_CTV02_sapin.mp4', f'{BASE}/IT/3-final/UGC_NATAL_IT5_CTV01_timelapse.mp4', f'{BASE}/IT/3-final/UGC_NATAL_IT6_CTV02_albero.mp4', 'C:/Users/User/Desktop/UGC CROCHE CASA DE/3-final/UGC_CASA_DE1_parede.mp4', 'C:/Users/User/Desktop/UGC CROCHE CASA DE/3-final/UGC_CASA_DE2_gemuetlich.mp4', 'C:/Users/User/Desktop/UGC CROCHE CASA FR/3-final/UGC_CASA_FRC1_salon.mp4', 'C:/Users/User/Desktop/UGC CROCHE CASA FR/3-final/UGC_CASA_FRC2_douillette.mp4']
rng = np.random.default_rng(7)

def bandsweep(noise, f0, f1, q=2.0):
    # filtro passa-banda varrendo f0->f1 (biquad simples amostra a amostra, vetorizado em blocos)
    out = np.zeros_like(noise); y1 = y2 = x1 = x2 = 0.0
    n = len(noise); blk = 64
    for s in range(0, n, blk):
        f = f0 * (f1 / f0) ** (s / n)
        w = 2 * np.pi * f / SR; al = np.sin(w) / (2 * q)
        b0, b2 = al, -al; a0 = 1 + al; a1 = -2 * np.cos(w); a2 = 1 - al
        b0, b2, a1, a2 = b0 / a0, b2 / a0, a1 / a0, a2 / a0
        for i in range(s, min(s + blk, n)):
            x = noise[i]; y = b0 * x + b2 * x2 - a1 * y1 - a2 * y2
            x2, x1 = x1, x; y2, y1 = y1, y; out[i] = y
    return out

def whoosh(d=0.42, f0=300, f1=4500, peak=0.6):
    n = int(SR * d); t = np.linspace(0, 1, n)
    s = bandsweep(rng.standard_normal(n), f0, f1)
    env = np.where(t < peak, (t / peak) ** 2, ((1 - t) / (1 - peak)) ** 1.5)
    s *= env; return s / np.abs(s).max()

def impact(d=0.9):
    n = int(SR * d); t = np.arange(n) / SR
    f = 120 * np.exp(-t * 9) + 42
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 5)
    click = rng.standard_normal(n) * np.exp(-t * 60) * 0.5
    s = body + click; return s / np.abs(s).max()

def pop(d=0.18):
    n = int(SR * d); t = np.arange(n) / SR
    f = 1400 * np.exp(-t * 25) + 500
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30); return s / np.abs(s).max()

def sparkle(d=0.7):
    n = int(SR * d); t = np.arange(n) / SR; s = np.zeros(n)
    for k, fr in enumerate([2093, 2637, 3136, 4186]):
        st = int(k * 0.06 * SR); tt = t[: n - st]
        s[st:] += np.sin(2 * np.pi * fr * tt) * np.exp(-tt * 9)
    return s / np.abs(s).max()

def bell(d=1.6, f=1568):
    # sino: parciais inarmônicos com decaimento longo
    n = int(SR * d); t = np.arange(n) / SR; s = np.zeros(n)
    for r, a, k in [(1, 1, 3.0), (2.76, .55, 4.5), (5.40, .35, 6.5), (8.93, .2, 9)]:
        s += a * np.sin(2 * np.pi * f * r * t) * np.exp(-t * k)
    s *= np.minimum(1, t / 0.003); return s / np.abs(s).max()

def jingle(d=0.9, hits=6):
    # guizos de trenó: rajadas de ruído agudo em sequência
    n = int(SR * d); s = np.zeros(n)
    for h in range(hits):
        st = int(h * d / hits * SR * 0.9); m = int(0.12 * SR); tt = np.arange(m) / SR
        burst = rng.standard_normal(m) * np.exp(-tt * 40)
        burst = np.diff(np.diff(burst, prepend=0), prepend=0)   # realça agudos
        for fr in (5200, 6900, 8400):
            burst += 0.25 * np.sin(2 * np.pi * fr * tt) * np.exp(-tt * 30)
        e = min(n, st + m); s[st:e] += burst[: e - st] * (0.6 + 0.4 * (h % 2))
    return s / np.abs(s).max()

def cuts(v):
    r = subprocess.run(['ffmpeg', '-i', v, '-vf', "select='gt(scene,0.22)',showinfo", '-f', 'null', '-'],
                       capture_output=True, text=True)
    ts = [float(x) for x in re.findall(r'pts_time:([0-9.]+)', r.stderr)]
    out = []
    for t in ts:  # junta detecções do mesmo crossfade
        if not out or t - out[-1] > 0.45: out.append(t)
    return out

def bright(v, t):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', v, '-frames:v', '1',
                                   '-vf', 'scale=32:56,format=gray', '-f', 'rawvideo', '-'])
    return np.frombuffer(raw, np.uint8).mean()

def dur(v):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', v]))

W = [whoosh(0.40, 250, 5000), whoosh(0.34, 400, 6000, 0.55), whoosh(0.46, 200, 3500, 0.65)]
import sys
ONLY = sys.argv[1:]
for v in VIDS:
    if ONLY and not any('_%s_' % o.upper() in v for o in ONLY): continue
    if not os.path.exists(v): continue
    D = dur(v); track = np.zeros(int(SR * (D + 1)))
    def add(s, t, g):
        i = int(t * SR); i = max(i, 0); j = min(len(track), i + len(s)); track[i:j] += s[: j - i] * g
    if '_IT2_' not in v and '_FR2_' not in v and '_FR2B_' not in v and '_FR6_' not in v and '_FR7_' not in v and '_FR8_' not in v and '_FR9_' not in v and '_FR10_' not in v and '_IT3_' not in v and '_IT4_' not in v: add(impact(), 0.0, 0.55)           # impacto na entrada do gancho
    add(sparkle(), 0.15, 0.12)
    # só em pontos específicos (tempos da linha do tempo do compose.py): fim do gancho, mesa, capa, 1ª ficha, CTA
    PTS = {'DE': [(3.45, 'w'), (10.35, 'w'), (14.05, 'capa'), (16.55, 'w'), (31.85, 'w')],
           'FR': [(3.15, 'w'), (9.25, 'w'), (12.15, 'capa'), (14.25, 'w'), (28.65, 'w')],
           'IT': [(3.4, 'w'), (9.5, 'w'), (13.4, 'capa'), (15.2, 'w'), (28.4, 'w')],
           'IT2': [(6.6, 'w'), (16.8, 'capa'), (19.9, 'w'), (30.5, 'w'), (48.5, 'w')],
           'FR2B': [(5.1, 'w'), (13.1, 'capa'), (16.0, 'w'), (25.98, 'w'), (27.68, 'pop'), (28.83, 'pop'), (29.58, 'pop'),
                    (29.88, 'pop'), (30.68, 'pop'), (30.98, 'pop'), (31.6, 'w'), (32.92, 'w'), (34.72, 'w'), (42.3, 'seta')],
           'FR6': [(0.05, 'pop'), (7.2, 'w'), (13.2, 'w'), (19.26, 'capa'), (25.06, 'w'), (31.3, 'w'), (34.29, 'w'), (35.99, 'pop'),
                   (37.14, 'pop'), (37.89, 'pop'), (38.19, 'pop'), (38.99, 'pop'), (39.29, 'pop'), (41.72, 'w'), (43.9, 'w'),
                   (46.64, 'w'), (49.68, 'seta')],
           'FR7': [(5.1, 'w'), (11.5, 'w'), (12.26, 'capa'), (18.06, 'w'), (24.3, 'w'), (27.29, 'w'), (28.99, 'pop'),
                   (30.14, 'pop'), (30.89, 'pop'), (31.19, 'pop'), (31.99, 'pop'), (32.29, 'pop'), (34.72, 'w'), (36.9, 'w'),
                   (39.64, 'w'), (42.68, 'seta')],
           'FR9': [(0.05, 'pop'), (1.6, 'w'), (3.3, 'w'), (5.1, 'w'), (8.2, 'w'), (11.5, 'w'), (12.26, 'capa'), (18.06, 'w'),
                   (24.3, 'w'), (27.29, 'w'), (28.99, 'pop'), (30.14, 'pop'), (30.89, 'pop'), (31.19, 'pop'), (31.99, 'pop'),
                   (32.29, 'pop'), (34.72, 'w'), (36.9, 'w'), (39.64, 'w'), (42.68, 'seta')],
           'FR10': [(0.05, 'pop')] + [(t + 0.655, k) for t, k in [(5.1, 'w'), (11.5, 'w'), (12.26, 'capa'), (18.06, 'w'), (24.3, 'w'),
                   (27.29, 'w'), (28.99, 'pop'), (30.14, 'pop'), (30.89, 'pop'), (31.19, 'pop'), (31.99, 'pop'), (32.29, 'pop'),
                   (34.72, 'w'), (36.9, 'w'), (39.64, 'w'), (42.68, 'seta')]],
           'IT3': [(0.05, 'pop'), (6.35, 'w'), (14.85, 'w'), (16.1, 'capa'), (19.75, 'w'), (26.4, 'w'), (29.85, 'w'), (31.55, 'pop'),
                   (32.7, 'pop'), (33.45, 'pop'), (33.75, 'pop'), (34.55, 'pop'), (34.85, 'pop'), (35.5, 'w'), (37.7, 'w'),
                   (42.1, 'w'), (48.25, 'seta')],
           'IT4': [(0.05, 'pop'), (6.6, 'w'), (14.8, 'w'), (18.75, 'capa'), (20.5, 'w'), (24.95, 'w'), (26.65, 'pop'),
                   (27.8, 'pop'), (28.55, 'pop'), (28.85, 'pop'), (29.65, 'pop'), (30.85, 'w'), (33.8, 'seta')],
           'FR11': [(0.05, 'pop'), (2.94, 'w'), (4.5, 'pop')] + [(t + 0.655, k) for t, k in [(5.1, 'w'), (11.5, 'w'), (12.26, 'capa'), (18.06, 'w'), (24.3, 'w'),
                   (27.29, 'w'), (28.99, 'pop'), (30.14, 'pop'), (30.89, 'pop'), (31.19, 'pop'), (31.99, 'pop'), (32.29, 'pop'),
                   (34.72, 'w'), (36.9, 'w'), (39.64, 'w'), (42.68, 'seta')]],
           'FR12': [(0.03, 'bell'), (0.05, 'jingle'), (1.2, 'bell2'), (2.4, 'w'), (5.1, 'jingle'), (8.2, 'w'), (11.5, 'w'),
                    (12.26, 'capa'), (12.4, 'jingle'), (18.06, 'w'), (24.3, 'bell'), (27.29, 'w'), (28.99, 'pop'), (30.14, 'pop'),
                    (30.89, 'pop'), (31.19, 'pop'), (31.99, 'pop'), (32.29, 'pop'), (34.72, 'w'), (36.9, 'w'), (39.64, 'jingle'),
                    (42.68, 'seta')],
           'IT5': [(0.05, 'pop'), (3.2, 'w'), (4.9, 'pop'), (6.35, 'w'), (14.85, 'w'), (16.1, 'capa'), (19.75, 'w'), (26.4, 'w'),
                   (29.85, 'w'), (31.55, 'pop'), (32.7, 'pop'), (33.45, 'pop'), (33.75, 'pop'), (34.55, 'pop'), (34.85, 'pop'),
                   (35.5, 'w'), (37.7, 'w'), (42.1, 'w'), (48.25, 'seta')],
           'IT6': [(0.03, 'bell'), (0.05, 'jingle'), (1.6, 'bell2'), (3.1, 'w'), (6.6, 'jingle'), (10.6, 'w'), (14.8, 'w'),
                   (18.75, 'capa'), (18.9, 'jingle'), (20.5, 'w'), (24.95, 'w'), (26.65, 'pop'), (27.8, 'pop'), (28.55, 'pop'),
                   (28.85, 'pop'), (29.65, 'pop'), (29.95, 'pop'), (30.85, 'bell'), (33.8, 'seta')],
           'DE1': [(0.05, 'pop'), (2.26, 'w'), (5.02, 'w'), (6.76, 'w'), (8.94, 'w'), (12.76, 'w'), (16.32, 'capa'), (20.76, 'w'), (25.6, 'w'), (28.88, 'w'), (30.58, 'pop'), (31.73, 'pop'), (32.48, 'pop'), (33.58, 'pop'), (36.86, 'w'), (39.9, 'w'), (40.92, 'w'), (45.36, 'w'), (51.18, 'seta')],
           'DE2': [(0.03, 'pop'), (1.8, 'w'), (3.74, 'w'), (5.5, 'w'), (7.08, 'w'), (11.12, 'w'), (12.66, 'capa'), (16.56, 'w'), (20.28, 'w'), (24.04, 'w'), (26.94, 'w'), (28.64, 'pop'), (29.79, 'pop'), (30.54, 'pop'), (31.64, 'pop'), (32.62, 'w'), (36.2, 'w'), (41.7, 'w'), (46.64, 'seta')],
           'FRC1': [(0.05, 'pop'), (1.44, 'w'), (2.7, 'w'), (4.08, 'w'), (5.36, 'w'), (6.88, 'w'), (10.06, 'w'), (12.5, 'capa'), (15.5, 'w'), (18.7, 'w'), (21.18, 'w'), (22.88, 'pop'), (24.03, 'pop'), (24.78, 'pop'), (25.88, 'pop'), (28.48, 'w'), (31.82, 'w'), (32.76, 'w'), (36.9, 'w'), (40.78, 'seta')],
           'FRC2': [(0.05, 'pop'), (1.26, 'w'), (3.22, 'w'), (4.72, 'w'), (6.18, 'w'), (9.96, 'w'), (10.9, 'capa'), (14.08, 'w'), (16.48, 'w'), (20.04, 'w'), (22.34, 'w'), (24.04, 'pop'), (25.19, 'pop'), (25.94, 'pop'), (27.04, 'pop'), (27.2, 'w'), (30.1, 'w'), (34.2, 'w'), (37.68, 'seta')],
           'FR2': [(5.1, 'w'), (13.1, 'capa'), (16.0, 'w'), (25.98, 'w'), (42.3, 'seta')]}
    log = []
    for k, (t, kind) in enumerate(PTS['FRC1' if '_FRC1_' in v else 'FRC2' if '_FRC2_' in v else 'DE1' if '_DE1_' in v else 'DE2' if '_DE2_' in v else 'IT5' if '_IT5_' in v else 'IT6' if '_IT6_' in v else 'FR12' if '_FR12_' in v else 'FR11' if '_FR11_' in v else 'IT4' if '_IT4_' in v else 'IT3' if '_IT3_' in v else 'FR10' if '_FR10_' in v else 'FR9' if '_FR9_' in v else 'FR7' if ('_FR7_' in v or '_FR8_' in v) else 'FR6' if '_FR6_' in v else 'FR2B' if '_FR2B_' in v else 'FR2' if '_FR2_' in v else 'IT2' if '_IT2_' in v else 'DE' if '_DE_' in v else 'IT' if '_IT_' in v else 'FR']):
        if kind == 'seta':   # seta vermelha: pop + brilho
            add(pop(), t, 0.7); add(pop(), t + 0.12, 0.45); add(sparkle(), t + 0.05, 0.25); log.append(f'{t:.2f} seta'); continue
        if kind in ('bell', 'bell2'):
            add(bell(f=1568 if kind == 'bell' else 2093), t, 0.32); log.append(f'{t:.2f} {kind}'); continue
        if kind == 'jingle':
            add(jingle(), t, 0.28); log.append(f'{t:.2f} jingle'); continue
        if kind == 'pop':    # destaque na ficha
            add(pop(), t, 0.55); log.append(f'{t:.2f} pop'); continue
        if kind == 'capa':   # flash branco da capa
            add(W[0], t - 0.30, 0.45); add(sparkle(), t, 0.22); log.append(f'{t:.2f} capa')
        else:
            w = W[k % 3]
            add(w, t - len(w) / SR * 0.6, 0.38); log.append(f'{t:.2f} whoosh')
    tmpwav = v.replace('.mp4', '_sfx.wav')
    pcm = (np.clip(track, -1, 1) * 32767).astype(np.int16)
    with wave.open(tmpwav, 'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(pcm.tobytes())
    out = v.replace('.mp4', '_SFX.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', v, '-i', tmpwav, '-filter_complex',
                    '[1:a]volume=0.9[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]',
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', out], check=True)
    os.remove(tmpwav)
    print(os.path.basename(out), len(log), 'efeitos:', ', '.join(log))
