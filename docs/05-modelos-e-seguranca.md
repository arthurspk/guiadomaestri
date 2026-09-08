# 05 · Modelos e segurança

Duas decisões atravessam todas as 212 partituras: **qual modelo rege qual papel** e
**quais salvaguardas nunca são negociáveis**. Esta página explica as duas.

---

## Política de modelos

O princípio é simples: **Fable rege, Opus executa, Codex/Gemini contestam**.

| Papel | Comando de partida | Por quê |
|---|---|---|
| **Maestro / Orquestrador / Conductor / IC / Juiz / Lead** | `claude --dangerously-skip-permissions --model fable` | Orquestração: raciocínio sobre o todo, delegação, síntese. |
| **Arquiteto e executores** (builders, engenheiros, validadores) | `claude --dangerously-skip-permissions --model opus` | Execução: escrever contrato e código com profundidade. |
| **Revisão adversarial** (release, wardens de release, duelo) | `codex` | Um agente diferente pega o que o outro deixou passar. |
| **UX/a11y, docs, duelo** | `gemini` | Diversidade de modelo na verificação e nos duelos. |

Por que misturar modelos de propósito? Modelos distintos erram de formas distintas. Um
revisor `codex` sobre código escrito por `opus`, ou um `gemini` verificando
acessibilidade, encontra classes de problema que um segundo passe do mesmo modelo
tenderia a repetir. As partituras de **Duelo de Agentes** levam isso ao limite: o mesmo
problema vai para `claude`, `codex` e `gemini` em paralelo, e um Juiz fica com o melhor de
cada um.

> Sobre os modelos: **Fable 5.1** é o modelo generally-available mais capaz da Anthropic,
> da classe Mythos, acima de Opus em capacidade, com salvaguardas adicionais para
> capacidades dual-use. Aqui ele rege justamente por ser a inteligência de orquestração.
> Consulte a doc da Anthropic para IDs e disponibilidade atuais.

### `--dangerously-skip-permissions`

Todos os comandos `claude` das partituras usam `--dangerously-skip-permissions`. Isso faz
o agente **não pedir confirmação** a cada ação — necessário para um time autônomo tocar em
paralelo dentro do Maestri, mas é uma faca de dois gumes:

- Use em **repositórios e diretórios em que você confia**, idealmente isolados (um
  **Andar**/floor do Maestri, um clone, um container).
- **Não** aponte um time assim, sem supervisão, para segredos de produção ou para o seu
  home inteiro.
- O Maestro é instruído a subir processos de longa duração em **background com log** e a
  **derrubar tudo no fim** — mas a responsabilidade final de onde ele roda é sua.

## O domínio financeiro: a stack-checklist de 30 camadas

As partituras de **Pipeline Completo** para produtos que movem dinheiro (remessa,
carteira, marketplace, e-commerce, delivery, crédito) carregam a nota **`stack-checklist`**
com 30 camadas — do frontend à trilha de auditoria — e uma **regra de corte** explícita:

> Nenhuma fatia que toque **movimentação de dinheiro, identidade, segredo ou superfície
> pública** é considerada pronta sem as camadas **7, 8, 9, 10, 14, 27, 28, 29 e 30**
> avaliadas — verdes com evidência, ou com achado aberto e registrado. **Silêncio não
> conta como aprovação.**

Essas camadas são: autenticação e autorização (7), permissões e controle de acesso (8),
segurança e RLS (9), validação de dados (10), variáveis de ambiente e secrets (14),
idempotência e ledger financeiro (27), KYC/AML e triagem de sanções (28), precisão
monetária/FX/arredondamento (29) e trilha de auditoria e retenção (30). O **Stack Warden**
é dono da nota: uma camada só fica verde quando **ele viu a evidência**. Intenção não é
evidência.

## Princípios de segurança de processo

Herdados das partituras oficiais e embutidos nos prompts:

- **Achados, não correções.** Wardens e revisores só **reportam**, com evidência, e
  verificam ao vivo no portal. Nunca consertam sozinhos; correção é um engajamento
  separado, só depois que você aprova.
- **Nunca alegue verificação que você não viu.** Uma checagem que o agente não conseguiu
  fazer é reportada como *não verificada*, nunca liberada no chute.
- **Contrato antes de código.** O arquiteto escreve o contrato numa nota antes de qualquer
  implementação, para o trabalho paralelo não se distanciar.
- **O Maestro é dono do runtime.** Só ele sobe servidores — uma vez, num lugar só, em
  background com log — para nada colidir em porta.

## Red team: somente escopo autorizado

As partituras de **Red Team** e qualquer engajamento ofensivo carregam salvaguardas
**duras**, escritas no prompt de cada operador e na nota `rules-of-engagement`:

- **Só escopo autorizado por escrito.** Sem a nota `rules-of-engagement` preenchida e
  confirmada — alvo, janela, técnicas permitidas, contato do cliente — o time **não
  começa**; pergunta ao Lead via `maestri notify`.
- **Nunca produção. Nunca dados de pessoas reais.** Só contas e dados sintéticos de teste;
  nenhum dado pessoal real em evidência ou log.
- **Achados com evidência, não dano.** Prova de conceito mínima que demonstra a falha, com
  passos de reprodução e remediação sugerida — nunca exploit weaponizado pronto para uso
  malicioso, sem exfiltração, sem persistência, sem pivô além do combinado.
- **Escalonamento imediato** se o operador encontrar comprometimento ativo por terceiro ou
  dado sensível real exposto: para, escala ao Lead e ao contato do cliente.

Isso está alinhado ao uso defensivo e a testes de segurança **autorizados**. Fora desse
enquadramento — produção, dados reais, alvos sem autorização — as partituras não devem ser
usadas, e os prompts instruem os agentes a recusar.

## Segurança ao importar partituras

Vale para qualquer partitura, não só as deste guia:

- Adicionar uma partitura **sobe os terminais dela e executa comandos na sua máquina**.
  **Leia os comandos** na tela de revisão antes de importar.
- Só aceite partituras de **fontes confiáveis**. A importação de um **pacote**
  `.maestripartituras` pula a tela individual de cada template e aplica suas
  responsabilidades locais em conflitos de nome.
- As partituras deste repositório usam `claude`, `codex` e `gemini` — os agentes que o
  Maestri espera já instalados. Se você não tem um deles, o terminal correspondente
  simplesmente não sobe o agente.

---

Volta ao [índice](../README.md) · veja também os
[arquétipos de responsabilidade](../agentes/README.md).
