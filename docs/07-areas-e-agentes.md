# 07 · Áreas e agentes disponíveis

Este guia divide as **257 partituras** em **12 áreas** (veja o
[catálogo mestre](../partituras/CATALOGO.md)). Esta página mostra de onde vem essa divisão,
como ela conversa com catálogos de agentes existentes, e como transformar um agente de
terceiro numa **responsabilidade** do Maestri.

---

## De onde vêm as áreas

A divisão por áreas espelha a ideia de **"divisões de uma agência de IA"** — cada área é um
departamento com seus especialistas. A referência principal é o
[**agency-agents** (msitarzewski)](https://github.com/msitarzewski/agency-agents), um
catálogo aberto com **mais de 230 agentes** organizados em **18 divisões**. Lá, cada agente
é um arquivo markdown com frontmatter (`name`, `description`, `emoji`, `color`, `vibe`) e
seções de identidade, missão, regras e entregáveis — o mesmo formato conceitual de uma
**responsabilidade** (role) do Maestri.

### Onde há agentes disponíveis (agency-agents), por divisão

Contagem verificada no repositório:

| Divisão (agency-agents) | Agentes | Área correspondente aqui |
|---|:--:|---|
| Engineering | 59 | 💻 Tecnologia |
| Specialized | 58 | (várias — jurídico, RH, operações, etc.) |
| Marketing | 36 | 📢 Marketing & Conteúdo |
| GIS | 13 | (não coberta — geoespacial) |
| Security | 12 | 🔒 Segurança & Compliance / 💻 Red Team |
| Design | 10 | 🎨 Design & UX |
| Sales | 9 | 💼 Vendas |
| Testing | 9 | 💻 Tecnologia (Portão de Release, Depuração) |
| Paid Media | 7 | (parcial — dentro de Marketing) |
| Project Management | 7 | 🗂️ Gestão de Projetos |
| Academic | 6 | 🔬 Pesquisa & Conteúdo Técnico |
| Game Development | 6 | (não coberta — jogos) |
| Spatial Computing | 6 | (não coberta — XR/visionOS) |
| Support | 6 | 🛟 Suporte & Sucesso |
| Finance | 5 | 💵 Financeiro |
| Product | 5 | 📦 Produto |
| Healthcare | 3 | (não coberta — saúde) |
| Research | 1 | 🔬 Pesquisa & Conteúdo Técnico |
| Strategy (playbooks) | — | (runbooks, sem frontmatter de agente) |

> As áreas **GIS**, **Game Development**, **Spatial Computing** e **Healthcare** existem no
> agency-agents mas ainda **não** têm partituras aqui — são candidatos naturais de
> expansão (veja abaixo). O foco deste guia continua sendo **tecnologia**, com as demais
> áreas de negócio cobrindo os fluxos de trabalho mais comuns ao redor de um time de
> produto.

### Como as 12 áreas daqui se posicionam

| Área (partituras) | Famílias | Inspiração no agency-agents |
|---|---|---|
| 💻 Tecnologia | 23 famílias, 212 partituras | Engineering + Testing |
| 🎨 Design & UX | 5 | Design |
| 📦 Produto | 5 | Product |
| 📢 Marketing & Conteúdo | 5 | Marketing + Paid Media |
| 💼 Vendas | 4 | Sales |
| 📊 Dados & Analytics | 4 | Engineering (data) + Specialized |
| 🔒 Segurança & Compliance | 4 | Security + Specialized (compliance) |
| 💵 Financeiro | 4 | Finance |
| ⚖️ Jurídico | 3 | Specialized (legal) |
| 🛟 Suporte & Sucesso | 4 | Support |
| 🗂️ Gestão de Projetos | 4 | Project Management |
| 🔬 Pesquisa & Conteúdo Técnico | 3 | Research + Academic |

O detalhe família a família está em cada catálogo de área (links no
[catálogo mestre](../partituras/CATALOGO.md)) e o elenco de papéis em
[agentes/README.md](../agentes/README.md).

---

## Partitura × agente: qual a diferença

- Um **agente** (como no agency-agents) é **um** especialista com um prompt. É a peça.
- Uma **partitura** do Maestri é **um time montado**: vários terminais com papéis,
  conectados a um maestro, com notas e portais e as conexões prontas. É a orquestra.

Ou seja: um agente do agency-agents vira, aqui, uma **responsabilidade** (o `prompt` de um
role); uma partitura combina várias delas num fluxo com verificação viva.

## Transformar um agente de terceiro numa responsabilidade

Peguemos um agente do agency-agents (ex.: `design/design-ui-designer.md`) e usemos como
role de um terminal:

1. **Extraia o corpo do prompt** do arquivo `.md` (o texto depois do frontmatter). Traduza
   para pt-BR se quiser manter o padrão deste guia.
2. **Adapte ao vocabulário do Maestri**: acrescente as linhas de `maestri list` / `ask` /
   `note` / `portal`, a disciplina de "achados, não correções" e "verificação viva". Os
   blocos reutilizáveis já estão em [`scripts/roles_lib.py`](../scripts/roles_lib.py)
   (`SETUP`, `ASKBACK`, `REPORT`).
3. **Registre como role** numa partitura, via o builder `area_specialist(...)` ou
   `specialist(...)`, ou direto no app: **Configurações → Agentes** cria um role com nome,
   cor e instruções (o Maestri gera um `role.json` portátil ao lado do `CLAUDE.md`/`AGENTS.md`).
4. **Atribua ao terminal** (`maestri role assign`, ou no Maestro), conecte às notas e ao
   portal, e salve como sua própria partitura (`Ctrl+P` → "Nova Partitura a partir da
   seleção").

Assim você reaproveita a biblioteca de 230+ agentes do agency-agents **dentro** da
mecânica de orquestração do Maestri.

---

## Validação do layout: guiadevbrasil

O pedido incluía validar o [**guiadevbrasil**](https://github.com/arthurspk/guiadevbrasil)
e conferir se este guia segue o mesmo layout. O guiadevbrasil é um guia pt-BR de recursos
(15k+ estrelas) com um layout muito reconhecível:

- **Cabeçalho centralizado** com logo e título (`<p align="center">` + `<img>` + `<h1>`).
- **Blockquote de proposta** logo abaixo ("O guia para alavancar a sua carreira").
- **Badges sociais** e seções de apoio (doações, e-book, colabore, tradução).
- **Um grande `## 📚 ÍNDICE`** com links de âncora, um por linha, no formato
  `[🔧 Título](#-titulo) <br>`.
- **Seções `## emoji Título`**, cada uma com uma intro em `>` e uma **lista de itens**
  `- [Nome](url) - descrição`.

Este repositório **adota esse layout** no [README](../README.md): cabeçalho centralizado
com badges, blockquote de proposta, um `## 📚 Índice` com âncoras, e seções com emoji +
intro em `>` + listas de itens no padrão `[Nome](link) — descrição`. A diferença de
conteúdo é natural: onde o guiadevbrasil lista **links externos** de estudo, aqui os itens
são **partituras e docs** deste repositório. A estrutura visual e a navegação seguem o
mesmo modelo.

O agency-agents contribui com o **modelo de organização por divisões/áreas** e com o
formato de agente; o guiadevbrasil contribui com o **modelo de layout** do índice e das
seções em pt-BR. Este guia junta os dois: divisão por áreas ao estilo agência, apresentada
no layout de índice do guiadevbrasil.

---

## Expandir para novas áreas

Adicionar uma área nova (ex.: GIS, Jogos, Saúde) é mecânico:

1. Em [`generate_partituras.py`](../scripts/generate_partituras.py), adicione a área ao
   dicionário `AREAS` (slug, rótulo, emoji, nome do pacote, descrição).
2. Crie o catálogo de variantes e uma função de família usando o helper `_area_team(...)`
   (ou `_team_pipeline(...)` para áreas técnicas), e registre em `NEW_AREA_FAMILIES`.
3. Rode `python3 scripts/generate_partituras.py` e `python3 tests/validate_partituras.py`.

Os UUIDs determinísticos garantem que regenerar não bagunça o que já existe.

---

Volta ao [índice](../README.md).
