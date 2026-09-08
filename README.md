<div align="center">

# 🎼 Guia do Maestri

**O guia em português (com ênfase em tecnologia) para o [Maestri](https://www.themaestri.app/pt-br) —
o canvas infinito para reger times de agentes de IA no macOS.**

[![Templates](https://img.shields.io/badge/partituras-212-5856D6)](partituras/tecnologia/CATALOGO.md)
[![Famílias](https://img.shields.io/badge/fam%C3%ADlias-23-007AFF)](partituras/tecnologia/CATALOGO.md)
[![Formato](https://img.shields.io/badge/formato-.maestripartitura%20v1-34C759)](docs/04-formato-maestripartitura.md)
[![Validado](https://img.shields.io/badge/valida%C3%A7%C3%A3o-0%20diverg%C3%AAncias-FF9500)](tests/validate_partituras.py)
[![Modelos](https://img.shields.io/badge/fable%20rege%20·%20opus%20executa%20·%20codex%2Fgemini%20contestam-AF52DE)](docs/05-modelos-e-seguranca.md)
[![pt-BR](https://img.shields.io/badge/idioma-pt--BR-FFCC00)](#)

</div>

---

O **Maestri** é um app onde você rege um time de agentes de código — Claude Code, Codex,
Gemini — num **canvas infinito**: terminais são agentes, notas markdown são a fonte de
verdade compartilhada, portais são navegadores embutidos para verificação viva, e o
**maestro** delega e coordena.

Este repositório é ao mesmo tempo um **guia** e um **gerador**. O coração é um gerador em
Python (só stdlib) que produz **🎯 212 partituras de tecnologia** (`.maestripartitura`)
prontas para arrastar para o canvas e reger — cada uma é um time completo, com
responsabilidades embutidas, notas, portais e conexões.

## ⭐ Comece por aqui

> ### 🎯 [**Catálogo de 212 partituras de tecnologia →**](partituras/tecnologia/CATALOGO.md)
> Ship Feature, Depuração, Portão de Release, Scaffold, Validação BFF, Pipeline Completo
> (30 camadas), Cloud & Infra, IaC, Kubernetes, CI/CD, Database, Data Pipeline, AI Feature,
> Migração, Ship Mobile, Acessibilidade, API Contract, Performance, Documentação, Red Team,
> Solo, Duelo de Agentes e War Room.
>
> **Importar tudo:** painel de Partituras → ⋯ → **Importar Partituras…** →
> [`Tecnologia.maestripartituras`](partituras/tecnologia/Tecnologia.maestripartituras).

## 📚 Documentação

| # | Documento | O que cobre |
|---|---|---|
| 01 | [**Conceitos**](docs/01-conceitos.md) | Canvas, terminais, notas, portais, conexões, Modo Maestro, Ombro, Batuta, Andares, Rotinas, Ambientes, Wire |
| 02 | [**Como usar os templates**](docs/02-como-usar-os-templates.md) | Importar, reger na prática, escolher e adaptar uma partitura |
| 03 | [**Atalhos e comandos**](docs/03-atalhos.md) | Atalhos de teclado do macOS + a CLI `maestri` |
| 04 | [**Formato `.maestripartitura`**](docs/04-formato-maestripartitura.md) | A especificação JSON completa, calibrada contra os arquivos oficiais |
| 05 | [**Modelos e segurança**](docs/05-modelos-e-seguranca.md) | Fable/Opus/Codex, skip-permissions, stack-checklist de 30 camadas, red team autorizado |
| 🎭 | [**Agentes**](agentes/README.md) | Arquétipos de responsabilidade e o elenco de especialistas |

## 🧩 As 23 famílias

Cada família é parametrizada por um catálogo (stacks, domínios, provedores…). O produto
famílias × variantes passa de 200 templates.

| Família | Nº | Padrão |
|---|:--:|---|
| 🚢 Ship Feature | 24 | maestro + arquiteto + 2 builders + warden, por stack |
| 🐞 Depuração | 24 | reprodutor → causa raiz → correção → verificador, por stack |
| ✅ Portão de Release | 24 | conductor + 4 revisores adversariais, por stack |
| 🏗️ Scaffold | 24 | esqueleto + setup + vertical slice + warden, por stack |
| 🔎 Validação BFF | 8 | SPA × BFF: paridade, CORS, cookie, por domínio |
| 💸 Pipeline Completo | 10 | 30 camadas em 4 superfícies, por produto (regra de corte financeira) |
| ☁️ Cloud & Infra | 9 | rede/compute + dados/storage + warden, por provedor |
| 📦 IaC | 4 | módulos + policy-as-code, por ferramenta |
| 🗄️ Database | 9 | schema/migração + índices, por banco |
| 🔀 Data Pipeline | 4 | ingestão + qualidade de dados |
| 🧠 AI Feature | 7 | IA + evals & guardrails |
| 🔧 Migração | 12 | migração + verificador de paridade |
| 📱 Ship Mobile | 7 | app + QA/a11y no portal de dispositivo |
| ♿ Acessibilidade | 4 | correção + verificação com AT real (WCAG 2.2 AA) |
| 🔗 API Contract | 4 | design-first + contract tests |
| ⚡ Performance | 4 | otimização + benchmark, guiado por medição |
| 🔁 CI/CD | 4 | pipeline + release/rollback |
| ☸️ Kubernetes | 4 | plataforma + segurança de cluster |
| 📖 Documentação | 5 | escritor + verificador contra o código |
| 🔴 Red Team | 4 | **só escopo autorizado** — lead + operadores + relatório |
| 🧑‍💻 Solo | 7 | um especialista sozinho |
| ⚔️ Duelo de Agentes | 5 | claude × codex × gemini + juiz |
| 🚨 War Room | 5 | comandante + investigação + mitigação + comunicação |

## 🤖 Política de modelos

**Fable rege · Opus executa · Codex/Gemini contestam.** Os maestros sobem em `--model
fable`, os especialistas em `--model opus`, e a revisão adversarial usa `codex`/`gemini` de
propósito — um agente diferente pega o que o outro deixou passar. Detalhes e as
salvaguardas de red team em [docs/05](docs/05-modelos-e-seguranca.md).

## 🛠️ Regenerar e validar

O gerador não depende de nada além da stdlib do Python 3.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 212 templates" + pacote + CATALOGO.md
python3 tests/validate_partituras.py        # → "Zero divergências" vs a partitura oficial
```

UUIDs determinísticos: regerar produz **os mesmos arquivos byte a byte**.

```
scripts/
├── maestri_build.py          # classe Partitura, serialização, ropePoints, layout
├── roles_lib.py              # prompts de responsabilidade (pt-BR) + templates de nota
└── generate_partituras.py    # 23 famílias parametrizadas por catálogos
tests/
└── validate_partituras.py    # compara chaves de topo/payload/nós/roles com o oficial
partituras/tecnologia/
├── CATALOGO.md               # índice por família (gerado)
├── Tecnologia.maestripartituras  # pacote coletivo (gerado)
└── *.maestripartitura        # 212 templates (gerados)
referencia/
└── partituras-oficiais/      # exemplos reais do formato, usados para calibrar e validar
```

## ⚠️ Segurança

Adicionar uma partitura ao canvas **inicia os terminais dela e executa comandos na sua
máquina** (`claude`, `codex`, `gemini`). **Leia os comandos** na tela de revisão antes de
importar e só aceite partituras de fontes confiáveis. As partituras de **Red Team** e
qualquer engajamento ofensivo operam **exclusivamente em escopo autorizado**, nunca em
produção e nunca com dados de pessoas reais. Detalhes em
[docs/05 · Modelos e segurança](docs/05-modelos-e-seguranca.md).

## 🔗 Referências

- Documentação oficial do Maestri: <https://www.themaestri.app/pt-br/docs>
- Formato de arquivo (esta calibração): [docs/04](docs/04-formato-maestripartitura.md)

---

<div align="center">
<sub>Feito para reger agentes. Fable rege, Opus executa, Codex e Gemini contestam. 🎻</sub>
</div>
