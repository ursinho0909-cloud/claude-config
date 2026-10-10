"""Faixa do gancho em paleta de Natal: placa verde-pinheiro c/ texto creme + placa vermelha c/ texto branco, bordas douradas.
uso: python faixa_natal.py "<linha1>" "<linha2>" "<faixa vermelha>" <saida.png>
"""
import sys
from PIL import Image, ImageDraw, ImageFont
l1, l2, red, out = sys.argv[1:5]
W = 1080; FB = 'C:/Windows/Fonts/arialbd.ttf'
GREEN, RED, GOLD, CREAM = (31, 77, 54, 255), (200, 24, 36, 255), (214, 170, 72, 255), (255, 246, 229)
im = Image.new('RGBA', (W, 420), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
f1 = ImageFont.truetype(FB, 66)
while max(d.textlength(l1, font=f1), d.textlength(l2, font=f1)) > W - 160: f1 = ImageFont.truetype(FB, f1.size - 2)
tw = max(d.textlength(l1, font=f1), d.textlength(l2, font=f1))
d.rounded_rectangle(((W - tw) / 2 - 44, 6, (W + tw) / 2 + 44, 194), radius=22, fill=GREEN, outline=GOLD, width=6)
d.text((W / 2, 60), l1, font=f1, fill=CREAM, anchor='mm'); d.text((W / 2, 140), l2, font=f1, fill=CREAM, anchor='mm')
f2 = ImageFont.truetype(FB, 92)
while d.textlength(red, font=f2) > W - 120: f2 = ImageFont.truetype(FB, f2.size - 2)
rw = d.textlength(red, font=f2)
d.rounded_rectangle(((W - rw) / 2 - 42, 210, (W + rw) / 2 + 42, 334), radius=18, fill=RED, outline=GOLD, width=6)
d.text((W / 2 + 3, 275), red, font=f2, fill=(110, 10, 18), anchor='mm')   # sombra
d.text((W / 2, 272), red, font=f2, fill=(255, 255, 255), anchor='mm')
im.save(out); print('OK', out)
