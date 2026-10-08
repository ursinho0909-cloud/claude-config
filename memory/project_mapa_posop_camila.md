---
name: project_mapa_posop_camila
description: "Parceria com fisio Camila Cleto Jardim (@fisiocamilacleto, pós-op Itapetininga) — \"Mapa do Pós-Operatório\" p/ profissionais, modelo Dra Ana Corso (Mapa Toxina Pro R$97)"
metadata:
  node_type: memory
  type: project
  originSessionId: 9b1592bf-b71a-4bb8-b37b-71750db94712
  modified: 2026-09-30T12:21:55.395Z
---

Parceria iniciada 2026-09-30. Camila = fisio dermato funcional, 8 anos, "referência em pós-operatório região de Itapetininga", 4,3k seguidores, podcast Café sem Filtro. Material original dela (PDF slides 51 págs, Downloads\Drenagem_Linfatica__20250721_090128_0000.pdf) = teoria de drenagem em slides bege, SEM manobras, fotos de internet.

Modelo a copiar: Dra Ana Corso (page 131028756763362) — apostila "Mapa Toxina Pro" R$97 Hotmart, anúncio direto pro checkout, vídeos dela folheando a apostila impressa.

Decisão (30/09): oferta principal = **Mapa do Pós-Operatório** pra profissionais (não drenagem genérica — concorre com curso grátis c/ certificado; não leiga). Pós-op = equivalente da toxina (medo de errar + ticket alto). 2º produto = guia pra paciente operada. Lipedema (7.600 anúncios BR) = 3º/bônus. Copy v1 (versão drenagem) em Desktop\PROJETOS\mapa-drenagem-linfatica\COPY_APOSTILA.md.

**Why:** drenagem genérica tem ~360 anúncios de escola com certificado grátis/R$67; pós-op só cirurgião anuncia.
**How to apply:** conteúdo técnico das manobras/protocolos vem da Camila (marcado [CAMILA]), nunca inventar. Validar com enquete no story dela antes de ilustrar. Divisão da parceria ainda não fechada.

Pipeline de fichas (30/09): ilustrações ChatGPT (Manus bloqueou por política; prompts "seguros" = top+short de ciclista nude, "manual de fisioterapia", sem palavras íntimas) em ilustracoes/lote01 → `fichas/build.py` + `fichas_lote1.py` desenham setas/gânglios em SVG por coordenada (832x1248) sobre template.html → PNG+PDF. Fichas 12-17 prontas como RASCUNHO (sequências minhas, pela lógica de quadrantes do material dela); faltam 03 corpo frente e 08 braço (refazer). Perguntas pra Camila em fichas/perguntas-*.png.
Atualização 30/09: PDF único fichas/Mapa-Pos-Op_Fichas_RASCUNHO.pdf com 13 págs (04 sistema, 05 manobras, 12-22 cirurgias incl. lipoabdomino, rino, lifting/blefaro). Manobras = nomes clássicos Vodder com símbolos de movimento (sem mãos); ilustração de mãos depende de vídeo da Camila. Gestante (bônus) ainda sem ilustração no estilo.
Apostila completa 30/09: Desktop\PROJETOS\mapa-drenagem-linfatica\Mapa-da-Drenagem-Pos-Operatoria_RASCUNHO.pdf (28 págs, 13,8 MB). Remontar com: cd fichas && python montar_apostila.py [arte-capa.png]. Foto Camila (Instagram, texto do post apagado) em fotos-camila\camila-quem-e.jpg. Capa segue padrão Ana (modelo, não a autora); prompt da arte em GPT_CAPA.txt. Downloads múltiplos do Chrome são bloqueados: baixar 1 por vez.
v2 30/09: 35 págs, 15 cirurgias (+combinadas, explante, pós-bariátrica, prótese glúteo), capa GPT em ilustracoes\capa\capa-final-a4.png (15 editado em PIL), aberturas de módulo, semáforo/ícones SVG. Fotos de objetos: GPT_OBJETOS.txt -> ilustracoes\objetos\{dreno,cinta,placa}.png entram sozinhas. NÃO usar imagens do Google (direito autoral).
v3 30/09: fotos reais do Pexels (licença comercial livre) em fotos-reais\ (manobras x4, sala, aberturas M1/M2), fontes em fotos-reais\CREDITOS_PEXELS.txt. Baixar Pexels via curl images.pexels.com/photos/ID/pexels-photo-ID.jpeg?w=1600 (sem limite de download do Chrome).
