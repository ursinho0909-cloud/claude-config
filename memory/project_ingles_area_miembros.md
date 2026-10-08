---
name: project_ingles_area_miembros
description: "Área de membros do Inglés en Casa — casca pronta (10 cadernos × 10 fichas), repo ingles-area-miembros, faltam todas as imagens"
metadata: 
  node_type: memory
  type: project
  originSessionId: 43eb19eb-09cf-4a86-bbc1-2c5be43e8ec2
  modified: 2026-08-11T14:22:12.880Z
---

Entregável de [[project_ingles_en_casa]], criado em 2026-08-11.

- **Pasta:** `C:\Users\User\Desktop\ingles-area-miembros`
- **Repo:** github.com/ursinho0909-cloud/ingles-area-miembros (privado)
- **CF Pages:** projeto `ingles-area-miembros` — **ainda não criado**
- **Local:** `python -m http.server 8902`

Clone estrutural de `caligrafia-area-miembros` — **mesmo `styles.css` e `app.js`, sem uma linha alterada**. Gerado por script a partir do template (o script fica em `scratchpad/gen_ingles_area.py`), o que preservou SVGs, lightbox e navegação intactos.

**Estado:** só a casca. `index.html` + `cuaderno-1..10.html`, 10 slots de ficha em cada, todos mostrando placeholder tracejado. Nenhuma imagem existe além das pastas com `.gitkeep`.

**Armadilha do clone:** nos cadernos em que o título curto == a tag da sidebar (Vocales, Sílabas, Palabras, Frases), uma substituição global de título reescreve o `<small>` da sidebar junto. Restringir ao contexto (`<h1>…</h1>`, `<small>…</small>`) e aplicar na ordem 1→10. Vale pra qualquer clone futuro dessa estrutura.

`.trabajo/build_cuadernos_pdf.py` monta os PDFs de download (capa = página 1 + 10 fichas, A4 150 dpi). Já com os nomes de arquivo do inglês.

**Regra das fichas:** cada uma precisa de *palabra en inglés + dibujo + pronunciación en español* — é o que a landing promete.
