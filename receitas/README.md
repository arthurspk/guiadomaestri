# 🧑‍🍳 Receitas curadas

> Nem tudo no Maestri é um arquivo com "importar/exportar". Muita coisa se compartilha como
> **receita**: um trecho de configuração, um script, um prompt para copiar e colar. Esta
> pasta reúne essas receitas do ecossistema Maestri.

## Conteúdo

- **[🪝 Hooks de andar](./hooks/)** — scripts de Setup/Run/Teardown para os andares (Floors):
  [`setup-node.sh`](./hooks/setup-node.sh), [`setup-python.sh`](./hooks/setup-python.sh),
  [`run-tests.sh`](./hooks/run-tests.sh), [`teardown.sh`](./hooks/teardown.sh). Cole no
  ícone ⚡ do andar; usam as variáveis `$MAESTRI_FLOOR_*`.
- **[⏰ Rotinas](./rotinas.md)** — prompts agendados prontos (guardião de CI, vigia de
  deploy, clipping de concorrência, fechamento diário, triagem de tickets).
- **[🔌 Maestri Wire](./wire/)** — cliente Python de exemplo do protocolo Wire (porta 7434)
  e ideias de integração (notificações de atenção, dashboard read-only, CI/CD).
- **[🧰 Ambientes](./ambientes/)** — receitas de Docker Sandbox, Docker Container, SSH e
  Custom Runtime, mais um [`devcontainer.json`](./ambientes/devcontainer.json) base.

## Como contribuir uma receita

1. Escolha a pasta certa (ou proponha uma nova).
2. Adicione o script/arquivo com um cabeçalho explicando o que faz e como aplicar no Maestri.
3. Linke a partir do README da pasta e deste índice.
4. Se a receita executa algo, deixe claro o que ela toca e nunca embuta segredos.

Veja também os recursos **nativos** de importar/exportar do hub em
[docs/10 · Importar e exportar](../docs/10-importar-e-exportar.md).
