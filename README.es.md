<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Guía de Maestri" width="160" height="160">
  </a>
</p>

<h1 align="center">Guía de Maestri</h1>

<p align="center">
  <b>La guía para dirigir equipos de agentes de IA en <a href="https://www.themaestri.app">Maestri</a> — con énfasis en tecnología y un generador de 257 partituras listas, organizadas por área.</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/partituras-257-5856D6?style=for-the-badge" alt="257 partituras"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/%C3%A1reas-12-007AFF?style=for-the-badge" alt="12 áreas"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/formato-.maestripartitura%20v1-34C759?style=for-the-badge" alt="Formato"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/validaci%C3%B3n-0%20divergencias-FF9500?style=for-the-badge" alt="Validado"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/idioma-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

> **Nota:** Esta es una traducción. La guía base y los documentos detallados en `docs/` están en portugués de Brasil.

## 🎯 Qué es esto

> **Maestri** es una app de macOS donde **diriges un equipo de agentes de código** — Claude Code, Codex, Gemini, OpenCode — en un **lienzo infinito**: los terminales son agentes, las notas markdown son la fuente de verdad compartida, los portales son navegadores embebidos para verificación en vivo, y el **maestro** delega y coordina. Este repositorio es a la vez una **guía** y un **generador en Python** que produce **257 partituras** (`.maestripartitura`) listas para arrastrar al lienzo y dirigir — cada una es un equipo completo, con responsabilidades embebidas, notas, portales y conexiones. El énfasis es **tecnología**, más 11 áreas de negocio (diseño, producto, marketing, ventas, datos, seguridad, finanzas, legal, soporte, gestión, investigación).

## 💡 Cómo está organizada esta guía

> Dos influencias, juntas. La **división por áreas** (departamentos de una agencia de IA) viene de [agency-agents](https://github.com/msitarzewski/agency-agents), un catálogo de 230+ agentes en 18 divisiones. El **diseño** — cabecera, propuesta, índice con anclas y secciones — sigue a [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil). Detalles de esa comparación en [docs/07](docs/07-areas-e-agentes.md).

## 🌍 Traducción

> Si quieres seguir esta guía en otro idioma, elige abajo. También puedes colaborar traduciendo a más idiomas o corrigiendo errores; la comunidad lo agradece. Los documentos detallados en `docs/` están en portugués.

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

## ⭐ Empieza aquí

> Si solo quieres las plantillas: abre el catálogo, elige un área, arrástrala a Maestri.

- [🎼 **Catálogo de partituras por área**](partituras/CATALOGO.md) — el índice maestro de las 257 partituras, con enlace a cada área y su paquete.
- [💻 **Catálogo de Tecnología**](partituras/tecnologia/CATALOGO.md) — las 212 partituras de ingeniería (el corazón de la guía).
- [📦 **Importar todo de una vez**](partituras/Guia-do-Maestri.maestripartituras) — un paquete con todas las áreas (panel de Partituras → ⋯ → Importar Partituras…).

## 📖 Documentación

> Nueve documentos más la guía de agentes, en portugués. Empieza por el 01 si Maestri es nuevo para ti, o salta al 02 y al 06 si ya lo conoces.

- **01 · Conceptos** ([docs/01](docs/01-conceitos.md)) — lienzo, terminales, notas, portales, conexiones, Modo Maestro, Ombro, Batuta, Andares (floors), Rutinas, Entornos, Wire.
- **02 · Usar las plantillas** ([docs/02](docs/02-como-usar-os-templates.md)) — importar, dirigir en la práctica, elegir y adaptar una partitura.
- **03 · Atajos y comandos** ([docs/03](docs/03-atalhos.md)) — atajos de teclado de macOS y la CLI `maestri`.
- **04 · El formato `.maestripartitura`** ([docs/04](docs/04-formato-maestripartitura.md)) — la especificación JSON, calibrada contra los archivos oficiales.
- **05 · Modelos y seguridad** ([docs/05](docs/05-modelos-e-seguranca.md)) — Fable/Opus/Codex, skip-permissions, checklist de 30 capas, red team autorizado.
- **06 · Maestri en el día a día** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) — andares, portales, notas, rutinas y Ombro en situaciones reales.
- **07 · Áreas y agentes disponibles** ([docs/07](docs/07-areas-e-agentes.md)) — la división por áreas, el mapa a agency-agents y la validación del diseño.
- **08 · Andares + Partituras (recetas)** ([docs/08](docs/08-andares-e-partituras.md)) — cómo usar los andares junto con las partituras, con recetas por situación y hooks.
- **09 · Portales: web, móvil, emuladores** ([docs/09](docs/09-portais-mobile-web-emulador.md)) — cómo añadir portales de navegador, web-móvil y de dispositivo (simulador iOS / emulador Android) a las partituras.
- **10 · Importar y exportar en Maestri** ([docs/10](docs/10-importar-e-exportar.md)) — todo lo que puedes importar/exportar de forma nativa más las recetas curadas, y dónde vive cada cosa en el hub.
- **🎭 · Agentes** ([agentes/README.md](agentes/README.md)) — arquetipos de responsabilidad y el elenco de especialistas.
- **📨 · Prompts** ([prompts](prompts/README.md)) — una biblioteca de prompts listos (crear una partitura, validar el Discord de Maestri).

## 🗂️ Partituras por área

> 257 partituras en 12 áreas. Cada área tiene un catálogo detallado y un paquete `.maestripartituras` para importar de una vez.

- [💻 **Tecnología**](partituras/tecnologia/CATALOGO.md) — 212 partituras · ingeniería de extremo a extremo: features, bugs, release, infra, datos, IA, migración, móvil.
- [🎨 **Diseño & UX**](partituras/design/CATALOGO.md) — 5 partituras · design systems, investigación de UX, landing pages, auditoría de UI.
- [📦 **Producto**](partituras/produto/CATALOGO.md) — 5 partituras · discovery, roadmap, PRD, síntesis de feedback, competencia.
- [📢 **Marketing y Contenido**](partituras/marketing/CATALOGO.md) — 5 partituras · campañas, SEO, social, email de ciclo de vida, blog técnico.
- [💼 **Ventas**](partituras/vendas/CATALOGO.md) — 4 partituras · outbound, propuestas/RFP, sales enablement, discovery.
- [📊 **Datos & Analytics**](partituras/dados/CATALOGO.md) — 4 partituras · dashboards de BI, análisis exploratorio, métricas, A/B.
- [🔒 **Seguridad y Compliance**](partituras/seguranca/CATALOGO.md) — 4 partituras · RGPD/LGPD, SOC 2, threat modeling, respuesta a incidentes.
- [💵 **Finanzas**](partituras/financeiro/CATALOGO.md) — 4 partituras · cierre, modelado, FP&A, due diligence.
- [⚖️ **Legal**](partituras/juridico/CATALOGO.md) — 3 partituras · revisión de contratos, intake, análisis de riesgo.
- [🛟 **Soporte y Éxito**](partituras/suporte/CATALOGO.md) — 4 partituras · base de conocimiento, triaje, onboarding, churn.
- [🗂️ **Gestión de Proyectos**](partituras/gestao/CATALOGO.md) — 4 partituras · sprint, coordinación multiequipo, acta, retrospectiva.
- [🔬 **Investigación y Contenido Técnico**](partituras/pesquisa/CATALOGO.md) — 3 partituras · estado del arte, síntesis, análisis de mercado.

## 📦 Más recursos para importar/exportar

> Un hub de Maestri es más que partituras. Estos usan los otros formatos portátiles de la app (roles, temas, instrucciones, notas) o reúnen recetas listas. Panorama completo en [docs/10 · Importar y exportar](docs/10-importar-e-exportar.md).

- [🎭 **Responsabilidades (`role.json`)**](roles/CATALOGO.md) — 30 roles reutilizables en el formato nativo; suéltalos en la carpeta `.maestri` del proyecto y usa "Descubrir Responsabilidades".
- [🎨 **Temas de terminal (Ghostty)**](temas/README.md) — 4 temas para instalar en `~/.maestri/terminal/themes/`.
- [🧭 **Instrucciones `CLAUDE.md` / `AGENTS.md`**](instrucoes/README.md) — plantillas por stack que se entregan a los agentes al iniciar en un workspace.
- [📝 **Plantillas de nota**](notas/README.md) — contrato, workboard, playbook, stack-checklist, case-file y más, para arrastrar al lienzo.
- [🧑‍🍳 **Recetas curadas**](receitas/README.md) — hooks de andar, rutinas programadas, un cliente Maestri Wire y recetas de entornos.
- [📨 **Prompts**](prompts/README.md) — prompts listos para el Compositor de Prompts.
- [🗂️ **Espacios de trabajo (`.maestri`)**](workspaces/README.md) — cómo importar/compartir un workspace.

## 🧩 Las 23 familias de tecnología

> El área de Tecnología está parametrizada por catálogos (stacks, dominios, proveedores). Familias × variantes supera las 200 plantillas.

- **🚢 Ship Feature** (24) — maestro + arquitecto + 2 builders + warden, por stack.
- **🐞 Depuración** (24) — reproductor → causa raíz → corrección → verificador, por stack.
- **✅ Puerta de Release** (24) — conductor + 4 revisores adversariales, por stack.
- **🏗️ Scaffold** (24) — esqueleto + setup + vertical slice + warden, por stack.
- **🔧 Migración** (12) — migración + verificador de paridad, incremental y reversible.
- **💸 Pipeline Completo** (10) — 30 capas en 4 superficies, por producto (regla de corte financiera).
- **☁️ Cloud & Infra** (9) — red/cómputo + datos/almacenamiento + warden, por proveedor.
- **🗄️ Base de Datos** (9) — schema/migración + índices con evidencia, por base de datos.
- **🔎 Validación BFF** (8) — SPA × BFF: paridad, CORS, cookie, por dominio.
- **🧠 AI Feature** (7) — IA + evals & guardrails.
- **📱 Ship Mobile** (7) — app + QA/a11y en un portal de dispositivo.
- **🧑‍💻 Solo** (7) — un único especialista.
- **📖 Documentación** (5), **⚔️ Duelo de Agentes** (5), **🚨 War Room** (5).
- **🔗 API Contract** (4), **♿ Accesibilidad** (4), **🔁 CI/CD** (4), **🔀 Data Pipeline** (4), **📦 IaC** (4), **☸️ Kubernetes** (4), **⚡ Performance** (4), **🔴 Red Team** (4, solo ámbito autorizado).

## ⚡ Maestri en el día a día

> Las partituras son el comienzo; el valor está en el flujo. La [guía del día a día](docs/06-maestri-no-dia-a-dia.md) muestra cómo usar las funciones de Maestri en situaciones reales, y los docs [08](docs/08-andares-e-partituras.md) y [09](docs/09-portais-mobile-web-emulador.md) profundizan en andares y portales.

- **🏢 Andares (Floors)** — copias aisladas del repo con su propia rama: trabaja varios frentes en paralelo sin `git stash`, con hooks de Setup/Run/Teardown. Combínalos con una partitura para levantar un equipo entero aislado en una rama.
- **🌐 Portales** — verificación en vivo en navegador, web-móvil y **dispositivo** (simulador iOS / emulador Android / dispositivo físico): probar un bug, aceptar una feature, revisar una landing, probar la app nativa.
- **📝 Notas** — la fuente de verdad que sobrevive a la sesión; mueve al repo lo que debe ir en git, encadena en mapa mental, deja que Ombro resuma.
- **⏰ Rutinas** — el trabajo repetitivo por sí solo: guardián de CI, vigía de deploy, clipping de competencia, cierre diario, triaje de tickets.
- **👤 Ombro** — el copiloto de atención local: "¿qué hicieron los agentes mientras no estaba?".

## 🤖 Política de modelos

> Fable dirige, Opus ejecuta, Codex/Gemini cuestionan.

- **🎼 Orquestación** (maestro, conductor, IC, juez, lead) — `claude --dangerously-skip-permissions --model fable`.
- **🔨 Ejecución** (arquitecto, builders, especialistas) — `--model opus`.
- **🛡️ Revisión adversarial** (release, wardens, duelo) — `codex` / `gemini`, a propósito: un modelo distinto pilla lo que el otro dejó pasar.
- Detalles y salvaguardas en [docs/05](docs/05-modelos-e-seguranca.md).

## 🛠️ Regenerar y validar

> El generador no necesita nada más que la biblioteca estándar de Python 3. UUIDs deterministas: regenerar produce archivos idénticos byte a byte.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → "Zero divergências" vs la partitura oficial
python3 tests/validate_hub.py               # → valida los role.json y la estructura del hub
```

- `scripts/maestri_build.py` — la clase `Partitura`, serialización, ropePoints, layout.
- `scripts/roles_lib.py` — prompts de responsabilidad (pt-BR) + plantillas de nota.
- `scripts/generate_partituras.py` — familias parametrizadas por catálogos, agrupadas por área.
- `tests/validate_partituras.py` — compara claves de top/payload/nodos/roles con el archivo oficial.

## ⚠️ Seguridad

> Añadir una partitura al lienzo **inicia sus terminales y ejecuta comandos en tu máquina** (`claude`, `codex`, `gemini`).

- **Lee los comandos** en la pantalla de revisión antes de importar, y solo acepta partituras de fuentes confiables.
- Las partituras de **Red Team** y cualquier engagement ofensivo operan **exclusivamente en ámbito autorizado**, nunca en producción y nunca con datos de personas reales.
- Detalles en [docs/05](docs/05-modelos-e-seguranca.md).

## 🔗 Referencias

- [Documentación oficial de Maestri](https://www.themaestri.app/pt-br/docs) — lienzo, terminales, notas, portales, andares, rutinas, Wire.
- [agency-agents](https://github.com/msitarzewski/agency-agents) — catálogo de 230+ agentes en 18 divisiones (inspiración de las áreas).
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) — guía pt-BR de referencia (inspiración del diseño).

---

<p align="center">
  <sub>Hecho para dirigir agentes. Fable dirige, Opus ejecuta, Codex y Gemini cuestionan. 🎻</sub>
</p>
