---
name: Chrome DevTools MCP — controle do Chrome pelo Claude Code
description: MCP server que deixa o Claude Code (terminal) ver e clicar no Chrome real do usuário com sessões logadas. Igual Playwright mas usa a instância aberta do Chrome.
type: reference
originSessionId: e10b02b5-a48e-4fc2-83f1-f13d7b23483f
---
# Chrome DevTools MCP

Instalado no PC "Pc" em 2026-10-07. Comando:
```
claude mcp add chrome-devtools --scope user -- npx chrome-devtools-mcp@latest
```

Config salva em `C:\Users\Pc\.claude.json` (chave `mcpServers.chrome-devtools`).

## O que destrava
Depois de instalado + Claude Code reiniciado, o Claude ganha ferramentas pra controlar o **Chrome real do usuário**:
- `navigate_page(url)`
- `click(selector)`
- `fill(selector, text)`
- `take_screenshot()`
- `list_pages()` — abas abertas
- `evaluate_script(js)`

Usa o Chrome que já tá aberto com todas sessões logadas (HeyGen, Hotmart, Gmail, ChatGPT, etc.) — não precisa logar de novo.

## Quando usar
- Baixar vídeo de app logado (HeyGen "Download" button)
- Fazer checkout Hotmart/Cakto
- Gerar imagem no ChatGPT/Nano Banana via web
- Qualquer coisa que exigiria clicar visualmente em botão de site

## Depois de instalar
**OBRIGATÓRIO fechar e reabrir o Claude Code** pra ele carregar as ferramentas novas. Sem reboot da sessão as tools do MCP não aparecem.

## No outro PC (User)
Provavelmente tem MCP equivalente (talvez Playwright MCP, talvez também chrome-devtools-mcp). Confirmar e padronizar entre os 2 PCs.
