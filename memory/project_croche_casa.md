---
name: project_croche_casa
description: Crochê para Casa (100 receitas + 4 bônus) traduzido DE (Desktop\CROCHE ALEMANHA) e FR (Desktop\CROCHE FRANÇA, 29/09); pipeline OCR+inpaint reutilizável p/ IT/PT
metadata:
  node_type: memory
  type: project
  originSessionId: d0af3b83-b6b9-459b-9e1d-c50c70faed58
  modified: 2026-09-28T20:31:19.294Z
---

Info-produto "Crochê para Casa" (material do usuário, feito no Manus, fonte em Desktop\MATERIAL CHOCHE). Mesma oferta p/ Alemanha, França, Itália (+ Portugal com o PT original ajustado PT-PT). Ordem: DE → FR → PT → IT; site depois (padrão Pilates).

Status em 2026-09-28: versão DE PRONTA em Desktop\CROCHE ALEMANHA ("100 Häkelanleitungen fürs Zuhause.pdf" 29 MB, 101 p. + BONUS 1-4.pdf), aguardando revisão do usuário.

Pipeline em CROCHE ALEMANHA\_quellen (sem git): extract.py → ocr.py/ocr2.py (RapidOCR) → blocks.py → traduções tr_<lang>/*.txt (idx\ttexto, "|" por linha, "=" mantém, "~" apaga) → render.py <lang> (inpaint + redesenho) → overrides_<lang>.json (por bloco "pasta/pNNN:x,y" e "pNNN:extra" com textos manuais) → hdr.py + hdr_spec.json (cabeçalhos com título grande itálico, p060-p101) → cover_de.py (capa) → ins_de.py (imagens embutidas nos bônus) → vec_render.py (páginas vetoriais dos bônus) → assemble.py.
Pra outro idioma: copiar _quellen, criar tr_fr etc. reaproveitando chaves de to_translate.json; overrides/hdr_spec/cover precisam de versão do idioma.

Status 2026-09-29: versão FR PRONTA em Desktop\CROCHE FRANÇA ("100 Modèles au crochet pour la maison.pdf" 101 p. + BONUS 1-4), traduzida a partir do DE (tr_fr, tr_vec_fr_*, overrides_fr.json via mk_ovr_fr.py, cover_fr.py, ins_fr.py, assemble_fr.py). Registro "vous", abreviações ml/mc/ms/B/DB/dB. Usuário pôs order bumps FR próprios na mesma pasta.
Defeitos herdados que continuam no DE (corrigidos só no FR): "de Crochê" em PT na capa do Bônus 4; placa "HERZLICH" gigante na foto do p043; texto branco sobre foto no passo 3 do p063. Defeitos do layout original (nos dois): cabeçalho vazio da tabela TEX no Bônus 1 p.4 e cards sobrepondo o título no Bônus 3 p.5.
Render é lento (~20 s/página, ~35 min o livro todo).
