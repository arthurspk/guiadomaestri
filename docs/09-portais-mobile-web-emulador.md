# 09 · Portais: web, mobile e emuladores

O **portal** é a janela embutida no canvas onde o trabalho vira **evidência**: um agente
conectado dirige um navegador ou um dispositivo pela CLI `maestri portal` e prova o que
aconteceu, em vez de adivinhar pelo código. Esta página cobre os **três tipos de alvo** —
web desktop, web mobile e **dispositivo (simulador iOS / emulador Android / aparelho
físico)** — e como colocar cada um nas suas partituras.

Fonte oficial: <https://www.themaestri.app/pt-br/docs/portals>.

---

## Os dois tipos de portal

O Maestri tem dois tipos de portal, e o segundo se desdobra em plataformas:

1. **Portal de Navegador** — instância isolada de WebKit (Safari; suporte a Chrome
   planejado), com armazenamento próprio. Serve para **web desktop** e **web mobile** (basta
   apontar para a URL certa e dimensionar como um telefone).
2. **Portal de Dispositivo** — um dispositivo de verdade no canvas:
   - **Simulador iOS** (apenas macOS com Xcode);
   - **Emulador Android** (macOS e Windows);
   - **Aparelho Android físico** conectado.

Ambos têm as **mesmas** capacidades de conexão e automação; muda o que o agente pode fazer
(clicar vs. tocar, teclado vs. botões físicos).

---

## O que o agente faz em cada um

Quando o portal está **conectado ao terminal** do agente, a automação acontece pela CLI
`maestri`, sem MCP nem configuração externa.

### Portal de navegador (web desktop e web mobile)
```bash
maestri portal navigate <url>     # navega para uma URL (voltar, atualizar)
maestri portal snapshot           # captura o estado da página (refs de elementos)
maestri portal click <ref>        # clica (prefira refs de snapshot a coordenadas)
maestri portal fill <ref> "<txt>" # preenche um campo
maestri portal key "<tecla>"      # envia uma tecla
maestri portal screenshot         # screenshot
```
O agente também lê o DOM, vê o console do navegador e roda JavaScript.

### Portal de dispositivo (simulador / emulador / aparelho)
O agente **toca, digita, rola e desliza**, **pressiona botões físicos** (home, lock, side,
back, recents), **inicia e encerra apps** por identificador (bundle id / package),
**abre URLs** pelo handler nativo, **lê a árvore de elementos** (inclusive web views
embutidas), tira **screenshots** e **liga/desliga** o dispositivo. Na prática, os mesmos
verbos de verificação viva (`snapshot`/`screenshot`/`tap`/`type`), agora no app nativo.

> A CLI `maestri portal` é a mesma superfície; os verbos exatos para dispositivo (tap,
> swipe, button, launch/terminate app) aparecem quando um portal de dispositivo está
> conectado. Onde a sintaxe exata importar, confirme na doc oficial — e veja o
> [prompt de validação do Discord](../prompts/validar-discord-maestri.md), que inclui
> "confirmar os verbos de `maestri portal` para dispositivo" como tarefa.

---

## Como colocar cada tipo numa partitura

### Web desktop
É o padrão das partituras deste guia. Já vem montado: um portal apontando para
`http://localhost:5173` (ou a porta da família), conectado ao Maestro e ao warden. Para
usar, aponte para a URL real do seu app (Editar o portal → URL, ou `maestri portal edit`).

### Web mobile
Duas formas:
- **No app:** crie um portal de navegador (`P` ou botão Portal), aponte para a URL mobile e
  **redimensione** o frame para proporção de telefone (estreito e alto). A família
  **Ship Mobile** já entrega um portal "App (web mobile)" assim.
- **No gerador:** um portal de navegador com frame estreito. Exemplo:
  ```python
  p.portal("App (web mobile)", "http://localhost:19000", x=-1400, y=-1100, w=520, h=1080)
  ```

### Dispositivo (simulador iOS / emulador Android / aparelho físico)

**No app (caminho recomendado e garantido):**
1. Abra **New Portal** e alterne para **Devices** — ou use a ação **@New Device Portal** no
   Compositor de Prompts.
2. Escolha a plataforma (simulador iOS, emulador Android ou aparelho conectado) e o
   dispositivo.
3. **Conecte o portal ao terminal** do agente que vai verificar (ferramenta de conexão ou
   `Ctrl+L`). Pronto: o QA mobile dirige o app nativo pela CLI.
4. **Salve como sua partitura** (`Ctrl+P` → "Nova Partitura a partir da seleção") para
   reusar o arranjo com o portal de dispositivo já incluído.

> ⚠️ Uma partitura **não** captura configs de runtime nem caminhos absolutos; um portal de
> dispositivo salvo numa partitura guarda o tipo e o alvo, mas o simulador/emulador precisa
> existir na máquina que importa. Simuladores iOS exigem macOS + Xcode.

**No gerador (avançado):** ver a seção abaixo.

---

## Gerar partituras com portal de dispositivo

Aqui vale a honestidade técnica: as partituras **oficiais** que usei para calibrar o
formato só contêm **portais de navegador** (`surface: {"browser": {}}`). O JSON exato de um
**portal de dispositivo** não está entre os exemplos oficiais, então o gerador **não emite
portais de dispositivo por padrão** — assim as 257 partituras continuam importando de forma
garantida e a validação segue byte-estável. Há dois caminhos para incluí-los:

### Caminho A — verbatim de um export real (100% confiável)
1. No Maestri, monte a partitura com o portal de dispositivo que você quer e **exporte**
   (arraste o card para o Finder, ou "Salvar em…").
2. Abra o `.maestripartitura`, localize o **nó do portal** (em `payload.nodes`, o objeto
   cujo `content` tem a chave `portal`).
3. Passe esse nó verbatim para o gerador com o helper `raw_portal`:
   ```python
   import json
   from maestri_build import Partitura, CMD_OPUS

   device_node = json.load(open("meu-export.maestripartitura"))["payload"]["nodes"][N]
   p = Partitura("Ship Mobile · iOS nativo", "…")
   # … monte terminais e notas …
   qa = p.terminal("Argus · QA", role="…", command=CMD_OPUS)
   pid = p.raw_portal(device_node, x=-1400, y=-1100)   # insere o portal exatamente como exportado
   p.connect_portal(pid, qa)
   ```
   Como o nó vem de um export real do seu Maestri, o schema é o correto para a sua versão.

### Caminho B — `device_portal()` (provisório, a confirmar)
O builder tem um helper de conveniência:
```python
pid = p.device_portal("iPhone 16", platform="ios_simulator",
                      device="iPhone 16", app_bundle_id="com.acme.app",
                      x=-1400, y=-1100)
p.connect_portal(pid, qa)
```
Ele produz uma estrutura **best-effort** seguindo o padrão de união etiquetada do formato
(`surface: {"device": {}}`, `source: {"device": {"_0": {…}}}`). **Ainda não confirmada**
contra um export oficial — por isso não é usada nas partituras geradas. Use o Caminho A
quando puder; use o B como ponto de partida e **confirme com um export real** (ou pela
[validação do Discord](../prompts/validar-discord-maestri.md)) antes de distribuir.

---

## Padrão recomendado para a família Ship Mobile

1. Importe **Ship Mobile · \<plataforma\>** — já traz o time e o portal web-mobile.
2. Dentro de um **andar** (`feat/<feature>`) para isolar o build (veja
   [08-andares-e-partituras.md](08-andares-e-partituras.md)).
3. Adicione **no app** um portal de dispositivo (New Portal → Devices) e conecte ao
   terminal "Argus · QA/a11y".
4. Deixe o QA verificar o fluxo real no simulador/emulador (tap, type, screenshot) e a
   acessibilidade (VoiceOver/TalkBack), reportando achados — nunca "acho que funciona".
5. Salve como sua partitura para reusar com o portal de dispositivo embutido.

---

## Dica: portais que compartilham sessão

Portais podem ser **ligados entre si** (conexão portal↔portal) para compartilhar
armazenamento — cookies e estado de login. Útil quando o fluxo precisa de um usuário
autenticado em várias telas (ex.: um portal web logado e outro seguindo o mesmo fluxo), ou
para manter a sessão entre navegações. No gerador, use `p.link_portals(a_node, b_node)`.

---

Volta ao [índice](../README.md) · veja também
[08 · Andares + Partituras](08-andares-e-partituras.md) e
[06 · O Maestri no dia a dia](06-maestri-no-dia-a-dia.md).
