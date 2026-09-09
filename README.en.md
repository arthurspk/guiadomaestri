<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Maestri Guide" width="160" height="160">
  </a>
</p>

<h1 align="center">Maestri Guide</h1>

<p align="center">
  <b>The guide to conducting teams of AI agents in <a href="https://www.themaestri.app">Maestri</a> — with a focus on technology and a generator of 257 ready-made scores, organized by area.</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/scores-257-5856D6?style=for-the-badge" alt="257 scores"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/areas-12-007AFF?style=for-the-badge" alt="12 areas"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/format-.maestripartitura%20v1-34C759?style=for-the-badge" alt="Format"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/validation-0%20mismatches-FF9500?style=for-the-badge" alt="Validated"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/language-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

> **Note:** This is a translation. The base guide and the detailed documents under `docs/` are written in Brazilian Portuguese.

## 🎯 What this is

> **Maestri** is a macOS app where you **conduct a team of coding agents** — Claude Code, Codex, Gemini, OpenCode — on an **infinite canvas**: terminals are agents, markdown notes are the shared source of truth, portals are embedded browsers for live verification, and the **maestro** delegates and coordinates. This repository is both a **guide** and a **Python generator** that produces **257 scores** (`.maestripartitura`) ready to drag onto the canvas and conduct — each one a full team, with embedded responsibilities, notes, portals, and connections. The focus is **technology**, plus 11 more business areas (design, product, marketing, sales, data, security, finance, legal, support, project management, research).

## 💡 How this guide is organized

> Two influences, combined. The **division by areas** (departments of an AI agency) comes from [agency-agents](https://github.com/msitarzewski/agency-agents), a catalog of 230+ agents across 18 divisions. The **layout** — header, pitch, anchored index, and sections — follows [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil). Details of that comparison in [docs/07](docs/07-areas-e-agentes.md).

## 🌍 Translation

> If you would like to follow this guide in another language, pick one below. You can also help translate it into more languages or fix mistakes; the community thanks you. The detailed documents under `docs/` are in Portuguese.

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

## ⭐ Start here

> If you just want the templates: open the catalog, pick an area, drag it into Maestri.

- [🎼 **Catalog of scores by area**](partituras/CATALOGO.md) — the master index of the 257 scores, linking each area and its bundle.
- [💻 **Technology catalog**](partituras/tecnologia/CATALOGO.md) — the 212 engineering scores (the heart of the guide).
- [📦 **Import everything at once**](partituras/Guia-do-Maestri.maestripartituras) — a bundle with every area (Scores panel → ⋯ → Import Scores…).

## 📖 Documentation

> Nine documents plus the agents guide, in Portuguese. Start at 01 if Maestri is new to you, or jump to 02 and 06 if you already know it.

- **01 · Concepts** ([docs/01](docs/01-conceitos.md)) — canvas, terminals, notes, portals, connections, Maestro Mode, Ombro, Batuta, Floors, Routines, Environments, Wire.
- **02 · Using the templates** ([docs/02](docs/02-como-usar-os-templates.md)) — import, conduct in practice, choose and adapt a score.
- **03 · Shortcuts and commands** ([docs/03](docs/03-atalhos.md)) — macOS keyboard shortcuts and the `maestri` CLI.
- **04 · The `.maestripartitura` format** ([docs/04](docs/04-formato-maestripartitura.md)) — the JSON spec, calibrated against the official files.
- **05 · Models and security** ([docs/05](docs/05-modelos-e-seguranca.md)) — Fable/Opus/Codex, skip-permissions, the 30-layer stack checklist, authorized red team.
- **06 · Maestri day to day** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) — floors, portals, notes, routines, and Ombro in real situations across areas.
- **07 · Areas and available agents** ([docs/07](docs/07-areas-e-agentes.md)) — the division by areas, the map to agency-agents, and the layout validation.
- **08 · Floors + Scores (recipes)** ([docs/08](docs/08-andares-e-partituras.md)) — how to use floors together with scores, with per-situation recipes and hooks.
- **09 · Portals: web, mobile, emulators** ([docs/09](docs/09-portais-mobile-web-emulador.md)) — how to add browser, mobile-web, and device portals (iOS simulator / Android emulator) to scores.
- **10 · Import and export in Maestri** ([docs/10](docs/10-importar-e-exportar.md)) — everything you can natively import/export plus the curated recipes, and where each one lives in the hub.
- **🎭 · Agents** ([agentes/README.md](agentes/README.md)) — responsibility archetypes and the cast of specialists.
- **📨 · Prompts** ([prompts](prompts/README.md)) — a library of ready prompts (create a score, validate the Maestri Discord).

## 🗂️ Scores by area

> 257 scores across 12 areas. Each area has a detailed catalog and a `.maestripartituras` bundle to import at once.

- [💻 **Technology**](partituras/tecnologia/CATALOGO.md) — 212 scores · end-to-end engineering: features, bugs, release, infra, data, AI, migration, mobile.
- [🎨 **Design & UX**](partituras/design/CATALOGO.md) — 5 scores · design systems, UX research, landing pages, UI audit.
- [📦 **Product**](partituras/produto/CATALOGO.md) — 5 scores · discovery, roadmap, PRD, feedback synthesis, competition.
- [📢 **Marketing & Content**](partituras/marketing/CATALOGO.md) — 5 scores · campaigns, SEO, social, lifecycle email, technical blog.
- [💼 **Sales**](partituras/vendas/CATALOGO.md) — 4 scores · outbound, proposals/RFP, sales enablement, discovery.
- [📊 **Data & Analytics**](partituras/dados/CATALOGO.md) — 4 scores · BI dashboards, exploratory analysis, metrics, A/B.
- [🔒 **Security & Compliance**](partituras/seguranca/CATALOGO.md) — 4 scores · GDPR/LGPD, SOC 2, threat modeling, incident response.
- [💵 **Finance**](partituras/financeiro/CATALOGO.md) — 4 scores · close, modeling, FP&A, due diligence.
- [⚖️ **Legal**](partituras/juridico/CATALOGO.md) — 3 scores · contract review, intake, risk analysis.
- [🛟 **Support & Success**](partituras/suporte/CATALOGO.md) — 4 scores · knowledge base, triage, onboarding, churn.
- [🗂️ **Project Management**](partituras/gestao/CATALOGO.md) — 4 scores · sprint, multi-team coordination, minutes, retrospective.
- [🔬 **Research & Technical Content**](partituras/pesquisa/CATALOGO.md) — 3 scores · state of the art, synthesis, market analysis.

## 📦 More resources to import/export

> A Maestri hub is more than scores. These use the app's other portable formats (roles, themes, instructions, notes) or bundle ready-made recipes. Full overview in [docs/10 · Import and export](docs/10-importar-e-exportar.md).

- [🎭 **Responsibilities (`role.json`)**](roles/CATALOGO.md) — 30 reusable roles in the native format; drop into the project's `.maestri` folder and use "Discover Responsibilities".
- [🎨 **Terminal themes (Ghostty)**](temas/README.md) — 4 themes to install in `~/.maestri/terminal/themes/`.
- [🧭 **`CLAUDE.md` / `AGENTS.md` instructions**](instrucoes/README.md) — per-stack templates delivered to agents when they start in a workspace.
- [📝 **Note templates**](notas/README.md) — contract, workboard, playbook, stack-checklist, case-file and more, to drag onto the canvas.
- [🧑‍🍳 **Curated recipes**](receitas/README.md) — floor hooks, scheduled routines, a Maestri Wire client, and environment recipes.
- [📨 **Prompts**](prompts/README.md) — ready prompts for the Prompt Composer.
- [🗂️ **Workspaces (`.maestri`)**](workspaces/README.md) — how to import/share a workspace.

## 🧩 The 23 technology families

> The Technology area is parameterized by catalogs (stacks, domains, providers). Families × variants exceeds 200 templates.

- **🚢 Ship Feature** (24) — maestro + architect + 2 builders + warden, per stack.
- **🐞 Debugging** (24) — reproducer → root cause → fix → verifier, per stack.
- **✅ Release Gate** (24) — conductor + 4 adversarial reviewers, per stack.
- **🏗️ Scaffold** (24) — skeleton + setup + vertical slice + warden, per stack.
- **🔧 Migration** (12) — migration + parity verifier, incremental and reversible.
- **💸 Full Pipeline** (10) — 30 layers across 4 surfaces, per product (financial cutoff rule).
- **☁️ Cloud & Infra** (9) — network/compute + data/storage + warden, per provider.
- **🗄️ Database** (9) — schema/migration + indexes backed by evidence, per database.
- **🔎 BFF Validation** (8) — SPA × BFF: parity, CORS, cookie, per domain.
- **🧠 AI Feature** (7) — AI + evals & guardrails.
- **📱 Ship Mobile** (7) — app + QA/a11y on a device portal.
- **🧑‍💻 Solo** (7) — a single specialist.
- **📖 Documentation** (5), **⚔️ Agent Duel** (5), **🚨 War Room** (5).
- **🔗 API Contract** (4), **♿ Accessibility** (4), **🔁 CI/CD** (4), **🔀 Data Pipeline** (4), **📦 IaC** (4), **☸️ Kubernetes** (4), **⚡ Performance** (4), **🔴 Red Team** (4, authorized scope only).

## ⚡ Maestri day to day

> The scores are the start; the value is in the workflow. The [day-to-day guide](docs/06-maestri-no-dia-a-dia.md) shows how to use Maestri's features in real situations, and docs [08](docs/08-andares-e-partituras.md) and [09](docs/09-portais-mobile-web-emulador.md) go deep on floors and portals.

- **🏢 Floors** — isolated copies of the repo with their own branch: work several fronts in parallel without `git stash`, with Setup/Run/Teardown hooks. Combine with a score to spin up a whole team isolated on a branch.
- **🌐 Portals** — live verification in browser, mobile-web, and **device** (iOS simulator / Android emulator / physical device): prove a bug, accept a feature, check a landing page, test the native app.
- **📝 Notes** — the source of truth that outlives the session; move to the repo what belongs in git, chain into a mind map, let Ombro summarize.
- **⏰ Routines** — repetitive work on its own: CI guardian, deploy watcher, competitor clipping, daily close, ticket triage.
- **👤 Ombro** — the local attention co-pilot: "what did the agents do while I was away?".

## 🤖 Model policy

> Fable conducts, Opus executes, Codex/Gemini challenge.

- **🎼 Orchestration** (maestro, conductor, IC, judge, lead) — `claude --dangerously-skip-permissions --model fable`.
- **🔨 Execution** (architect, builders, specialists) — `--model opus`.
- **🛡️ Adversarial review** (release, wardens, duel) — `codex` / `gemini`, on purpose: a different model catches what the other missed.
- Details and safeguards in [docs/05](docs/05-modelos-e-seguranca.md).

## 🛠️ Regenerate and validate

> The generator needs nothing beyond the Python 3 standard library. Deterministic UUIDs: regenerating produces byte-for-byte identical files.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → "Zero divergências" vs the official score
python3 tests/validate_hub.py               # → validates the role.json files and the hub structure
```

- `scripts/maestri_build.py` — the `Partitura` class, serialization, ropePoints, layout.
- `scripts/roles_lib.py` — responsibility prompts (pt-BR) + note templates.
- `scripts/generate_partituras.py` — families parameterized by catalogs, grouped by area.
- `tests/validate_partituras.py` — compares top/payload/node/role keys against the official file.

## ⚠️ Security

> Adding a score to the canvas **starts its terminals and runs commands on your machine** (`claude`, `codex`, `gemini`).

- **Read the commands** on the review screen before importing, and only accept scores from trusted sources.
- **Red Team** scores and any offensive engagement operate **strictly within authorized scope**, never in production and never with real people's data.
- Details in [docs/05](docs/05-modelos-e-seguranca.md).

## 🔗 References

- [Official Maestri documentation](https://www.themaestri.app/pt-br/docs) — canvas, terminals, notes, portals, floors, routines, Wire.
- [agency-agents](https://github.com/msitarzewski/agency-agents) — a catalog of 230+ agents across 18 divisions (inspiration for the areas).
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) — a reference pt-BR guide (inspiration for the layout).

---

<p align="center">
  <sub>Built to conduct agents. Fable conducts, Opus executes, Codex and Gemini challenge. 🎻</sub>
</p>
