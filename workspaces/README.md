# 🗂️ Espaços de trabalho (`.maestri`)

> Um **espaço de trabalho** do Maestri pode ser compartilhado como um arquivo `.maestri`,
> que carrega o layout do canvas, as posições dos terminais, as atribuições de agentes e as
> configurações.

## Importar

**Arquivo → Importar Espaço de Trabalho** e abra um `.maestri` compartilhado. O Maestri
mostra o que há dentro antes de aplicar e deixa você escolher onde colocá-lo.

## Sobre exportar / contribuir um workspace aqui

A documentação pública descreve a **importação** de um `.maestri`, mas não detalha o comando
exato para **exportá-lo**, nem o schema do arquivo. Por isso este hub **não gera** arquivos
`.maestri` automaticamente — seria adivinhar o formato. O caminho confiável:

1. Monte o workspace no Maestri (terminais, notas, portais, configurações).
2. Exporte/compartilhe o `.maestri` pelo próprio app (menu de compartilhamento do workspace).
3. Coloque o arquivo nesta pasta com um `.md` ao lado explicando para que serve e quais
   pré-requisitos ele espera (diretórios, agentes instalados, ambiente).

> Para montar times prontos sem depender do formato `.maestri`, prefira as
> **[partituras](../partituras/CATALOGO.md)**: elas importam de forma garantida e trazem
> terminais, notas, portais e conexões. Um workspace é o "projeto inteiro"; uma partitura é
> um "arranjo" que você solta em qualquer workspace.

## O que confirmar

O schema do `.maestri` e o comando de exportação são dois pontos a confirmar contra um
**export real** e a [documentação oficial](https://www.themaestri.app/pt-br/docs/workspaces).
Assim que confirmados, dá para automatizar a geração de workspaces-modelo aqui.
