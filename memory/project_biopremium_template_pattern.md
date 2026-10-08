---
name: project-biopremium-template-pattern
description: "Playbook completo dos modelos BioPremium (link-in-bio nichado). Estrutura, paleta, layout, quiz, diferenciais e fluxo de deploy. Quando usuário pede \"novo modelo X\" ou \"modelo-[nicho]\", siga isso sem perguntar do zero."
metadata: 
  node_type: memory
  type: project
  originSessionId: 08f866a1-2ad9-4e22-bdf3-a15878d79b47
---

# BioPremium · Modelo Base de Template (catálogo nichado)

Cada template segue ESTA receita. Quando user pedir um novo nicho, replicar o padrão e só trocar paleta + diferencial + perguntas.

## 📁 Estrutura de pasta

```
C:\Users\User\Desktop\modelo-<nicho>\
├── index.html       (página única, CSS+JS inline)
├── vsl.mp4          (VSL principal, lossless faststart)
├── foto-1.jpg ... foto-N.jpg  (galeria, q:v 3 otimizado)
├── thumb-ad-N.jpg   (opcional: poster pra lazy load vídeo antes/depois)
├── README.md
└── .gitignore       (.vercel apenas)
```

## 🛠️ Stack técnico

- HTML único, CSS inline em `<style>`, JS inline no fim
- Google Fonts CDN (preconnect + 2 famílias máx)
- Sem build step, deploy direto Vercel static
- `ffmpeg -c copy -movflags +faststart` pra vídeos (zero re-encode, faststart pra streaming)
- `ffmpeg -q:v 3` pra JPGs (visualmente lossless)
- Lazy load: `<video preload="none" data-src="x.mp4" poster="thumb-x.jpg">` + JS injeta `<source>` no clique do dot/scroll

## 🎨 Paletas por categoria (já validadas)

| Categoria | Background | Accent | Detalhe | Fontes |
|---|---|---|---|---|
| **Beleza estética escura** (lash) | preto #0a0a0a | rose gold #b76e79 | champagne / dourado | Cormorant Garamond italic + Inter |
| **Arte corporal** (tatuador) | preto fosco #131313 | dourado #c9a961 | bronze | Bebas Neue + Cinzel + Inter |
| **Fitness/academia** (personal) | preto #0a0a0a | laranja vibrante #ff6b1a | – | Bebas Neue + Outfit + Inter |
| **Estética clinic-premium** (estética facial) | off-white #faf7f0 | rose nude #d4a99a | champagne / dourado / rose deep | Playfair Display italic + Outfit + Inter |
| **Wellness mulher 40+** (alternativa personal) | verde-floresta #1d3a2b | coral #e8826a | dourado champagne | Playfair italic + Outfit + Inter |

**Padrão de variáveis CSS** sempre:
```css
:root{
  --bg, --bg-card, --primary, --primary-claro, --primary-esc,
  --accent, --texto, --texto-claro, --sombra, --sombra-card
}
```

## 📐 Layout (ordem fixa de seções, mobile-first)

### 1. Header (compacto ~50px)
- `padding:14px 18px 10px`
- Logo SVG 28-34px + `marca-nome` (Bebas Neue/Cormorant/Playfair, ~17-22px, letterspacing 2-3px, uppercase)
- `<h1>` curto italic em 15-17px

### 2. VSL vertical 9:16
- `padding:8px 20px 10px`
- `.vsl-container max-width:240px`
- `.vsl-wrapper max-width:220px; aspect-ratio:9/16; max-height:42vh; border:2px solid var(--primary); border-radius:16-18px`
- `<video autoplay muted loop playsinline controls preload="metadata">`
- `.vsl-badge` "▶ Assista" canto top-left com pulse 2s

### 3. Quiz (`padding:14px 20px 40px`)
- `.quiz-container max-width:420-460px`
- Header: tag pill + título display + sub uppercase
- Progresso bar 4px height
- 4-5 etapas com 4 opções cada
- Avanço automático após clique (350ms)
- Última etapa = **diferencial** + nome + botão WhatsApp

### 4. Galeria/Carrossel (opcional, varia por nicho)
- Fotos OU vídeos antes/depois
- Padrão snap scroll: `display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:14px`
- `padding:0 calc(50% - 110px)` pra centralizar primeiro/último
- Slides `flex:0 0 220-320px`, ativo scale 1 opacity 1, outros scale 0.78 opacity 0.4
- Dots embaixo + hint "‹ arraste para ver mais ›"
- Drag mouse (desktop) + swipe nativo (mobile)

### 5. Footer minimal
- Tagline italic + copyright

## ❓ Quiz pattern (5 etapas padrão)

```js
const respostas = { campo1:'', campo2:'', ..., nome:'' };
let etapaAtual = 1;
const totalEtapas = 5;
```

**Estrutura típica:**
1. **O que está buscando** (4 opções com emoji)
2. **Experiência prévia** (4 opções)
3. **Como se sente / problema atual** (4 opções)
4. **Prazo / quando** (4 opções)
5. **Diferencial interativo** + nome + botão WhatsApp

**Opção HTML:**
```html
<button class="opcao" data-pergunta="campo" data-valor="Valor">
  <span class="opcao-emoji">🔥</span> Texto da opção
</button>
```

**Avanço automático** após clique:
```js
setTimeout(() => {
  if(etapaAtual < totalEtapas && pergunta !== 'periodo') irParaEtapa(etapaAtual + 1);
}, 350);
```

## 🎯 Catálogo de diferenciais interativos (já implementados ou desenhados)

| Nicho | Diferencial | Mecânica |
|---|---|---|
| **Lash designer** | Calendário + horários | Grid de dias do mês + slots disponíveis |
| **Tatuador** | Régua de cm (1-50) + "não tenho ideia" | Slider com viz proporcional + comparações ("≈ palma da mão") |
| **Personal trainer** | Período do dia | 4 opções simples (manhã/tarde/noite/flexível) |
| **Estética facial** | **Mapa do rosto interativo** | Foto real + 11 hotspots numerados sobre cada área + botão "ainda não sei" |
| **Fotógrafo casamento** | Countdown evento | Date picker + "faltam X dias" |
| **Dentista estética** | Simulador sorriso | Multi-select de incômodos (dente torto/manchado/etc) |
| **Cabeleireiro** | Galeria de cortes clicáveis | 6 cortes selecionáveis → perfil de estilo |
| **Nail designer** | Construtor visual | Formato + tamanho + cor → preview |
| **Maquiador** | Quiz de ocasião + paleta | Slider day-to-night + estilo |
| **Veterinário** | Idade pet em anos humanos | Calculadora + quiz sintomas |
| **Advogado** | "Tenho direito a quanto?" | Calculadora com inputs do caso |
| **Coach/Psicólogo** | Termômetro emocional | Sliders múltiplos (humor/ansiedade/sono) |
| **Arquiteto** | Mood board | Estilos clicáveis + slider de orçamento |
| **Esteticista corporal** | Mapa do corpo | Mesma mecânica do rosto, body parts |
| **Tarólogo** | 3 cartas flip | Cartas viradas que cliente "tira" |
| **Eletricista** | Mini-planta da casa | Cômodos clicáveis + tipo de problema |

**Pattern do hotspot interativo** (mapa do rosto/corpo):
- Foto real como fundo, `aspect-ratio` exato da imagem (não usar 4/5 padrão se foto for outra proporção)
- Hotspots `position:absolute` com `transform:translate(-50%,-50%)` no centro do ponto
- Default: anel visível + número dentro + pulse animado
- Hover: scale + border mais grossa
- Ativo: filled com gradient primary + ✓ branco no centro (oculta o número)
- Botão "Não tenho ideia / Ainda não sei" abaixo como escape hatch

## 💬 Mensagem WhatsApp (padrão)

```
Oi! Acabei de responder o quiz no seu site, [emoji do nicho]

📋 *Meu perfil:*
• [Campo 1]: [valor]
• [Campo 2]: [valor]
...

🎯 *[Bloco do diferencial, se houver]:*
• [...]

😊 Meu nome é [nome].

[CTA pergunta: "Quando começamos?" / "Quando posso fazer?" / "Pode confirmar pra mim?"]
```

**Tela de sucesso** (sempre neutra de gênero):
- Ícone circular com emoji do nicho
- "Que bom te ver aqui, [nome]!" (NÃO usar "linda/guerreira/parceiro" como default — colocar algo neutro tipo "atleta", "querida(o)" ou só o nome)
- Resumo com 3 itens chave
- Redirect 1.8s pra `https://wa.me/<WHATSAPP_NUMERO>?text=<encoded>`

## 🚀 Deploy workflow (sequência exata)

```bash
# 1. Setup pasta + assets
mkdir -p /c/Users/User/Desktop/modelo-<nicho>
# Copia vídeo lossless + faststart:
ffmpeg -y -i source.mp4 -c copy -movflags +faststart "modelo-<nicho>/vsl.mp4"
# Otimiza fotos:
for n in 1 2 3; do ffmpeg -y -i "foto-$n.jpg" -q:v 3 "modelo-<nicho>/foto-$n.jpg"; done

# 2. .gitignore + README
echo -e ".vercel\n.DS_Store\nnode_modules\n*.log\n.env\n.env.local" > .gitignore

# 3. Git init + push GitHub (conta ursinho0909-cloud, sempre PRIVADO)
git init -b main
git add .
git -c user.email="ursinho0909@gmail.com" -c user.name="ursinho0909-cloud" commit -m "Modelo <nicho>"
gh repo create modelo-<nicho> --private --source=. --remote=origin --push

# 4. Deploy Vercel (já autenticado como ursinho0909-3457)
npx --yes vercel@latest --prod --yes --name modelo-<nicho>

# 5. Vercel auto-adiciona .vercel ao .gitignore (duplicado), desdup:
# (remove a linha duplicada, commita, push)
```

**URL pattern:** `https://modelo-<nicho>.vercel.app` (se nome estiver livre globalmente, senão pega `-two` ou similar)

## 💻 Localhost dev workflow

```bash
cd "/c/Users/User/Desktop/modelo-<nicho>"
python -m http.server 80XX  # 8080 lash, 8081 tatuador, 8082 personal, 8083 estética, próximo 8084+

# Abre Opera GX (preferência do user)
& "C:\Users\User\AppData\Local\Programs\Opera GX\opera.exe" http://localhost:80XX
```

**Sempre matar python existente antes:**
```bash
taskkill //F //IM python.exe 2>/dev/null
```

## 🔧 Pendência única em CADA template

Trocar o número no JS:
```js
const WHATSAPP_NUMERO = '5511999999999'; // ← cliente real
```

Formato: `55` + DDD + número (sem espaços/traços).

## 📊 Templates já no ar (catálogo BioPremium)

| Nicho | URL Vercel | Repo |
|---|---|---|
| Nutricionista | template-nutricionista-biopremium.vercel.app | (pré-existente) |
| Corretor MCMV (Gabriel Lera) | gabriel-lera-mcmv.vercel.app | gabriel-lera-mcmv |
| Lash Designer | modelo-lashdesinger.vercel.app | modelo-lashdesinger |
| Tatuador | modelo-tatuador.vercel.app | modelo-tatuador |
| Personal Trainer | modelo-personal.vercel.app | modelo-personal |
| Estética Facial | modelo-estetica-two.vercel.app | modelo-estetica |

## 🎯 Preço atual da oferta

- **Setup:** R$247 (uma vez)
- **Mensalidade:** R$39,90/mês (com 2 alterações inclusas + hospedagem Vercel)
- **Alterações extras:** orçamento avulso

Estratégia: validar volume no orgânico primeiro. Subir pra R$397 + R$67/mês quando passar de 50 clientes.

## 🚦 Ao receber pedido "modelo-<nicho>"

Sequência sem perguntar:
1. Ver pasta de assets que user vai indicar (ex: `C:\Users\User\Desktop\<nicho>`)
2. Listar vídeos + fotos disponíveis
3. Copiar/renomear pra pasta `modelo-<nicho>` com nomes limpos (vsl.mp4 / foto-1.jpg etc)
4. ffmpeg lossless faststart no vídeo + q3 nas fotos
5. Montar HTML seguindo o pattern acima — escolher paleta + fontes + diferencial conforme nicho
6. Subir localhost porta nova + abrir Opera GX
7. Aguardar feedback antes de deploy
8. Deploy: gh repo create privado + vercel --prod
9. Reportar URLs

**O que VARIA por nicho:**
- Paleta (consultar tabela acima)
- Fontes (consultar tabela acima)
- 5 perguntas do quiz (adaptar ao nicho)
- Diferencial interativo (consultar catálogo)
- Copy do header / quiz / mensagem WhatsApp / footer
- Emoji do ícone de sucesso

**O que NÃO muda:**
- Estrutura de seções (header → VSL → quiz → galeria → footer)
- Padrão de avanço automático no quiz
- Lazy load nos vídeos antes/depois
- Mensagem WhatsApp formato
- Deploy workflow

[[user_business]] [[project_biopremium]] [[project_github_sync]] [[feedback_dev_preview_layout]]
