# 🎭 Biblioteca de Responsabilidades (`role.json`)

> **30 responsabilidades** reutilizáveis no formato nativo do Maestri. Cada `role.json` traz nome, cor do badge, ícone e o prompt em pt-BR.

## Como importar no Maestri

1. Copie o(s) arquivo(s) `*.role.json` para a pasta `.maestri` do diretório de trabalho do seu projeto (ao lado de `CLAUDE.md`/`AGENTS.md`).
2. Ao abrir as configurações de um terminal, clique em **Descobrir Responsabilidades**: o Maestri varre o diretório e oferece os roles encontrados.
3. Ou crie manualmente em **Configurações → Agentes** colando o prompt.

> ⚠️ O schema segue o formato do objeto de role das partituras oficiais (`color`, `icon`, `id`, `name`, `prompt`, `schemaVersion`). Se a sua versão do Maestri divergir, exporte uma responsabilidade real e compare (veja [docs/10](../docs/10-importar-e-exportar.md)).

## Índice por categoria


### Contrato & Estratégia

- **Arquiteto de Contrato** — [`contrato-estrategia/arquiteto-de-contrato.role.json`](./contrato-estrategia/arquiteto-de-contrato.role.json)
- **Estrategista de Área** — [`contrato-estrategia/estrategista-de-area.role.json`](./contrato-estrategia/estrategista-de-area.role.json)

### Depuração

- **Analista de Causa Raiz** — [`depuracao/analista-de-causa-raiz.role.json`](./depuracao/analista-de-causa-raiz.role.json)
- **Engenheiro de Correção** — [`depuracao/engenheiro-de-correcao.role.json`](./depuracao/engenheiro-de-correcao.role.json)
- **Reprodutor de Bug** — [`depuracao/reprodutor-de-bug.role.json`](./depuracao/reprodutor-de-bug.role.json)
- **Verificador de Correção** — [`depuracao/verificador-de-correcao.role.json`](./depuracao/verificador-de-correcao.role.json)

### Duelo & Adversarial

- **Duelista** — [`duelo-adversarial/duelista.role.json`](./duelo-adversarial/duelista.role.json)
- **Red Team Lead** — [`duelo-adversarial/red-team-lead.role.json`](./duelo-adversarial/red-team-lead.role.json)
- **Red Team Operator** — [`duelo-adversarial/red-team-operator.role.json`](./duelo-adversarial/red-team-operator.role.json)

### Execução

- **Engenheiro de Plataforma** — [`execucao/engenheiro-de-plataforma.role.json`](./execucao/engenheiro-de-plataforma.role.json)
- **Especialista (genérico)** — [`execucao/especialista-generico.role.json`](./execucao/especialista-generico.role.json)
- **Especialista Solo** — [`execucao/especialista-solo.role.json`](./execucao/especialista-solo.role.json)
- **Especialista de Área** — [`execucao/especialista-de-area.role.json`](./execucao/especialista-de-area.role.json)
- **Implementador de Fatia** — [`execucao/implementador-de-fatia.role.json`](./execucao/implementador-de-fatia.role.json)

### Incidente

- **Engenheiro de Mitigação** — [`incidente/engenheiro-de-mitigacao.role.json`](./incidente/engenheiro-de-mitigacao.role.json)
- **Investigador de Incidente** — [`incidente/investigador-de-incidente.role.json`](./incidente/investigador-de-incidente.role.json)
- **Líder de Comunicação** — [`incidente/lider-de-comunicacao.role.json`](./incidente/lider-de-comunicacao.role.json)

### Orquestração

- **Debug Maestro** — [`orquestracao/debug-maestro.role.json`](./orquestracao/debug-maestro.role.json)
- **Incident Commander** — [`orquestracao/incident-commander.role.json`](./orquestracao/incident-commander.role.json)
- **Juiz de Duelo** — [`orquestracao/juiz-de-duelo.role.json`](./orquestracao/juiz-de-duelo.role.json)
- **Maestro** — [`orquestracao/maestro.role.json`](./orquestracao/maestro.role.json)
- **Maestro de Área** — [`orquestracao/maestro-de-area.role.json`](./orquestracao/maestro-de-area.role.json)
- **Orquestrador (ReAct)** — [`orquestracao/orquestrador-react.role.json`](./orquestracao/orquestrador-react.role.json)
- **Release Conductor** — [`orquestracao/release-conductor.role.json`](./orquestracao/release-conductor.role.json)

### Revisão

- **Code Quality Reviewer** — [`revisao/code-quality-reviewer.role.json`](./revisao/code-quality-reviewer.role.json)
- **Correctness Verifier** — [`revisao/correctness-verifier.role.json`](./revisao/correctness-verifier.role.json)
- **Quality Warden** — [`revisao/quality-warden.role.json`](./revisao/quality-warden.role.json)
- **Revisor de Área** — [`revisao/revisor-de-area.role.json`](./revisao/revisor-de-area.role.json)
- **Security Auditor** — [`revisao/security-auditor.role.json`](./revisao/security-auditor.role.json)
- **UX & A11y Reviewer** — [`revisao/ux-a11y-reviewer.role.json`](./revisao/ux-a11y-reviewer.role.json)
