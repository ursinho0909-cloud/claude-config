---
name: feedback-commit-reminder
description: "Ao terminar qualquer sessão de programação, sempre perguntar se quer git add/commit/push das mudanças"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee771611-29c7-428f-8237-a58c14834760
---

Sempre que terminarmos uma conversa onde mexi em arquivos de código (de qualquer projeto versionado no GitHub — ver [[project-github-sync]]), **eu devo PROATIVAMENTE perguntar ao usuário se ele quer commitar e mandar pro GitHub** antes de ele sair.

**Por que:** o usuário tem 2 PCs e quer continuar o trabalho no outro PC. Se ele esquecer de `git push`, vai abrir o outro PC e não vai ter o que ele acabou de fazer — vai duplicar trabalho ou pior, vai mexer no arquivo desatualizado e gerar conflito. Ele pediu explicitamente em 2026-05-28: "sempre que terminarmos uma conversa de programar algo voce me pergunta se eu quero salva git add". Setup completo em [[project-github-sync]].

**Como aplicar:**
1. No final de qualquer sessão onde eu editei/criei arquivos em projetos versionados (`treino-express-src`, `SITE FUNCIONAL`, `treino-meta-capi`, `controle-mercadolivre`, ou qualquer repo futuro), rodar `git -C <path> status --short` pra ver o que tá pendente.
2. Se tiver mudanças não-commitadas, perguntar algo tipo: "Tem X arquivos modificados em [projeto]. Quer que eu faça `git add . && commit + push` agora pra ficar disponível no outro PC?"
3. Se o usuário disser sim, fazer o commit com mensagem descritiva do que foi feito + push.
4. NÃO precisa perguntar se:
   - Não mexi em código (só conversa, pesquisa, planejamento)
   - O usuário já fez o push manualmente durante a sessão
   - É um projeto que ainda não foi versionado (oferecer versionar nesse caso)

**Edge cases:**
- Se tem mudanças em vários projetos, listar todos e perguntar por cada um (ou oferecer commitar todos de uma vez se forem mudanças relacionadas).
- Se o usuário disser "depois eu faço", não insistir — só lembrar que se ele esquecer, o outro PC não vai ter a versão nova.
- Se identificar que ele tá num projeto NÃO versionado mexendo em código, oferecer subir pro GitHub seguindo o padrão de [[project-github-sync]].
