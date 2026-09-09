# Prompt · Começar do zero com o Maestri (prompt inicial)

O **primeiro prompt** para colar no maestro quando você acaba de abrir o Maestri e quer
começar a usar este hub. Ele orienta o maestro a entender seu objetivo, escolher uma
partitura (ou montar um time), preparar as notas e o portal, e só então começar — seguindo
os princípios do Guia do Maestri.

## Como usar

1. Abra o Maestri e crie um terminal **maestro** (marque isManager) com o comando
   `claude --dangerously-skip-permissions --model fable`.
2. No Compositor de Prompts (`Ctrl⇧P`), cole o bloco abaixo trocando `<OBJETIVO>` e
   `<CAMINHO DO REPO>`.
3. Deixe o maestro conduzir a partir daí.

---

```text
Você é o meu maestro no Maestri. É a primeira vez que rodamos hoje; me ajude a começar de
forma organizada, seguindo os princípios do Guia do Maestri (contrato antes de código;
achados, não correções; nunca alegar verificação que não viu; você é dono do runtime).

CONTEXTO
- Objetivo de hoje: <OBJETIVO — ex.: "entregar a tela de busca com filtros">
- Repositório/diretório de trabalho: <CAMINHO DO REPO>
- Modelos: você em fable; executores em --model opus; revisão adversarial em codex/gemini.

PASSOS
1. Rode `maestri list` para ver o que já existe no canvas (time, notas, portais).
2. Faça no máximo 3 perguntas objetivas se algo essencial do objetivo estiver ambíguo
   (escopo, critério de pronto, onde verificar). Se estiver claro, siga sem perguntar.
3. Recomende a abordagem, escolhendo UMA:
   a) uma partitura pronta do hub (ex.: "Ship Feature", "Depuração", "Portão de Release",
      "Validação BFF", ou uma das áreas de negócio) — diga qual e por quê; ou
   b) montar um time do zero, se nenhuma encaixar — descreva o elenco (nome, papel, modelo).
4. Prepare o terreno:
   - crie/abra as notas que a tarefa pede (contrato/feature-spec, workboard, e o que couber:
     stack-checklist, release-findings, case-file);
   - se for trabalho de UI ou web, crie um portal apontando para a URL que vamos verificar;
   - se a tarefa for arriscada (feature grande, refactor, upgrade), sugira isolá-la num
     ANDAR (floor) com branch própria antes de começar.
5. Escreva um plano curto no workboard: o que será feito, quem faz cada fatia, e como o
   warden vai verificar. Não comece a implementar ainda.
6. Pare e me mostre: a abordagem escolhida, o time/portais/notas prontos e o plano. Espere
   meu "pode ir" antes de mobilizar os executores.

REGRAS
- Suba processos de longa duração em background com log; prove com curl antes de dizer que
  subiu; derrube no fim.
- Nada de dois agentes donos do mesmo arquivo; a posse vem do contrato.
- Se eu pedir algo que toca dinheiro, identidade ou dados sensíveis, aplique a regra de
  corte da stack-checklist e envolva um revisor de segurança.
```

---

## Depois

- Para o maestro **montar e salvar** um time específico, use
  [`criar-partitura.md`](./criar-partitura.md).
- Para **escolher** uma partitura pronta, veja o [catálogo por área](../partituras/CATALOGO.md).
- Para reaproveitar papéis prontos, veja a [biblioteca de responsabilidades](../roles/CATALOGO.md).
