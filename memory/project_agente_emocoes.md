---
name: project_agente_emocoes
description: "Info-produto BR \"Agente das Emoções\" — +100 atividades socioemocionais em formato de missão secreta, foco professora 1º-5º ano, modelo visual aprovado 2026-09-14"
metadata: 
  node_type: memory
  type: project
  originSessionId: b5ae0295-9679-4791-bb02-07334668685d
  modified: 2026-09-14T18:44:23.538Z
---

Oferta BR: "+100 atividades socioemocionais" com gancho "Agente das Emoções: Missões Secretas". Comprador principal = professora do Fundamental I (1º ao 5º ano); mãe é secundário. Pico de compra professora jan/fev; lançar antes pra validar criativo.

Padrão de ficha APROVADO (2026-09-14, "Detector de Gentileza", Missão 07): A4 retrato, cabeçalho mascote agente + CONFIDENCIAL + selo BNCC, título, 1 linha de instrução com legenda visual, grade 3x2 de cenas numeradas (criança responde em cima das imagens), "Minha missão de hoje" com 3 cartões, rodapé MISSÃO CUMPRIDA. Imagem de referência: Downloads\ChatGPT_Image_14_de_set._de_2026,_09_04_34.png

**Why:** usuário rejeitou a 1ª versão (texto, 2 níveis por ano na mesma folha) — quer atividade VISUAL, focada, que a professora entenda de olhar, SEM ano escolar escrito, só alinhamento BNCC.

Pastas: prompts Manus em Desktop\PROJETOS\agente-das-emocoes\ (MODULO_1, MODULO_2, CORRECAO_MODULO_1 + MODELO_APROVADO.png). Entregável em Desktop\entregavel-socioemocionais\ (PNGs por módulo + PDF\ A4 via pymupdf, PNG→JPEG q90 senão dá ~1,8 MB/página). Numeração contínua: módulo N = missões (N-1)1..N0. Módulo 1 recebido 2026-09-14 (01/04/10 precisam correção); prompt do Módulo 2 (Raiva e Calma) pronto.

Landing (2026-09-14): Desktop\PROJETOS\agente-das-emocoes-landing\index.html, clone estrutural de archivo-secreto-clase.pages.dev (fonte em Desktop\PROJETOS\expediente-secreto). Porta local 8791. 2 ofertas: Básica 50 ativ. R$14,90 sem bônus / Completa 100 ativ. + 3 bônus (Crachá de Agente, Mural de Patentes, Certificado) R$24,90. Paleta marinho #1E2A4A + amarelo #F5B82E, fontes Fredoka/Nunito. Imagens = slots vazios; checkouts #CHECKOUT-BASICO/#CHECKOUT-COMPLETO; sem pixel; sem git ainda.

Status 2026-09-14: AS 100 FICHAS PRONTAS, 10 PDFs por módulo. Landing com imagens reais: exemplos = missões 51,15,92,22,84,54; celular = 12,33,57,61,69,74,88,100. LIVE 2026-09-14 em agente-das-emocoes.pages.dev (CF Pages, deploy via wrangler da pasta landing, sem git). UTMify pixel 6aa83e524cee13d73a472fcc no head (2026-09-14). ENTREGA\ tem PDF COMPLETO (100+3 bônus), BÁSICO (50), EXTRAS (planejamento+adaptadas+7 datas). Pendente: correções M1/M2/M4/M5. Landing tem pop-up de upgrade (básica→R$19,90 checkout zQyKko0QHy1c7XZoXegW); checkouts ggcheckout básica 8t22wgTwXpVDiJkpzeQq / completa KPbl13MpDckRcl49M8yg. fix_footer.py copia rodapé de ficha boa pras quebradas (Manus quebrou 8/10 rodapés no M7). Correções pendentes: M1 fichas 01/04/10, M2 11/13, M4 38 (diz 5 tristes, tem 3), M5 49 (tabuleiro fora de ordem). Prompt do módulo 6 (Gentileza e Empatia, 51-60, BNCC Competência 9) pronto. Manus às vezes escreve a resposta dentro do card (M42) — checar. Scripts make_pdf.py e fix_ghost.py (apaga texto fantasma sob etiqueta MISSÃO) salvos em Desktop\PROJETOS\agente-das-emocoes\. Módulos 5-10 planejados: Frustração, Gentileza/Empatia (Detector de Gentileza = Missão 51), Amizade, Respeito às Diferenças, Resolver Conflitos, Autoestima.

Erros recorrentes do Manus: escreve "MIÓSÃO/MIÓSÚLO" no cabeçalho, texto fantasma sob etiquetas, varia posição das etiquetas, tira óculos da mascote, molde de dado desalinhado.

**How to apply:** prompts ChatGPT seguem esse layout; texto literal no topo + lista exata de cenas + checklist (ver [[feedback_manus_prompt_order]]). Revisar cena por cena (gabarito depende da ordem). Bumps planejados: Missões Adaptadas (pictogramas/inclusão), Missões de Datas, Kit Mural de Patentes + combo ([[feedback_orderbump_playbook]]). Não afirmar condição do usuário no anúncio (autismo/TDAH).
