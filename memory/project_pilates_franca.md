---
name: project-pilates-franca
description: Pilates Visual traduzido para FRANÇA (2026-09-21) — produto, bônus, bumps e landing FR em Desktop\PILATES FRANÇA; falta deploy e revisão
metadata:
  type: project
---

Versão FR do "+120 Exercícios de Pilates Explicados Visualmente" (o PT roda em Portugal: pilates-visual.pages.dev, pasta Desktop\PROJETOS\pilates-pt-landing, Hotmart V107351060M a 13,90 €).

Tudo em `C:\Users\User\Desktop\PILATES FRANÇA\` (sem git): 1-PRODUIT-PRINCIPAL (11 PDFs), 2-BONUS, 3-ORDER-BUMPS (Planches, Guide 50 étirements, Carte 30 jours), landing\ (FR, 14,90 €, SEM pixel (removido 2026-09-21), checkout Hotmart B107705279J), _fontes\.

Decisões: vouvoiement em tudo; seção de depoimentos (prints WhatsApp PT-BR) removida; módulo 10 do zip original era cópia idêntica do 9 → FR tem 10 módulos (Erreurs virou 10); nomes de exercícios ficaram em inglês (padrão Pilates).

Material principal/pranchas/guia eram imagem pura: traduzidos por OCR (rapidocr) + apagar e reescrever. Pipeline reutilizável em `_fontes\traducao-imagens` (blocks.py → trtxt/*.txt → conv.py → render.py → build_pdfs.py; patches.json p/ trechos que o OCR não pegou). Serve pra levar a Alemanha/Espanha: só traduzir trtxt.

**Pendente:** deploy CF Pages, e-mail de suporte FR, revisão visual por francófono (algumas páginas têm fontes menores onde o FR ficou maior), preço riscado "Au lieu de 39,90 €" é risco de Directiva Omnibus/DGCCRF.

**Upsell Défi Pilates au mur (2026-09-28):** PDF 30 dias traduzido do alemão (Wand-Pilates) → Downloads\Pilates-au-mur-30-jours_FR.pdf; pipeline em _fontes\wand-pilates (render2.py = inpainting + fonte manuscrita, overrides.json por página). Página de upsell LIVE em defi-pilates-mur.pages.dev (CF Pages, pasta PILATES FRANÇA\upsell-mur\site, sem git), clone FR de pilates-wand-challenge.pages.dev. Checkout Hotmart T107798676A a 16,90 €. Pendente: PDF tem página "aperçu 26/30 dias" (faltam dias 26, 28-30); bônus 1/2 prometidos na página precisam existir; configurar essa URL como página de upsell no Hotmart do produto principal B107705279J.
