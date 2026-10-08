---
name: reference-restaurar-projeto
description: Pastas locais dos repos em Desktop\PROJETOS sao descartaveis; restaurar com Desktop\restaurar-projeto.sh
metadata:
  type: reference
---

Depois da limpeza de 2026-09-08, as pastas locais dos projetos que tem repo no GitHub foram apagadas do PC. Elas sao descartaveis por design: o GitHub tem tudo, inclusive os assets pesados (que estao commitados, nao no .gitignore).

Para trabalhar em qualquer projeto de novo:

    bash ~/Desktop/restaurar-projeto.sh              # lista os projetos disponiveis
    bash ~/Desktop/restaurar-projeto.sh <nome>       # clona um de volta em Desktop\PROJETOS
    bash ~/Desktop/restaurar-projeto.sh --todos      # clona todos

O script tem o mapa nome-da-pasta -> URL do remote embutido, entao nao precisa lembrar o nome do repo (que as vezes difere do nome da pasta, ex: pasta `coreano-area-membros-es` -> repo `coreano-area-miembros`).

Antes de apagar qualquer pasta de projeto de novo, checar `git status` E os arquivos ignorados (`git ls-files --others --ignored --exclude-standard`): pastas tipo `_backup_originais/` e `_origem/` guardam os PNG originais antes da compressao WebP e NAO estao no git. Os que existiam foram movidos pra `G:\Meu Drive\_backup-pc\originais-sem-git\`.

As ~30 pastas sem git em Desktop\PROJETOS (codice-pdfs, caligrafia-originais, CTV SANTOS, pilates-pt-landing, photocards-entregaveis...) nao tem backup nenhum. Ver [[feedback-commit-reminder]].
