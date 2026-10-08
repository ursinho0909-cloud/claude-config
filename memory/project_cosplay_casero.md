---
name: project-cosplay-casero
description: "info-produto LATAM \"+100 cosplays caseros/baratos\" (ES), 10 módulos de anime x 10 personagens, US$9,90 + bônus"
metadata: 
  node_type: memory
  type: project
  originSessionId: ed58b0d7-6d38-4c7b-997a-2bc48e4f14be
---

Info-produto novo (iniciado 2026-07-11) pra LATAM/ES: **"+100 Cosplays Caseros/Baratos"**, infográfico passo a passo "Cómo hacer un cosplay increíble" por personagem (modelo de referência que o user mandou = infográfico craft/scrapbook estilo Naruto).

**Estrutura:** 10 módulos = 10 animes mais famosos, 10 personagens cada = 100. Módulos: Naruto, Dragon Ball, One Piece, Demon Slayer, My Hero Academia, Jujutsu Kaisen, Sailor Moon, Pokémon, Spy x Family, Death Note. (Evitar cosplay difícil tipo armadura/equipamento — fura a promessa "faço em casa barato".)

**Ângulo de venda:** ECONOMIA ("pare de pagar caro em fantasia"), anime é só isca. NÃO competir com tutorial grátis. Preço US$9,90 + order bump + bônus (maquiagem cosplay, pelucas caseras, cosplay de última hora, dónde comprar barato).

**DECISÃO TÉCNICA CHAVE:** gerador de imagem (Manus) EMBOLA o texto em espanhol ("NARUTO UZUAMMI") — inviável pros 100. Solução: **template HTML** (texto real, nunca embola, escala trocando --accent + texto) + ilustrações do Manus só (busto + resultado, fundo transparente) encaixadas nos slots. Manus gera HTML e renderiza a PNG 2000x2666, NUNCA "pinta" as letras.

**Arquivos em `Desktop\cosplay-casero\`:** `template\cosplay_naruto.html` (molde-ouro preenchido, page 1000x1333), `ENTREGAR_AO_MANUS.txt` (prompt com 10 personagens + cores de acento). Também PRODUCCION.md e PROMPT_FINAL_MANUS.txt (versões antigas do fluxo).

**Status:** template pronto, aguardando Manus gerar as 10 do lote-teste. Se Manus travar no render, user manda HTMLs+ilustrações e eu ploto/renderizo. Marca provável: "Cosplay Sin Complicaciones". Lançar mirando Halloween/temporada de convenção. Segue padrão [[project-coreano-launch-latam]] (Hotmart Internacional). É oferta B (impulso mais fraco que educação), mas custo de produção ~zero.
