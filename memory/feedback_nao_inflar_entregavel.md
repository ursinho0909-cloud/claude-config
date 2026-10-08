---
name: feedback_nao_inflar_entregavel
description: Não produzir documento longo sem confirmar antes — usuário reclama de gasto desproporcional pro tamanho da tarefa
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1cacc721-6f16-4aaf-887a-9af0274954fb
  modified: 2026-08-12T12:07:01.014Z
---

Quando a tarefa é "escreve um prompt/doc", entregar o **mínimo que funciona** e perguntar antes de expandir. Em 2026-08-12 escrevi 3 arquivos de ~500 linhas (prompts Manus dos cadernos 9/10 + bônus do Inglés en Casa) sem checar o tamanho esperado, e a resposta foi *"pq gastar tudo isso de token pra criar 5 prompt, calma amigão"*.

**Why:** ele mede custo/benefício por tarefa. Clonar a estrutura completa de um `.md` de 460 linhas parecia certo porque o padrão existente era esse, mas ele só queria os prompts, não uma revisão do pipeline junto.

**How to apply:** perguntar "quer o prompt enxuto ou o formato completo igual ao caderno 8?" antes de começar. Achados laterais (bugs no `build_prompts.py`, etc.) reportar em uma linha e perguntar se quer que arrume — não arrumar junto por iniciativa. Vale principalmente pros projetos de info-produto, onde ele já tem o padrão na cabeça e só quer o artefato.

Relacionado: [[feedback_directness]], [[project_ingles_en_casa]], [[project_ingles_area_miembros]], [[feedback_manus_prompt_order]]
