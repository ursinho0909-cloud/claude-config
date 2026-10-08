---
name: project_exercicios_idosos_pt
description: "Landing PT-PT \"+500 Exercícios Ilustrados para Pessoas Idosas\", oferta única 13,90 €, pasta Desktop\\PROJETOS\\exercicios-idosos-pt"
metadata: 
  node_type: memory
  type: project
  originSessionId: ae737138-a7b0-4543-b644-63bd30e8197b
  modified: 2026-09-08T13:38:46.967Z
---

Info-produto para Portugal: "+500 Exercícios, atividades físicas e alongamentos para pessoas idosas" (PDF + 4 bónus). Público: profissionais de exercício físico, cuidadores, fisioterapeutas.

Landing em `C:\Users\User\Desktop\PROJETOS\exercicios-idosos-pt\index.html` (HTML único, sem build, sem git ainda). Imagens originais em `imgs-raw\` (do zip do Downloads), otimizadas WebP em `img\`. Preview local: `python -m http.server 8790` na pasta.

Decisões tomadas (2026-09-08):
- **Oferta única de 13,90 €** — sem pacote básico, sem pop-up, sem downsell. Ancoragem: de 89,00 €.
- Bónus com valores em euros (27/17/12/22 = 78 €), secção de bónus **depois** de "O que encontra no material" e "Para quem é indicado", colada à oferta.
- Carrossel **duplo** (duas fileiras marquee CSS em direções opostas) com as 10 fichas de exercício.
- Mockup de telemóvel com slideshow automático das fichas (padrão reutilizado das outras ofertas).
- Contador de 15 min em sessionStorage, data do dia no topo.

Pendente: link do checkout (constante `CHECKOUT_URL` no topo do `<script>`), pixel/tracking, deploy Cloudflare Pages, repo GitHub.

Copy segue [[feedback_pt_pt_vs_pt_br]]. Imagens seguem [[feedback_imagens_peso_landing]]. Relacionado: [[project_pt_latam_split_2026]], [[project_matematica_landing_pt]].

**Fichas novas via Manus (2026-09-08):** 30 exercícios em 3 blocos de 10 — Bloco 1 mobilidade/alongamento, Bloco 2 força funcional, Bloco 3 equilíbrio/coordenação/postura. Nenhum repete os 10 originais. Prompts prontos em `manus-prompts\BLOCO-*.txt` (1 prompt autónomo por ficha, estrutura de 4 partes de [[feedback_manus_prompt_order]]). Regenerar com `python _gerar.py` depois de editar `_dados_a/b/c.py`.

Estilo visual das fichas (extraído das originais): retrato 9:16, quadrado verde com nº no canto sup. esq., título 2 linhas (azul-marinho #16335E + verde #2E7D32), painel MÚSCULOS TRABALHADOS com 2 silhuetas à direita, depois COMO FAZER + DICAS IMPORTANTES lado a lado, SÉRIES E REPETIÇÕES em 3 colunas, BENEFÍCIOS em 3 colunas, faixa de rodapé com dica. Fundo creme #FBFAF7.

Entregável atual em `entregavel\` (6 PDFs do zip do cliente). Faltam os bónus "30 Sequências" e "50 Exercícios Sentados" que a landing promete. "cordenação" está mal escrito no nome de um PDF.
