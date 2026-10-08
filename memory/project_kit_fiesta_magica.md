---
name: project-kit-fiesta-magica
description: "Info-produto LATAM \"+10.000 Moldes de Fiesta Infantil\" (Mãe Festeira), landing live em kit-fiesta-magica.pages.dev"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3975077d-6a50-4f6e-95de-aa370edd9fc2
  modified: 2026-08-13T15:53:36.318Z
---

Info-produto LATAM em ES: **"+10.000 Moldes de Fiesta Infantil"**, marca *Mãe Festeira*, US$ 9,90.

- Pasta: `C:\Users\User\Desktop\mae-festeira-landing` — **não é repo git**, não está no GitHub (o outro PC não tem)
- Deploy: `python deploy.py` → CF Pages projeto `kit-fiesta-magica`, live em `kit-fiesta-magica.pages.dev`
- O `deploy.py` usa **lista branca** (`index.html` + `img` + `video`) de propósito: `entrega/` contém o PDF com os links do Google Drive do produto pago, e Pages publicaria tudo se não fosse filtrado. Não trocar por lista de exclusões.
- Checkout: Hotmart `pay.hotmart.com/Q107133124R` (ele é **produtor**). Link centralizado na var `CHECKOUT` do `index.html`, aplicada aos `[data-checkout]`.
- BM: **Studio Fernanda Milan** (`520484365968994`)

Tracking (fechado em 2026-08-13, validado no Network):
- Pixel **`pixel-FiestaLT` / `2243242263102632`** no `<head>` da landing, com `PageView`
- `InitiateCheckout` (value 9.90 USD) **só no botão `id="checkout"`** — o segundo botão de compra não dispara, por decisão dele contra duplicação
- `Purchase` vem do Hotmart (Configuração de Pixel → envio via WEB → só Compra aprovada)
- **CAPI não configurada**: o token está bloqueado porque o BM não tem e-mail comercial verificado. Ver [[project-pirataria-tu-aula-digital]] para o gotcha do Hotmail vs `@facebookmail.com` — usar Gmail no e-mail comercial.
