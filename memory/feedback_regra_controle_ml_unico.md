---
name: controle-mercadolivre roda em 1 PC por vez
description: Regra crítica — o app controle-mercadolivre NÃO pode rodar nos 2 PCs ao mesmo tempo, senão o token ML quebra
type: feedback
originSessionId: 0f11b19e-a543-4fc7-a16d-84b252059897
---
**Regra:** Antes de abrir o controle-mercadolivre no PC B, DESLIGAR o app no PC A, atualizar `tokens.json` via Drive, e só então abrir no PC B.

**Why:** O app usa refresh_token do Mercado Livre que renova a cada 6h. Se os 2 PCs renovarem ao mesmo tempo, um dos dois tokens invalida e quebra o login. Também usa ngrok com domínio único `tableware-unhitched-eternal` que só aceita 1 instância ativa.

**How to apply:**
- Quando o usuário pedir pra rodar/abrir controle-mercadolivre, sempre confirmar antes: "tá rodando no outro PC agora?"
- Se trocar de PC: lembrar de (1) fechar `iniciar.bat` no PC origem, (2) rodar `ATUALIZAR_BACKUP_DRIVE.bat`, (3) esperar Drive sincronizar, (4) copiar `tokens.json` novo do Drive ANTES de abrir no PC destino.
- Se app no PC destino pedir reautorização no ML = esqueceu de copiar o token novo.
