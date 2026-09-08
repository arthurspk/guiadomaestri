#!/usr/bin/env python3
"""
generate_hub.py — Gera os recursos "importáveis/exportáveis" do hub (além das partituras):

  roles/       Biblioteca de responsabilidades em `role.json` (formato nativo do Maestri,
               descoberto pelo botão "Descobrir Responsabilidades"). Um arquivo por role,
               agrupado por categoria, + um CATALOGO.md.
  notas/       Templates de nota (.md) avulsos — arraste para o canvas como nota, ou
               use como base de uma nota gerenciada. + README.
  instrucoes/  Templates de CLAUDE.md / AGENTS.md por stack — instruções que o agente
               recebe ao iniciar num workspace. + README.

Determinístico e sem dependências além da stdlib.

⚠️ Sobre o `role.json`: as partituras oficiais confirmam o formato do objeto de role
(color, icon, id, name, prompt, schemaVersion). O arquivo-satélite `role.json` que o
Maestri descobre no diretório de trabalho segue esse mesmo formato conceitual (nome, cor
do badge, prompt). Se o schema exato divergir na sua versão do app, exporte uma
responsabilidade real e compare — veja docs/10 e prompts/validar-discord-maestri.md.
"""

import json
import os
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from maestri_build import COLORS, det_uuid  # noqa: E402
import roles_lib as R  # noqa: E402
import generate_partituras as G  # noqa: E402


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    out = []
    for ch in s.lower():
        out.append(ch if ch.isalnum() else "-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


# ===========================================================================
# 1) Biblioteca de responsabilidades (role.json)
# ===========================================================================
# Conjunto CURADO de responsabilidades reutilizáveis (não uma cópia de cada variante
# de partitura). (categoria, nome, cor, prompt).

def _roles_catalog():
    C = COLORS
    R_ = R
    cat = []

    def add(category, name, color, prompt, icon="person.text.rectangle"):
        cat.append((category, name, color, prompt, icon))

    # -- Orquestração --------------------------------------------------------
    add("Orquestração", "Maestro", C["pink"],
        R_.maestro("entregar trabalho pronto e verificado coordenando um time de agentes"))
    add("Orquestração", "Orquestrador (ReAct)", C["indigo"],
        R_.orchestrator_generic("coordenar um time de especialistas de propósito geral"))
    add("Orquestração", "Release Conductor", C["green"], R_.release_conductor())
    add("Orquestração", "Debug Maestro", C["purple"], R_.debug_maestro())
    add("Orquestração", "Incident Commander", C["red"], R_.incident_commander("um incidente de produção"))
    add("Orquestração", "Juiz de Duelo", C["yellow"], R_.judge("o mesmo problema atacado por vários modelos"))
    add("Orquestração", "Maestro de Área", C["pink"],
        R_.area_orchestrator("uma área de negócio", "um entregável pronto e verificado"))

    # -- Contrato / estratégia ----------------------------------------------
    add("Contrato & Estratégia", "Arquiteto de Contrato", C["yellow"],
        R_.architect("transformar um objetivo numa especificação que o time constrói em paralelo"))
    add("Contrato & Estratégia", "Estrategista de Área", C["indigo"],
        R_.area_strategist("uma área de negócio", "escrever o briefing que o time executa sem drift"))

    # -- Execução ------------------------------------------------------------
    add("Execução", "Implementador de Fatia", C["purple"],
        R_.implementer("a stack do projeto (front + back)"))
    add("Execução", "Especialista (genérico)", C["blue"],
        R_.specialist("Especialista", "Você executa uma fatia técnica bem definida, presa ao contrato."))
    add("Execução", "Especialista Solo", C["teal"],
        R_.solo_specialist("Especialista Solo", "Você planeja, executa e verifica sozinho, dono do seu runtime."))
    add("Execução", "Engenheiro de Plataforma", C["orange"],
        R_.platform_engineer("Você cuida de infra, deploy, secrets, filas e observabilidade."))
    add("Execução", "Especialista de Área", C["blue"],
        R_.area_specialist("uma área de negócio", "Especialista", "Você produz uma peça presa ao briefing."))

    # -- Revisão (achados, não correções) -----------------------------------
    add("Revisão", "Quality Warden", C["orange"], R_.warden("a feature em revisão"))
    add("Revisão", "Code Quality Reviewer", C["blue"], R_.code_quality_reviewer())
    add("Revisão", "Security Auditor", C["pink"], R_.security_reviewer())
    add("Revisão", "Correctness Verifier", C["yellow"], R_.correctness_verifier())
    add("Revisão", "UX & A11y Reviewer", C["purple"], R_.ux_a11y_reviewer())
    add("Revisão", "Revisor de Área", C["orange"],
        R_.area_reviewer("uma área de negócio", "consistência e exatidão"))

    # -- Depuração -----------------------------------------------------------
    add("Depuração", "Reprodutor de Bug", C["blue"], R_.bug_reproducer())
    add("Depuração", "Analista de Causa Raiz", C["orange"], R_.root_cause_analyst())
    add("Depuração", "Engenheiro de Correção", C["green"], R_.fix_engineer())
    add("Depuração", "Verificador de Correção", C["red"], R_.fix_verifier())

    # -- Duelo & Red Team ----------------------------------------------------
    add("Duelo & Adversarial", "Duelista", C["blue"],
        R_.duelist("Claude/Codex/Gemini", "o mesmo problema, resolvido de forma independente"))
    add("Duelo & Adversarial", "Red Team Lead", C["red"],
        R_.redteam_lead("um engajamento ofensivo AUTORIZADO"))
    add("Duelo & Adversarial", "Red Team Operator", C["orange"],
        R_.redteam_operator("uma superfície no escopo autorizado", "ferramental de segurança apropriado"))

    # -- War room ------------------------------------------------------------
    add("Incidente", "Investigador de Incidente", C["orange"],
        R_.specialist("Investigador de Incidente",
                      "Você acha o que quebrou com evidência: logs, métricas, mudanças recentes."))
    add("Incidente", "Engenheiro de Mitigação", C["blue"],
        R_.specialist("Engenheiro de Mitigação",
                      "Você para o sangramento agora: rollback, feature-flag, isolamento."))
    add("Incidente", "Líder de Comunicação", C["purple"],
        R_.specialist("Líder de Comunicação",
                      "Você mantém quem precisa saber informado, claro e honesto."))
    return cat


def gen_roles():
    base = os.path.join(ROOT, "roles")
    os.makedirs(base, exist_ok=True)
    cat = _roles_catalog()
    from collections import defaultdict
    by_cat = defaultdict(list)
    for category, name, color, prompt, icon in cat:
        cslug = slugify(category)
        d = os.path.join(base, cslug)
        os.makedirs(d, exist_ok=True)
        role = {
            "schemaVersion": 1,
            "id": det_uuid(f"hubrole:{category}:{name}"),
            "name": name,
            "prompt": prompt.strip(),
            "color": color,
            "icon": icon,
        }
        slug = slugify(name)
        with open(os.path.join(d, slug + ".role.json"), "w", encoding="utf-8") as f:
            json.dump(role, f, ensure_ascii=False, indent=2)
        by_cat[category].append((name, cslug, slug))
    # CATALOGO
    lines = ["# 🎭 Biblioteca de Responsabilidades (`role.json`)\n",
             f"> **{len(cat)} responsabilidades** reutilizáveis no formato nativo do Maestri. "
             "Cada `role.json` traz nome, cor do badge, ícone e o prompt em pt-BR.\n",
             "## Como importar no Maestri\n",
             "1. Copie o(s) arquivo(s) `*.role.json` para a pasta `.maestri` do diretório de "
             "trabalho do seu projeto (ao lado de `CLAUDE.md`/`AGENTS.md`).\n"
             "2. Ao abrir as configurações de um terminal, clique em **Descobrir "
             "Responsabilidades**: o Maestri varre o diretório e oferece os roles encontrados.\n"
             "3. Ou crie manualmente em **Configurações → Agentes** colando o prompt.\n",
             "> ⚠️ O schema segue o formato do objeto de role das partituras oficiais "
             "(`color`, `icon`, `id`, `name`, `prompt`, `schemaVersion`). Se a sua versão do "
             "Maestri divergir, exporte uma responsabilidade real e compare "
             "(veja [docs/10](../docs/10-importar-e-exportar.md)).\n",
             "## Índice por categoria\n"]
    for category in sorted(by_cat):
        lines.append(f"\n### {category}\n")
        for name, cslug, slug in sorted(by_cat[category]):
            lines.append(f"- **{name}** — [`{cslug}/{slug}.role.json`](./{cslug}/{slug}.role.json)")
    with open(os.path.join(base, "CATALOGO.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(cat)


# ===========================================================================
# 2) Notas avulsas (.md)
# ===========================================================================

def gen_notas():
    base = os.path.join(ROOT, "notas")
    os.makedirs(base, exist_ok=True)
    notes = {
        "stack-checklist.md": R.STACK_CHECKLIST_30,
        "release-playbook.md": R.RELEASE_PLAYBOOK,
        "release-findings.md": R.RELEASE_FINDINGS,
        "feature-spec.md": R.FEATURE_SPEC_EMPTY,
        "workboard.md": R.WORKBOARD_EMPTY,
        "case-file.md": R.CASE_FILE_EMPTY,
        "incident-timeline.md": R.INCIDENT_TIMELINE_EMPTY,
        "rules-of-engagement.md": R.RULES_OF_ENGAGEMENT_EMPTY,
        "engagement-plan.md": R.ENGAGEMENT_PLAN_EMPTY,
        "findings.md": R.FINDINGS_EMPTY,
        "briefing.md": R.AREA_BRIEF_EMPTY,
        "board.md": R.AREA_BOARD_EMPTY,
        "area-findings.md": R.AREA_FINDINGS_EMPTY,
    }
    for fn, txt in notes.items():
        with open(os.path.join(base, fn), "w", encoding="utf-8") as f:
            f.write(txt.strip() + "\n")
    readme = ["# 📝 Templates de nota\n",
              "> Notas markdown prontas para o Maestri: contrato, workboard, playbook de "
              "release, stack-checklist de 30 camadas, case-file de depuração, timeline de "
              "incidente, regras de engajamento de red team e o par briefing/board/findings "
              "das áreas de negócio.\n",
              "## Como importar\n",
              "- **Arraste** um arquivo `.md` deste diretório para o canvas do Maestri: ele "
              "vira uma nota apontando para o arquivo (fica no local original).\n"
              "- Ou copie o conteúdo para uma nota gerenciada nova (`Ctrl⇧D`).\n"
              "- Conecte a nota aos terminais que devem lê-la e escrevê-la.\n",
              "## Arquivos\n"]
    for fn in notes:
        readme.append(f"- [`{fn}`](./{fn})")
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme) + "\n")
    return len(notes)


# ===========================================================================
# 3) Instruções por stack (CLAUDE.md / AGENTS.md)
# ===========================================================================

def _instr_body(name_short, front, back):
    return f"""# Instruções do projeto — {name_short}

> Este arquivo é entregue automaticamente aos agentes ao iniciarem neste workspace do
> Maestri. Ajuste ao seu projeto. O Maestri mantém `CLAUDE.md` e `AGENTS.md` sincronizados.

## Stack
- **Frontend:** {front}
- **Backend:** {back}

## Como trabalhar aqui
- Responda em pt-BR; mantenha código, identificadores, flags e nomes de arquivo em inglês.
- **Contrato antes de código:** leia a nota de contrato (`feature-spec`) e a sua fatia no
  `workboard` antes de escrever qualquer linha. Fique dentro das suas fronteiras de arquivo.
- **Nunca chute diante de ambiguidade:** dúvida de contrato vai ao Arquiteto, dúvida de
  produto vai ao Maestro (`maestri ask "<nome>" "<pergunta>"`).
- **Achados, não correções:** revisores só reportam, com evidência, e verificam ao vivo no
  portal. Nunca alegue verificação que você não viu.

## Comandos
```bash
# ajuste aos scripts reais do projeto
install:  <gerenciador> install
dev:      <cmd de dev>          # o Maestro é dono do runtime; suba em background com log
test:     <cmd de testes>
build:    <cmd de build>
lint:     <cmd de lint/format>
```

## Qualidade
- Sem `any` e sem cast que mente; trate estados de erro/loading/vazio.
- HTML semântico e acessibilidade real (teclado, foco, contraste).
- Sem refactor de carona fora da fatia; siga as convenções ao redor.

## Segurança
- Nada de segredo em texto claro no repo; use variáveis de ambiente.
- Valide entradas em toda fronteira de confiança.
- Trabalho que toca dinheiro, identidade ou dados sensíveis passa pelo revisor de segurança.
"""


def gen_instrucoes():
    base = os.path.join(ROOT, "instrucoes")
    os.makedirs(base, exist_ok=True)
    made = []
    # genérico + por stack
    generic = _instr_body("Genérico", "sua stack de frontend", "sua stack de backend")
    gdir = os.path.join(base, "generico")
    os.makedirs(gdir, exist_ok=True)
    for fn in ("CLAUDE.md", "AGENTS.md"):
        with open(os.path.join(gdir, fn), "w", encoding="utf-8") as f:
            f.write(generic)
    made.append(("Genérico", "generico"))
    for name_short, front, back, _ck, _icon in G.STACKS:
        slug = slugify(name_short)
        d = os.path.join(base, slug)
        os.makedirs(d, exist_ok=True)
        body = _instr_body(name_short, front, back)
        for fn in ("CLAUDE.md", "AGENTS.md"):
            with open(os.path.join(d, fn), "w", encoding="utf-8") as f:
                f.write(body)
        made.append((name_short, slug))
    readme = ["# 🧭 Templates de instruções (`CLAUDE.md` / `AGENTS.md`)\n",
              "> Instruções que o agente recebe ao iniciar num workspace. O Maestri entrega "
              "`CLAUDE.md` (Claude Code) e `AGENTS.md` (Codex/Gemini/OpenCode) e pode mantê-los "
              "sincronizados. Um par por stack, mais um genérico.\n",
              "## Como usar\n",
              "1. Copie o `CLAUDE.md` e o `AGENTS.md` da stack desejada para a raiz do seu "
              "projeto (ou defina o caminho nas configurações do workspace).\n"
              "2. Ajuste os comandos e convenções ao seu repositório.\n"
              "3. Ative a sincronização `CLAUDE.md ↔ AGENTS.md` nas configurações do workspace.\n",
              "## Stacks\n"]
    for name_short, slug in made:
        readme.append(f"- **{name_short}** — [`{slug}/CLAUDE.md`](./{slug}/CLAUDE.md) · "
                      f"[`{slug}/AGENTS.md`](./{slug}/AGENTS.md)")
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme) + "\n")
    return len(made)


def main():
    n_roles = gen_roles()
    n_notas = gen_notas()
    n_instr = gen_instrucoes()
    print(f"Hub gerado: {n_roles} roles, {n_notas} notas, {n_instr} conjuntos de instruções.")


if __name__ == "__main__":
    main()
