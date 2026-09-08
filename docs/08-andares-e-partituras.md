# 08 · Andares + Partituras (receitas)

Os **andares** (floors) e as **partituras** foram feitos um para o outro. A partitura te dá
um **time montado**; o andar te dá um **espaço isolado com branch própria** para esse time
trabalhar sem sujar o resto. Juntos, você toca várias frentes em paralelo, cada uma com
seu time, sua branch e seu runtime — e integra quando estiver pronto.

Esta página é de **receitas**: padrões concretos de andar + partitura. Para os conceitos,
veja [01-conceitos.md](01-conceitos.md#andares-floors); para o dia a dia geral,
[06-maestri-no-dia-a-dia.md](06-maestri-no-dia-a-dia.md).

---

## Por que combinar os dois

- Uma partitura importada **no térreo** (ground floor) age sobre a branch atual do seu
  working tree. Bom para trabalho pequeno e de baixo risco.
- Uma partitura importada **dentro de um andar** age sobre uma **cópia isolada** com branch
  própria. O térreo continua estável; o time do andar pode quebrar, experimentar e refazer
  à vontade. Quando o veredito é verde, você faz **Land** e leva os commits de volta.

Regra prática: **todo trabalho que muda código de forma não trivial merece um andar.** Bug
crítico, feature nova, refactor, upgrade, spike — cada um no seu andar, com o time certo.

---

## A receita base (o padrão que você repete)

1. **Crie o andar.** Botão de andar (canto inferior direito) → nomeie com o padrão
   `tipo/assunto` (ex.: `feat/busca-filtros`, `fix/login-timeout`, `chore/upgrade-node`) →
   escolha branch nova → **opcionalmente clone o layout do térreo**.
2. **Configure o hook de Setup** (ícone ⚡) para preparar o ambiente e subir o app:
   ```bash
   cd "$MAESTRI_FLOOR_PATH" && npm ci && npm run dev > /tmp/dev-$MAESTRI_FLOOR_NAME.log 2>&1 &
   ```
   O Maestro é dono do runtime, mas o hook garante que o app já suba junto com o andar.
3. **Importe a partitura certa dentro do andar.** O time inteiro nasce isolado naquela
   branch. Veja o [catálogo por área](../partituras/CATALOGO.md).
4. **Briefe o Maestro** (`Ctrl⇧P`) com o objetivo. Ele lê a nota de contrato/briefing,
   delega em paralelo e fecha pelo warden/revisor no portal.
5. **Land.** Quando o veredito é verde, **Land** → escolha a branch de destino → confira o
   preview de diff e conflitos → integre.
6. **Apague o andar** (mantendo ou não a branch) quando terminar.

> Os hooks recebem `$MAESTRI_FLOOR_NAME`, `$MAESTRI_BRANCH_NAME`, `$MAESTRI_FLOOR_PATH`,
> `$MAESTRI_ROOT_PATH`, `$MAESTRI_PROJECT_NAME`. Use o **Teardown** para limpar (derrubar o
> dev server, apagar `/tmp/dev-…log`).

---

## Receitas por situação

### 🚢 Feature nova sem travar o resto
- **Andar:** `feat/<assunto>` (branch nova a partir de `main`).
- **Partitura:** **Ship Feature · \<sua stack\>**.
- **Fluxo:** hook de Setup sobe o app → o arquiteto escreve o contrato → dois
  implementadores tocam fatias em paralelo → o warden verifica no portal → **Land** na
  `main` quando passa. O térreo continua entregando enquanto isso.

### 🐞 Hotfix em produção em paralelo ao trabalho normal
- **Andares:** deixe o térreo no que estava; crie `fix/<bug>` a partir da branch de
  produção (ou tag).
- **Partitura:** **Depuração · \<stack\>**.
- **Fluxo:** o Reprodutor prova o bug no portal do andar → causa raiz → menor conserto →
  verificação independente → **Land** direto na branch de release. Você não perdeu o
  contexto do que fazia no térreo.

### 🔧 Upgrade ou migração arriscada
- **Andar:** `chore/upgrade-<x>` (ex.: Node 22→24, Angular v17→v22, Postgres major).
- **Partitura:** família **Migração · \<tipo\>**.
- **Por que o andar é essencial:** o novo runtime fica confinado ao andar; se der ruim,
  você apaga o andar e a branch e nada vaza para o térreo. O verificador de paridade prova
  que o comportamento não regrediu antes do **Land**.
- **Hook de Setup** aqui costuma instalar a versão nova (ex.: `fnm use 24 && npm ci`).

### ✅ Revisar o PR de um colega sem largar o seu trabalho
- **Andar:** crie a partir da **branch do PR** (branch existente).
- **Partitura:** **Portão de Release · \<stack\>**.
- **Fluxo:** os quatro revisores (qualidade, segurança, correção, UX/a11y) analisam a
  branch do PR isolada; o Conductor dá o veredito. Você comenta no PR com base em evidência,
  sem misturar com o seu working tree.

### ⚔️ Comparar duas abordagens (um andar por abordagem)
- **Andares:** `spike/abordagem-a` e `spike/abordagem-b`, ambos a partir de `main`.
- **Partitura:** **Duelo de Agentes · \<problema\>** — ou rode a mesma **Ship Feature** em
  cada andar com uma diretriz diferente.
- **Fluxo:** cada abordagem evolui isolada; você compara os dois pelo portal e pelos
  testes, e faz **Land** só do vencedor. O perdedor é descartado apagando o andar.

### 🏗️ Arrancar um projeto/serviço novo dentro do monorepo
- **Andar:** `feat/<novo-servico>`.
- **Partitura:** **Scaffold · \<stack\>**.
- **Fluxo:** o esqueleto, as ferramentas e o vertical slice nascem no andar; o warden prova
  que `install/build/test/dev` rodam antes do **Land**.

### 🚨 Incidente: war room no térreo, correção no andar
- **Térreo:** **War Room · \<tipo de incidente\>** coordena a resposta (timeline, mitigação,
  comunicação) — não mexe no código.
- **Andar:** `fix/incidente-<data>` recebe a **Depuração** ou o conserto propriamente dito.
- **Por quê:** separa "coordenar a resposta" de "mexer no código", e o conserto fica
  isolado até ser verificado.

---

## Padrões multi-andar

- **Um andar por frente de trabalho ativa.** Feature da semana, hotfix, spike de pesquisa —
  cada um com seu time. `Ctrl⇧\` abre a visão geral dos andares; `↑`/`↓` percorre.
- **`AltCtrlA`** lista todos os terminais aguardando atenção **em todos os andares** — o seu
  inbox de decisões, não importa em qual andar o agente parou.
- **Não faça Land de dois andares no mesmo arquivo sem conferir.** A posse de arquivos vem
  do contrato de cada partitura; entre andares, o preview de diff/conflito do **Land** é a
  sua rede de segurança. Aterrisse um, reveja, aterrisse o outro.
- **Térreo estável, andares experimentais.** Mantenha o térreo na branch que você não pode
  quebrar; toda experimentação vive em andar.

---

## Hooks: deixe o andar se preparar sozinho

Três hooks (ícone ⚡ ao lado do botão de andar):

| Hook | Quando roda | Bom para |
|---|---|---|
| **Setup** | ao criar o andar (pode ser automático) | `npm ci`, subir o dev server, semear banco |
| **Run** | sob demanda | rodar a suíte, um build, um seed pesado |
| **Teardown** | ao apagar o andar | derrubar processos, limpar `/tmp`, dropar banco de teste |

Exemplo de Setup para uma partitura **Ship Feature** com portal em `localhost:5173`:
```bash
cd "$MAESTRI_FLOOR_PATH"
npm ci
npm run dev > "/tmp/dev-$MAESTRI_FLOOR_NAME.log" 2>&1 &
# o warden da partitura vai verificar em http://localhost:5173 pelo portal
```
Teardown correspondente:
```bash
pkill -f "$MAESTRI_FLOOR_PATH" 2>/dev/null || true
rm -f "/tmp/dev-$MAESTRI_FLOOR_NAME.log"
```

> Requisitos dos andares: volume APFS (padrão no macOS) e repositório git inicializado. No
> Windows, os andares usam branches git isoladas em vez do clone APFS.

---

## Salvar seu próprio combo

Depois de ajustar uma partitura dentro de um andar (trocou modelos, editou o contrato,
apontou portais para as suas URLs), **salve como sua própria partitura**: `Ctrl+P` →
"Nova Partitura a partir da seleção". Da próxima vez, é um arranjo só seu, pronto para
cair em qualquer andar novo.

---

Próximo: [09 · Portais: web, mobile e emuladores](09-portais-mobile-web-emulador.md).
