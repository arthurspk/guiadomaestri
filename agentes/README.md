# 🎭 Agentes — arquétipos de responsabilidade e elenco

Uma **responsabilidade** (role) é o prompt que define o papel de um terminal: quem ele é,
o que faz, o que **não** faz, e como se comunica com o time pela CLI `maestri`. Neste guia
os prompts são gerados por [`scripts/roles_lib.py`](../scripts/roles_lib.py), em pt-BR,
segunda pessoa, no estilo das partituras oficiais do Maestri.

As 257 partituras usam **102 responsabilidades distintas**, montadas a partir de um punhado
de **arquétipos** parametrizados. Entender os arquétipos é entender qualquer partitura do
catálogo. Os arquétipos de tecnologia estão descritos abaixo; as áreas de negócio (design,
produto, marketing, vendas, dados, segurança, financeiro, jurídico, suporte, gestão,
pesquisa) usam um conjunto genérico paralelo — **Maestro de área**, **Estrategista**
(equivalente ao arquiteto, escreve o briefing), **especialistas** e **Revisor**
(achados-não-correções, verificação viva no portal) — com a mesma filosofia sem pressupor
código. Veja [docs/07 · Áreas e agentes](../docs/07-areas-e-agentes.md) para o mapa
completo e como reaproveitar agentes de catálogos externos como o agency-agents.

---

## Princípios que atravessam todo mundo

Estão embutidos nos prompts, herdados das partituras oficiais (Ship Goats, Slop Haters,
Money Send, KYC, The Bug is on the Canvas):

1. **Contrato antes de código.** O arquiteto escreve o contrato numa nota antes de
   qualquer implementação; ninguém constrói contra um contrato velho.
2. **Achados, não correções.** Wardens e revisores só reportam, com evidência, e verificam
   ao vivo no portal. Correção é engajamento separado, só com aprovação do usuário.
3. **Nunca alegue verificação que você não viu.** Checagem não feita é reportada como não
   verificada.
4. **Peça de volta em vez de chutar.** Dúvida de contrato vai ao Arquiteto; de produto, ao
   Maestro. Uma pergunta custa um minuto; um palpite errado custa o time.
5. **O Maestro é dono do runtime.** Só ele sobe servidores, em background com log.

---

## Arquétipos

### 🎼 Maestros e orquestradores
O ponto único de contato do usuário. Transforma um pedido em trabalho pronto e verificado:
esclarece a intenção, roda `maestri list`, faz o Arquiteto escrever o contrato, delega
fatias em paralelo com `maestri ask --batch`, acompanha com `maestri check`, fecha pelo
warden e reporta com evidência. Sobe em **`--model fable`**. Variantes:
`maestro()`, `orchestrator_generic()`, `release_conductor()`, `debug_maestro()`,
`incident_commander()`, `judge()`, `redteam_lead()`.

### 📐 Arquiteto de contrato
Quebra um objetivo em fatias independentes, define interfaces compartilhadas exatas, posse
de arquivos (todo arquivo pertence a exatamente uma fatia) e critério de pronto por fatia.
Projeta e coordena; **não edita código-fonte**. `architect()`.

### 🔨 Implementadores e especialistas
Constroem exatamente uma fatia por vez, presos ao contrato. Ficam dentro das fronteiras de
arquivo, batem o contrato exatamente, escrevem com qualidade (sem `any`, a11y real, estados
de erro). Sobem em **`--model opus`**. `implementer()`, `specialist()`, `solo_specialist()`,
`platform_engineer()`.

### 🛡️ Wardens e revisores adversariais
A defesa contra drift e defeito. Revisam contra o contrato, checam drift entre fatias,
qualidade e segurança, e **verificam vivo no portal**. Só achados, com evidência. As raias
de release rodam em **`codex`/`gemini`** de propósito. `warden()`,
`code_quality_reviewer()`, `security_reviewer()`, `correctness_verifier()`,
`ux_a11y_reviewer()`.

### 🐞 Time de depuração
Método científico contra bugs: **Reprodutor** (repro determinística),
**Analista de Causa Raiz** (o porquê, com prova — arquivo, linha, mecanismo),
**Engenheiro de Correção** (menor conserto correto para causa confirmada) e
**Verificador** (cético, tenta quebrar a correção, dirige o portal). Nenhum conserto está
pronto na palavra do próprio autor. `bug_reproducer()`, `root_cause_analyst()`,
`fix_engineer()`, `fix_verifier()`.

### 🚨 War room
**Comandante de Incidente** (organiza, não conserta), **Investigador** (o que quebrou, com
evidência), **Engenheiro de Mitigação** (para o sangramento agora, mesmo que feio) e
**Líder de Comunicação** (informa quem precisa saber). Mitigar primeiro, causa raiz depois,
post-mortem sem culpa. `incident_commander()`, mais especialistas.

### ⚔️ Duelistas e Juiz
Três modelos atacam o mesmo problema em paralelo, sem espiar um ao outro; o **Juiz**
escolhe, combina e entrega. `duelist()`, `judge()`.

### 🔴 Red team (só escopo autorizado)
**Lead**, **operadores** de recon e validação, **analista de relatório**. Salvaguardas
duras: só escopo autorizado por escrito na nota `rules-of-engagement`, nunca produção,
nunca dados reais, achados com evidência e remediação — nunca dano. `redteam_lead()`,
`redteam_operator()`. Veja [docs/05](../docs/05-modelos-e-seguranca.md).

---

## Elenco de especialistas

Os arquétipos acima se especializam por catálogo. O elenco recorrente:

- **Frontend / Backend / Full-stack builder** — fatias de UI e de API presas ao contrato.
- **Setup / Skeleton engineer** — ferramentas, lint, CI mínima, vertical slice (Scaffold).
- **Network & Compute / Data & Storage engineer** — infra em cloud (Cloud & Infra).
- **Module author / Policy engineer** — IaC com policy-as-code.
- **Schema & Migration / Query & Index tuner** — modelagem e performance de banco.
- **Ingestion / Data quality engineer** — pipelines de dados idempotentes.
- **AI engineer / Eval & Guardrails engineer** — features de IA medidas por eval.
- **Migration engineer / Parity verifier** — migrações reversíveis com paridade provada.
- **Mobile engineer / Mobile QA & a11y** — apps verificados no portal de dispositivo.
- **Pipeline / Release & Rollback engineer** — CI/CD seguro e com volta.
- **Platform / Cluster security engineer** — Kubernetes endurecido.
- **A11y engineer / Assistive tech verifier** — WCAG 2.2 AA verificado com AT real.
- **API designer / Contract test engineer** — contratos que não quebram consumidores.
- **Performance / Benchmark engineer** — ganho provado por número, sem regressão.
- **Doc writer / Doc verifier** — documentação conferida contra o código.
- **Solo specialist** — um especialista que planeja, executa e verifica sozinho.

---

## Reutilizar e customizar

Cada função de [`roles_lib.py`](../scripts/roles_lib.py) devolve uma string de prompt.
Para criar um papel novo, componha a partir dos blocos comuns (`SETUP`, `ASKBACK`,
`REPORT`, `NO_SERVERS`, `QUALITY`) ou use `specialist(title, focus, rules)` como molde.
Depois de importar uma partitura no Maestri, você também pode reatribuir responsabilidades
pelo Maestro ou em **Configurações → Agentes**.
