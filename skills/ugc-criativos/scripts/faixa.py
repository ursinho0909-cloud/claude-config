"""Faixa do gancho no estilo validado: 2 linhas pretas em placa branca + linha branca em placa vermelha (1080x420, PNG transparente).
uso: python faixa.py "LINHA 1" "LINHA 2" "100% AU CROCHET" saida.png
(para a versão com cores de Natal verde/vermelho/dourado use faixa_natal.py com os mesmos argumentos)
"""
import sys
from PIL import Image, ImageDraw, ImageFont

l1, l2, red, out = sys.argv[1:5]
W, FB = 1080, 'C:/Windows/Fonts/arialbd.ttf'
im = Image.new('RGBA', (W, 420), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
f1 = ImageFont.truetype(FB, 64)
while max(d.textlength(l1, font=f1), d.textlength(l2, font=f1)) > W - 120: f1 = ImageFont.truetype(FB, f1.size - 2)
f2 = ImageFont.truetype(FB, 92)
while d.textlength(red, font=f2) > W - 120: f2 = ImageFont.truetype(FB, f2.size - 2)
tw = max(d.textlength(l1, font=f1), d.textlength(l2, font=f1))
d.rounded_rectangle(((W - tw) / 2 - 40, 10, (W + tw) / 2 + 40, 190), radius=18, fill=(255, 255, 255, 255))
d.text((W / 2, 60), l1, font=f1, fill=(20, 20, 20), anchor='mm'); d.text((W / 2, 140), l2, font=f1, fill=(20, 20, 20), anchor='mm')
rw = d.textlength(red, font=f2)
d.rounded_rectangle(((W - rw) / 2 - 42, 210, (W + rw) / 2 + 42, 331), radius=14, fill=(200, 24, 36, 255))
d.text((W / 2, 272), red, font=f2, fill=(255, 255, 255), anchor='mm')
im.save(out)
print('OK', out)
