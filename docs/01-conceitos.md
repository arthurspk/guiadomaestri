# 01 · Conceitos do Maestri

O Maestri é um app de macOS (e Windows) para a era da IA agêntica: um **canvas
infinito** onde você **rege um time de agentes de código** — Claude Code, Codex,
Gemini, OpenCode — em vez de pular entre abas de terminal. Ele não é um agente; é a
**camada de orquestração** que coordena os agentes que você já usa.

Fonte oficial: <https://www.themaestri.app/pt-br/docs>.

> Este guia tem ênfase em **tecnologia**: os conceitos abaixo são a base para entender
> as 212 partituras em [`partituras/tecnologia/`](../partituras/tecnologia/CATALOGO.md).

---

## O Canvas

O espaço 2D infinito onde tudo vive: terminais, notas, portais, árvores de arquivos,
blocos de texto e desenhos. Você navega com pan e zoom, agrupa elementos e organiza o
trabalho espacialmente. Cada **espaço de trabalho** (workspace) é um canvas; você
alterna entre eles com `Ctrl↑`/`Ctrl↓`.

Ferramentas de canvas (com nada selecionado, tecla simples): `T` terminal, `N` nota,
`P` portal, `F` árvore de arquivos, `L` bloco de texto, `H` pan, `V` seleção.

## Terminais (agentes)

Cada **terminal** é uma janela de shell desenhada no canvas onde um agente opera. É
onde o trabalho de verdade acontece. Um terminal carrega:

- Um **comando de partida** — o que sobe o agente. Ex.: `claude
  --dangerously-skip-permissions --model fable` (maestro), `--model opus` (executor),
  `codex` ou `gemini` (revisão adversarial).
- Uma **responsabilidade** (role) opcional — instruções que definem o papel daquele
  agente. Veja [agentes/README.md](../agentes/README.md).
- Flags de comportamento: **isManager** (é um maestro, pode recrutar), **monitorWithOmbro**
  (o Ombro acompanha), cor e ícone.

Quando um agente pausa esperando decisão, o Maestri mostra um **ponto de atenção**
vermelho no cabeçalho. `Ctrl⇧A` pula para o próximo terminal pedindo atenção.

## Notas

**Notas** são arquivos markdown fixados no canvas. São a **fonte de verdade
compartilhada**: contrato de feature, workboard, findings, case-file. Agentes conectados
a uma nota leem e escrevem nela pela CLI (`maestri note read/write/edit`), então uma nota
funciona como um caderno persistente que sobrevive entre sessões.

Dois modos de armazenamento: **managed** (o app guarda internamente, padrão nas
partituras deste guia) e **arquivo** (a nota aponta para um `.md` num caminho seu). Cores
disponíveis: `blue`, `green`, `yellow`, `purple`, `slate`, `orange`, `pink`, `red`,
`teal`. Notas podem ser **encadeadas** (nota→nota) formando um mapa mental navegável.

## Portais

**Portais** são janelas embutidas no canvas — um navegador (WebKit isolado, com Chrome
planejado) ou um dispositivo (simulador iOS, emulador Android, aparelho físico). Quando
um portal está **conectado a um terminal**, o agente controla o navegador pela CLI:
navegar, clicar, preencher, tirar screenshot, ler o DOM, ver o console, rodar
JavaScript. É a base da **verificação viva**: o agente prova o comportamento no portal em
vez de adivinhar pelo código.

## Conexões

Cabos animados com física que ligam elementos e **habilitam comunicação real** entre
agentes, com qualquer CLI. Tipos:

- **Terminal↔terminal** — os agentes conversam (`maestri ask`). Claude fala com Codex.
- **Terminal↔nota** — acesso persistente ao conteúdo da nota.
- **Terminal↔portal** — o agente dirige o navegador/dispositivo.
- **Nota↔nota** — encadeamento em mapa mental.

Crie com `Ctrl+L` (a partir do elemento selecionado) ou a ferramenta de conexão. Estilos
"Corda" (física) e "Circuito" (linhas retas).

## Modo Maestro

Um terminal marcado como **Maestro** vira gerente do time: pode **recrutar** novos
terminais com o agente e a responsabilidade certos, **conectá-los** a notas, **reatribuir**
papéis no meio da tarefa, **dispensar** quando termina, **provisionar** workspaces e
andares, e **notificar** o humano quando precisa de uma decisão. É o ponto único de
contato do usuário. Nas partituras deste guia, o Maestro sobe em `--model fable`.

## Partituras

Uma **partitura** é um arranjo salvo do canvas: terminais com seus agentes e
responsabilidades, notas, portais, desenhos, grupos e todas as conexões — um **template
reutilizável** que você arrasta para qualquer workspace ou compartilha como arquivo. O
formato é JSON: `.maestripartitura` (uma) e `.maestripartituras` (pacote). Detalhes em
[04-formato-maestripartitura.md](04-formato-maestripartitura.md).

> ⚠️ Adicionar uma partitura **sobe os terminais dela e executa comandos na sua
> máquina**. Leia os comandos na tela de revisão antes de importar.

## Ombro

Companheiro de IA **no dispositivo** que monitora seus agentes de uma janela flutuante.
Roda **localmente** com Apple Foundation Models (requer Mac com Apple Silicon, macOS
Tahoe 26+; **não** existe no Maestri para Windows). Ele avisa quando um agente termina ou
trava, responde perguntas sobre o estado ("o que o Codex está fazendo?") e gerencia uma
nota "Ombro Notes". Abra/feche com `Ctrl⇧O`. Terminais das partituras deste guia têm
`monitorWithOmbro` ligado.

## Batuta Search

A **paleta de comandos** do Maestri, pensada para o teclado. Abra com `Ctrl+P`. Busca
difusa (ignora maiúsculas e acentos) sobre nomes, tipos, workspaces, apelidos e o corpo
completo das notas. Age no lugar: criar terminais/notas/portais, editar, recarregar,
enviar mensagens a agentes, salvar. É por aqui que você faz "Nova Partitura a partir da
seleção".

## Andares (Floors)

**Ambientes de branch isolados** dentro de um workspace: cópias completas do repositório
que compartilham storage via APFS copy-on-write (no Windows, branches git isoladas). Cada
andar tem seu próprio terminal, branch e working tree — você trabalha em tarefas
separadas sem `git stash`. Quando pronto, faça **Land** para levar os commits de volta.
Hooks de **Setup/Run/Teardown** automatizam o ciclo de vida, com variáveis como
`$MAESTRI_FLOOR_NAME`, `$MAESTRI_BRANCH_NAME`, `$MAESTRI_FLOOR_PATH`.

## Rotinas (Routines)

Prompts **agendados** que executam nos seus agentes em intervalos definidos (a cada 5
min, a cada hora). Encadeie passos com `&&` (cada um só dispara após o anterior). Úteis
para testes contínuos, verificação de deploy, revisão periódica de commits. Acesse em
**Arquivo → Rotinas**.

## Ambientes (Environments)

Definem **onde** os terminais rodam: Local, Local (tmux), WSL (Windows), SSH, Docker
Container, Docker Sandbox ou um runtime customizado (Podman, Apple container, Lima).
Configure em **Configurações → Geral → Ambientes** e escolha por workspace ou por
terminal. Ambientes remotos compartilham variáveis padrão (`MAESTRI_TERMINAL_ID`,
`MAESTRI_HOST`, `MAESTRI_TOKEN`, `MAESTRI_CLI`) e usam a **Bridge Port** (padrão `7433`).

## Maestri Wire

O **protocolo** que permite a um host Maestri se comunicar com outros dispositivos e
ferramentas (a base do Maestri Remote para iPhone/iPad e de integrações customizadas).
Servidor em TCP `7434`, só HTTPS/WSS, certificado autoassinado com pinning de SHA-256 da
chave pública, pareamento por código de 6 dígitos e token de dispositivo. Papéis `owner`
(leitura/escrita) e `guest` (só leitura). Detalhes de dev em
<https://www.themaestri.app/pt-br/docs/wire>.

---

Próximo: [02 · Como usar os templates](02-como-usar-os-templates.md).
