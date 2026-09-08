# Release Readiness Playbook

## Missão
Verificar o trabalho antes de subir. Revisores reportam achados, o Conductor decide,
correções acontecem só quando o usuário pede.

## Escala de severidade
- BLOCKER: consertar antes do release. Buracos de segurança, perda de dados, fluxos core
  quebrados, falhas duras de acessibilidade em caminhos críticos.
- MAJOR: deveria consertar. Subir com isso é decisão consciente, não acidente.
- MINOR: problema real, não bloqueia o release.
- NIT: polimento, estilo, gosto.

## Formato de achado
Uma linha por achado, dentro da sua seção de `release-findings`:
- [SEVERIDADE] caminho/arquivo:linha - o que está errado. Correção sugerida.

## Vereditos
Cada revisor termina com exatamente um: SHIP, SHIP WITH NITS, NEEDS WORK, DO NOT SHIP.
