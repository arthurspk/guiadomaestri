# Prompt · Validar o Discord do Maestri com o Claude (Cowork / agente com navegador)

Este é um **prompt pronto para colar** num agente Claude que tenha acesso ao **Discord do
Maestri** — via Claude no modo Cowork, via automação de navegador (Claude in Chrome), ou
via um conector de Discord. O objetivo é o agente **percorrer o servidor inteiro**, extrair
o que for útil e **validar** as informações deste repositório (o "Guia do Maestri") contra o
que a comunidade e a equipe oficial dizem.

## Como usar

1. Garanta que o agente tenha acesso ao servidor Discord do Maestri (entre pelo convite no
   rodapé de <https://www.themaestri.app>, se ainda não for membro).
2. Cole o bloco abaixo como mensagem inicial. Ajuste o caminho do repositório se quiser que
   ele compare com os arquivos locais (`docs/`, `partituras/`, `scripts/`).
3. Deixe o agente trabalhar em modo **somente leitura** e entregar o relatório.

> Segurança e etiqueta: o prompt instrui o agente a **só ler**, nunca postar, nunca enviar
> DM, nunca coletar dados pessoais, e respeitar as regras do servidor. Reveja o relatório
> antes de agir sobre ele.

---

```text
Você é um analista de pesquisa. Sua missão é percorrer TODO o servidor Discord do Maestri
(app de macOS para orquestrar agentes de IA num canvas — themaestri.app) e produzir um
relatório que (a) reúna as informações úteis e (b) VALIDE o conteúdo do repositório "Guia do
Maestri" contra o que a equipe e a comunidade dizem.

REGRAS INEGOCIÁVEIS
- SOMENTE LEITURA. Não poste, não responda, não reaja, não envie DM, não entre em call.
- Não colete dados pessoais (nomes reais, e-mails, handles fora de contexto, prints de DM).
  Refira-se às pessoas por papel ("um membro da equipe", "um usuário"), nunca por identidade.
- Respeite as regras do servidor e os canais restritos. Se um canal for privado ou pedir
  papel/permissão, registre "sem acesso" e siga em frente — não tente burlar.
- Cite a FONTE de cada afirmação: nome do canal + data da mensagem (+ link se houver).
  Distinga claramente: [OFICIAL] (equipe/anúncio/pin/doc) vs [COMUNIDADE] (usuário).
- Nunca invente. O que você não encontrar, marque como "não encontrado", não como falso.

COBERTURA (percorra o servidor inteiro, de forma sistemática)
- Liste todos os canais visíveis. Para cada um: propósito e se você teve acesso.
- Priorize, nesta ordem: #announcements/#changelog/#novidades, #docs/#guia, #faq,
  #getting-started, #support/#ajuda/#troubleshooting, #feature-requests, #showcase, #dev/
  #api/#wire, e os canais de discussão geral. Leia os mensagens FIXADAS (pins) de cada canal
  primeiro — costumam conter a verdade curada.
- Vá fundo o suficiente para pegar o estado ATUAL (últimas semanas) e os fatos estáveis
  (pins antigos, FAQ). Registre a versão do app mais recente mencionada e a data.

O QUE EXTRAIR
1. Versão atual do app e destaques do changelog recente.
2. Vocabulário REAL da CLI `maestri`: todos os comandos e subcomandos mencionados, com
   sintaxe exata e exemplos (list, ask, check, note, portal, role, notify e outros).
3. PORTAIS DE DISPOSITIVO — prioridade alta: como criar simulador iOS / emulador Android /
   aparelho físico; e QUALQUER pista do JSON de um portal de dispositivo numa partitura
   exportada (as chaves de `surface` e `source`, se aparecerem num export compartilhado).
   Verbos de `maestri portal` para dispositivo (tap, type, swipe, button, launch/terminate).
4. ANDARES (floors): detalhes de hooks (Setup/Run/Teardown), variáveis de ambiente
   disponíveis, comportamento de Land, diferenças macOS vs Windows.
5. Partituras: dicas de importação/exportação, o pacote plural (.maestripartituras),
   pegadinhas de segurança, e como a comunidade organiza bibliotecas de partituras.
6. Ombro, Batuta, Rotinas, Ambientes, Maestri Wire/Remote: qualquer detalhe além da doc.
7. Requisitos e limitações (versão de macOS, Apple Silicon, Xcode para simulador, etc.).
8. FAQ e problemas comuns com as soluções que a equipe deu.
9. Recursos não documentados, atalhos escondidos e boas práticas repetidas pela comunidade.

VALIDAÇÃO CONTRA O GUIA (se você tiver acesso aos arquivos do repositório em
`/Users/coutinho/Documents/GitHub/guiadomaestri`, leia docs/, partituras/ e scripts/;
senão, valide contra o seu conhecimento do que o guia afirma)
Confirme, corrija ou marque como "não encontrado" cada um destes pontos:
- A lista de comandos seguros da CLI (list/ask/check/note/portal/role assign/notify) e a
  sintaxe de cada um.
- Os atalhos de teclado de macOS listados em docs/03-atalhos.md.
- O formato .maestripartitura de docs/04 (chaves de topo, payload, terminal/stickyNote/
  portal, roles, ropePoints com 21 pontos).
- O JSON de um portal de DISPOSITIVO (docs/09 assume provisório) — este é o ponto mais
  importante a confirmar.
- Detalhes dos andares e hooks (docs/06 e docs/08).
- Requisitos do Ombro e do Wire (docs/01).
- A política de modelos (fable/opus/codex/gemini) — é uma convenção deste guia, não do app;
  confirme se a comunidade descreve algo diferente.

FORMATO DO RELATÓRIO (entregue em Markdown, em pt-BR)
1. Resumo executivo (5-10 linhas): o que mudou/importa, e as maiores divergências achadas.
2. Mapa de canais: tabela (canal | propósito | acesso).
3. Achados por tema (um bloco por item de "O QUE EXTRAIR"), com [OFICIAL]/[COMUNIDADE] e
   fonte (canal + data) em cada afirmação.
4. Tabela de validação: | Afirmação do guia | Veredito (Confirma / Corrige / Não encontrado)
   | Evidência (canal + data) | Correção sugerida |.
5. Lista priorizada de correções a fazer no repositório (arquivo + o que mudar).
6. Perguntas em aberto que só a equipe do Maestri pode responder (para eu perguntar depois).

Comece listando os canais que você consegue ver e o plano de varredura. Depois execute.
```

---

## Depois do relatório

- Aplique as correções priorizadas nos arquivos de `docs/` e, se o JSON do portal de
  dispositivo for confirmado, ajuste `scripts/maestri_build.py` (`device_portal()`) e gere
  as partituras de mobile com portal nativo.
- Rerode a validação: `python3 scripts/generate_partituras.py && python3 tests/validate_partituras.py`.
- Guarde as "perguntas em aberto" para levar à equipe do Maestri (canal de suporte ou docs).
