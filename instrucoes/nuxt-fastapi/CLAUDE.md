# Instruções do projeto — Nuxt + FastAPI

> Este arquivo é entregue automaticamente aos agentes ao iniciarem neste workspace do
> Maestri. Ajuste ao seu projeto. O Maestri mantém `CLAUDE.md` e `AGENTS.md` sincronizados.

## Stack
- **Frontend:** Nuxt 4
- **Backend:** FastAPI (Python 3.14)

## Como trabalhar aqui
- Responda em pt-BR; mantenha código, identificadores, flags e nomes de arquivo em inglês.
- **Contrato antes de código:** leia a nota de contrato (`feature-spec`) e a sua fatia no
  `workboard` antes de escrever qualquer linha. Fique dentro das suas fronteiras de arquivo.
- **Nunca chute diante de ambiguidade:** dúvida de contrato vai ao Arquiteto, dúvida de
  produto vai ao Maestro (`maestri ask "<nome>" "<pergunta>"`).
- **Achados, não correções:** revisores só reportam, com evidência, e verificam ao vivo no
  portal. Nunca alegue verificação que você não viu.

## Comandos
```bash
# ajuste aos scripts reais do projeto
install:  <gerenciador> install
dev:      <cmd de dev>          # o Maestro é dono do runtime; suba em background com log
test:     <cmd de testes>
build:    <cmd de build>
lint:     <cmd de lint/format>
```

## Qualidade
- Sem `any` e sem cast que mente; trate estados de erro/loading/vazio.
- HTML semântico e acessibilidade real (teclado, foco, contraste).
- Sem refactor de carona fora da fatia; siga as convenções ao redor.

## Segurança
- Nada de segredo em texto claro no repo; use variáveis de ambiente.
- Valide entradas em toda fronteira de confiança.
- Trabalho que toca dinheiro, identidade ou dados sensíveis passa pelo revisor de segurança.
