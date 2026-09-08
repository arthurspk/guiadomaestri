<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Guida Maestri" width="160" height="160">
  </a>
</p>

<h1 align="center">Guida Maestri</h1>

<p align="center">
  <b>La guida per dirigere team di agenti IA in <a href="https://www.themaestri.app">Maestri</a> — con focus sulla tecnologia e un generatore di 257 partiture pronte, organizzate per area.</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/partiture-257-5856D6?style=for-the-badge" alt="257 partiture"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/aree-12-007AFF?style=for-the-badge" alt="12 aree"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/formato-.maestripartitura%20v1-34C759?style=for-the-badge" alt="Formato"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/validazione-0%20scarti-FF9500?style=for-the-badge" alt="Validato"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/lingua-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

> **Nota:** questa è una traduzione. La guida di base e i documenti dettagliati in `docs/` sono in portoghese brasiliano.

## 🎯 Di cosa si tratta

> **Maestri** è un'app macOS in cui **dirigi un team di agenti di codice** — Claude Code, Codex, Gemini, OpenCode — su una **tela infinita**: i terminali sono agenti, le note markdown sono la fonte di verità condivisa, i portali sono browser incorporati per la verifica dal vivo, e il **maestro** delega e coordina. Questo repository è insieme una **guida** e un **generatore Python** che produce **257 partiture** (`.maestripartitura`) pronte da trascinare sulla tela e dirigere — ognuna è un team completo, con responsabilità, note, portali e connessioni integrati. Il focus è la **tecnologia**, più 11 aree di business (design, prodotto, marketing, vendite, dati, sicurezza, finanza, legale, supporto, project management, ricerca).

## 💡 Come è organizzata questa guida

> Due influenze, insieme. La **divisione per aree** (dipartimenti di un'agenzia IA) viene da [agency-agents](https://github.com/msitarzewski/agency-agents), un catalogo di 230+ agenti in 18 divisioni. Il **layout** — intestazione, presentazione, indice con ancore e sezioni — segue [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil). Dettagli di questo confronto in [docs/07](docs/07-areas-e-agentes.md).

## 🌍 Traduzione

> Se vuoi seguire questa guida in un'altra lingua, scegli qui sotto. Puoi anche contribuire con traduzioni o correzioni; la community ringrazia. I documenti dettagliati in `docs/` sono in portoghese.

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

## ⭐ Inizia qui

> Se vuoi solo i template: apri il catalogo, scegli un'area, trascinala in Maestri.

- [🎼 **Catalogo delle partiture per area**](partituras/CATALOGO.md) — l'indice principale delle 257 partiture, con link a ogni area e al suo pacchetto.
- [💻 **Catalogo Tecnologia**](partituras/tecnologia/CATALOGO.md) — le 212 partiture di ingegneria (il cuore della guida).
- [📦 **Importa tutto in una volta**](partituras/Guia-do-Maestri.maestripartituras) — un pacchetto con tutte le aree (pannello Partiture → ⋯ → Importa Partiture…).

## 📖 Documentazione

> Nove documenti più la guida agli agenti, in portoghese. Inizia dal 01 se Maestri è nuovo per te, o salta al 02 e al 06 se lo conosci già.

- **01 · Concetti** ([docs/01](docs/01-conceitos.md)) — tela, terminali, note, portali, connessioni, Modalità Maestro, Ombro, Batuta, Piani (Floors), Routine, Ambienti, Wire.
- **02 · Usare i template** ([docs/02](docs/02-como-usar-os-templates.md)) — importare, dirigere in pratica, scegliere e adattare una partitura.
- **03 · Scorciatoie e comandi** ([docs/03](docs/03-atalhos.md)) — scorciatoie da tastiera macOS e la CLI `maestri`.
- **04 · Il formato `.maestripartitura`** ([docs/04](docs/04-formato-maestripartitura.md)) — la specifica JSON, calibrata sui file ufficiali.
- **05 · Modelli e sicurezza** ([docs/05](docs/05-modelos-e-seguranca.md)) — Fable/Opus/Codex, skip-permissions, checklist a 30 livelli, red team autorizzato.
- **06 · Maestri nel quotidiano** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) — piani, portali, note, routine e Ombro in situazioni reali.
- **07 · Aree e agenti disponibili** ([docs/07](docs/07-areas-e-agentes.md)) — la divisione per aree, la mappa verso agency-agents, la validazione del layout.
- **08 · Piani + Partiture (ricette)** ([docs/08](docs/08-andares-e-partituras.md)) — come usare i piani insieme alle partiture, con ricette per situazione e hook.
- **09 · Portali: web, mobile, emulatori** ([docs/09](docs/09-portais-mobile-web-emulador.md)) — come aggiungere portali browser, web-mobile e dispositivo (simulatore iOS / emulatore Android) alle partiture.
- **🎭 · Agenti** ([agentes/README.md](agentes/README.md)) — archetipi di responsabilità e il cast di specialisti.
- **📨 · Prompt: validare il Discord di Maestri** ([prompts](prompts/validar-discord-maestri.md)) — un prompt pronto per un Claude con accesso a Discord per validare e raccogliere informazioni.

## 🗂️ Partiture per area

> 257 partiture in 12 aree. Ogni area ha un catalogo dettagliato e un pacchetto `.maestripartituras` da importare in una volta.

- [💻 **Tecnologia**](partituras/tecnologia/CATALOGO.md) — 212 partiture · ingegneria end-to-end: feature, bug, release, infra, dati, IA, migrazione, mobile.
- [🎨 **Design & UX**](partituras/design/CATALOGO.md) — 5 partiture · design system, ricerca UX, landing page, audit UI.
- [📦 **Prodotto**](partituras/produto/CATALOGO.md) — 5 partiture · discovery, roadmap, PRD, sintesi di feedback, concorrenza.
- [📢 **Marketing & Contenuti**](partituras/marketing/CATALOGO.md) — 5 partiture · campagne, SEO, social, email di ciclo di vita, blog tecnico.
- [💼 **Vendite**](partituras/vendas/CATALOGO.md) — 4 partiture · outbound, proposte/RFP, sales enablement, discovery.
- [📊 **Dati & Analytics**](partituras/dados/CATALOGO.md) — 4 partiture · dashboard BI, analisi esplorativa, metriche, A/B.
- [🔒 **Sicurezza & Compliance**](partituras/seguranca/CATALOGO.md) — 4 partiture · GDPR/LGPD, SOC 2, threat modeling, risposta agli incidenti.
- [💵 **Finanza**](partituras/financeiro/CATALOGO.md) — 4 partiture · chiusura, modellazione, FP&A, due diligence.
- [⚖️ **Legale**](partituras/juridico/CATALOGO.md) — 3 partiture · revisione contratti, intake, analisi del rischio.
- [🛟 **Supporto & Success**](partituras/suporte/CATALOGO.md) — 4 partiture · knowledge base, triage, onboarding, churn.
- [🗂️ **Project Management**](partituras/gestao/CATALOGO.md) — 4 partiture · sprint, coordinamento multi-team, verbale, retrospettiva.
- [🔬 **Ricerca & Contenuti Tecnici**](partituras/pesquisa/CATALOGO.md) — 3 partiture · stato dell'arte, sintesi, analisi di mercato.

## 🧩 Le 23 famiglie tecnologiche

> L'area Tecnologia è parametrizzata da cataloghi (stack, domini, provider). Famiglie × varianti supera i 200 template.

- **🚢 Ship Feature** (24) — maestro + architetto + 2 builder + warden, per stack.
- **🐞 Debugging** (24) — riproduttore → causa radice → correzione → verificatore, per stack.
- **✅ Gate di Release** (24) — conductor + 4 revisori avversariali, per stack.
- **🏗️ Scaffold** (24) — scheletro + setup + vertical slice + warden, per stack.
- **🔧 Migrazione** (12) — migrazione + verificatore di parità, incrementale e reversibile.
- **💸 Pipeline Completa** (10) — 30 livelli su 4 superfici, per prodotto (regola di taglio finanziaria).
- **☁️ Cloud & Infra** (9) — rete/compute + dati/storage + warden, per provider.
- **🗄️ Database** (9) — schema/migrazione + indici basati su evidenze, per database.
- **🔎 Validazione BFF** (8) — SPA × BFF: parità, CORS, cookie, per dominio.
- **🧠 Funzione IA** (7) — IA + eval & guardrail.
- **📱 Ship Mobile** (7) — app + QA/a11y su un portale dispositivo.
- **🧑‍💻 Solo** (7) — un singolo specialista.
- **📖 Documentazione** (5), **⚔️ Duello di Agenti** (5), **🚨 War Room** (5).
- **🔗 API Contract** (4), **♿ Accessibilità** (4), **🔁 CI/CD** (4), **🔀 Data Pipeline** (4), **📦 IaC** (4), **☸️ Kubernetes** (4), **⚡ Performance** (4), **🔴 Red Team** (4, solo ambito autorizzato).

## ⚡ Maestri nel quotidiano

> Le partiture sono l'inizio; il valore è nel flusso. La [guida al quotidiano](docs/06-maestri-no-dia-a-dia.md) mostra come usare le funzionalità di Maestri in situazioni reali, e i doc [08](docs/08-andares-e-partituras.md) e [09](docs/09-portais-mobile-web-emulador.md) approfondiscono piani e portali.

- **🏢 Piani (Floors)** — copie isolate del repo con un proprio branch: lavora su più fronti in parallelo senza `git stash`, con hook Setup/Run/Teardown. Combina con una partitura per far nascere un intero team isolato su un branch.
- **🌐 Portali** — verifica dal vivo su browser, web-mobile e **dispositivo** (simulatore iOS / emulatore Android / dispositivo fisico): dimostrare un bug, accettare una feature, controllare una landing, testare l'app nativa.
- **📝 Note** — la fonte di verità che sopravvive alla sessione; sposta nel repo ciò che deve stare in git, concatena in mappa mentale, lascia che Ombro riassuma.
- **⏰ Routine** — il lavoro ripetitivo da solo: guardiano della CI, sentinella del deploy, clipping dei concorrenti, chiusura giornaliera, triage dei ticket.
- **👤 Ombro** — il copilota di attenzione locale: «cosa hanno fatto gli agenti mentre non c'ero?».

## 🤖 Politica dei modelli

> Fable dirige, Opus esegue, Codex/Gemini contestano.

- **🎼 Orchestrazione** (maestro, conductor, IC, giudice, lead) — `claude --dangerously-skip-permissions --model fable`.
- **🔨 Esecuzione** (architetto, builder, specialisti) — `--model opus`.
- **🛡️ Revisione avversariale** (release, warden, duello) — `codex` / `gemini`, di proposito: un modello diverso coglie ciò che l'altro ha lasciato passare.
- Dettagli e salvaguardie in [docs/05](docs/05-modelos-e-seguranca.md).

## 🛠️ Rigenerare e validare

> Il generatore non dipende da nulla oltre alla libreria standard di Python 3. UUID deterministici: rigenerare produce file identici byte per byte.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 tests/validate_partituras.py        # → "Zero divergências" vs la partitura ufficiale
```

- `scripts/maestri_build.py` — la classe `Partitura`, serializzazione, ropePoints, layout.
- `scripts/roles_lib.py` — prompt di responsabilità (pt-BR) + template di nota.
- `scripts/generate_partituras.py` — famiglie parametrizzate da cataloghi, raggruppate per area.
- `tests/validate_partituras.py` — confronta le chiavi top/payload/nodo/ruolo con il file ufficiale.

## ⚠️ Sicurezza

> Aggiungere una partitura alla tela **avvia i suoi terminali ed esegue comandi sulla tua macchina** (`claude`, `codex`, `gemini`).

- **Leggi i comandi** nella schermata di revisione prima di importare, e accetta partiture solo da fonti affidabili.
- Le partiture **Red Team** e qualsiasi ingaggio offensivo operano **esclusivamente in ambito autorizzato**, mai in produzione e mai con dati di persone reali.
- Dettagli in [docs/05](docs/05-modelos-e-seguranca.md).

## 🔗 Riferimenti

- [Documentazione ufficiale di Maestri](https://www.themaestri.app/pt-br/docs) — tela, terminali, note, portali, piani, routine, Wire.
- [agency-agents](https://github.com/msitarzewski/agency-agents) — catalogo di 230+ agenti in 18 divisioni (ispirazione delle aree).
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) — guida pt-BR di riferimento (ispirazione del layout).

---

<p align="center">
  <sub>Fatto per dirigere agenti. Fable dirige, Opus esegue, Codex e Gemini contestano. 🎻</sub>
</p>
