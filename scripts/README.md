# 📜 Scripts

Os geradores e bibliotecas em Python que produzem tudo neste hub. **Sem dependências além
da stdlib do Python 3.** Os UUIDs são determinísticos: regerar produz os mesmos arquivos
byte a byte, então o repositório fica estável no git.

## Visão geral

| Script | Tipo | O que faz |
|---|---|---|
| [`maestri_build.py`](./maestri_build.py) | biblioteca | Classe `Partitura` (terminais, notas, portais, conexões), serialização no formato `.maestripartitura`, `ropePoints`, helpers de layout e portais de dispositivo. Não roda sozinho. |
| [`roles_lib.py`](./roles_lib.py) | biblioteca | Prompts de responsabilidade (roles) em pt-BR e templates de nota (contrato, workboard, stack-checklist, etc.). Não roda sozinho. |
| [`generate_partituras.py`](./generate_partituras.py) | gerador | Monta as **257 partituras** por área, o pacote coletivo por área, o `Guia-do-Maestri.maestripartituras` e os `CATALOGO.md`. |
| [`generate_hub.py`](./generate_hub.py) | gerador | Gera a biblioteca de **`role.json`** (`roles/`), as **notas avulsas** (`notas/`) e os **templates de instrução** (`instrucoes/`). |
| [`../tests/validate_partituras.py`](../tests/validate_partituras.py) | validação | Compara chaves de topo/payload/nós/roles de cada partitura com a oficial `Money_Send_Pipeline.maestripartitura`. Zero divergências. |
| [`../tests/validate_hub.py`](../tests/validate_hub.py) | validação | Valida cada `role.json`, as notas e os pares `CLAUDE.md`/`AGENTS.md`. |

## Como rodar

Tudo a partir da raiz do repositório:

```bash
# 1) gerar as partituras (.maestripartitura) por área
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"

# 2) gerar os recursos do hub (roles, notas, instruções)
python3 scripts/generate_hub.py            # → "Hub gerado: 30 roles, 13 notas, 25 conjuntos de instruções."

# 3) validar tudo
python3 tests/validate_partituras.py        # → "Zero divergências"
python3 tests/validate_hub.py               # → "Zero problemas"
```

## O que cada gerador escreve

- `generate_partituras.py` → `partituras/<area>/*.maestripartitura`,
  `partituras/<area>/<Area>.maestripartituras`, `partituras/<area>/CATALOGO.md`,
  `partituras/Guia-do-Maestri.maestripartituras` e `partituras/CATALOGO.md`.
- `generate_hub.py` → `roles/<categoria>/*.role.json` + `roles/CATALOGO.md`,
  `notas/*.md` + `notas/README.md`, `instrucoes/<stack>/CLAUDE.md` e `AGENTS.md` +
  `instrucoes/README.md`.

## Estender

- **Mais partituras:** adicione uma variante a um catálogo (ex.: `STACKS`, `CLOUDS`,
  `BFF_DOMAINS`) ou uma nova função de família em `generate_partituras.py`. Para uma **área
  nova**, adicione uma entrada em `AREAS` e registre a família em `NEW_AREA_FAMILIES`.
- **Mais roles/notas/instruções:** edite as listas em `generate_hub.py`
  (`_roles_catalog()`, `gen_notas()`), reaproveitando os builders de `roles_lib.py`.
- **Portais de dispositivo:** veja `device_portal()` e `raw_portal()` em `maestri_build.py`
  e [docs/09](../docs/09-portais-mobile-web-emulador.md).

Depois de qualquer mudança, rode os dois geradores e as duas validações acima.

## Detalhes do formato

A especificação completa do `.maestripartitura` está em
[docs/04](../docs/04-formato-maestripartitura.md). O que dá para importar/exportar de forma
nativa (partituras, roles, temas, instruções, notas) e as receitas curadas estão em
[docs/10](../docs/10-importar-e-exportar.md).
