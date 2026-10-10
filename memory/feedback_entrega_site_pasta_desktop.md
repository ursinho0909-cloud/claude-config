---
name: Entrega de sites clonados — sempre 2 artefatos no Desktop
description: Toda vez que usar my-clone (ou Next.js com output:export) para clonar/mexer em site, gerar SEMPRE 2 artefatos no Desktop: pasta com index para o PC do usuário + pacote enviável com launcher .bat. Nunca falar em localhost como entrega.
type: feedback
originSessionId: f3eab526-522f-4a59-aa05-61a9c6550eff
---
Sempre que mexer no projeto `C:\Users\Pc\Desktop\my-clone` ou usar qualquer Next.js com `output: "export"`, ENTREGAR SEMPRE 2 artefatos:

## Artefato 1 — Pasta no Desktop (PRA O PC DO USUÁRIO)
- Caminho: `C:\Users\Pc\Desktop\<nome-do-site>\` (ex.: `universodepapel`)
- Conteúdo: cópia limpa de `out/` (index.html + _next/ + images/ + favicon/icon.png + etc.)
- Esta pasta é o que o usuário vai eventualmente subir num Netlify/Vercel/cPanel

## Artefato 2 — Pacote enviável (PRA MANDAR PRA OUTRA PESSOA)
A mesma pasta acima também deve conter 3 arquivos extras pra virar pacote "tudo-em-um" pra Windows:
- `ABRIR-SITE.bat` — launcher que o destinatário clica 2x
- `_servidor.ps1` — servidor PowerShell HttpListener na porta 8765 (built-in do Windows, sem instalação)
- `LEIA-ME.txt` — instruções: clique 2x no .bat → janela preta abre → navegador abre sozinho. Mencionar que se o Windows mostrar "O Windows protegeu seu PC", clicar em "Mais informações" → "Executar mesmo assim".

E por fim gerar `C:\Users\Pc\Desktop\<nome>.zip` com TUDO dentro (pasta inteira + os 3 arquivos extras). Esse é o que ele manda por WhatsApp/Drive/email.

## Fluxo após qualquer edit
1. `npm run build` no projeto
2. Apagar e recriar a pasta `<nome>` no Desktop a partir de `out/`
3. Recolocar `ABRIR-SITE.bat`, `_servidor.ps1`, `LEIA-ME.txt` dentro (eles somem a cada rebuild)
4. Recriar o `<nome>.zip` a partir da pasta
5. Confirmar pro usuário os 2 caminhos: pasta e zip

## Vocabulário (IMPORTANTE)
- Falar SEMPRE em "index" / "pasta no Desktop" / "arquivo do site"
- NUNCA terminar tarefa com "veja em localhost:3000" — o usuário não considera localhost uma entrega
- Localhost é só pra preview interno meu, nunca pra apresentar resultado

**Why:** O usuário trabalha em vários PCs (vai mexer em outro PC amanhã) e precisa que cada entrega seja portátil. Ele não é técnico — abrir `index.html` direto trava por CORS no Next.js (ES modules bloqueados em `file://`), então o pacote com `.bat` é a única forma confiável de mandar offline. Localhost só faz sentido enquanto eu estou rodando preview internamente.

**How to apply:** Antes de dizer "pronto" em qualquer mudança no site, conferir mentalmente: (1) pasta atualizada no Desktop? (2) os 3 arquivos extras estão dentro dela? (3) zip recriado? Se algum dos 3 faltar, voltar e completar antes de devolver a resposta.
