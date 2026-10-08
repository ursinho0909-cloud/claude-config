---
name: project-ugc-croche-modelo
description: "Criativo UGC vencedor do Crochê FR (\"ugc ofi.mp4\", 02/10/2026) — estrutura e roteiro; versões FR/PT/DE escritas em 05/10"
metadata:
  node_type: memory
  type: project
  originSessionId: df30c755-fde9-4e2c-9c48-3d6013e099d9
  modified: 2026-10-05T17:17:43.632Z
---

Vencedor: Desktop\CTV CROCHE FRANÇA\ugc ofi.mp4 (55 s, 9:16). Tela dividida: avatar IA mulher ~50 anos em selfie na sala (cima) + faixa fixa "+100 RECETTES DE CROCHET POUR LA MAISON" + legenda palavra a palavra amarela + b-roll (baixo) trocando a cada 2-3 s.
Roteiro: "pilha de novelos num canto" → "sempre as mesmas peças" → "encontrei um guia" → +100 modelos passo a passo → exemplos (tapete, cesto, almofada, sousplat) → material/etapas/detalhes → escolhe e começa → 100% digital → "sempre no meu telemóvel ao lado do cesto" → CTA "commentez je le veux".

Roteiros novos em Desktop\CTV UGC CROCHE 3 PAISES\ROTEIROS-UGC-CROCHE.md: FR = gancho novo (vizinha elogiou o cesto); PT e DE = vencedor adaptado.

Pipeline em Desktop\CTV UGC CROCHE 3 PAISES: src\broll.py gera broll_pt/de.mp4 (cenas neutras do vídeo FR + capa/fichas/celular do PDF do país); src\compose.py <lang> <avatar.mp4> monta avatar em cima + b-roll + faixa (fonte Luckiest Guy em fonts\) + legenda palavra a palavra via faster-whisper. Avatar é gerado pelo usuário na HeyGen web (sem API key aqui). FR original tem marca d'água HeyGen.

**How to apply:** em país novo, levar o roteiro vencedor adaptado primeiro; no país onde ele já roda, mudar só o gancho e manter a estrutura. Serve de molde para UGC de outras ofertas (ex.: [[project-pain-retrouve]]).
