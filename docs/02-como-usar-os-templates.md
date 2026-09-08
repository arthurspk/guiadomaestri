# 02 · Como usar os templates

As 212 partituras deste guia estão em
[`partituras/tecnologia/`](../partituras/tecnologia/CATALOGO.md). Cada uma é um time
pronto — terminais com responsabilidades, notas compartilhadas, portais de verificação e
conexões — que você **arrasta para o canvas do Maestri e começa a reger**.

> ⚠️ **Segurança primeiro.** Adicionar uma partitura ao canvas **inicia os terminais dela
> e executa os comandos na sua máquina** (`claude`, `codex`, `gemini`). Leia os comandos
> na tela de revisão antes de importar. As partituras de **Red Team** e qualquer
> engajamento ofensivo só operam em **escopo autorizado**, nunca em produção, nunca com
> dados de pessoas reais. Veja [05 · Modelos e segurança](05-modelos-e-seguranca.md).

---

## Importar

Você tem duas formas:

1. **Um template só.** Arraste o arquivo `<slug>.maestripartitura` para o canvas, ou dê
   duplo clique nele no Finder. A tela de revisão mostra o layout, as responsabilidades e
   os **comandos de partida** — confira antes de aceitar.
2. **O pacote inteiro.** No painel de **Partituras**, menu ⋯ → **Importar Partituras…** e
   escolha [`Tecnologia.maestripartituras`](../partituras/tecnologia/Tecnologia.maestripartituras).
   Isso adiciona as 212 de uma vez à sua biblioteca (a importação de pacote pula a tela
   individual de cada uma e aplica suas responsabilidades locais em conflitos de nome).

Atalho: `Ctrl⇧L` abre o painel de Partituras.

## O que uma partitura traz montado

- **Um Maestro central** (`--model fable`) conectado a todos os outros terminais —
  topologia estrela — com malha leve entre vizinhos.
- **Especialistas** (`--model opus`) e, onde faz sentido, **revisores adversariais**
  (`codex`/`gemini`), cada um com sua responsabilidade em pt-BR embutida.
- **Notas compartilhadas**: contrato (`feature-spec`/`contract`), `workboard`, e conforme
  a família `stack-checklist`, `release-findings`, `case-file`, `incident-timeline`,
  `rules-of-engagement`.
- **Um ou mais portais** para verificação viva, conectados ao Maestro e ao warden.

## Reger, na prática

1. **Ligue o runtime que a partitura pressupõe.** O Maestro é dono do runtime, mas ele
   sobe seu app de dev, não a partitura. Se a família espera algo em `http://localhost:...`,
   deixe seu projeto pronto para o Maestro subir (ele faz isso em background com log).
2. **Fale com o Maestro pelo Compositor de Prompts** (`Ctrl⇧P`). Diga o objetivo em
   linguagem natural: "implemente a busca com filtros na tela de pedidos". O Maestro roda
   `maestri list`, manda o Arquiteto escrever o contrato, delega fatias em paralelo e
   fecha pelo warden.
3. **Acompanhe pela atenção.** `Ctrl⇧A` pula para quem está pedindo decisão. O **Ombro**
   (`Ctrl⇧O`) resume o que cada agente fez.
4. **Deixe o warden verificar no portal.** "Achados, não correções": revisores reportam
   com evidência; correções só quando você aprova.

## Escolher a partitura certa

Consulte o [CATALOGO.md](../partituras/tecnologia/CATALOGO.md), organizado por família:

| Quero… | Família |
|---|---|
| Entregar uma feature ponta a ponta | **Ship Feature · \<stack\>** |
| Caçar um bug com método | **Depuração · \<stack\>** |
| Decidir se sobe ou não | **Portão de Release · \<stack\>** |
| Arrancar um projeto novo | **Scaffold · \<stack\>** |
| Validar SPA × BFF (contrato, CORS, cookie) | **Validação BFF · \<domínio\>** |
| Produto financeiro com 30 camadas de rigor | **Pipeline Completo · \<produto\>** |
| Infra, IaC, K8s, CI/CD | **Cloud & Infra**, **IaC**, **Kubernetes**, **CI/CD** |
| Banco, pipeline de dados | **Database**, **Data Pipeline** |
| Feature de IA com evals | **AI Feature** |
| Migração incremental e reversível | **Migração** |
| Mobile, acessibilidade, contrato de API, performance | **Ship Mobile**, **Acessibilidade**, **API Contract**, **Performance** |
| Documentação verificada contra o código | **Documentação** |
| Pentest (só escopo autorizado) | **Red Team** |
| Um especialista sozinho | **Solo** |
| Comparar modelos no mesmo problema | **Duelo de Agentes** |
| Responder a um incidente | **War Room** |

## Adaptar uma partitura

As partituras são ponto de partida, não camisa de força. Depois de importar:

- **Troque o comando** de um terminal (Editar → Detalhes) para mudar o modelo ou o agente.
- **Reatribua a responsabilidade** com o Maestro ou em Configurações → Agentes.
- **Edite as notas** de contrato para o seu domínio.
- **Aponte os portais** para as URLs reais do seu projeto.
- **Salve como sua própria partitura** (`Batuta Search` → "Nova Partitura a partir da
  seleção"), para reusar depois.

## Regerar os templates

Todos os arquivos são **gerados** pelo Python em [`scripts/`](../scripts/). Para
regenerar (por exemplo, depois de expandir um catálogo):

```bash
python3 scripts/generate_partituras.py     # grava 212 templates + pacote + CATALOGO.md
python3 tests/validate_partituras.py        # valida contra o formato oficial
```

Os UUIDs são determinísticos, então regenerar produz **os mesmos arquivos byte a byte** —
o repositório fica estável no git.

---

Próximo: [03 · Atalhos e comandos](03-atalhos.md).
