---
name: project-ejercicios-faciales
description: "Info-produto LATAM +100 Ejercicios Faciales Ilustrados (ES) — 6 módulos por zona, fichas geradas por prompt no ChatGPT, entregável em PDF por módulo"
metadata:
  type: project
---

Info-produto LATAM em ES, decidido e iniciado 2026-09-02. Ver [[project-pt-latam-split-2026]].

**Nome:** "+100 Ejercicios Faciales Ilustrados — Entrena los músculos de tu rostro en casa".
Camada de âncora na landing: "7 protocolos · +100 fichas ilustradas".

**Estrutura — 100 fichas de exercício + 20 de apoio (entrega 120):**
M1 Frente y entrecejo 14 (lavanda) · M2 Ojos y mirada 16 (azul noche) ·
M3 Mejillas y pómulos 16 (coral) · M4 Boca y contorno labial 14 (frambuesa) ·
M5 Mandíbula y papada 22 (ciruela) · M6 Cuello y escote 18 (salvia) ·
M0 Base 8 (grafito) · M7 Rutinas 12 (ocre). Cor por módulo, numeração `M.N`.

**Regra que faz as 100 não se repetirem:** cada módulo mistura ~60% ejercicio,
~30% automasaje/drenaje, ~10% estiramiento. As de massagem são as que sustentam
a porta profissional (a esteticista executa em cabine).

**Pastas:**
- `Desktop\PROJETOS\ejercicios-faciales\` — `prompt-modulo-5.md`, `prompt-modulo-6.md`
- `Desktop\entregavel-faciais\` — PDFs por módulo (capa + fichas)

**Produção:** ChatGPT gera a ficha inteira (texto sai perfeito, ao contrário do
histórico). Formato fixo **1536 × 2304**. Prompt = regras fixas + texto LITERAL
por ficha + checklist final.

**Estado em 2026-09-02 (fim da sessão):**
- Prontos: **M3** (3.1–3.10, coral), **M4** (4.1–4.10, frambuesa),
  **M5** (5.1–5.11, ciruela), **M6** (6.1–6.10, salvia) — 41 fichas.
- Prompts em `Desktop\PROJETOS\ejercicios-faciales\prompt-modulo-{3,4,5,6}.md`
- PDFs (capa + fichas) em `Desktop\entregavel-faciais\`
- **Faltam M2 · Ojos y mirada (azul noche) e M1 · Frente y entrecejo (lavanda)**,
  deixados para o fim por serem os mais fracos em tráfego frio.
- Falta também completar M5 (12 fichas até às 22) e M6 (8 até às 18), e regenerar
  a 5.1 a 1536×2304 — saiu a 1054×1492.

Badge por módulo já gerado: M3 #994A35 · M4 #6D3246 · M5 #583C53 · M6 #495C51.

**Gotchas já apanhados:**
- "marca de agua al 3% de opacidad" fez o modelo imprimir **"3%"** na ficha.
  Nunca pôr percentagens na instrução de marca de água.
- A 5.1 saiu a 1054×1492 (A4) e o resto a 1536×2304 — falta regenerar a 5.1.
- O ícone de MÚSCULOS INVOLUCRADOS continua a sair bíceps mesmo pedindo cabeça de perfil.
- Capa: primeira versão tinha "RESULTADOS REALES / REJUVENECE / RESULTADOS QUE SE
  NOTAN" — promessas de resultado que o Meta reprova em aparência pessoal.
  Corrigido para "PASO A PASO / RELAJA / +100 FICHAS ILUSTRADAS". Manter duas
  versões da capa: produto e anúncio.

**Criativos por ordem:** papada > cuello y escote > código de barras > óvalo.
Olhos e entrecejo são fracos em tráfego frio (movimento subtil, restrição extra).
O movimento em si é o anúncio — antes/depois é proibido.

**Why:** nicho sem concorrência paga em ES (verificado pelo user). Ser primeiro
significa sem âncora de preço a puxar para baixo, e CPM barato enquanto durar.

**How to apply:** validar com ~15 fichas + landing + $50-100 antes de produzir as
outras 85 ([[feedback-nao-inflar-entregavel]]). Marca de água em todas e área de
membros com auth desde o início — já foi clonado antes ([[project-pirataria-tu-aula-digital]]).
