# 06 · O Maestri no dia a dia

Esta página é prática. Menos "o que é cada coisa" (isso está em
[01-conceitos.md](01-conceitos.md)) e mais **como o Maestri entra na sua rotina** — em
tecnologia e nas outras áreas — usando os **andares**, os **portais**, as **notas**, as
**rotinas**, o **Ombro** e as partituras deste guia.

O fio condutor é sempre o mesmo: **você fala com um Maestro em linguagem natural; ele
delega a especialistas; as notas guardam a verdade; os portais provam o que aconteceu.**
Você rege, não digita em cinco terminais ao mesmo tempo.

---

## O ritmo de um dia típico

Um jeito de organizar o dia com o Maestri, do café ao fim do expediente:

1. **Abra o workspace do projeto.** Um workspace por produto/cliente. `Ctrl↑`/`Ctrl↓`
   alterna entre eles.
2. **Deixe uma rotina de manhã puxar o mundo.** Uma **Rotina** (Arquivo → Rotinas) que
   roda às 9h no terminal do maestro: `puxe as últimas mudanças && rode a suíte de testes
   && resuma o que quebrou na nota "diário"`. Você chega e lê o resumo.
3. **Escolha a partitura da tarefa do dia.** Vai entregar uma feature? Arraste
   **Ship Feature · \<sua stack\>**. Vai caçar um bug? **Depuração · \<stack\>**. Não é
   código? **Marketing · Campanha**, **Produto · Discovery**, e por aí. Veja o
   [catálogo por área](../partituras/CATALOGO.md).
4. **Briefe o Maestro** pelo **Compositor de Prompts** (`Ctrl⇧P`): o objetivo, em uma ou
   duas frases. Ele roda `maestri list`, manda escrever o contrato/briefing e delega.
5. **Trabalhe em paralelo, sem babá.** Vá cuidar de outra coisa. Quando um agente pausa,
   o **ponto de atenção** acende; `Ctrl⇧A` te leva até ele. O **Ombro** (`Ctrl⇧O`) resume
   "o que cada um está fazendo" sem você abrir terminal por terminal.
6. **Isole o arriscado num andar.** Mudança grande, refactor, upgrade? Faça num **Andar**
   (floor) para não sujar o working tree principal (adiante).
7. **Deixe o warden verificar no portal** antes de dar algo por pronto. Achados, não
   correções.
8. **Feche o dia** com o Maestro reportando o que foi feito e o que ficou aberto; uma
   rotina noturna pode rodar o lint e deixar o terreno limpo para amanhã.

---

## Andares (Floors): o superpoder do trabalho paralelo

Um **andar** é uma cópia isolada do seu repositório com a própria branch e working tree,
criada num instante via APFS copy-on-write (no Windows, uma branch git isolada). É o que
deixa você tocar **várias frentes ao mesmo tempo sem `git stash` e sem conflito**.

### Quando criar um andar

- **Feature de risco em paralelo ao trabalho principal.** O térreo (ground floor) segue a
  branch estável; o andar "Fix login bug" experimenta à vontade.
- **Comparar duas abordagens.** Dois andares, a mesma tarefa, um em cada — casa muito bem
  com a partitura **Duelo de Agentes**: cada duelista trabalha num andar, o Juiz compara e
  faz **Land** do vencedor.
- **Upgrade ou migração** (partituras da família **Migração**): o andar segura o novo Node
  / Angular / Postgres enquanto o térreo continua entregando.
- **Revisão de um PR de terceiro** sem largar o que você está fazendo: um andar na branch
  do PR, com a partitura **Portão de Release**.

### O ciclo de um andar

1. **Criar** — botão de andar (canto inferior direito, perto do minimapa) → nomeie ("Fix
   login bug") → escolha branch nova ou existente → opcionalmente clone o layout do térreo
   (notas, terminais, blocos de texto) → **Create**. `Ctrl⇧\` alterna a visão geral dos
   andares; `↑`/`↓` percorre.
2. **Trabalhar** — cada andar tem seus próprios terminais e portais. Faça commits, rode
   testes, veja o diff no painel do andar.
3. **Automatizar com hooks** — o ícone de raio (⚡) dá três hooks de ciclo de vida:
   **Setup** (roda ao criar, ótimo para `npm install` e subir o app), **Run** (sob
   demanda) e **Teardown** (limpa ao apagar). Eles recebem variáveis como
   `$MAESTRI_FLOOR_NAME`, `$MAESTRI_BRANCH_NAME`, `$MAESTRI_FLOOR_PATH`,
   `$MAESTRI_ROOT_PATH`, `$MAESTRI_PROJECT_NAME`. Exemplo de Setup:
   ```bash
   cd "$MAESTRI_FLOOR_PATH" && npm ci && npm run dev > /tmp/dev-$MAESTRI_FLOOR_NAME.log 2>&1 &
   ```
4. **Aterrissar (Land)** — quando pronto, **Land** leva os commits de volta ao repositório;
   você escolhe a mesma branch ou outra, e vê um preview com diff e possíveis conflitos.
5. **Apagar** — o X remove o andar; você decide manter ou apagar a branch associada.

> Requisitos: volume APFS (padrão no macOS) e um repositório git inicializado.

### Andar + partitura: o combo

Importe uma partitura **dentro de um andar** e o time inteiro nasce isolado naquela
branch. Padrão que funciona muito bem:

- Andar `feat/busca-filtros` + partitura **Ship Feature · Next.js + Nest**. O Maestro sobe
  o app pelo hook de Setup, o time constrói, o warden verifica no portal, você faz **Land**
  quando o veredito é verde.

---

## Portais no dia a dia: verificação viva

O portal é onde o trabalho **deixa de ser alegação e vira evidência**. Um agente conectado
a um portal dirige o navegador pela CLI (`maestri portal navigate/snapshot/click/fill/
screenshot`). Usos além do óbvio "abrir o localhost":

- **Provar um bug de UI** (Depuração): o Reprodutor navega, clica, tira screenshot do erro.
- **Aceitar uma feature** (Ship Feature): o warden percorre o fluxo real, não o código.
- **Conferir uma landing publicada** (Marketing): o Revisor abre a URL de produção e checa
  copy, CTA e responsividade de verdade.
- **Olhar o concorrente** (Produto / Pesquisa): o portal abre o site do concorrente para o
  time ancorar a análise em algo real.
- **Ler um dashboard** (Dados / Financeiro): o Revisor confere o número no painel, não na
  suposição.
- **Portal de dispositivo** (Ship Mobile): simulador iOS / emulador Android no canvas, com
  toque, digitação e screenshot — a mesma verificação viva, no app mobile.

Dica: portais podem ser **ligados entre si** para compartilhar sessão (cookies/login), útil
quando o fluxo precisa de um usuário autenticado em várias telas.

---

## Notas: a fonte de verdade que sobrevive à sessão

As partituras já trazem as notas certas montadas (contrato/briefing, board, findings,
case-file, timeline). No dia a dia:

- **Trate a nota como o contrato, não o chat.** Quando o board e a realidade discordam,
  conserte o board — o Maestro é instruído a fazer isso.
- **Mova para o repo o que deve viver no repo.** A barra da nota → "Mover para…" grava a
  nota como um `.md` no seu projeto (e ela continua existindo se você tirar do canvas).
  Ótimo para specs e ADRs que devem ir no git.
- **Encadeie notas** (nota→nota) para um mapa mental navegável: um índice que aponta para
  spec, decisões e findings, e o agente percorre a cadeia.
- **Deixe o Ombro resumir** as notas depois de uma pausa ("resuma o que mudou nas notas").

---

## Rotinas: o trabalho que se repete sozinho

Rotinas rodam prompts nos seus agentes em intervalo definido. Encadeie com `&&` (o próximo
só dispara quando o anterior termina). Exemplos por situação:

- **Guardião de CI (dev):** a cada 30 min no maestro — `puxe main && rode os testes &&
  se algo falhar, abra um caso na nota "diário" e me notifique`.
- **Vigia de deploy (SRE):** a cada 5 min — `cheque o health do endpoint de produção pelo
  portal e registre latência na nota "status"`.
- **Clipping de concorrência (Marketing/Produto):** toda manhã — `abra os 3 sites
  concorrentes no portal, resuma mudanças de preço/mensagem na nota "radar"`.
- **Fechamento diário (Financeiro):** ao fim do dia — `concilie os lançamentos de hoje e
  aponte divergências na nota "fechamento"`.
- **Triagem de tickets (Suporte):** de hora em hora — `classifique os tickets novos por
  urgência e proponha resposta na nota "triagem"` (com aprovação humana antes de responder).

Rotinas ativas mostram indicador visual; pause, edite ou apague sem perder a config.

---

## O Ombro no dia a dia

O **Ombro** (`Ctrl⇧O`, macOS com Apple Silicon, roda **local**) é o seu co-piloto de
atenção. No fluxo real:

- **Você saiu para uma reunião.** Ao voltar: "o que os agentes fizeram enquanto eu estava
  fora?" e ele resume terminal por terminal.
- **Muitos agentes rodando.** "o warden já terminou? o Codex ainda está revisando?" sem
  caçar o terminal certo.
- **Notas demais.** "resuma tudo que mudou nas notas hoje" — bom antes de passar contexto a
  um agente novo.
- **Anotar sem sair do fluxo.** "adiciona na Ombro Notes que falta escrever os testes de
  auth."

---

## Situações reais, por área

Cada cenário abaixo aponta a partitura que já vem pronta. Todas usam o mesmo tecido:
maestro (fable) → especialistas (opus) → revisor adversarial (codex/gemini) → notas +
portal.

### 💻 Tecnologia
- **"Preciso entregar a busca com filtros até sexta."** Andar `feat/busca` + **Ship
  Feature · \<stack\>**. Contrato do arquiteto, duas fatias em paralelo, warden no portal.
- **"O checkout quebra às vezes e não sei por quê."** **Depuração · \<stack\>**: repro
  determinística → causa raiz com prova → menor conserto → verificação independente.
- **"Vamos subir a v2 amanhã, está pronto?"** **Portão de Release · \<stack\>**: quatro
  revisores (qualidade, segurança, correção, UX/a11y) e um veredito.
- **"Migrar de Angular v17 para v22 sem parar o time."** Andar dedicado + **Migração ·
  Angular v17 → v22**: incremental, reversível, paridade provada.

### 🎨 Design & UX
- **"Nosso design está inconsistente entre telas."** **Design & UX · Design System**:
  tokens, componentes, e o revisor confere contraste e foco no portal.
- **"Essa landing converte mal."** **Design & UX · Landing Page** + portal na URL real.

### 📦 Produto
- **"Recebi 300 respostas de pesquisa, e agora?"** **Produto · Síntese de Feedback**:
  temas, decisões, com rastreabilidade até a resposta.
- **"Preciso decidir o próximo trimestre."** **Produto · Roadmap & Priorização**: impacto
  × esforço com critério explícito, não achismo.

### 📢 Marketing & Conteúdo
- **"Lançamento em duas semanas."** **Marketing · Campanha de Lançamento**: briefing de
  mensagem, peças por canal, revisão de marca e fato.
- **"Blog técnico que não pode ter erro."** **Marketing · Blog Técnico** + o revisor
  confere as afirmações contra o produto/código.

### 💼 Vendas
- **"Responder um RFP grande até quinta."** **Vendas · Proposta / RFP**: temas de ganho,
  prova, revisão de precisão e conformidade.

### 📊 Dados & Analytics
- **"Esse dashboard está com número errado."** **Dados · Dashboard de BI**: cada métrica
  com definição e query, revisor confere no painel pelo portal.
- **"Esse teste A/B deu resultado de verdade?"** **Dados · Experimento A/B**: desenho e
  leitura com rigor estatístico.

### 🔒 Segurança & Compliance
- **"Precisamos estar em conformidade com a LGPD."** **Segurança · Auditoria LGPD**:
  mapa de dados, bases legais, gaps com evidência. (Pentest técnico fica em **Tecnologia
  · Red Team**, só escopo autorizado.)

### 💵 Financeiro
- **"Fechar o mês com trilha de auditoria."** **Financeiro · Fechamento Mensal**:
  conciliação, o que não fecha vira achado, não arredondamento.

### ⚖️ Jurídico
- **"Revisar esse contrato antes de assinar."** **Jurídico · Revisão de Contrato**:
  cláusulas e riscos citando o trecho — apoio, com recomendação de revisão humana.

### 🛟 Suporte & Sucesso
- **"Nossa central de ajuda está desatualizada."** **Suporte · Base de Conhecimento**:
  artigos verificados contra o produto no portal, nada de passo que não roda.

### 🗂️ Gestão de Projetos
- **"Transformar a reunião de agora em ações."** **Gestão · Ata de Reunião**: decisões e
  tarefas com dono e data, nada de item órfão.

### 🔬 Pesquisa & Conteúdo Técnico
- **"Levantar o estado da arte sobre X."** **Pesquisa · Estado da Arte**: síntese citada,
  contradições registradas, sem fonte inventada.

---

## Multi-time, multi-andar: o Maestri em escala

Quando o trabalho cresce, o padrão escala:

- **Um workspace por produto**, alternados com `Ctrl↑`/`Ctrl↓`.
- **Andares por frente de trabalho** dentro do produto: um para a feature da semana, um
  para o hotfix, um para o spike de pesquisa — cada um com sua branch e seu time.
- **Batuta Search (`Ctrl+P`)** para saltar a qualquer terminal, nota ou ação sem trocar de
  contexto manualmente; ela busca até dentro do corpo das notas.
- **`AltCtrlA`** lista todos os terminais aguardando atenção, em todos os andares —
  o seu "inbox" de decisões pendentes.
- **Maestri Wire / Remote** para acompanhar do celular: ver quem pede atenção e mandar um
  prompt de longe (veja [01-conceitos.md](01-conceitos.md#maestri-wire)).

O princípio não muda com a escala: **as notas seguram a verdade, os portais provam o
resultado, e você rege em vez de executar.**

---

Próximo: [07 · Áreas e agentes disponíveis](07-areas-e-agentes.md).
