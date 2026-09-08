# 🎨 Temas de terminal (formato Ghostty)

> Temas de cores para os terminais do Maestri, no formato **Ghostty**. O Maestri já traz
> 30+ esquemas embutidos (formato de cores do iTerm2); estes são temas próprios do guia,
> pensados para diferenciar os papéis do time no canvas.

## Temas

| Arquivo | Para quê |
|---|---|
| [`maestri-dark.ghostty`](./maestri-dark.ghostty) | Escuro, roxo Maestri — uso geral. |
| [`maestri-light.ghostty`](./maestri-light.ghostty) | Claro, para ambientes iluminados. |
| [`maestro-fable.ghostty`](./maestro-fable.ghostty) | Roxo do orquestrador (`--model fable`). |
| [`warden-codex.ghostty`](./warden-codex.ghostty) | Âmbar dos revisores adversariais (`codex`/`gemini`). |

## Como instalar (importar)

1. Copie os arquivos para a pasta de temas do Maestri:
   ```bash
   mkdir -p ~/.maestri/terminal/themes
   cp temas/*.ghostty ~/.maestri/terminal/themes/
   ```
2. No Maestri, abra as configurações de um terminal e escolha o tema pela lista (os temas
   próprios aparecem junto dos embutidos).
3. Opcional: use "Seguir aparência do sistema" para parear um tema claro e um escuro.

## Formato

Cada arquivo é texto simples no formato Ghostty: `chave = valor`. As chaves usadas aqui:

- `background`, `foreground` — cores base (hex sem `#`).
- `cursor-color`, `cursor-text` — cursor.
- `selection-background`, `selection-foreground` — seleção.
- `palette = N=#RRGGBB` — as 16 cores ANSI (0–15).

Para criar o seu, copie um destes, troque as cores e salve com outro nome na mesma pasta.

> As cores seguem a paleta de system colors da Apple usada no restante do guia. Se um
> detalhe do formato divergir na sua versão do Maestri, confira a documentação oficial de
> [Terminais e Agentes](https://www.themaestri.app/pt-br/docs/terminals).
