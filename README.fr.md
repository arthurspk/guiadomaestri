<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Guide Maestri" width="160" height="160">
  </a>
</p>

<h1 align="center">Guide Maestri</h1>

<p align="center">
  <b>Le guide pour diriger des équipes d'agents IA dans <a href="https://www.themaestri.app">Maestri</a> — axé sur la technologie, avec un générateur de 257 partitions prêtes à l'emploi, organisées par domaine.</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/partitions-257-5856D6?style=for-the-badge" alt="257 partitions"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/domaines-12-007AFF?style=for-the-badge" alt="12 domaines"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/format-.maestripartitura%20v1-34C759?style=for-the-badge" alt="Format"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/validation-0%20%C3%A9cart-FF9500?style=for-the-badge" alt="Validé"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/langue-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

> **Note :** Ceci est une traduction. Le guide de base et les documents détaillés sous `docs/` sont en portugais brésilien.

## 🎯 De quoi s'agit-il

> **Maestri** est une app macOS où vous **dirigez une équipe d'agents de code** — Claude Code, Codex, Gemini, OpenCode — sur un **canevas infini** : les terminaux sont des agents, les notes markdown sont la source de vérité partagée, les portails sont des navigateurs intégrés pour la vérification en direct, et le **maestro** délègue et coordonne. Ce dépôt est à la fois un **guide** et un **générateur Python** qui produit **257 partitions** (`.maestripartitura`) prêtes à glisser sur le canevas et à diriger — chacune est une équipe complète, avec responsabilités, notes, portails et connexions intégrés. L'accent est mis sur la **technologie**, plus 11 domaines métier (design, produit, marketing, ventes, données, sécurité, finance, juridique, support, gestion de projet, recherche).

## 💡 Comment ce guide est organisé

> Deux influences réunies. La **division par domaines** (départements d'une agence IA) vient de [agency-agents](https://github.com/msitarzewski/agency-agents), un catalogue de 230+ agents répartis en 18 divisions. La **mise en page** — en-tête, présentation, sommaire ancré et sections — suit [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil). Détails de cette comparaison dans [docs/07](docs/07-areas-e-agentes.md).

## 🌍 Traduction

> Si vous souhaitez suivre ce guide dans une autre langue, choisissez ci-dessous. Vous pouvez aussi contribuer aux traductions ou corriger des erreurs ; la communauté vous en remercie. Les documents détaillés sous `docs/` sont en portugais.

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

## ⭐ Commencer ici

> Si vous voulez juste les modèles : ouvrez le catalogue, choisissez un domaine, glissez-le dans Maestri.

- [🎼 **Catalogue des partitions par domaine**](partituras/CATALOGO.md) — l'index principal des 257 partitions, avec un lien vers chaque domaine et son bundle.
- [💻 **Catalogue Technologie**](partituras/tecnologia/CATALOGO.md) — les 212 partitions d'ingénierie (le cœur du guide).
- [📦 **Tout importer d'un coup**](partituras/Guia-do-Maestri.maestripartituras) — un bundle avec tous les domaines (panneau Partitions → ⋯ → Importer des Partitions…).

## 📖 Documentation

> Neuf documents plus le guide des agents, en portugais. Commencez par le 01 si Maestri est nouveau pour vous, ou passez au 02 et au 06 si vous le connaissez déjà.

- **01 · Concepts** ([docs/01](docs/01-conceitos.md)) — canevas, terminaux, notes, portails, connexions, Mode Maestro, Ombro, Batuta, Étages (Floors), Routines, Environnements, Wire.
- **02 · Utiliser les modèles** ([docs/02](docs/02-como-usar-os-templates.md)) — importer, diriger en pratique, choisir et adapter une partition.
- **03 · Raccourcis et commandes** ([docs/03](docs/03-atalhos.md)) — raccourcis clavier macOS et la CLI `maestri`.
- **04 · Le format `.maestripartitura`** ([docs/04](docs/04-formato-maestripartitura.md)) — la spécification JSON, calibrée sur les fichiers officiels.
- **05 · Modèles et sécurité** ([docs/05](docs/05-modelos-e-seguranca.md)) — Fable/Opus/Codex, skip-permissions, checklist de 30 couches, red team autorisée.
- **06 · Maestri au quotidien** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) — étages, portails, notes, routines et Ombro en situations réelles.
- **07 · Domaines et agents disponibles** ([docs/07](docs/07-areas-e-agentes.md)) — la division par domaines, la carte vers agency-agents, la validation de la mise en page.
- **08 · Étages + Partitions (recettes)** ([docs/08](docs/08-andares-e-partituras.md)) — comment utiliser les étages avec les partitions, avec des recettes par situation et des hooks.
- **09 · Portails : web, mobile, émulateurs** ([docs/09](docs/09-portais-mobile-web-emulador.md)) — comment ajouter des portails navigateur, web-mobile et appareil (simulateur iOS / émulateur Android) aux partitions.
- **10 · Importer et exporter dans Maestri** ([docs/10](docs/10-importar-e-exportar.md)) — tout ce qui s'importe/exporte nativement plus les recettes curées, et où chaque chose vit dans le hub.
- **🎭 · Agents** ([agentes/README.md](agentes/README.md)) — archétypes de responsabilité et la troupe de spécialistes.
- **📨 · Prompts** ([prompts](prompts/README.md)) — une bibliothèque de prompts prêts (créer une partition, valider le Discord de Maestri).

## 🗂️ Partitions par domaine

> 257 partitions dans 12 domaines. Chaque domaine a un catalogue détaillé et un bundle `.maestripartituras` à importer en une fois.

- [💻 **Technologie**](partituras/tecnologia/CATALOGO.md) — 212 partitions · ingénierie de bout en bout : fonctionnalités, bugs, release, infra, données, IA, migration, mobile.
- [🎨 **Design & UX**](partituras/design/CATALOGO.md) — 5 partitions · design systems, recherche UX, landing pages, audit UI.
- [📦 **Produit**](partituras/produto/CATALOGO.md) — 5 partitions · discovery, roadmap, PRD, synthèse de feedback, concurrence.
- [📢 **Marketing & Contenu**](partituras/marketing/CATALOGO.md) — 5 partitions · campagnes, SEO, social, e-mail de cycle de vie, blog technique.
- [💼 **Ventes**](partituras/vendas/CATALOGO.md) — 4 partitions · outbound, propositions/RFP, sales enablement, discovery.
- [📊 **Données & Analytics**](partituras/dados/CATALOGO.md) — 4 partitions · tableaux de bord BI, analyse exploratoire, métriques, A/B.
- [🔒 **Sécurité & Conformité**](partituras/seguranca/CATALOGO.md) — 4 partitions · RGPD/LGPD, SOC 2, threat modeling, réponse aux incidents.
- [💵 **Finance**](partituras/financeiro/CATALOGO.md) — 4 partitions · clôture, modélisation, FP&A, due diligence.
- [⚖️ **Juridique**](partituras/juridico/CATALOGO.md) — 3 partitions · revue de contrat, intake, analyse de risque.
- [🛟 **Support & Succès**](partituras/suporte/CATALOGO.md) — 4 partitions · base de connaissances, triage, onboarding, churn.
- [🗂️ **Gestion de Projet**](partituras/gestao/CATALOGO.md) — 4 partitions · sprint, coordination multi-équipes, compte-rendu, rétrospective.
- [🔬 **Recherche & Contenu Technique**](partituras/pesquisa/CATALOGO.md) — 3 partitions · état de l'art, synthèse, analyse de marché.

## 📦 Plus de ressources à importer/exporter

> Un hub Maestri, ce n'est pas que des partitions. Ces ressources utilisent les autres formats portables de l'app (rôles, thèmes, instructions, notes) ou regroupent des recettes prêtes. Panorama complet dans [docs/10 · Importer et exporter](docs/10-importar-e-exportar.md).

- [🎭 **Responsabilités (`role.json`)**](roles/CATALOGO.md) — 30 rôles réutilisables au format natif ; déposez-les dans le dossier `.maestri` du projet et utilisez « Découvrir les responsabilités ».
- [🎨 **Thèmes de terminal (Ghostty)**](temas/README.md) — 4 thèmes à installer dans `~/.maestri/terminal/themes/`.
- [🧭 **Instructions `CLAUDE.md` / `AGENTS.md`**](instrucoes/README.md) — des modèles par stack, remis aux agents au démarrage d'un workspace.
- [📝 **Modèles de note**](notas/README.md) — contrat, workboard, playbook, stack-checklist, case-file et plus, à glisser sur le canevas.
- [🧑‍🍳 **Recettes curées**](receitas/README.md) — hooks d'étage, routines planifiées, un client Maestri Wire et des recettes d'environnements.
- [📨 **Prompts**](prompts/README.md) — des prompts prêts pour le Compositeur de Prompts.
- [🗂️ **Espaces de travail (`.maestri`)**](workspaces/README.md) — comment importer/partager un workspace.

## 🧩 Les 23 familles technologiques

> Le domaine Technologie est paramétré par des catalogues (stacks, domaines, fournisseurs). Familles × variantes dépasse 200 modèles.

- **🚢 Ship Feature** (24) — maestro + architecte + 2 builders + warden, par stack.
- **🐞 Débogage** (24) — reproducteur → cause racine → correctif → vérificateur, par stack.
- **✅ Porte de Release** (24) — conductor + 4 relecteurs adversariaux, par stack.
- **🏗️ Scaffold** (24) — squelette + setup + vertical slice + warden, par stack.
- **🔧 Migration** (12) — migration + vérificateur de parité, incrémental et réversible.
- **💸 Pipeline Complet** (10) — 30 couches sur 4 surfaces, par produit (règle de coupure financière).
- **☁️ Cloud & Infra** (9) — réseau/compute + données/stockage + warden, par fournisseur.
- **🗄️ Base de données** (9) — schéma/migration + index étayés par des preuves, par base.
- **🔎 Validation BFF** (8) — SPA × BFF : parité, CORS, cookie, par domaine.
- **🧠 Fonction IA** (7) — IA + evals & garde-fous.
- **📱 Ship Mobile** (7) — app + QA/a11y sur un portail appareil.
- **🧑‍💻 Solo** (7) — un seul spécialiste.
- **📖 Documentation** (5), **⚔️ Duel d'Agents** (5), **🚨 War Room** (5).
- **🔗 API Contract** (4), **♿ Accessibilité** (4), **🔁 CI/CD** (4), **🔀 Data Pipeline** (4), **📦 IaC** (4), **☸️ Kubernetes** (4), **⚡ Performance** (4), **🔴 Red Team** (4, périmètre autorisé uniquement).

## ⚡ Maestri au quotidien

> Les partitions sont le début ; la valeur est dans le flux. Le [guide du quotidien](docs/06-maestri-no-dia-a-dia.md) montre comment utiliser les fonctionnalités de Maestri dans des situations réelles, et les docs [08](docs/08-andares-e-partituras.md) et [09](docs/09-portais-mobile-web-emulador.md) approfondissent étages et portails.

- **🏢 Étages (Floors)** — copies isolées du dépôt avec leur propre branche : travaillez plusieurs fronts en parallèle sans `git stash`, avec des hooks Setup/Run/Teardown. Combinez avec une partition pour faire naître une équipe entière isolée sur une branche.
- **🌐 Portails** — vérification en direct dans le navigateur, web-mobile et **appareil** (simulateur iOS / émulateur Android / appareil physique) : prouver un bug, accepter une fonctionnalité, vérifier une landing, tester l'app native.
- **📝 Notes** — la source de vérité qui survit à la session ; déplacez vers le dépôt ce qui doit aller dans git, chaînez en carte mentale, laissez Ombro résumer.
- **⏰ Routines** — le travail répétitif tout seul : gardien de CI, veille de déploiement, veille concurrentielle, clôture quotidienne, triage de tickets.
- **👤 Ombro** — le copilote d'attention local : « qu'ont fait les agents pendant mon absence ? ».

## 🤖 Politique des modèles

> Fable dirige, Opus exécute, Codex/Gemini contestent.

- **🎼 Orchestration** (maestro, conductor, IC, juge, lead) — `claude --dangerously-skip-permissions --model fable`.
- **🔨 Exécution** (architecte, builders, spécialistes) — `--model opus`.
- **🛡️ Revue adversariale** (release, wardens, duel) — `codex` / `gemini`, volontairement : un modèle différent attrape ce que l'autre a laissé passer.
- Détails et garde-fous dans [docs/05](docs/05-modelos-e-seguranca.md).

## 📜 Scripts disponibles

> Tout le hub est généré par Python (stdlib uniquement). Usage et extension dans [`scripts/README.md`](scripts/README.md).

| Script | Type | Ce qu'il fait |
|---|---|---|
| [`scripts/maestri_build.py`](scripts/maestri_build.py) | bibliothèque | Classe `Partitura`, sérialisation `.maestripartitura`, ropePoints, layout, portails. |
| [`scripts/roles_lib.py`](scripts/roles_lib.py) | bibliothèque | Prompts de responsabilité (pt-BR) et modèles de note. |
| [`scripts/generate_partituras.py`](scripts/generate_partituras.py) | générateur | Construit les 257 partitions par domaine, les bundles et les catalogues. |
| [`scripts/generate_hub.py`](scripts/generate_hub.py) | générateur | Génère `roles/` (role.json), `notas/` et `instrucoes/`. |
| [`tests/validate_partituras.py`](tests/validate_partituras.py) | validation | Compare chaque partition à la référence officielle (zéro écart). |
| [`tests/validate_hub.py`](tests/validate_hub.py) | validation | Valide les role.json, les notes et les paires CLAUDE.md/AGENTS.md. |

## 🛠️ Régénérer et valider

> Le générateur ne dépend que de la bibliothèque standard de Python 3. UUID déterministes : régénérer produit des fichiers identiques octet par octet.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → "Zero divergências" vs la partition officielle
python3 tests/validate_hub.py               # → valide les role.json et la structure du hub
```

- `scripts/maestri_build.py` — la classe `Partitura`, sérialisation, ropePoints, layout.
- `scripts/roles_lib.py` — prompts de responsabilité (pt-BR) + modèles de note.
- `scripts/generate_partituras.py` — familles paramétrées par catalogues, groupées par domaine.
- `tests/validate_partituras.py` — compare les clés top/payload/nœud/rôle au fichier officiel.

## ⚠️ Sécurité

> Ajouter une partition au canevas **démarre ses terminaux et exécute des commandes sur votre machine** (`claude`, `codex`, `gemini`).

- **Lisez les commandes** sur l'écran de revue avant d'importer, et n'acceptez de partitions que de sources fiables.
- Les partitions **Red Team** et tout engagement offensif opèrent **strictement dans un périmètre autorisé**, jamais en production et jamais avec des données de personnes réelles.
- Détails dans [docs/05](docs/05-modelos-e-seguranca.md).

## 🔗 Références

- [Documentation officielle de Maestri](https://www.themaestri.app/pt-br/docs) — canevas, terminaux, notes, portails, étages, routines, Wire.
- [agency-agents](https://github.com/msitarzewski/agency-agents) — catalogue de 230+ agents en 18 divisions (inspiration des domaines).
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) — guide pt-BR de référence (inspiration de la mise en page).

---

<p align="center">
  <sub>Conçu pour diriger des agents. Fable dirige, Opus exécute, Codex et Gemini contestent. 🎻</sub>
</p>
