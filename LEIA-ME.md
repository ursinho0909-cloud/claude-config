# claude-config — o "cérebro" do Claude Code nos 2 PCs

Aqui ficam a memória, as skills e as configurações. Login (`.credentials.json`) e `.env` **não** vêm pra cá.

## Outro PC (só a primeira vez)
```
winget install GitHub.cli
gh auth login
gh repo clone ursinho0909-cloud/claude-config C:\Users\<seu-usuario>\claude-config
powershell -ExecutionPolicy Bypass -File C:\Users\<seu-usuario>\claude-config\instalar-claude.ps1
```
Depois instale a extensão **Claude in Chrome** e, no terminal do Claude, aperte **Shift+Tab** até ficar em **auto**.

## Dia a dia (nos dois PCs)
Rode `sync-claude.ps1` **ao começar** (puxa o que o outro PC aprendeu) e **ao terminar** (envia o que este aprendeu).
Ou só peça pro Claude: "sincroniza a memória".

Abra o Claude sempre a partir da pasta do usuário (`C:\Users\<usuario>`), senão ele procura a memória em outra pasta.
