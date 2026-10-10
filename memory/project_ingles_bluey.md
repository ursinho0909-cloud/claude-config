---
name: Projeto Inglés en Casa · 10 Cuadernos inspirados en Bluey
description: Info-produto de inglês infantil ES/LATAM, US$9.90, landing + área de membros já no ar, PDF de entrega Hotmart pronto
type: project
originSessionId: d3e68d85-a40f-4393-97c3-ac3e817f1d6a
---
Info-produto **10 Cuadernos de Inglés inspirados en Bluey** — 100 fichas, +400 exercícios, +300 palavras, US$ 9,90.

**Ângulo da oferta:** o gancho não é "aprender inglês" — é **"tu hijo aprende inglés aunque tú no sepas inglés"**. Objeção nº 1 da mãe LATAM, resolvida pelo Bônus #1 (guia de pronúncia escrita em espanhol). Toda a copy aponta pra isso. Âncora de preço na unidade (10 cuadernos), não na atividade.

**Repos + live:**
- Landing → `ursinho0909-cloud/ingles-en-casa-landing` → https://ingles-para-ninos.pages.dev (pasta local: `Desktop\ingles-bluey-landing`)
- Área de membros → `ursinho0909-cloud/ingles-area-miembros` → https://ingles-para-ninos-miembros.pages.dev (pasta local: `Desktop\ingles-area-miembros`)

**10 cuadernos:** Saludos, Colores, Números 1-20, Familia, Cuerpo, Animales, Comida, Casa, Rutina Diaria, Primeras Frases.
**3 bônus:** Guía de Pronunciación pra pais (o mais importante), 100 Flashcards Recortables, Póster de Pared.

**PDF de entrega Hotmart:** `entrega/acceso-area-de-miembros.pdf` já pronto (2 páginas: banner Bluey no topo + CTA laranja "ABRIR MI ÁREA DE MIEMBROS" + como entrar; página 2 com 10 cuadernos + 3 bonos). Gerado por `scripts/make_entrega_pdf.py` (reportlab + PIL, converte banner.webp em memória).

**Paleta Bluey (do styles.css):** azul primário #4FA3E3, azul escuro #1B4F8A, laranja Bingo #F28C38, dourado #F3C24B, cream #FFF9F0, text-dark #12314F.

**Deploy:** Cloudflare Pages (auto-deploy do repo). Nunca `wrangler pages deploy .` direto — usa `deploy.py` com lista branca (senão vaza `.trabajo/`).

**Why:** Produto de nicho grande (mães LATAM que querem inglês pros filhos mas não sabem inglês). Bluey é o desenho de referência dessa faixa. Preço baixo pra volume.

**How to apply:** Ao mexer nesses repos, seguir a paleta Bluey; se criar novo entregável, replicar padrão do PDF (banner + botão laranja + como entrar + lista do incluído). Nunca falar em "aprender inglês" — sempre "que tu hijo aprenda aunque tú no sepas".
