---
name: project-coreano-upsell-video
description: Upsell de aulas em vídeo dentro da área de membros ES (Coreano Sin Complicaciones) usando NotebookLM Video Overview + roteiros que eu gero a partir dos mapas mentais existentes
metadata: 
  node_type: memory
  type: project
  originSessionId: b23284c3-0da7-49d4-9d2d-493c4f230350
---

Em fase de validação (iniciado 2026-06-25). Plano: gerar aulas em vídeo (~6-8 min cada) baseadas nos 90+ mapas mentais existentes da área ES, usando NotebookLM Video Overview. Cliente que compra o pack base (US$9,90 Hotmart Internacional) terá opção de upsell para acessar as aulas em vídeo dentro da própria área de membros.

**Why:** Aumentar AOV. Mapas mentais (PNG) são "estáticos"; vídeo aumenta percepção de valor e justifica upsell. NotebookLM gera material rápido (~5h trabalho real pra 30 aulas) sem precisar gravar vídeo real nem usar avatar pago. Aproveita conteúdo já existente.

**How to apply:**
- Eu (Claude) leio o mapa mental (PNG do site coreano-area-miembros.pages.dev/modulos-content/...) e escrevo roteiro estruturado em seções markdown
- Usuário cola roteiro como source no NotebookLM → escolhe estilo visual → cola instruções de foco → gera
- Saída: MP4 de 6-10 min com 2 hosts conversando em ES + slides visuais
- Sequência futura: validar com banner pré-venda → produzir 5 piloto → escalar pra 30+ se aprovar

**Status 2026-07-07:**
- VALIDADO E ESCALANDO. Preço do pack DEFINIDO em **US$ 8,90** (mudado 2026-07-07 na página upsell, na área de membros modulo-videoclases E no Hotmart produto B106504030B). Checkout Hotmart B106504030B.
- **7 vídeos já produzidos** (no Drive): 7_Frases_en_Coreano (isca), 10_Frases_de_K-Dramas, El_Alfabeto (Hangul), Escribe_Tu_Nombre, Korean_Hierarchy, Letras_Secretas_de_BTS, Números_en_Coreano
- **Roteiros no repo** (aulas-videoclases-roteiros/): aula01 (isca fandom), aula02 (kdrama 10 frases), + 4 NOVOS gerados 2026-07-07: aula03 K-Pop (comentar Instagram do bias), aula04 K-Drama (amor/confissões), aula05 Cultura (Aegyo/Kawaii), aula06 Viaje (pedir comida/Aquarela)
- Meta do pack = 30 videoclases: 10 K-Pop + 10 K-Drama + 5 Cultura + 5 Viaje. Faltam ~19 roteiros pra completar.
- CIERRE dos roteiros INTERNOS (aula03+) motiva próxima aula, SEM pitch de venda (isca aula01 é a única com CTA de compra)

**Template de roteiro (formato validado, ~3min leitura → ~7min áudio NotebookLM):**
```
TÍTULO: <nome da aula>
NIVEL: <A1/A2/.../K-pop>
DURACIÓN OBJETIVO: 6-8 minutos
TONO: <energético/amigável/técnico>

INTRODUÇÃO (15-30s) — gancho + o que vai aprender
SEÇÃO 1 (30-90s) — conceito principal
SEÇÃO 2 (30-90s) — exemplos
SEÇÃO 3 (30-90s) — aplicação prática
SEÇÃO 4 (30-90s) — opcional, depende do tema
CIERRE (15-30s) — resumo + próxima aula + motivação prática
```
Cada conceito coreano = Hangul GRANDE + romanização + tradução ES em cursiva.

**Instrução padrão de foco pra colar no NotebookLM (segundo campo da personalização):**
"Sé conciso. Máximo 8 minutos en español neutro latinoamericano. Tono [varia por tema, ex: 'energético tipo fan a fan' para K-pop / 'profesor amigable' para A1]. Ve directo al grano sin digresiones, anécdotas ni repeticiones. Cubre TODOS los puntos del material. Pronuncia caracteres coreanos con claridad y muéstralos GRANDES en pantalla. Empieza con energía y termina motivando la práctica."

**Guia de estilo visual NotebookLM por tipo de aula:**
- K-pop / K-drama / Fandom → **Anime**
- A1 Fundamentos (Hangul, vocab básico) → **Kawaii**
- A2 Gramática (partículas, verbos, conectores) → **Quadro branco**
- B1/B2 Estruturas avançadas → **Quadro branco** ou **Clássico**
- Cultura coreana, comida, viagem → **Aquarela**
- Filosofia/conceitos (jeong, han, nunchi) → **Aquarela**
- História da Coreia, dinastias, palácios → **Impressão retrô**
- Vocab moderno (tech, finanças, negócios) → **Clássico**
- Curiosidades, expressões idiomáticas → **Retrô**
- Em dúvida → **Seleção automática**

**Próximos passos quando retomar (amanhã):**
1. Pedir feedback do vídeo K-drama gerado
2. Se aprovou → fechar preço + hosting → eu gero 5 roteiros piloto em batch
3. Se não aprovou → pivot pra HeyGen avatar OU áudio NotebookLM + Canva manual
4. Discutir: banner "ACCESO ANTICIPADO" na área pra validar demanda antes de produzir as 30+
5. Possibilidade de automação via script Python+FFmpeg (Ken Burns nos PNGs dos mapas + áudio NotebookLM) — discutido mas não implementado

**Conexões com outras memórias:**
- [[project-coreano-area-miembros-es]] — área de membros onde o upsell será integrado
- [[user-business]] — modelo info-produto BR→LATAM
- [[feedback-directness]] — playbook real sem hedging
