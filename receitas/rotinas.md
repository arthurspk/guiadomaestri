# ⏰ Receitas de Rotinas (Routines)

> **Rotinas** rodam um prompt nos seus agentes em intervalos definidos. Configure em
> **Arquivo → Rotinas → Nova Rotina**: escolha o terminal, cole o prompt, defina o
> intervalo. Encadeie passos com `&&` (o próximo só dispara quando o anterior termina).

Estas são **receitas** para copiar e colar. Não é um formato de arquivo importável; é o
texto do prompt e a cadência sugerida.

---

## Dev — guardião de CI
- **Terminal:** o maestro. **Intervalo:** a cada 30 min.
```
puxe as últimas mudanças da main
&&
rode a suíte de testes
&&
se algo falhou, abra um caso na nota "diario" com o erro e me notifique com maestri notify
```

## SRE — vigia de deploy
- **Terminal:** um especialista de plataforma com portal conectado. **Intervalo:** 5 min.
```
navegue no portal até o endpoint de health de produção
&&
registre status e latência na nota "status" com carimbo de hora
&&
se estiver fora do ar ou lento, me notifique
```

## Marketing / Produto — clipping de concorrência
- **Terminal:** um pesquisador com portal. **Intervalo:** toda manhã (a cada 24h).
```
abra no portal os 3 sites concorrentes da nota "radar"
&&
resuma mudanças de preço, mensagem ou feature na nota "radar" com a data
```

## Financeiro — fechamento diário
- **Terminal:** um analista financeiro. **Intervalo:** fim do dia.
```
concilie os lançamentos de hoje
&&
aponte qualquer divergência na nota "fechamento", sem arredondar para fechar
```

## Suporte — triagem de tickets
- **Terminal:** um especialista de suporte. **Intervalo:** de hora em hora.
```
classifique os tickets novos por urgência
&&
proponha uma resposta para cada um na nota "triagem"
&&
não responda ao cliente sem aprovação humana; me notifique se algo for urgente
```

## Documentação — doc que não envelhece
- **Terminal:** um doc verifier. **Intervalo:** diário.
```
verifique as afirmações do README e da nota "api-reference" contra o código
&&
liste divergências na nota "doc-drift"
```

---

## Boas práticas
- Rotinas ativas mostram indicador visual; pause, edite ou apague sem perder a config.
- Deixe a rotina **reportar numa nota** (a fonte de verdade), não só no chat do terminal.
- Para ações que afetam terceiros (responder cliente, publicar), sempre exija aprovação
  humana via `maestri notify` — a rotina propõe, você aprova.
