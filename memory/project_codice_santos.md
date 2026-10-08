---
name: project-codice-santos
description: "Códice de los Santos (LATAM) — landing, área de membros, Hotmart e pixels; estado em 18/08/2026"
metadata: 
  node_type: memory
  type: project
  originSessionId: 608b577b-fc34-43d0-af3f-a2fe5970b380
  modified: 2026-08-18T14:20:53.821Z
---

3º da série Códice (depois de [[project-codice-mitologia]] e [[project-codice-prehistorico]]).
Info-produto católico infantil ES/LATAM: 100 expedientes ilustrados de santos, 5 módulos × 20.

| Peça | Onde |
|---|---|
| Landing | santos-para-ninos.pages.dev · pasta `Desktop\codice-santos-landing` · repo `codice-santos-landing` |
| Área de membros | santos-area-miembros.pages.dev · pasta `Desktop\codice-santos-area` · repo `codice-santos-area` |
| Checkout | Hotmart `M107204069M` (`pay.hotmart.com/M107204069M?checkoutMode=10`), US$ 9,90 |
| Pixel UTMify | `6a84639365bff3914f76042c` (instalado 18/08/2026) |
| Pixel Meta | `2492805024464547` — **carregado pela própria UTMify**, não instalar snippet separado senão duplica evento |

Estado em 18/08/2026:
- 50 das 100 lâminas prontas. As outras 50 aparecem com **cadeado** e a data "19 de agosto · 12:00" — nada automático, o cadeado sai quando o arquivo existir e se rodar o build.
- As 5 capas de módulo e a de bônus estão no ar.
- Download do módulo é **PDF A4 a 200 DPI** (uma lâmina por folha), não ZIP.
- Falta: os 3 PDFs de bônus, e plugar Purchase da UTMify na Hotmart.

Pendências de arte conhecidas (ver `PENDIENTES.md` no repo da área):
- `#001 San Pedro` escreve `CODICE` **sem til** — única das 50 assim, não usar em criativo.
- `#082 San Martín de Porres` está numerado como `#045` e é a única em 1024px.
- Módulos AMIGOS, TIERRA e NINOS 01-02 vieram em 2:3 em vez de A4 — é o que deixa margem branca ao imprimir.
- San Sebastián aparece seminu e amarrado ao poste na capa do módulo 2 e na de bônus (regra de tom proíbe).

Order bump em produção: "30 Días Caminando con Jesús", `Desktop\30-dias-caminando-con-jesus`, PDF vetorial de 34 páginas gerado por `build.py` (HTML → Edge headless). Ver [[feedback-pdf-vetorial-html]].
