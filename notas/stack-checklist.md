# stack-checklist

A definição compartilhada de pronto. Dono: o Stack Warden; cada agente mantém as próprias camadas honestas.

Vocabulário de status: `[ ]` não iniciado · `[~]` em progresso · `[x]` verde COM EVIDÊNCIA ·
`[!]` vermelho, achado aberto · `[-]` n/a, com motivo escrito.
Uma camada é verde só quando o Warden viu evidência. Intenção não é evidência.

| # | Camada | Dono | Status | Evidência |
|---|--------|------|--------|-----------|
| 1 | Frontend | — | [ ] | |
| 2 | Interface, UX e responsividade | — | [ ] | |
| 3 | Estado da aplicação | — | [ ] | |
| 4 | APIs e lógica de backend | — | [ ] | |
| 5 | Banco de dados e armazenamento | — | [ ] | |
| 6 | Modelagem de dados | — | [ ] | |
| 7 | Autenticação e autorização | — | [ ] | |
| 8 | Permissões e controle de acesso | — | [ ] | |
| 9 | Segurança e RLS | — | [ ] | |
| 10 | Validação de dados | — | [ ] | |
| 11 | Hospedagem e deploy | — | [ ] | |
| 12 | Cloud e infraestrutura | — | [ ] | |
| 13 | CI/CD e versionamento | — | [ ] | |
| 14 | Variáveis de ambiente e secrets | — | [ ] | |
| 15 | Cache e CDN | — | [ ] | |
| 16 | Rate limiting | — | [ ] | |
| 17 | Filas e processamento assíncrono | — | [ ] | |
| 18 | Webhooks e integrações externas | — | [ ] | |
| 19 | Logs e monitoramento | — | [ ] | |
| 20 | Rastreamento de erros | — | [ ] | |
| 21 | Testes automatizados | — | [ ] | |
| 22 | Performance e otimização | — | [ ] | |
| 23 | Escalabilidade | — | [ ] | |
| 24 | Backup e recuperação | — | [ ] | |
| 25 | Disponibilidade e incidentes | — | [ ] | |
| 26 | Documentação e manutenção | — | [ ] | |
| 27 | Idempotência e ledger financeiro | — | [ ] | |
| 28 | KYC, AML e triagem de sanções | — | [ ] | |
| 29 | Precisão monetária, FX e arredondamento | — | [ ] | |
| 30 | Trilha de auditoria e retenção | — | [ ] | |

## Regra de corte
Nenhuma fatia que toque movimentação de dinheiro, identidade, segredo ou superfície
pública é considerada pronta sem as camadas 7, 8, 9, 10, 14, 27, 28, 29 e 30 avaliadas —
verdes ou com achado aberto e registrado. Silêncio não conta como aprovação.
