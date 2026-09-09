# 04 · O formato `.maestripartitura`

Uma partitura é um documento **JSON** em texto claro. O Maestri guarda em
`~/.maestri/partituras/`. Extensões: `.maestripartitura` (uma) e `.maestripartituras`
(pacote com várias). Esta página descreve o `formatVersion` 1 (appVersion ~0.45.x),
calibrado byte a byte contra o formato que o próprio Maestri exporta. O schema esperado
está embutido no validador [`tests/validate_partituras.py`](../tests/validate_partituras.py).

> Este documento é a especificação que o gerador em [`scripts/`](../scripts/) implementa.
> Se algo aqui divergir de um arquivo oficial, o arquivo oficial vence.

---

## Chaves de topo

```json
{
  "appVersion": "0.45.6",
  "color": "#007AFF",
  "createdAt": "2026-09-08T12:00:00Z",
  "description": "…",
  "formatVersion": 1,
  "icon": "globe",
  "id": "D99C07A3-CED4-4E8E-BC7D-86BCE5A1F79C",
  "name": "Ship Feature · React + Node",
  "workspaceId": "C9B7A5CD-…",
  "payload": { … },
  "roles": [ … ]
}
```

| Chave | Tipo | Notas |
|---|---|---|
| `appVersion` | string | Versão do app que gravou (ex.: `0.45.6`). |
| `color` | string | Hex de uma **system color** da Apple (`#007AFF`, `#5856D6`, …). |
| `createdAt` | string | ISO 8601 em UTC. |
| `description` | string | Descrição livre (aparece na tela de importação). |
| `formatVersion` | int | `1`. |
| `icon` | string | Um **SF Symbol** (`paperplane`, `magnifyingglass`) **ou** um emoji (`🐐`). |
| `id` | string | UUID **maiúsculo**. |
| `name` | string | Nome exibido. |
| `workspaceId` | string | UUID do workspace de origem. |
| `payload` | objeto | Os nós e conexões (abaixo). |
| `roles` | lista | As responsabilidades (abaixo). |

## `payload`

```json
"payload": {
  "connections": [ … ],
  "drawings": [],
  "nodes": [ … ],
  "noteConnections": [ … ],
  "noteTexts": { "<nodeId>": "<markdown>" },
  "noteToNoteConnections": [ … ],
  "portalConnections": [ … ],
  "portalToPortalConnections": [ … ],
  "sourceWorkingDirectory": "",
  "sourceWorkspaceId": "C9B7A5CD-…"
}
```

- **`nodes`** — todos os nós (terminais, notas, portais) na mesma lista.
- **`connections`** — cabos terminal↔terminal.
- **`noteConnections`** / **`portalConnections`** — terminal↔nota e terminal↔portal.
- **`noteToNoteConnections`** / **`portalToPortalConnections`** — encadeamentos.
- **`noteTexts`** — dicionário `id do nó da nota → markdown`. O texto vive aqui, não dentro
  do nó.
- **`drawings`** — desenhos (vazio nas partituras deste guia).
- **`sourceWorkingDirectory`** — vazio; caminhos absolutos **não** são preservados.
- **`sourceWorkspaceId`** — UUID do workspace de origem.

## Nós

Todo nó tem a mesma casca; o que muda é o `content`, que carrega **um** de três tipos,
sempre embrulhado em `"_0"`.

```json
{
  "content": { "<tipo>": { "_0": { … } } },
  "frame": [[x, y], [w, h]],
  "id": "<UUID do nó>",
  "zIndex": 61,
  "isLocked": false,
  "createdAt": "…",
  "lastModifiedAt": "…"
}
```

`frame` é `[[x, y], [largura, altura]]` em pontos do canvas infinito.

### `terminal._0`
```json
{
  "agentType": "claude_code",
  "assignedRoleId": "<UUID de roles>",
  "autoScrollLocked": false,
  "color": "#007AFF",
  "command": "claude --dangerously-skip-permissions --model fable",
  "icon": "seal",
  "id": "<UUID interno do terminal>",
  "isManager": true,
  "isUnloaded": false,
  "lastActiveAt": "1970-01-01T00:00:00Z",
  "monitorWithOmbro": true,
  "name": "Maestro · orquestrador",
  "scrollbackFile": "",
  "scrollbackLineCount": 0,
  "shellPath": "",
  "shortcutMode": { "kind": "automatic" },
  "status": "restored",
  "workingDirectory": ""
}
```
- **`command`** define o modelo/agente. Convenção deste guia: `--model fable` no maestro,
  `--model opus` nos executores, `codex`/`gemini` nos revisores adversariais.
- **`isManager`** marca o maestro.
- **`assignedRoleId`** liga o terminal a uma entrada de `roles` (opcional).
- ⚠️ O **`id` interno do terminal é diferente do `id` do nó**. As conexões
  terminal↔terminal e o `terminalId` das conexões de nota/portal usam **este id interno**,
  não o do nó.

### `stickyNote._0`
```json
{
  "color": "blue",
  "fileName": "feature-spec.md",
  "fontSize": 14,
  "hasCustomName": true,
  "isContentLocked": false,
  "isPreviewing": true,
  "storageMode": { "managed": {} }
}
```
Cores: `blue`, `green`, `yellow`, `purple`, `slate`, `orange`, `pink`, `red`, `teal`. O
texto markdown fica em `payload.noteTexts[<id do nó>]`.

### `portal._0`
```json
{
  "chromeHidden": false,
  "currentURL": "http://localhost:5173",
  "id": "<UUID interno do portal>",
  "isUnloaded": false,
  "name": "Web · Desktop",
  "source": { "url": { "_0": "http://localhost:5173" } },
  "status": "idle",
  "storageScope": "isolated",
  "surface": { "browser": {} }
}
```
As `portalConnections` referenciam o **`id` do NÓ** do portal (não o id interno).

## `roles`

```json
{
  "id": "357E9E9E-…",
  "name": "Feature Architect",
  "prompt": "Você transforma um pedido em um contrato…",
  "color": "#FFCC00",
  "icon": "person.text.rectangle",
  "schemaVersion": 1
}
```
Vários terminais podem compartilhar o mesmo role pelo `id`. Os prompts são em **segunda
pessoa** e orientados à CLI `maestri`.

## Conexões e `ropePoints`

Cada conexão carrega uma lista **`ropePoints`**: pontos `[x, y]` que desenham a curva do
cabo. Nas partituras oficiais são **21 pontos**, de borda a borda dos nós, com um leve
"sag" (o cabo pesa no meio). O gerador reproduz isso com uma curva senoidal.

```json
// terminal↔terminal
{ "id": "…", "terminalIdA": "<id interno>", "terminalIdB": "<id interno>",
  "createdAt": "…", "ropePoints": [[x,y], … 21 pontos …] }

// terminal↔nota
{ "id": "…", "noteNodeId": "<id do nó da nota>", "terminalId": "<id interno>",
  "createdAt": "…", "ropePoints": [ … ] }

// terminal↔portal
{ "id": "…", "portalNodeId": "<id do nó do portal>", "terminalId": "<id interno>",
  "createdAt": "…", "ropePoints": [ … ] }

// nota↔nota
{ "id": "…", "noteNodeIdA": "…", "noteNodeIdB": "…", "createdAt": "…", "ropePoints": [ … ] }
```

## Pacote `.maestripartituras`

```json
{ "formatVersion": 1, "partituras": [ { …partitura… }, { …partitura… } ] }
```
Uma lista de partituras completas sob a chave `partituras`.

## O que **não** é preservado

Por design, uma partitura é um template portátil, então ela **exclui**: histórico de
scrollback e estado de execução dos terminais; configs de SSH/Docker/Sandbox/runtime e
variáveis de ambiente; **caminhos absolutos** e diretórios de trabalho; nós de arquivo
anexados; conexões entre andares; e portais que apontam para arquivos/pastas locais. As
responsabilidades ficam **embutidas**, então as notas compartilhadas funcionam na hora,
sem referência quebrada.

## Como o gerador garante fidelidade

- **UUIDs determinísticos**: `sha1(seed)` em maiúsculas. Regerar produz os mesmos arquivos.
- **Validação obrigatória**: [`tests/validate_partituras.py`](../tests/validate_partituras.py)
  carrega cada arquivo e compara chaves de topo, de payload, de cada `_0` e de cada role
  **exatamente** contra o schema embutido do formato, além de checar integridade
  referencial das conexões e os 21 `ropePoints`. Zero divergências.

---

Próximo: [05 · Modelos e segurança](05-modelos-e-seguranca.md).
