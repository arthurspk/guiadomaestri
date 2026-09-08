# 🧰 Receitas de Ambientes (Environments)

> Os **Ambientes** definem ONDE os terminais do Maestri rodam: Local, Local (tmux), WSL
> (Windows), SSH, Docker Container, **Docker Sandbox** ou um runtime customizado (Podman,
> Apple container, Lima). Configure em **Configurações → Geral → Ambientes** e escolha por
> workspace ou por terminal. Doc oficial:
> <https://www.themaestri.app/pt-br/docs/environments>.

Estas são **receitas** de setup (não um formato importável): arquivos e passos para deixar
um ambiente pronto para o Maestri se conectar.

---

## Docker Sandbox (ambiente isolado para agentes de IA)

Bom quando você quer que os agentes rodem num container isolado, com rede sob escopo. O
Maestri usa a CLI `sbx` e configura políticas de rede automaticamente ao testar a conexão.

- Ver [`devcontainer.json`](./devcontainer.json) como base do container de desenvolvimento.
- No Maestri: **Configurações → Ambientes → Docker Sandbox**, informe o nome do sandbox e o
  shell (`/bin/bash`), e clique em **Testar**.

## Docker Container (anexar a um container existente)

O Maestri nunca cria nem apaga containers — ele **anexa** a um em execução via `docker exec`.

```bash
# suba um container de dev de longa duração (exemplo)
docker run -d --name meu-dev -v "$PWD:/work" -w /work node:24 sleep infinity
```
No Maestri: **Ambientes → Docker Container**, informe `meu-dev`, o shell (`/bin/sh`) e o
usuário. O container alcança o Maestri por `host.docker.internal:<Bridge Port>` (padrão 7433).

## SSH (host remoto)

```
# ~/.ssh/config
Host meu-servidor
  HostName 203.0.113.10
  User deploy
  IdentityFile ~/.ssh/id_ed25519
```
No Maestri: **Ambientes → SSH**, informe o host (ou o alias `meu-servidor`), a porta e o
usuário, e clique em **Testar**. O Maestri instala o wrapper da CLI e as Skills no servidor.

## Custom Runtime (ex.: Podman)

```
Nome:                   Podman Development
Executável:             podman
Argumentos de Comando:  exec -i development
Argumentos Interativos: exec -i -t development
Shell:                  /bin/bash
Host do Bridge:         host.containers.internal
```

---

## Variáveis padrão em ambientes remotos
Todo ambiente remoto recebe: `MAESTRI_TERMINAL_ID`, `MAESTRI_HOST`, `MAESTRI_TOKEN`,
`MAESTRI_CLI`, além de `TERM`, `COLORTERM`, `HOME`. Modificações do terminal são
encaminhadas, mas não podem sobrescrever `HOME`, `PATH` ou valores `MAESTRI_*`.

> A **Bridge Port** (padrão `7433`) é compartilhada por SSH/Docker/Sandbox/Custom para a
> comunicação bidirecional com o Maestri. Não confunda com a porta do Wire (`7434`).
