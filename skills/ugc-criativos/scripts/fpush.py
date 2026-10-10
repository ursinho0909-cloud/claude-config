"""Clipe "câmera guiada" por uma ficha real: página inteira -> Matériel -> Couleurs -> Instructions,
com moldura de destaque animada em cada bloco. Usado no trecho "chaque modèle vous montre le matériel...".
uso: python fpush.py <ficha.png> <saida.mp4> [preset]   (tempos/caixas no topo, coords da página 1536x2304; preset "53" = Couronne de l'Avent, "23" = Père Noël, "11" = Set de table rond)
"""
import sys, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC, OUT = sys.argv[1], sys.argv[2]
W, H, FPS, DUR = 1080, 1920, 25, 6.0
RED = (179, 32, 47)

# câmera: (tempo local, centro x, centro y, escala px_saida/px_pagina)
CAM = [
    (0.00, 768, 1152, 0.60),
    (1.20, 768, 1152, 0.66),
    (1.75, 434, 1354, 1.36),   # Matériel
    (2.55, 434, 1370, 1.40),
    (2.90, 434, 1728, 1.36),   # Couleurs
    (3.30, 434, 1735, 1.40),
    (3.65, 1154, 790, 1.55),   # Instructions 1-2
    (4.25, 1154, 820, 1.58),
    (4.70, 1154, 1560, 1.55),  # Instructions 3-4
    (DUR, 1154, 1590, 1.60),
]
# destaques: (aparece, some, caixa)
HL = [
    (1.70, 2.75, (62, 1218, 806, 1490)),
    (2.85, 3.50, (62, 1504, 382, 1952)),
    (3.60, 4.60, (830, 548, 1478, 1012)),
    (3.90, 4.60, (830, 1034, 1478, 1344)),
    (4.70, DUR, (830, 1364, 1478, 1706)),
    (5.00, DUR, (830, 1726, 1478, 1946)),
]

if len(sys.argv) > 3 and sys.argv[3] == '53':
    CAM = [
        (0.00, 768, 1152, 0.60),
        (1.20, 768, 1152, 0.66),
        (1.75, 408, 1354, 1.40),   # Matériel
        (2.55, 408, 1370, 1.44),
        (2.90, 300, 1700, 1.50),   # Couleurs
        (3.30, 300, 1708, 1.54),
        (3.65, 1160, 866, 1.55),   # Instructions 1-2
        (4.25, 1160, 890, 1.58),
        (4.70, 1160, 1534, 1.55),  # Instructions 3-4
        (DUR, 1160, 1560, 1.60),
    ]
    HL = [
        (1.70, 2.75, (60, 1184, 756, 1524)),
        (2.85, 3.50, (60, 1534, 346, 1884)),
        (3.60, 4.60, (836, 536, 1484, 862)),
        (3.90, 4.60, (836, 870, 1484, 1194)),
        (4.70, DUR, (836, 1200, 1484, 1530)),
        (5.00, DUR, (836, 1538, 1484, 1884)),
    ]
if len(sys.argv) > 3 and sys.argv[3] == '23':
    CAM[2:6] = [(1.75, 434, 1385, 1.36), (2.55, 434, 1400, 1.40), (2.90, 300, 1775, 1.50), (3.30, 300, 1782, 1.54)]
    HL[0] = (1.70, 2.75, (62, 1220, 806, 1550))
    HL[1] = (2.85, 3.50, (62, 1560, 330, 1998))
    CAM[6:] = [(3.65, 1154, 883, 1.55), (4.25, 1154, 900, 1.58), (4.70, 1154, 1625, 1.50), (DUR, 1154, 1645, 1.54)]
    HL[2:] = [(3.60, 4.60, (830, 556, 1478, 890)), (3.90, 4.60, (830, 902, 1478, 1210)),
              (4.70, DUR, (830, 1226, 1478, 1690)), (5.00, DUR, (830, 1702, 1478, 2024))]
if len(sys.argv) > 3 and sys.argv[3] == '11':
    CAM[2:] = [(1.75, 436, 1312, 1.36), (2.55, 436, 1326, 1.40), (2.90, 300, 1658, 1.50), (3.30, 300, 1666, 1.54),
               (3.65, 1152, 862, 1.55), (4.25, 1152, 880, 1.58), (4.70, 1152, 1510, 1.55), (DUR, 1152, 1530, 1.60)]
    HL = [(1.70, 2.75, (64, 1176, 808, 1450)), (2.85, 3.50, (64, 1476, 384, 1842)),
          (3.60, 4.60, (828, 560, 1476, 862)), (3.90, 4.60, (828, 880, 1476, 1166)),
          (4.70, DUR, (828, 1184, 1476, 1510)), (5.00, DUR, (828, 1512, 1476, 1838))]

if len(sys.argv) > 3 and sys.argv[3] == '31':   # Étoile de Noël rouge
    CAM[2:] = [(1.75, 432, 1325, 1.36), (2.55, 432, 1340, 1.40), (2.90, 300, 1680, 1.50), (3.30, 300, 1688, 1.54),
               (3.65, 1155, 870, 1.55), (4.25, 1155, 890, 1.58), (4.70, 1155, 1525, 1.55), (DUR, 1155, 1545, 1.60)]
    HL = [(1.70, 2.75, (64, 1180, 800, 1470)), (2.85, 3.50, (64, 1490, 384, 1870)),
          (3.60, 4.60, (830, 570, 1480, 860)), (3.90, 4.60, (830, 880, 1480, 1170)),
          (4.70, DUR, (830, 1190, 1480, 1500)), (5.00, DUR, (830, 1530, 1480, 1860))]

if len(sys.argv) > 3 and sys.argv[3] == 'de54':   # crochê casa DE, p054 Kissen Blauer Garten (página 2110x2982)
    CAM = [(0.00, 1055, 1491, 0.50), (1.20, 1055, 1491, 0.54), (1.75, 1395, 835, 1.55), (2.55, 1395, 850, 1.60),
           (2.90, 370, 1485, 1.45), (3.30, 370, 1495, 1.50), (3.65, 690, 2170, 0.84), (4.25, 690, 2180, 0.86),
           (4.70, 690, 2630, 0.84), (DUR, 690, 2640, 0.87)]
    HL = [(1.70, 2.75, (1110, 510, 1680, 1160)), (2.85, 3.50, (60, 1120, 680, 1850)),
          (3.60, 4.60, (70, 1940, 1310, 2400)), (4.70, DUR, (70, 2400, 1310, 2860))]

ease = lambda x: x * x * (3 - 2 * x)

def cam(t):
    for (t0, *a), (t1, *b) in zip(CAM, CAM[1:]):
        if t <= t1:
            k = ease(min(1, max(0, (t - t0) / (t1 - t0))))
            return [p + (q - p) * k for p, q in zip(a, b)]
    return CAM[-1][1:]

page = Image.open(SRC).convert('RGB')
PW, PH = page.size
bg = page.resize((W, int(W * PH / PW))).crop((0, 0, W, H)) if W * PH / PW >= H else page.resize((int(H * PW / PH), H))
bg = bg.resize((W, H)).filter(ImageFilter.GaussianBlur(40))
bg = Image.eval(bg, lambda v: int(v * 0.55))

# página com sombra (pré-renderizada, transformada por frame)
SH = 40
paper = Image.new('RGBA', (PW + 2 * SH, PH + 2 * SH), (0, 0, 0, 0))
sh = Image.new('L', paper.size, 0)
ImageDraw.Draw(sh).rectangle((SH, SH + 12, SH + PW, SH + PH + 12), fill=150)
paper.putalpha(sh.filter(ImageFilter.GaussianBlur(22)))
paper.paste(page, (SH, SH))

ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                       '-i', '-', '-c:v', 'libx264', '-crf', '17', '-preset', 'fast', '-pix_fmt', 'yuv420p', OUT],
                      stdin=subprocess.PIPE)
for f in range(int(DUR * FPS)):
    t = f / FPS
    cx, cy, s = cam(t)
    frame = bg.copy()
    # transformação afim: ponto de saída (x,y) -> ponto no "paper" (inclui margem da sombra)
    a = 1 / s
    tx, ty = cx - W / 2 * a + SH, cy - H / 2 * a + SH
    layer = paper.transform((W, H), Image.AFFINE, (a, 0, tx, 0, a, ty), resample=Image.BICUBIC)
    frame.paste(layer, (0, 0), layer)
    d = ImageDraw.Draw(frame)
    for t0, t1, (x0, y0, x1, y1) in HL:
        if not (t0 <= t < t1): continue
        k = min(1, (t - t0) / 0.18)                       # entra com "pop": cresce de 1.06 -> 1.0
        grow = (1 - ease(k)) * 0.06
        bx0, by0 = (x0 - cx) * s + W / 2, (y0 - cy) * s + H / 2
        bx1, by1 = (x1 - cx) * s + W / 2, (y1 - cy) * s + H / 2
        mx, my = (bx1 - bx0) * grow, (by1 - by0) * grow
        d.rounded_rectangle((bx0 - 10 - mx, by0 - 10 - my, bx1 + 10 + mx, by1 + 10 + my), radius=22,
                            outline=RED, width=9)
    ff.stdin.write(frame.tobytes())
ff.stdin.close(); ff.wait()
print('OK', OUT)
