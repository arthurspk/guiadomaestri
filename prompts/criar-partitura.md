# Prompt · Criar uma partitura nova com o maestro

Prompt para colar no **maestro** (terminal `--model fable`) do Maestri quando você quer que
ele **monte um time e salve como partitura** para um objetivo seu, seguindo os princípios
deste guia.

## Como usar

1. Tenha um terminal maestro (isManager) rodando `claude --dangerously-skip-permissions --model fable`.
2. Cole o bloco abaixo no Compositor de Prompts (`Ctrl⇧P`), trocando `<OBJETIVO>`.
3. Ao final, salve o arranjo: `Ctrl+P` → "Nova Partitura a partir da seleção".

---

```text
Você é o maestro. Quero que você monte um time (uma "partitura") para este objetivo e o
deixe pronto para eu reger. NÃO comece a implementar ainda — primeiro monte o time e o
contrato.

OBJETIVO: <OBJETIVO — ex.: "validar a fronteira entre nossa SPA de checkout e o BFF">

Siga os princípios do Guia do Maestri:
- Topologia estrela: você no centro, conectado a todos; malha leve entre vizinhos.
- Contrato antes de código: recrute um Arquiteto para escrever o contrato numa nota
  compartilhada (feature-spec/contract) e as fatias num workboard, antes de qualquer build.
- Achados, não correções: recrute um warden/revisor que só reporta com evidência e verifica
  ao vivo num portal; nunca conserta sozinho.
- Política de modelos: você em fable; executores (arquiteto, builders, especialistas) em
  `--model opus`; revisão adversarial em `codex` (ou `gemini`).
- Nunca alegue verificação que você não viu.

Passos:
1. Rode `maestri list` para ver o que já existe.
2. Proponha o elenco: para cada terminal, diga nome, papel (responsabilidade), modelo/comando
   e a que ele se conecta (notas, portal). Justifique cada recruta por uma lacuna real.
3. Recrute os terminais, crie as notas compartilhadas (contrato, workboard, e o que a tarefa
   pedir: stack-checklist, release-findings, case-file, etc.) e conecte tudo.
4. Se for trabalho de UI ou web, crie um portal apontando para a URL que verificaremos.
5. Peça ao Arquiteto para escrever o contrato e as fatias; revise antes de mobilizar builders.
6. Pare e me mostre: o time montado, as conexões, e o contrato. Eu salvo como partitura e aí
   damos início.

Pergunte antes de assumir qualquer coisa ambígua sobre o objetivo.
```

---

Veja também a [biblioteca de responsabilidades](../roles/CATALOGO.md) para reaproveitar
prompts de papel prontos, e o [catálogo de partituras](../partituras/CATALOGO.md) para
partir de um time já montado em vez de criar do zero.
