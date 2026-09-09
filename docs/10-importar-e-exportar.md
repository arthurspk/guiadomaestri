# 10 · Importar e exportar no Maestri (e o que este hub oferece)

Este guia é um **hub público** de coisas do Maestri. Além das partituras, o Maestri tem
vários artefatos portáteis; abaixo está o que dá para **importar/exportar de forma nativa**,
o que se compartilha como **receita**, e onde cada um vive neste repositório.

Fontes: documentação oficial do Maestri (<https://www.themaestri.app/pt-br/docs>).

---

## Nativo — formatos que o Maestri importa/exporta

| Artefato | Formato | Importar | Exportar | Aqui no hub |
|---|---|---|---|---|
| **Partituras** | `.maestripartitura` / `.maestripartituras` | duplo clique, arrastar, painel ⋯ → Importar | arrastar card p/ Finder/Slack/Mail, "Salvar em…", ⋯ → Exportar todas | [`partituras/`](../partituras/CATALOGO.md) |
| **Responsabilidades** | `role.json` (satélite) | copiar p/ a pasta `.maestri` do projeto → "Descobrir Responsabilidades" | vive junto do projeto e viaja com ele | [`roles/`](../roles/CATALOGO.md) |
| **Temas de terminal** | Ghostty (`~/.maestri/terminal/themes/`) + iTerm2 embutidos | copiar arquivo p/ a pasta de temas | copiar arquivo | [`temas/`](../temas/README.md) |
| **Instruções de agente** | `CLAUDE.md` / `AGENTS.md` | ficam na raiz do projeto/workspace | idem (versionados no git) | [`instrucoes/`](../instrucoes/README.md) |
| **Notas** | `.md` / `.markdown` / `.txt` | arrastar do Finder p/ o canvas | "Mover para…" grava no seu projeto | [`notas/`](../notas/README.md) |
| **Espaços de trabalho** | `.maestri` | Arquivo → Importar Espaço de Trabalho | compartilhado pelo app (schema não documentado) | [`workspaces/`](../workspaces/README.md) |

### Detalhes que importam

- **Partituras** preservam nós, nomes, ícones, cores, tamanhos, texto de notas, URLs de
  portais, desenhos, grupos, conexões e as responsabilidades embutidas. **Não** preservam
  scrollback, estado de execução, configs de SSH/Docker/Sandbox e variáveis de ambiente,
  caminhos absolutos, nós de arquivo anexado, conectores entre andares e portais locais.
  Escopo **Global** ou **restrito a um workspace**.
- **Responsabilidades (`role.json`)**: o Maestri descobre esses arquivos no diretório de
  trabalho pelo botão **Descobrir Responsabilidades**. Cada um traz nome, cor do badge e
  prompt. O hub tem uma biblioteca curada em [`roles/`](../roles/CATALOGO.md).
- **Temas**: 30+ embutidos (formato iTerm2) mais temas Ghostty seus em
  `~/.maestri/terminal/themes/`. Veja [`temas/`](../temas/README.md).
- **Notas**: ao arrastar um `.md` do Finder, a nota aponta para o arquivo (fica no local).
  "Mover para…" grava uma nota gerenciada num caminho do projeto; se você tirar do canvas
  depois, **o arquivo permanece**.

## Trazer arquivos para dentro (import de conteúdo)

- **Árvore de arquivos**: arraste arquivos para o canvas como nós de preview (imagem, PDF,
  vídeo), edite no editor embutido e veja diffs git.
- **Compositor de Prompts** (`Ctrl⇧P`): anexe arquivos e imagens ao prompt (clipe de papel,
  "Arquivo…", colar screenshot, soltar arquivo). Imagens vão como imagem; outros arquivos
  viram um chip entregue ao agente como caminho.

## Receitas curadas (compartilha o texto, a pessoa aplica)

Não são formatos com "importar", mas são muito compartilháveis — o hub cataloga em
[`receitas/`](../receitas/README.md):

- **Hooks de andar** (Setup/Run/Teardown) — [`receitas/hooks/`](../receitas/hooks/).
- **Rotinas** (prompts agendados) — [`receitas/rotinas.md`](../receitas/rotinas.md).
- **Integrações Maestri Wire** (cliente + ideias) — [`receitas/wire/`](../receitas/wire/).
- **Ambientes** (Docker Sandbox/SSH/Custom) — [`receitas/ambientes/`](../receitas/ambientes/).
- **Prompts do Compositor** — [`prompts/`](../prompts/README.md).

## Gerar os recursos do hub

Os recursos programáticos (roles, notas, instruções) são gerados; as partituras têm o seu
próprio gerador. Tudo é determinístico.

```bash
python3 scripts/generate_partituras.py   # partituras (.maestripartitura) por área
python3 scripts/generate_hub.py          # roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py     # valida as partituras
python3 tests/validate_hub.py            # valida os role.json e a estrutura do hub
```

## Pontos a confirmar (fidelidade)

Três coisas não estão 100% na doc pública e o hub trata com honestidade:

1. **Schema exato do `role.json`** — a biblioteca usa o formato do objeto de role das
   partituras oficiais; confirme com um export real.
2. **Exportar workspace `.maestri`** — só a importação está documentada; o hub não gera
   `.maestri` às cegas.
3. **JSON do portal de dispositivo** — coberto em [docs/09](09-portais-mobile-web-emulador.md).

Feche essas três lacunas confirmando contra um **export real** do seu Maestri e a
[documentação oficial](https://www.themaestri.app/pt-br/docs).

---

Volta ao [índice](../README.md).
