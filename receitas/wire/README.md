# 🔌 Integrações Maestri Wire

> **Maestri Wire** é o protocolo (TCP 7434, HTTPS/WSS) que deixa outros dispositivos e
> ferramentas falarem com um host Maestri — a base do Maestri Remote e de integrações
> customizadas. Doc oficial: <https://www.themaestri.app/pt-br/docs/wire>.

## Cliente de exemplo

[`maestri_wire_client.py`](./maestri_wire_client.py) — cliente mínimo em Python (stdlib) que
pareia um dispositivo, lista workspaces e envia um prompt a um terminal.

```bash
# 1) descubra e confirme o fingerprint do host (uma vez, por canal confiável)
python3 maestri_wire_client.py fingerprint 192.168.0.10

# 2) pareie com o código de 6 dígitos que o Maestri mostra (válido 5 min)
python3 maestri_wire_client.py pair 192.168.0.10 483920 "Meu Cliente" --pin <sha256>
#    → devolve {"token": "...", "role": "owner"}

# 3) use o token nas chamadas seguintes
python3 maestri_wire_client.py list   192.168.0.10 <TOKEN> --pin <sha256>
python3 maestri_wire_client.py prompt 192.168.0.10 <TOKEN> <TERMINAL_ID> "rode os testes" --pin <sha256>
```

## Segurança (leia antes de usar)

- O certificado do host é **autoassinado**; a garantia vem do **pinning do SHA-256**, não de
  uma CA. O cliente **exige** o pin e valida o certificado do host contra ele antes de cada
  requisição. **Nunca** desligue a verificação TLS num uso real.
- Descubra o pin uma vez com `fingerprint`, confirme o valor com o dono do host, e reutilize.
- O token de dispositivo (64 hex) é um segredo: trate como senha, não commite.
- Use o papel **guest** (somente leitura) para dashboards e monitoramento; **owner** só onde
  precisa escrever.

## Ideias de integração

- **Notificações de atenção:** polling de `attentionCount` em `/api/workspaces` para alertar
  quando um agente precisa de você.
- **Dashboard read-only:** um painel web que lê o feed com um token `guest`.
- **CI/CD:** disparar prompts em terminais do Maestri a partir de um pipeline.
- **Monitoramento remoto:** stream de terminal (`WS /api/terminals/{id}/stream`) num cliente
  próprio.

> Endpoints principais (resumo): `GET /api/workspaces`, `GET /api/workspaces/{ws}/feed`,
> `WS /api/feed/stream?ws=`, `POST /api/terminals/{id}/prompt`, `POST /api/terminals/{id}/approve|reject`,
> `PUT /api/workspaces/{ws}/nodes/{id}/note`, `POST /api/workspaces/{ws}/floors`. A lista
> completa e as capabilities estão na doc oficial.
