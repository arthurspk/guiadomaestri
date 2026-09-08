# 03 · Atalhos e comandos

Duas linguagens para reger o Maestri: os **atalhos de teclado** do app (você, no canvas)
e a **CLI `maestri`** (os agentes, entre si). Esta página junta as duas.

Fonte oficial dos atalhos: <https://www.themaestri.app/pt-br/docs/shortcuts>. Tudo que
aparece em **Configurações → Atalhos** pode ser remapeado; comandos de menu e atalhos do
editor são fixos. A tabela abaixo é a de **macOS** (o seletor da página oficial troca para
Windows/Linux, que têm conjunto diferente).

---

## Atalhos de teclado (macOS)

Notação: `⌘` Command · `⌥` Option/Alt · `⇧` Shift · `⌃` Control. A doc do Maestri escreve
a tecla modificadora principal como **Ctrl**; no Mac ela corresponde à tecla de controle
usada pelo app.

### Espaços de trabalho
| Atalho | Ação |
|---|---|
| `Ctrl↓` / `Ctrl↑` | Próximo / anterior espaço de trabalho |
| `Ctrl]` / `Ctrl[` | Próximo / anterior (pelo menu Visualizar) |
| `Ctrl1`–`9` | Toque duas vezes e um número para pular a um workspace |
| `Ctrl⇧N` | Novo espaço de trabalho |

### Navegando pelo canvas
| Atalho | Ação |
|---|---|
| `⌃Tab` / `⌃⇧Tab` | Próximo / anterior elemento |
| `Ctrl1`–`9` | Pula direto para um terminal |
| `CtrlAlt→` / `CtrlAlt←` | Percorre o fio até o próximo / anterior elemento conectado |
| `Ctrl\` | Alterna o foco no elemento selecionado |
| `AltCtrl\` | Ajusta o zoom para enquadrar a seleção |
| `Ctrl⇧\` | Alterna a visão geral dos andares (`↑`/`↓` percorre) |
| `Ctrl+` / `Ctrl-` | Aproxima / afasta (`AltScroll` também) |
| `Ctrl⇧M` | Alterna o minimapa |

### Ferramentas do canvas (tecla simples, nada selecionado)
| Tecla | Ação |
|---|---|
| `H` | Pan (`Esc` para sair) |
| `V` | Ferramenta de seleção |
| `T` | Coloca um terminal |
| `N` | Coloca uma nota |
| `P` | Coloca um portal |
| `F` | Coloca uma árvore de arquivos |
| `L` | Coloca um bloco de texto |
| `B` | Desenha um retângulo (`[`/`]` traço mais fino/grosso) |
| `Space` | Segure para mover, ou Quick Look da seleção |

### Criando
| Atalho | Ação |
|---|---|
| `CtrlL` | Inicia uma conexão a partir do elemento selecionado |
| `Ctrl⇧L` | Abre as Partituras |
| `CtrlT` | Novo terminal |
| `Ctrl⇧D` | Nova nota adesiva |

### Trabalhando com elementos
| Atalho | Ação |
|---|---|
| `CtrlW` | Exclui o elemento selecionado |
| `CtrlC` / `CtrlV` | Copia / cola elementos |
| `AltDrag` | Duplica um elemento |
| `CtrlDrag` | Encaixa e organiza enquanto arrasta |
| `Ctrl⇧T` | Organiza a seleção em grade (de novo para alternar layouts) |
| `CtrlG` / `Ctrl⇧G` | Agrupa / desagrupa |
| `Esc` | Devolve um painel elevado ao canvas |

### Terminais
| Atalho | Ação |
|---|---|
| `Ctrl⇧C` / `Ctrl⇧V` | Cópia inteligente / cola (deixa `CtrlC` livre para interromper) |
| `CtrlF` | Busca no terminal em foco |
| `CtrlK` | Limpa o buffer |
| `Ctrl⇧B` | Alterna a trava de rolagem automática |
| `Ctrl⇧+` / `Ctrl⇧-` | Fonte maior / menor |

### Encontrando coisas
| Atalho | Ação |
|---|---|
| `CtrlP` | **Batuta Search** (paleta de comandos) |
| `Ctrl⇧A` | Pula para o próximo terminal pedindo atenção |
| `AltCtrlA` | Lista todos os terminais aguardando atenção |
| `AltCtrlE` | Lista os elementos deste workspace (todos os andares) |
| `⇧AltCtrlE` | Lista todos os elementos, em todos os workspaces e andares |

### Sempre disponíveis
| Atalho | Ação |
|---|---|
| `Ctrl,` | Configurações |
| `Ctrl⇧P` | Compositor de Prompts |
| `CtrlS` | Alterna a barra lateral |
| `CtrlZ` / `Ctrl⇧Z` | Desfaz / refaz no canvas |
| `CtrlR` | Recarrega o portal em foco |
| `Ctrl⇧O` | Mostra/esconde a janela do **Ombro** |

**Sem atalho por padrão** (defina em Configurações → Atalhos): **Elevar elemento** e
**Alinhar e distribuir**.

---

## CLI `maestri` (o vocabulário dos agentes)

Quando dois terminais são conectados, o Maestri instala uma skill em cada um para que
conversem por esta CLI — **independente do tipo de agente** (Claude fala com Codex). É o
vocabulário que as responsabilidades das partituras usam. Estes são os comandos **seguros**,
os mesmos vistos nas partituras oficiais; onde precisar de detalhe de sintaxe, a fonte é
a doc oficial (<https://www.themaestri.app/pt-br/docs>).

### Ver o time
```bash
maestri list          # lista colegas, notas e portais; o Maestro é marcado maestro: true
maestri check         # espia o progresso dos colegas sem reenviar prompt
```

### Falar com colegas
```bash
maestri ask "<nome>" "<mensagem>"     # envia uma mensagem/pergunta a um agente pelo nome
maestri ask --batch ...               # dispara várias de uma vez (delegação paralela)
maestri notify                        # notifica o humano quando precisa de decisão
```
O padrão de report: ao terminar, o agente responde a quem pediu com
`maestri ask "<nome>" "<resumo>"` para resolver a espera dele.

### Notas (a fonte de verdade)
```bash
maestri note read  "<nome>"           # lê o conteúdo de uma nota
maestri note write "<nome>" "<texto>" # escreve/substitui
maestri note edit  "<nome>"           # edita (usado para anexar achados a uma seção)
maestri note create --name "<nome>"   # cria uma nota nova
```

### Portais (verificação viva)
```bash
maestri portal navigate <url>         # navega o portal para uma URL
maestri portal snapshot               # captura o estado da página (refs de elementos)
maestri portal click   <ref>          # clica (prefira refs de snapshot a coordenadas)
maestri portal fill    <ref> "<txt>"  # preenche um campo
maestri portal key     "<tecla>"      # envia uma tecla
maestri portal screenshot             # tira um screenshot
maestri portal create  <url> "<nome>" # cria um portal novo
maestri portal edit    "<nome>" --url <url>   # aponta um portal para outra URL
```

### Responsabilidades
```bash
maestri role assign ...               # atribui uma responsabilidade a um terminal
```

> Não invente comandos que você não tem certeza. Este conjunto —
> `list` / `ask` / `check` / `note` / `portal` / `role assign` / `notify` — é o seguro.
> Para o resto, aponte para <https://www.themaestri.app/pt-br/docs>.

---

Próximo: [04 · Formato .maestripartitura](04-formato-maestripartitura.md).
