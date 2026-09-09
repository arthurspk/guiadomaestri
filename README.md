<p align="center">
  <a href="https://www.themaestri.app/pt-br">
    <img src="./images/maestri-logo.png" alt="Guia do Maestri" width="160" height="160">
  </a>
</p>

<h1 align="center">Guia do Maestri</h1>

<p align="center">
  O <b>Maestri</b> está disponível para <b>macOS e Windows</b>.<br>
  <a href="https://www.themaestri.app/pt-br">Site oficial</a> · <a href="https://www.themaestri.app/pt-br/docs">Documentação oficial</a>
</p>

## :dart: A proposta

> O **Maestri** é um app de macOS e Windows onde você **rege um time de agentes de código** — Claude Code, Codex, Gemini, OpenCode — num **canvas infinito**: terminais são agentes, notas markdown são a fonte de verdade compartilhada, portais são navegadores embutidos para verificação viva, e o **maestro** delega e coordena. Este repositório é ao mesmo tempo um **guia em pt-BR** e um **gerador em Python** que produz **257 partituras** (`.maestripartitura`) prontas para arrastar para o canvas e reger — cada uma é um time completo, com responsabilidades embutidas, notas, portais e conexões. A ênfase é **tecnologia**, e há mais 11 áreas de negócio (design, produto, marketing, vendas, dados, segurança, financeiro, jurídico, suporte, gestão, pesquisa).

## 💡 Como este guia é organizado

> Duas influências, juntas. A **divisão por áreas** (departamentos de uma agência de IA) vem do [agency-agents](https://github.com/msitarzewski/agency-agents), catálogo com 230+ agentes em 18 divisões. O **layout** — cabeçalho, proposta, índice com âncoras e seções em pt-BR — segue o [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil). Detalhes dessa validação em [docs/07](docs/07-areas-e-agentes.md).

## 🌍 Tradução

> Se você deseja acompanhar este guia em outro idioma, escolha abaixo. Você também pode colaborar com a tradução para outros idiomas e a correção de erros; a comunidade agradece. Os documentos detalhados em `docs/` estão em português.

🇧🇷・**Português (Brasil) —** [este arquivo](README.md)<br>
🇺🇸・**English —** [Click Here](README.en.md)<br>
🇪🇸・**Español —** [Clic aquí](README.es.md)<br>
🇨🇳・**中文 —** [点击这里](README.zh.md)<br>
🇮🇳・**हिन्दी —** [यहाँ क्लिक करें](README.hi.md)<br>
🇸🇦・**العربية —** [اضغط هنا](README.ar.md)<br>
🇫🇷・**Français —** [Cliquez ici](README.fr.md)<br>
🇮🇹・**Italiano —** [Clicca qui](README.it.md)<br>
🇰🇷・**한국어 —** [여기 클릭](README.ko.md)<br>
🇷🇺・**Русский —** [Нажмите здесь](README.ru.md)<br>
🇩🇪・**Deutsch —** [Hier klicken](README.de.md)<br>
🇯🇵・**日本語 —** [こちらをクリック](README.ja.md)<br>

## 📚 Índice

[⭐ Comece por aqui](#-comece-por-aqui) <br>
[📖 Documentação](#-documentação) <br>
[🗂️ Partituras por área](#️-partituras-por-área) <br>
[📦 Mais recursos para importar/exportar](#-mais-recursos-para-importarexportar) <br>
[🧩 As 23 famílias de tecnologia](#-as-23-famílias-de-tecnologia) <br>
[⚡ O Maestri no dia a dia](#-o-maestri-no-dia-a-dia) <br>
[🤖 Política de modelos](#-política-de-modelos) <br>
[📜 Scripts disponíveis](#-scripts-disponíveis) <br>
[🛠️ Regenerar e validar](#️-regenerar-e-validar) <br>
[🎼 Crie a sua própria partitura](#-crie-a-sua-própria-partitura) <br>
[⚠️ Segurança](#️-segurança) <br>
[🤝 Contribuição](#-contribuição) <br>

## ⭐ Comece por aqui

> Se você só quer os templates: abra o catálogo, escolha a área, arraste para o Maestri.

- [🎼 **Catálogo de partituras por área**](partituras/CATALOGO.md) — o índice mestre das 257 partituras, com link para cada área e seu pacote coletivo.
- [💻 **Catálogo de Tecnologia**](partituras/tecnologia/CATALOGO.md) — as 212 partituras de engenharia (o coração do guia).
- [📦 **Importar tudo de uma vez**](partituras/Guia-do-Maestri.maestripartituras) — pacote com todas as áreas (painel de Partituras → ⋯ → Importar Partituras…).

## 📖 Documentação

> Sete documentos, do conceito ao dia a dia. Comece pelo 01 se o Maestri é novo para você, ou pule direto para o 02 e o 06 se já conhece.

- [01 · **Conceitos**](docs/01-conceitos.md) — canvas, terminais, notas, portais, conexões, Modo Maestro, Ombro, Batuta, Andares, Rotinas, Ambientes, Wire.
- [02 · **Como usar os templates**](docs/02-como-usar-os-templates.md) — importar, reger na prática, escolher e adaptar uma partitura.
- [03 · **Atalhos e comandos**](docs/03-atalhos.md) — atalhos de teclado do macOS e a CLI `maestri`.
- [04 · **Formato `.maestripartitura`**](docs/04-formato-maestripartitura.md) — a especificação JSON, calibrada contra os arquivos oficiais.
- [05 · **Modelos e segurança**](docs/05-modelos-e-seguranca.md) — Fable/Opus/Codex, skip-permissions, stack-checklist de 30 camadas, red team autorizado.
- [06 · **O Maestri no dia a dia**](docs/06-maestri-no-dia-a-dia.md) — andares, portais, notas, rotinas e Ombro em situações reais de várias áreas.
- [07 · **Áreas e agentes disponíveis**](docs/07-areas-e-agentes.md) — a divisão por áreas, o mapa para o agency-agents e a validação do layout.
- [08 · **Andares + Partituras (receitas)**](docs/08-andares-e-partituras.md) — como usar os andares junto com as partituras, com receitas por situação e hooks.
- [09 · **Portais: web, mobile e emuladores**](docs/09-portais-mobile-web-emulador.md) — como colocar portais de navegador, web-mobile e de dispositivo (simulador iOS / emulador Android) nas partituras.
- [10 · **Importar e exportar no Maestri**](docs/10-importar-e-exportar.md) — tudo que dá para importar/exportar de forma nativa e as receitas curadas, e onde cada coisa vive no hub.
- [🎭 · **Agentes**](agentes/README.md) — arquétipos de responsabilidade e o elenco de especialistas.
- [📨 · **Prompts**](prompts/README.md) — biblioteca de prompts prontos (criar partitura, validar o Discord do Maestri).

## 🗂️ Partituras por área

> 257 partituras em 12 áreas. Cada área tem um catálogo detalhado e um pacote `.maestripartituras` para importar de uma vez.

- [💻 **Tecnologia**](partituras/tecnologia/CATALOGO.md) — 212 partituras · engenharia ponta a ponta: features, bugs, release, infra, dados, IA, migração, mobile.
- [🎨 **Design & UX**](partituras/design/CATALOGO.md) — 5 partituras · design systems, pesquisa de UX, landing pages, auditoria de UI.
- [📦 **Produto**](partituras/produto/CATALOGO.md) — 5 partituras · discovery, roadmap, PRD, síntese de feedback, concorrência.
- [📢 **Marketing & Conteúdo**](partituras/marketing/CATALOGO.md) — 5 partituras · campanhas, SEO, social, e-mail de ciclo de vida, blog técnico.
- [💼 **Vendas**](partituras/vendas/CATALOGO.md) — 4 partituras · outbound, propostas/RFP, sales enablement, discovery.
- [📊 **Dados & Analytics**](partituras/dados/CATALOGO.md) — 4 partituras · dashboards de BI, análise exploratória, métricas, A/B.
- [🔒 **Segurança & Compliance**](partituras/seguranca/CATALOGO.md) — 4 partituras · LGPD, SOC 2, threat modeling, resposta a incidente.
- [💵 **Financeiro**](partituras/financeiro/CATALOGO.md) — 4 partituras · fechamento, modelagem, FP&A, due diligence.
- [⚖️ **Jurídico**](partituras/juridico/CATALOGO.md) — 3 partituras · revisão de contrato, intake, análise de risco.
- [🛟 **Suporte & Sucesso**](partituras/suporte/CATALOGO.md) — 4 partituras · base de conhecimento, triagem, onboarding, churn.
- [🗂️ **Gestão de Projetos**](partituras/gestao/CATALOGO.md) — 4 partituras · sprint, coordenação multi-time, ata, retrospectiva.
- [🔬 **Pesquisa & Conteúdo Técnico**](partituras/pesquisa/CATALOGO.md) — 3 partituras · estado da arte, síntese, análise de mercado.

## 📦 Mais recursos para importar/exportar

> Um hub do Maestri não é só partituras. Estes recursos usam os outros formatos portáteis do app (roles, temas, instruções, notas) ou reúnem receitas prontas. Panorama completo em [docs/10 · Importar e exportar](docs/10-importar-e-exportar.md).

- [🎭 **Responsabilidades (`role.json`)**](roles/CATALOGO.md) — 30 papéis reutilizáveis no formato nativo; solte na pasta `.maestri` do projeto e use "Descobrir Responsabilidades".
- [🎨 **Temas de terminal (Ghostty)**](temas/README.md) — 4 temas para instalar em `~/.maestri/terminal/themes/`.
- [🧭 **Instruções `CLAUDE.md` / `AGENTS.md`**](instrucoes/README.md) — templates por stack, entregues aos agentes ao iniciar num workspace.
- [📝 **Templates de nota**](notas/README.md) — contrato, workboard, playbook, stack-checklist, case-file e mais, para arrastar ao canvas.
- [🧑‍🍳 **Receitas curadas**](receitas/README.md) — hooks de andar, rotinas agendadas, cliente Maestri Wire e receitas de ambientes.
- [📨 **Prompts**](prompts/README.md) — prompts prontos para o Compositor.
- [🗂️ **Espaços de trabalho (`.maestri`)**](workspaces/README.md) — como importar/compartilhar um workspace.

## 🧩 As 23 famílias de tecnologia

> A área de Tecnologia é parametrizada por catálogos (stacks, domínios, provedores). O produto famílias × variantes passa de 200 templates.

- **🚢 Ship Feature** (24) — maestro + arquiteto + 2 builders + warden, por stack.
- **🐞 Depuração** (24) — reprodutor → causa raiz → correção → verificador, por stack.
- **✅ Portão de Release** (24) — conductor + 4 revisores adversariais, por stack.
- **🏗️ Scaffold** (24) — esqueleto + setup + vertical slice + warden, por stack.
- **🔧 Migração** (12) — migração + verificador de paridade, incremental e reversível.
- **💸 Pipeline Completo** (10) — 30 camadas em 4 superfícies, por produto (regra de corte financeira).
- **☁️ Cloud & Infra** (9) — rede/compute + dados/storage + warden, por provedor.
- **🗄️ Database** (9) — schema/migração + índices sob evidência, por banco.
- **🔎 Validação BFF** (8) — SPA × BFF: paridade, CORS, cookie, por domínio.
- **🧠 AI Feature** (7) — IA + evals & guardrails.
- **📱 Ship Mobile** (7) — app + QA/a11y no portal de dispositivo.
- **🧑‍💻 Solo** (7) — um especialista sozinho.
- **📖 Documentação** (5), **⚔️ Duelo de Agentes** (5), **🚨 War Room** (5).
- **🔗 API Contract** (4), **♿ Acessibilidade** (4), **🔁 CI/CD** (4), **🔀 Data Pipeline** (4), **📦 IaC** (4), **☸️ Kubernetes** (4), **⚡ Performance** (4), **🔴 Red Team** (4, só escopo autorizado).

## ⚡ O Maestri no dia a dia

> As partituras são o começo; o valor está no fluxo. O [guia do dia a dia](docs/06-maestri-no-dia-a-dia.md) mostra como usar as features do Maestri em situações reais, e os docs [08](docs/08-andares-e-partituras.md) e [09](docs/09-portais-mobile-web-emulador.md) aprofundam andares e portais.

- **🏢 Andares (Floors)** — cópias isoladas do repo com branch própria: toque várias frentes em paralelo sem `git stash`, com hooks de Setup/Run/Teardown. Combine com uma partitura para nascer um time inteiro isolado numa branch ([receitas em docs/08](docs/08-andares-e-partituras.md)).
- **🌐 Portais** — verificação viva em navegador, web-mobile e **dispositivo** (simulador iOS / emulador Android / aparelho físico): provar um bug, aceitar uma feature, conferir uma landing, testar o app nativo ([docs/09](docs/09-portais-mobile-web-emulador.md)).
- **📝 Notas** — a fonte de verdade que sobrevive à sessão; mova para o repo o que deve ir no git, encadeie em mapa mental, deixe o Ombro resumir.
- **⏰ Rotinas** — o trabalho repetitivo sozinho: guardião de CI, vigia de deploy, clipping de concorrência, fechamento diário, triagem de tickets.
- **👤 Ombro** — o co-piloto de atenção local: "o que os agentes fizeram enquanto eu estava fora?".

## 🤖 Política de modelos

> Fable rege, Opus executa, Codex/Gemini contestam.

- **🎼 Orquestração** (maestro, conductor, IC, juiz, lead) — `claude --dangerously-skip-permissions --model fable`.
- **🔨 Execução** (arquiteto, builders, especialistas) — `--model opus`.
- **🛡️ Revisão adversarial** (release, wardens, duelo) — `codex` / `gemini`, de propósito: um modelo diferente pega o que o outro deixou passar.
- Detalhes e salvaguardas em [docs/05 · Modelos e segurança](docs/05-modelos-e-seguranca.md).

## 📜 Scripts disponíveis

> Todo o hub é gerado por Python (só stdlib). Detalhes de uso e como estender em [`scripts/README.md`](scripts/README.md).

| Script | Tipo | O que faz |
|---|---|---|
| [`scripts/maestri_build.py`](scripts/maestri_build.py) | biblioteca | Classe `Partitura`, serialização `.maestripartitura`, ropePoints, layout e portais. |
| [`scripts/roles_lib.py`](scripts/roles_lib.py) | biblioteca | Prompts de responsabilidade (pt-BR) e templates de nota. |
| [`scripts/generate_partituras.py`](scripts/generate_partituras.py) | gerador | Monta as 257 partituras por área, os pacotes e os catálogos. |
| [`scripts/generate_hub.py`](scripts/generate_hub.py) | gerador | Gera `roles/` (role.json), `notas/` e `instrucoes/`. |
| [`tests/validate_partituras.py`](tests/validate_partituras.py) | validação | Compara cada partitura com a oficial de referência (zero divergências). |
| [`tests/validate_hub.py`](tests/validate_hub.py) | validação | Valida os `role.json`, as notas e os pares `CLAUDE.md`/`AGENTS.md`. |

## 🛠️ Regenerar e validar

> O gerador não depende de nada além da stdlib do Python 3. UUIDs determinísticos: regerar produz os mesmos arquivos byte a byte.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → "Zero divergências" vs a partitura oficial
python3 tests/validate_hub.py               # → valida os role.json e a estrutura do hub
```

- `scripts/maestri_build.py` — classe `Partitura`, serialização, ropePoints, layout, portais.
- `scripts/roles_lib.py` — prompts de responsabilidade (pt-BR) + templates de nota.
- `scripts/generate_partituras.py` — famílias parametrizadas por catálogos, agrupadas por área.
- `scripts/generate_hub.py` — gera a biblioteca de `role.json`, as notas avulsas e as instruções.
- `tests/validate_partituras.py` / `tests/validate_hub.py` — validam partituras e recursos do hub.

## 🎼 Crie a sua própria partitura

> Uma partitura é só um arranjo salvo do seu canvas — você monta o time do seu jeito e guarda para reusar. Três caminhos:

**No app (o mais rápido):**
1. Monte o canvas: crie os terminais (com os comandos/modelos), escreva as notas de contrato e workboard, adicione os portais e conecte tudo (`Ctrl+L`).
2. Selecione os elementos (arraste uma seleção ou shift+clique).
3. Botão direito → **Partituras → Criar nova…** (ou `Ctrl+P` → "Nova Partitura a partir da seleção").
4. Dê nome, descrição, ícone e cor. As responsabilidades ficam embutidas, então a partitura funciona na hora em qualquer workspace.
5. Exporte arrastando o card para o Finder, ou compartilhe o `.maestripartitura`.

**Deixe o maestro montar por você:** cole o [prompt inicial](prompts/prompt-inicial.md) ou o [prompt "criar partitura"](prompts/criar-partitura.md) no maestro — ele monta o time e o contrato seguindo os princípios do guia, e você salva o resultado.

**No gerador (para produzir muitas de uma vez):** adapte os catálogos em [`scripts/generate_partituras.py`](scripts/generate_partituras.py); o formato está em [docs/04](docs/04-formato-maestripartitura.md) e o passo a passo em [docs/02](docs/02-como-usar-os-templates.md).

Reaproveite papéis prontos da [biblioteca de responsabilidades](roles/CATALOGO.md) e notas da [pasta de notas](notas/README.md).

## ⚠️ Segurança

> Adicionar uma partitura ao canvas **inicia os terminais dela e executa comandos na sua máquina** (`claude`, `codex`, `gemini`).

- **Leia os comandos** na tela de revisão antes de importar e só aceite partituras de fontes confiáveis.
- As partituras de **Red Team** e qualquer engajamento ofensivo operam **exclusivamente em escopo autorizado**, nunca em produção e nunca com dados de pessoas reais.
- Detalhes em [docs/05 · Modelos e segurança](docs/05-modelos-e-seguranca.md).

## 🤝 Contribuição

> Este repositório é um hub público do Maestri. Contribuições são bem-vindas — partituras, papéis, temas, instruções, receitas, traduções e correções.

- **Abra uma issue** para propor uma ideia, relatar um erro ou sugerir uma área/família nova.
- **Abra um pull request** com a sua adição. Formas comuns:
  - uma **partitura** nova (via catálogo em `scripts/generate_partituras.py`) ou um `.maestripartitura` exportado;
  - um **papel** (`role.json`) na biblioteca [`roles/`](roles/CATALOGO.md);
  - um **tema** (Ghostty) em [`temas/`](temas/README.md);
  - uma **instrução** (`CLAUDE.md`/`AGENTS.md`) em [`instrucoes/`](instrucoes/README.md);
  - uma **receita** (hook, rotina, ambiente, cliente Wire) em [`receitas/`](receitas/README.md);
  - uma **tradução** ou correção de um dos `README.<idioma>.md`.
- **Antes de enviar**, rode os geradores e as validações e garanta que tudo passa:
  ```bash
  python3 scripts/generate_partituras.py && python3 scripts/generate_hub.py
  python3 tests/validate_partituras.py && python3 tests/validate_hub.py
  ```
- **Mantenha o determinismo:** não edite arquivos gerados à mão — mude o gerador e regenere.
- Compartilhe partituras só com comandos que você confia; nunca embuta segredos.

Não sabe por onde começar? Veja [docs/10 · Importar e exportar](docs/10-importar-e-exportar.md) e o [scripts/README.md](scripts/README.md).

---

<p align="center">
  <sub>Feito para reger agentes. Fable rege, Opus executa, Codex e Gemini contestam. 🎻</sub>
</p>
