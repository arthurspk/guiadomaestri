<p align="center">
  <a href="https://www.themaestri.app/pt-br">
    <img src="https://img.shields.io/badge/%F0%9F%8E%BC-Guia%20do%20Maestri-5856D6?style=for-the-badge" alt="Guia do Maestri" height="40">
  </a>
</p>

<h1 align="center">🎼 Guia do Maestri</h1>

<p align="center">
  <b>O guia em português para reger times de agentes de IA no <a href="https://www.themaestri.app/pt-br">Maestri</a> — com ênfase em tecnologia e um gerador de 257 partituras prontas, divididas por área.</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/partituras-257-5856D6?style=for-the-badge" alt="257 partituras"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/%C3%A1reas-12-007AFF?style=for-the-badge" alt="12 áreas"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/formato-.maestripartitura%20v1-34C759?style=for-the-badge" alt="Formato"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/valida%C3%A7%C3%A3o-0%20diverg%C3%AAncias-FF9500?style=for-the-badge" alt="Validado"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/idioma-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

## :dart: A proposta

> O **Maestri** é um app de macOS onde você **rege um time de agentes de código** — Claude Code, Codex, Gemini, OpenCode — num **canvas infinito**: terminais são agentes, notas markdown são a fonte de verdade compartilhada, portais são navegadores embutidos para verificação viva, e o **maestro** delega e coordena. Este repositório é ao mesmo tempo um **guia em pt-BR** e um **gerador em Python** que produz **257 partituras** (`.maestripartitura`) prontas para arrastar para o canvas e reger — cada uma é um time completo, com responsabilidades embutidas, notas, portais e conexões. A ênfase é **tecnologia**, e há mais 11 áreas de negócio (design, produto, marketing, vendas, dados, segurança, financeiro, jurídico, suporte, gestão, pesquisa).

## 💡 Como este guia é organizado

> Duas influências, juntas. A **divisão por áreas** (departamentos de uma agência de IA) vem do [agency-agents](https://github.com/msitarzewski/agency-agents), catálogo com 230+ agentes em 18 divisões. O **layout** — cabeçalho, proposta, índice com âncoras e seções em pt-BR — segue o [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil). Detalhes dessa validação em [docs/07](docs/07-areas-e-agentes.md).

## 📚 Índice

[⭐ Comece por aqui](#-comece-por-aqui) <br>
[📖 Documentação](#-documentação) <br>
[🗂️ Partituras por área](#️-partituras-por-área) <br>
[🧩 As 23 famílias de tecnologia](#-as-23-famílias-de-tecnologia) <br>
[⚡ O Maestri no dia a dia](#-o-maestri-no-dia-a-dia) <br>
[🤖 Política de modelos](#-política-de-modelos) <br>
[🛠️ Regenerar e validar](#️-regenerar-e-validar) <br>
[⚠️ Segurança](#️-segurança) <br>
[🔗 Referências](#-referências) <br>

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
- [🎭 · **Agentes**](agentes/README.md) — arquétipos de responsabilidade e o elenco de especialistas.

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

> As partituras são o começo; o valor está no fluxo. O [guia do dia a dia](docs/06-maestri-no-dia-a-dia.md) mostra como usar as features do Maestri em situações reais.

- **🏢 Andares (Floors)** — cópias isoladas do repo com branch própria: toque várias frentes em paralelo sem `git stash`, com hooks de Setup/Run/Teardown. Combine com uma partitura para nascer um time inteiro isolado numa branch.
- **🌐 Portais** — verificação viva: provar um bug, aceitar uma feature, conferir uma landing publicada, olhar um concorrente, ler um dashboard, testar no simulador mobile.
- **📝 Notas** — a fonte de verdade que sobrevive à sessão; mova para o repo o que deve ir no git, encadeie em mapa mental, deixe o Ombro resumir.
- **⏰ Rotinas** — o trabalho repetitivo sozinho: guardião de CI, vigia de deploy, clipping de concorrência, fechamento diário, triagem de tickets.
- **👤 Ombro** — o co-piloto de atenção local: "o que os agentes fizeram enquanto eu estava fora?".

## 🤖 Política de modelos

> Fable rege, Opus executa, Codex/Gemini contestam.

- **🎼 Orquestração** (maestro, conductor, IC, juiz, lead) — `claude --dangerously-skip-permissions --model fable`.
- **🔨 Execução** (arquiteto, builders, especialistas) — `--model opus`.
- **🛡️ Revisão adversarial** (release, wardens, duelo) — `codex` / `gemini`, de propósito: um modelo diferente pega o que o outro deixou passar.
- Detalhes e salvaguardas em [docs/05 · Modelos e segurança](docs/05-modelos-e-seguranca.md).

## 🛠️ Regenerar e validar

> O gerador não depende de nada além da stdlib do Python 3. UUIDs determinísticos: regerar produz os mesmos arquivos byte a byte.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 tests/validate_partituras.py        # → "Zero divergências" vs a partitura oficial
```

- `scripts/maestri_build.py` — classe `Partitura`, serialização, ropePoints, layout.
- `scripts/roles_lib.py` — prompts de responsabilidade (pt-BR) + templates de nota.
- `scripts/generate_partituras.py` — famílias parametrizadas por catálogos, agrupadas por área.
- `tests/validate_partituras.py` — compara chaves de topo/payload/nós/roles com o arquivo oficial.

## ⚠️ Segurança

> Adicionar uma partitura ao canvas **inicia os terminais dela e executa comandos na sua máquina** (`claude`, `codex`, `gemini`).

- **Leia os comandos** na tela de revisão antes de importar e só aceite partituras de fontes confiáveis.
- As partituras de **Red Team** e qualquer engajamento ofensivo operam **exclusivamente em escopo autorizado**, nunca em produção e nunca com dados de pessoas reais.
- Detalhes em [docs/05 · Modelos e segurança](docs/05-modelos-e-seguranca.md).

## 🔗 Referências

- [Documentação oficial do Maestri](https://www.themaestri.app/pt-br/docs) — canvas, terminais, notas, portais, andares, rotinas, Wire.
- [agency-agents](https://github.com/msitarzewski/agency-agents) — catálogo de 230+ agentes em 18 divisões (inspiração das áreas).
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) — guia pt-BR de referência (inspiração do layout).

---

<p align="center">
  <sub>Feito para reger agentes. Fable rege, Opus executa, Codex e Gemini contestam. 🎻</sub>
</p>
