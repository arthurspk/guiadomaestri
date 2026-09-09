# 11 · Dicas

Dicas práticas para tirar mais do Maestri no dia a dia. São atalhos de raciocínio e hábitos
que economizam tempo — para os conceitos, veja [01-conceitos.md](01-conceitos.md); para o
fluxo completo, [06-maestri-no-dia-a-dia.md](06-maestri-no-dia-a-dia.md).

---

## Reger o time

- **Fale objetivo, não tarefa micro.** Diga ao maestro "entregue a busca com filtros",
  não "crie o arquivo X". Ele escreve o contrato e delega; você rege.
- **Comece pelo prompt inicial.** Cole o [prompt inicial](../prompts/prompt-inicial.md) na
  primeira mensagem do maestro para ele se organizar antes de sair implementando.
- **Deixe o contrato ser a verdade.** Quando o board e a realidade discordam, conserte o
  board. É a nota que manda, não o chat do terminal.
- **Uma pergunta vale mais que um palpite.** Ambiguidade de contrato vai ao Arquiteto; de
  produto, ao Maestro. Errar cedo custa o time inteiro.
- **Não deixe dois agentes donos do mesmo arquivo.** A posse vem do contrato; conflito de
  posse é problema de contrato, não de merge.

## Andares (Floors)

- **Todo trabalho de risco merece um andar.** Feature grande, refactor, upgrade — isole
  numa branch própria e faça **Land** quando o veredito for verde.
- **Nomeie por tipo/assunto:** `feat/busca`, `fix/login`, `chore/upgrade-node`. Fica fácil
  achar na visão geral (`Ctrl⇧\`).
- **Automatize com hooks.** Um hook de Setup que roda `install` e sobe o dev server deixa o
  andar pronto para o warden verificar no portal. Veja [receitas/hooks](../receitas/hooks/).
- **Compare abordagens em andares paralelos.** Casa bem com a partitura Duelo de Agentes:
  um andar por abordagem, Land só do vencedor.

## Portais

- **Prove, não afirme.** O warden aceita uma feature percorrendo o fluxo real no portal,
  não lendo o código. "Nunca alegue verificação que você não viu."
- **Use o portal para o mundo externo também:** abrir um concorrente, ler um dashboard,
  conferir uma landing publicada. Não é só localhost.
- **Mobile nativo entra no app.** O portal de dispositivo (simulador iOS / emulador
  Android) você adiciona pelo Maestri (New Portal → Devices) e conecta ao QA. Veja
  [docs/09](09-portais-mobile-web-emulador.md).
- **Portais ligados compartilham sessão.** Útil para fluxos que precisam de login em várias
  telas.

## Notas

- **Mova para o repo o que deve viver no git.** "Mover para…" grava a nota como `.md` no
  projeto; ótimo para specs e ADRs.
- **Encadeie notas** em mapa mental: um índice que aponta para contrato, decisões e
  findings, e o agente percorre a cadeia.
- **Reaproveite os templates.** Contrato, workboard, playbook, stack-checklist e mais estão
  prontos em [notas/](../notas/README.md) para arrastar ao canvas.

## Rotinas

- **Deixe o repetitivo rodar sozinho:** guardião de CI, vigia de deploy, clipping de
  concorrência, fechamento diário, triagem de tickets. Receitas em
  [receitas/rotinas.md](../receitas/rotinas.md).
- **Encadeie com `&&`:** `puxe a main && rode os testes && resuma na nota "diário"`.
- **A rotina propõe, você aprova.** Para ações que afetam terceiros (responder cliente,
  publicar), exija aprovação humana via `maestri notify`.

## Modelos e custo

- **Fable rege, Opus executa, Codex/Gemini contestam.** Misturar modelos de propósito pega
  erros que um segundo passe do mesmo modelo repetiria.
- **Ajuste a cerimônia à tarefa.** Um typo você resolve sozinho; um caminho crítico passa
  pelo loop completo (contrato → build → warden).
- **Guarde `--dangerously-skip-permissions` para diretórios em que você confia** — de
  preferência isolados (um andar, um clone, um container).

## Segurança

- **Leia os comandos antes de importar** uma partitura; ela sobe terminais e executa na sua
  máquina. Só aceite de fontes confiáveis.
- **Red team só em escopo autorizado**, nunca em produção, nunca com dados de pessoas reais.
- **Domínio financeiro tem regra de corte.** Fatia que toca dinheiro, identidade ou segredo
  não fica pronta sem as camadas críticas da stack-checklist avaliadas com evidência.

## Atalhos que valem ouro

- `Ctrl⇧A` — pula para o próximo terminal pedindo atenção. Seu "inbox" de decisões.
- `AltCtrlA` — lista todos os terminais aguardando, em todos os andares.
- `Ctrl+P` — Batuta Search: busca até dentro do corpo das notas, e faz "Nova Partitura a
  partir da seleção".
- `Ctrl⇧O` — Ombro: "o que os agentes fizeram enquanto eu estava fora?".
- Veja a lista completa em [03-atalhos.md](03-atalhos.md).

## Partituras

- **Salve o seu arranjo.** Depois de ajustar uma partitura (modelos, contrato, portais),
  salve como a sua própria com `Ctrl+P` → "Nova Partitura a partir da seleção".
- **Comece de uma pronta.** O [catálogo por área](../partituras/CATALOGO.md) quase sempre
  tem um ponto de partida melhor que o zero.
- **Reaproveite papéis.** A [biblioteca de responsabilidades](../roles/CATALOGO.md) tem 30
  roles prontos para colar num terminal.

---

Volta ao [índice](../README.md).
