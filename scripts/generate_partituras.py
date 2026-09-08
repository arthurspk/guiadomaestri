#!/usr/bin/env python3
"""
generate_partituras.py — Gera 200+ templates de partitura de tecnologia.

Estratégia: famílias de pipeline parametrizadas. Cada família é uma função que
recebe uma "variante" (stack, domínio, provedor de cloud, plataforma mobile, etc.)
e devolve um objeto Partitura montado. O produto cartesiano famílias × variantes
passa de 200 templates, todos com roles embutidas, notas, portais e conexões.

Saída (em partituras/tecnologia/):
  <slug>.maestripartitura            — um por template
  Tecnologia.maestripartituras       — pacote coletivo com todos
  CATALOGO.md                        — índice legível por família
"""

import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from maestri_build import (  # noqa: E402
    Partitura, COLORS, grid_positions, hub_layout, pack,
    CMD_FABLE, CMD_OPUS, CMD_CODEX, CMD_GEMINI, CMD_CLAUDE, CMD_SHELL,
)
import roles_lib as R  # noqa: E402

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "partituras")

# Áreas: slug -> (rótulo, emoji, arquivo do pacote coletivo, uma linha de descrição).
# Espelham as divisões de catálogos de agentes como o agency-agents, adaptadas
# ao Maestri (orquestração de agentes num canvas, com notas e portais).
AREAS = {
    "tecnologia": ("Tecnologia", "💻", "Tecnologia.maestripartituras",
                   "Engenharia ponta a ponta: features, bugs, release, infra, dados, IA, migração, mobile."),
    "design": ("Design & UX", "🎨", "Design.maestripartituras",
               "Design systems, pesquisa de UX, landing pages e auditoria de interface."),
    "produto": ("Produto", "📦", "Produto.maestripartituras",
                "Discovery, roadmap, PRD, síntese de feedback e análise de concorrência."),
    "marketing": ("Marketing & Conteúdo", "📢", "Marketing.maestripartituras",
                  "Campanhas, SEO/conteúdo, social, e-mail de ciclo de vida e blog técnico."),
    "vendas": ("Vendas", "💼", "Vendas.maestripartituras",
               "Prospecção outbound, propostas/RFP, sales enablement e preparo de discovery."),
    "dados": ("Dados & Analytics", "📊", "Dados.maestripartituras",
              "Dashboards de BI, análise exploratória, modelagem de métricas e experimentos A/B."),
    "seguranca": ("Segurança & Compliance", "🔒", "Seguranca.maestripartituras",
                  "LGPD, prontidão SOC 2, threat modeling e resposta a incidente de segurança."),
    "financeiro": ("Financeiro", "💵", "Financeiro.maestripartituras",
                   "Fechamento contábil, modelagem financeira, FP&A/orçamento e due diligence."),
    "juridico": ("Jurídico", "⚖️", "Juridico.maestripartituras",
                 "Revisão de contrato, intake de cliente e análise de risco/compliance."),
    "suporte": ("Suporte & Sucesso", "🛟", "Suporte.maestripartituras",
                "Base de conhecimento, triagem de tickets, onboarding e health/churn."),
    "gestao": ("Gestão de Projetos", "🗂️", "Gestao.maestripartituras",
               "Planejamento de sprint, coordenação multi-time, ata de reunião e retrospectiva."),
    "pesquisa": ("Pesquisa & Conteúdo Técnico", "🔬", "Pesquisa.maestripartituras",
                 "Estado da arte, síntese de pesquisa e análise competitiva de mercado."),
}

# (area_slug, categoria, nome, slug, icon, color, descricao, [roles], nº nós)
CATALOG = []


def slugify(s):
    out = []
    for ch in s.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_/.":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def save(p, category, area="tecnologia"):
    d = p.to_dict()
    slug = slugify(p.name)
    out = os.path.join(BASE, area)
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, slug + ".maestripartitura")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    CATALOG.append((area, category, p.name, slug, p.icon, p.color, p.description,
                    [r["name"] for r in d["roles"]], len(d["payload"]["nodes"])))
    return d


# ===========================================================================
# Catálogos de variantes
# ===========================================================================

# (nome curto, stack de front, stack de back, cor, ícone)
STACKS = [
    ("React + Node", "React 19 + Vite + TanStack Query", "Node 24 + Fastify 5", "blue", "globe"),
    ("Next.js + Nest", "Next.js 16 (App Router, RSC)", "NestJS 11 + Prisma", "indigo", "square.stack.3d.up"),
    ("Vue + Node", "Vue 3.6 + Nuxt 4", "Node 24 + Express 5", "green", "leaf"),
    ("Angular + Nest", "Angular v22 (signals)", "NestJS 11 + TypeORM", "red", "a.circle"),
    ("React + Python", "React 19 + Vite", "FastAPI (Python 3.14)", "yellow", "chevron.left.forwardslash.chevron.right"),
    ("Next.js + Go", "Next.js 16", "Go 1.26 + chi + sqlc", "teal", "bolt.horizontal"),
    ("Svelte + Node", "SvelteKit 2", "Node 24 + Hono", "orange", "flame"),
    ("Remix + Python", "Remix (React Router 7)", "Django 6 + DRF", "purple", "r.circle"),
    ("SolidStart + Go", "SolidStart", "Go 1.26 + Echo", "teal", "s.circle"),
    ("Nuxt + Nest", "Nuxt 4 (Vue 3.6)", "NestJS 11 + Prisma", "green", "n.circle"),
    ("Astro + Node", "Astro 5 (islands)", "Node 24 + Fastify", "orange", "star"),
    ("React Native + Node", "React Native 0.79 + Expo", "Node 24 + Fastify", "pink", "iphone"),
    ("React + Rails", "React 19 + Vite", "Ruby on Rails 8", "red", "diamond"),
    ("Next.js + Spring", "Next.js 16", "Spring Boot 3.4 (Java 25)", "green", "cup.and.saucer"),
    ("Blazor + .NET", "Blazor (WASM)", ".NET 10 Minimal APIs", "purple", "square.on.square"),
    ("HTMX + Go", "HTMX + templ", "Go 1.26 + chi", "teal", "bolt"),
    ("Laravel + Livewire", "Livewire 3 + Alpine", "Laravel 12 (PHP 8.4)", "orange", "l.circle"),
    ("Django full-stack", "Django templates + HTMX", "Django 6 + DRF", "green", "d.circle"),
    ("Phoenix LiveView", "Phoenix LiveView", "Elixir + Phoenix 1.8", "purple", "drop"),
    ("Qwik + Bun", "Qwik City", "Bun + Elysia", "yellow", "q.circle"),
    ("Nuxt + FastAPI", "Nuxt 4", "FastAPI (Python 3.14)", "green", "n.square"),
    ("Angular + Go", "Angular v22", "Go 1.26 + gRPC", "red", "a.square"),
    ("React + Kotlin", "React 19", "Kotlin + Ktor", "blue", "k.circle"),
    ("SvelteKit + Rust", "SvelteKit 2", "Rust + Axum", "orange", "gear"),
]

CLOUDS = [
    ("AWS", "VPC, ECS Fargate, RDS Aurora, S3, CloudFront, SQS/EventBridge", "orange", "cloud"),
    ("GCP", "VPC, Cloud Run, Cloud SQL, GCS, Cloud CDN, Pub/Sub", "blue", "cloud"),
    ("Azure", "VNet, Container Apps, Azure SQL, Blob, Front Door, Service Bus", "teal", "cloud"),
    ("Fly.io + Neon", "Fly Machines, Neon Postgres, Upstash Redis, Tigris S3", "purple", "airplane"),
    ("Kubernetes on-prem", "K8s 1.37 bare-metal, Longhorn, MetalLB, Harbor", "indigo", "cube"),
    ("Cloudflare", "Workers, D1, R2, KV, Durable Objects, Queues", "orange", "cloud"),
    ("Hetzner + Coolify", "Hetzner Cloud, Coolify, Postgres, MinIO", "red", "server.rack"),
    ("DigitalOcean", "App Platform, Managed Postgres, Spaces, Load Balancer", "blue", "drop"),
    ("Vercel + Supabase", "Vercel, Supabase (Postgres/Auth/Storage/Realtime)", "gray", "triangle"),
]

IAC = [
    ("Terraform", "Terraform 1.15 + OPA/checkov + Terratest", "purple", "square.grid.3x3"),
    ("OpenTofu", "OpenTofu + tflint + policy-as-code", "blue", "square.grid.3x3"),
    ("Pulumi", "Pulumi (TypeScript) + policy packs", "indigo", "square.grid.3x3"),
    ("AWS CDK", "AWS CDK (TypeScript) + cdk-nag", "orange", "square.grid.3x3"),
]

MOBILE = [
    ("React Native", "React Native 0.79 + Expo (New Architecture)", "pink", "iphone"),
    ("Flutter", "Flutter 3.35 + Riverpod", "blue", "iphone"),
    ("iOS nativo", "Swift 6 + SwiftUI + Observation", "gray", "apple.logo"),
    ("Android nativo", "Kotlin 2.2 + Jetpack Compose", "green", "smartphone"),
    ("Kotlin Multiplatform", "KMP + Compose Multiplatform", "purple", "iphone"),
    (".NET MAUI", ".NET MAUI 10", "indigo", "iphone"),
    ("Capacitor + Ionic", "Ionic 8 + Capacitor 7", "teal", "iphone"),
]

DATABASES = [
    ("PostgreSQL", "PostgreSQL 18 (partitioning, uuidv7, async I/O)", "blue", "cylinder"),
    ("MySQL", "MySQL 8.4 LTS", "orange", "cylinder"),
    ("MongoDB", "MongoDB 8 (replica set, change streams)", "green", "cylinder"),
    ("Redis/Valkey", "Valkey 9.1 (cache + streams)", "red", "cylinder"),
    ("ClickHouse", "ClickHouse (colunar, analítico)", "yellow", "cylinder"),
    ("SQLite/libSQL", "SQLite + libSQL/Turso (edge, embedded)", "teal", "cylinder"),
    ("Cassandra/Scylla", "ScyllaDB (wide-column, alta escrita)", "purple", "cylinder"),
    ("Neo4j", "Neo4j 5 (grafo, Cypher)", "indigo", "cylinder"),
    ("DynamoDB", "DynamoDB (single-table design, GSIs)", "orange", "cylinder"),
]

DATA_PIPES = [
    ("Batch ELT", "Airflow 3 + dbt + DuckDB/Snowflake", "orange", "arrow.triangle.branch"),
    ("Streaming", "Kafka + Flink + Iceberg", "red", "waveform"),
    ("Lakehouse", "Spark + Delta Lake + Unity Catalog", "blue", "cylinder.split.1x2"),
    ("CDC", "Debezium + Kafka Connect + sink incremental", "green", "arrow.triangle.branch"),
]

AI_FEATURES = [
    ("RAG", "chunking, embeddings, busca híbrida, rerank, pgvector/Qdrant", "purple", "brain"),
    ("Agente com tools", "ReAct + MCP + function calling + guardrails", "indigo", "brain.head.profile"),
    ("Fine-tuning/Evals", "SFT + preference opt + promptfoo/DeepEval", "pink", "brain"),
    ("Text-to-SQL", "NL → SQL com schema linking, validação e sandbox de execução", "blue", "brain"),
    ("Multimodal", "visão + texto, OCR, extração estruturada de documentos", "teal", "brain"),
    ("Voice pipeline", "ASR (Whisper) → LLM → TTS, streaming e barge-in", "orange", "waveform"),
    ("Recomendação", "embeddings + ANN + reranking + feedback loop", "green", "brain"),
]

PENTEST = [
    ("Web", "PortSwigger, Burp, nuclei, sqlmap, ffuf — OWASP Web + API + LLM", "red", "shield.lefthalf.filled"),
    ("Mobile", "MASVS/MASTG, Frida, objection, jadx, MobSF", "orange", "shield.lefthalf.filled"),
    ("Infra/AD", "AD (Kerberoast, ESC1-8, BloodHound), cloud IAM, K8s, C2", "pink", "shield.lefthalf.filled"),
    ("Cloud", "AWS/GCP/Azure IAM chains, IMDS, buckets, privesc", "purple", "shield.lefthalf.filled"),
]

MIGRATIONS = [
    ("Monólito → microsserviços", "strangler fig, extração incremental, anti-corruption layer", "indigo", "arrow.triangle.2.circlepath"),
    ("Angular v17 → v22", "codemods, signals migration, control flow, zoneless", "red", "arrow.up.circle"),
    ("Vue 2 → Vue 3", "Options → Composition, Vue compat build, Vite", "green", "arrow.up.circle"),
    ("REST → GraphQL", "schema-first, coexistência, deprecação de endpoints", "pink", "arrow.triangle.swap"),
    ("Postgres major upgrade", "expand-contract, dual-write, backfill, pgbouncer", "blue", "arrow.up.circle"),
    ("JS → TS", "ts-morph, allowJs incremental, strict por diretório", "yellow", "arrow.up.circle"),
    ("Webpack → Vite/Rspack", "coexistência de bundlers, code-split, HMR", "orange", "arrow.triangle.swap"),
    ("Pages → App Router", "Next.js Pages Router → App Router, RSC incremental", "indigo", "arrow.up.circle"),
    ("Redux → TanStack Query", "server state para cache, remoção de boilerplate", "purple", "arrow.triangle.swap"),
    ("npm → pnpm workspaces", "monorepo, hoisting, catalog, migração de lockfile", "orange", "arrow.triangle.swap"),
    ("Enzyme → Testing Library", "reescrita de testes para queries acessíveis", "green", "arrow.triangle.swap"),
    ("Moment → Temporal/date-fns", "remoção de moment, imutabilidade de datas", "yellow", "arrow.up.circle"),
]

BFF_DOMAINS = [
    ("KYC", "core-kyc (SPA) × core-kyc-api (BFF): paridade de schema, fronteira HTTP, cookie credenciado", "indigo", "magnifyingglass"),
    ("Checkout", "checkout-web (SPA) × checkout-bff: idempotência de pagamento, paridade de contrato", "green", "cart"),
    ("Onboarding", "onboarding-app × onboarding-bff: validação em várias etapas, upload de documentos", "blue", "person.badge.plus"),
    ("Dashboard", "admin-dashboard × admin-bff: RBAC, paginação, filtros, exportação", "orange", "chart.bar"),
    ("Open Finance", "of-consent-web × of-bff: consentimento, redirect, escopos OAuth", "teal", "building.columns"),
    ("Wallet", "wallet-app × wallet-bff: saldo, extrato, limites, WebSocket de saldo ao vivo", "green", "creditcard"),
    ("Seguros", "quote-web × quote-bff: cotação multi-etapa, upload de apólice, assinatura", "purple", "shield"),
    ("Investimentos", "invest-web × invest-bff: carteira, ordens, cotações em streaming, suitability", "orange", "chart.pie"),
]

FULL_PRODUCTS = [
    ("Remessa internacional", "remessa transfronteiriça (idempotência, ledger, KYC/AML, FX)", "blue", "paperplane", True),
    ("Marketplace", "marketplace de dois lados (split de pagamento, escrow, reputação)", "orange", "bag", True),
    ("Carteira digital", "carteira/PIX (saldo, ledger de partida dobrada, limites, MED)", "green", "creditcard", True),
    ("SaaS B2B", "SaaS B2B multi-tenant (RBAC, billing por assento, cotas, auditoria)", "indigo", "building.2", False),
    ("Streaming de vídeo", "plataforma de vídeo (ABR, DRM, CDN, catálogo, recomendação)", "pink", "play.rectangle", False),
    ("E-commerce", "e-commerce (catálogo, carrinho, checkout, estoque, antifraude)", "yellow", "cart", True),
    ("Delivery/logística", "app de delivery (roteirização, tracking em tempo real, pagamento)", "red", "shippingbox", True),
    ("Saúde/telemedicina", "telemedicina (agendamento, prontuário, LGPD, prescrição)", "teal", "cross.case", False),
    ("Educação/EAD", "plataforma EAD (cursos, progresso, avaliações, certificados)", "purple", "graduationcap", False),
    ("Fintech/crédito", "concessão de crédito (score, esteira de análise, motor de decisão, LGPD)", "green", "chart.line.uptrend.xyaxis", True),
]

DOCS_KINDS = [
    ("Referência de API", "OpenAPI + exemplos + guia de autenticação + versionamento", "blue", "book"),
    ("Guia de arquitetura", "C4, ADRs, diagramas, decisões e trade-offs", "indigo", "book"),
    ("Onboarding de devs", "setup local, convenções, primeiro PR, glossário", "green", "book"),
    ("Runbooks de operação", "alertas, playbooks de incidente, dashboards, on-call", "orange", "book"),
    ("Docs de usuário", "tutoriais, how-tos, referência e explicação (Diátaxis)", "teal", "book"),
]

SOLO_SPECIALISTS = [
    ("Frontend Engineer", "componentes acessíveis, estado, performance de render", "blue", "chevron.left.forwardslash.chevron.right"),
    ("Backend Engineer", "APIs, modelagem de dados, transações, idempotência", "green", "server.rack"),
    ("SRE / Platform", "observabilidade, SLOs, capacidade, confiabilidade", "orange", "gauge"),
    ("Data Engineer", "pipelines, qualidade de dados, modelagem dimensional", "purple", "cylinder.split.1x2"),
    ("Security Engineer", "hardening, threat modeling, revisão de segredos", "red", "lock.shield"),
    ("Refactorer", "reduzir complexidade e dívida sem mudar comportamento", "teal", "wand.and.stars"),
    ("Test Engineer", "cobertura significativa, testes determinísticos, fixtures", "yellow", "checkmark.seal"),
]

DUELS = [
    ("Algoritmo difícil", "um problema algorítmico com casos de contorno cruéis", "red", "flag.2.crossed"),
    ("Design de API", "desenhar uma API pública que envelhece bem", "blue", "flag.2.crossed"),
    ("Refactor arriscado", "refatorar um módulo enrolado sem mudar comportamento", "purple", "flag.2.crossed"),
    ("Otimização de query", "acelerar uma query lenta sem quebrar semântica", "green", "flag.2.crossed"),
    ("Bug intermitente", "achar e consertar um bug que só aparece às vezes", "orange", "flag.2.crossed"),
]

INCIDENTS = [
    ("Queda de produção", "erro 5xx em massa, serviço core indisponível", "red", "exclamationmark.triangle"),
    ("Vazamento/segurança", "suspeita de exposição de dados ou acesso indevido", "pink", "exclamationmark.shield"),
    ("Degradação de performance", "latência p99 explodindo, timeouts em cascata", "orange", "gauge"),
    ("Corrupção de dados", "dados inconsistentes, ledger fora do zero, dupla escrita", "purple", "cylinder"),
    ("Falha de deploy", "release ruim em produção, rollback necessário", "yellow", "arrow.uturn.backward"),
]

CICD = [
    ("GitHub Actions", "matrix, cache, OIDC para cloud, environments, required checks", "gray", "arrow.triangle.branch"),
    ("GitLab CI", "stages, needs DAG, cache, review apps, deploy gates", "orange", "arrow.triangle.branch"),
    ("Dagger", "pipeline como código portátil, cache de conteúdo", "purple", "arrow.triangle.branch"),
    ("Buildkite/Nx", "monorepo affected, distribuição de agentes, TIA", "teal", "arrow.triangle.branch"),
]

K8S = [
    ("Deploy GitOps", "Argo CD/Flux, Helm/Kustomize, progressive delivery", "blue", "cube"),
    ("Autoscaling", "HPA/VPA/KEDA, requests/limits, cluster autoscaler", "green", "cube"),
    ("Malha de serviço", "Istio/Linkerd, mTLS, tráfego canário, políticas", "purple", "cube"),
    ("Hardening", "PSA, NetworkPolicy, OPA/Gatekeeper, imagens distroless", "red", "cube"),
]

A11Y = [
    ("Web (WCAG 2.2 AA)", "fluxo web crítico contra WCAG 2.2 AA", "blue", "figure.wave"),
    ("Design System", "componentes acessíveis por construção, tokens, docs", "purple", "square.grid.2x2"),
    ("Formulários", "labels, erros, foco, mensagens, teclado", "green", "list.bullet.rectangle"),
    ("Mobile a11y", "VoiceOver/TalkBack, alvos de toque, contraste dinâmico", "orange", "figure.wave"),
]

API_CONTRACT = [
    ("REST/OpenAPI", "design-first, contract testing, versionamento, paginação", "blue", "link"),
    ("GraphQL", "schema design, N+1, persisted queries, deprecação", "pink", "link"),
    ("gRPC/Protobuf", "evolução de schema, backward compat, streaming", "teal", "link"),
    ("Eventos/AsyncAPI", "contratos de evento, schema registry, versionamento", "orange", "link"),
]

PERF = [
    ("Frontend (Core Web Vitals)", "LCP/INP/CLS, bundle, imagens, hidratação", "blue", "gauge"),
    ("Backend (latência/throughput)", "profiling, N+1, pool de conexões, cache", "green", "gauge"),
    ("Banco de dados", "planos de query, índices, particionamento, lock", "purple", "gauge"),
    ("Custo em cloud", "rightsizing, spot, cache de CDN, egress", "orange", "gauge"),
]


# ===========================================================================
# Helpers de composição
# ===========================================================================

def _proving(url):
    return url


# ===========================================================================
# FAMÍLIA 1 — Ship Feature (padrão Ship Goats, por stack)
# ===========================================================================

def fam_ship_feature(stack):
    name_short, front, back, ck, icon = stack
    p = Partitura(
        name=f"Ship Feature · {name_short}",
        description=(f"Entrega uma feature ponta a ponta em {front} + {back} através de "
                     f"especialistas paralelos presos a um contrato compartilhado. Arquiteto "
                     f"escreve o spec, dois implementadores constroem fatias, o warden verifica "
                     f"vivo no portal. Achados, não correções."),
        icon=icon, color=COLORS[ck],
    )
    p.role("Team Maestro", R.maestro(f"entrega de feature em {name_short}",
           repos_desc=f"Front: {front}. Back: {back}. Um repositório (ou monorepo) só.",
           extra="\nEste time entrega a feature; a decisão de subir é do usuário."),
           color=COLORS["pink"])
    p.role("Feature Architect", R.architect(f"feature em {name_short} ({front} + {back})"),
           color=COLORS["yellow"])
    p.role("Slice Implementer", R.implementer(f"{front} + {back}"), color=COLORS["purple"])
    p.role("Quality Warden", R.warden(f"a feature em {name_short}"), color=COLORS["orange"])

    m = p.terminal("Maestro · orquestrador", role="Team Maestro", manager=True, command=CMD_FABLE)
    pos = grid_positions(4, cols=4, gx=940, y0=800)
    arch = p.terminal("Meridian · contrato", role="Feature Architect", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    b1 = p.terminal("Rivet · fatia A", role="Slice Implementer", command=CMD_OPUS, x=pos[1][0], y=pos[1][1])
    b2 = p.terminal("Wren · fatia B", role="Slice Implementer", command=CMD_OPUS, x=pos[2][0], y=pos[2][1])
    wd = p.terminal("Argus · warden", role="Quality Warden", command=CMD_OPUS, x=pos[3][0], y=pos[3][1])

    spec = p.note("feature-spec.md", R.FEATURE_SPEC_EMPTY, x=1300, y=-360, color="blue")
    board = p.note("workboard.md", R.WORKBOARD_EMPTY, x=1880, y=-360, color="green")
    portal = p.portal("Proving Ground", "http://localhost:5173", x=-1420, y=-1050)

    hub_layout(p, m, [arch, b1, b2, wd], note_nodes=[spec, board])
    p.connect_portal(p.portal_node_id("Proving Ground"), m)
    p.connect_portal(p.portal_node_id("Proving Ground"), wd)
    return save(p, "Ship Feature")


# ===========================================================================
# FAMÍLIA 2 — Depuração (padrão The Bug is on the Canvas, por stack)
# ===========================================================================

def fam_debug(stack):
    name_short, front, back, ck, icon = stack
    p = Partitura(
        name=f"Depuração · {name_short}",
        description=(f"Caça um bug em {front} + {back} com método científico: reprodução "
                     f"determinística, causa raiz com prova, menor conserto correto, "
                     f"verificação adversarial independente no portal."),
        icon="ladybug", color=COLORS[ck],
    )
    p.role("Debug Maestro", R.debug_maestro(), color=COLORS["purple"])
    p.role("Reprodutor", R.bug_reproducer(), color=COLORS["blue"])
    p.role("Analista de Causa Raiz", R.root_cause_analyst(), color=COLORS["orange"])
    p.role("Engenheiro de Correção", R.fix_engineer(), color=COLORS["green"])
    p.role("Verificador", R.fix_verifier(), color=COLORS["red"])

    m = p.terminal("Maestro · depuração", role="Debug Maestro", manager=True, command=CMD_FABLE)
    pos = grid_positions(4, cols=4, gx=940, y0=800)
    rep = p.terminal("Echo · repro", role="Reprodutor", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    rca = p.terminal("Probe · causa raiz", role="Analista de Causa Raiz", command=CMD_OPUS, x=pos[1][0], y=pos[1][1])
    fix = p.terminal("Forge · correção", role="Engenheiro de Correção", command=CMD_OPUS, x=pos[2][0], y=pos[2][1])
    ver = p.terminal("Sentry · verificação", role="Verificador", command=CMD_CODEX, x=pos[3][0], y=pos[3][1])

    case = p.note("case-file.md", R.CASE_FILE_EMPTY, x=1300, y=-360, color="purple")
    portal = p.portal("Repro", "http://localhost:5173", x=-1420, y=-1050)

    hub_layout(p, m, [rep, rca, fix, ver], note_nodes=[case])
    p.connect_portal(p.portal_node_id("Repro"), m)
    p.connect_portal(p.portal_node_id("Repro"), rep)
    p.connect_portal(p.portal_node_id("Repro"), ver)
    return save(p, "Depuração")


# ===========================================================================
# FAMÍLIA 3 — Portão de Release (padrão Slop Haters, por stack)
# ===========================================================================

def fam_release_gate(stack):
    name_short, front, back, ck, icon = stack
    p = Partitura(
        name=f"Portão de Release · {name_short}",
        description=(f"Decide se sobe ou não em {front} + {back}. Quatro revisores "
                     f"adversariais (qualidade, segurança, correção, UX+a11y) reportam "
                     f"achados; o Conductor sintetiza um veredito. Correções só sob pedido."),
        icon="checkmark.shield", color=COLORS[ck],
    )
    p.role("Release Conductor", R.release_conductor(), color=COLORS["green"])
    p.role("Code Quality Reviewer", R.code_quality_reviewer(), color=COLORS["blue"])
    p.role("Security Auditor", R.security_reviewer(), color=COLORS["pink"])
    p.role("Correctness Verifier", R.correctness_verifier(), color=COLORS["yellow"])
    p.role("UX & A11y Reviewer", R.ux_a11y_reviewer(), color=COLORS["purple"])

    m = p.terminal("Conductor · release", role="Release Conductor", manager=True, command=CMD_FABLE)
    pos = grid_positions(4, cols=4, gx=940, y0=820)
    q = p.terminal("Burnish · qualidade", role="Code Quality Reviewer", command=CMD_CODEX, x=pos[0][0], y=pos[0][1])
    s = p.terminal("Palisade · segurança", role="Security Auditor", command=CMD_CODEX, x=pos[1][0], y=pos[1][1])
    c = p.terminal("Ferret · correção", role="Correctness Verifier", command=CMD_CODEX, x=pos[2][0], y=pos[2][1])
    u = p.terminal("Lumen · ux/a11y", role="UX & A11y Reviewer", command=CMD_GEMINI, x=pos[3][0], y=pos[3][1])

    playbook = p.note("release-playbook.md", R.RELEASE_PLAYBOOK, x=1300, y=-380, color="slate", h=460)
    findings = p.note("release-findings.md", R.RELEASE_FINDINGS, x=1880, y=-380, color="yellow", h=460)
    portal = p.portal("Proving Ground", "http://localhost:5173", x=-1420, y=-1050)

    hub_layout(p, m, [q, s, c, u], note_nodes=[playbook, findings])
    p.connect_portal(p.portal_node_id("Proving Ground"), m)
    p.connect_portal(p.portal_node_id("Proving Ground"), u)
    return save(p, "Portão de Release")


# ===========================================================================
# FAMÍLIA 4 — Scaffold (arranca um projeto novo, por stack)
# ===========================================================================

def fam_scaffold(stack):
    name_short, front, back, ck, icon = stack
    p = Partitura(
        name=f"Scaffold · {name_short}",
        description=(f"Arranca um projeto novo em {front} + {back}: estrutura, ferramentas, "
                     f"lint/format, testes, CI mínima e um vertical slice que roda. "
                     f"Arquiteto define o esqueleto; builders preenchem; warden verifica."),
        icon="square.grid.2x2", color=COLORS[ck],
    )
    p.role("Scaffold Maestro", R.maestro(f"scaffold de projeto {name_short}",
           repos_desc=f"Projeto novo em branco. Front: {front}. Back: {back}.",
           extra="\nObjetivo é um esqueleto que roda e um vertical slice, não a feature final."),
           color=COLORS["pink"])
    p.role("Skeleton Architect", R.architect(f"scaffold de {name_short}: estrutura de pastas, "
           f"ferramentas, convenções e o primeiro vertical slice"), color=COLORS["indigo"])
    p.role("Setup Engineer", R.specialist("Setup Engineer",
           f"Configura {name_short}: gerenciador de pacotes, TypeScript/tsconfig ou equivalente, "
           f"ESLint/Prettier ou linters da stack, scripts de dev/build/test, e a CI mínima.",
           rules="- Prefira o padrão idiomático da stack ao exótico; deixe tudo reproduzível do zero."),
           color=COLORS["green"])
    p.role("Vertical Slice Builder", R.implementer(f"{front} + {back}",
           extra="\nSeu trabalho é um vertical slice fino que atravessa front, back e dados, "
                  "provando que a stack inteira conversa."), color=COLORS["purple"])
    p.role("Setup Warden", R.warden(f"o scaffold de {name_short}",
           extra="\nVocê verifica que `install`, `build`, `test` e `dev` rodam do zero e que o "
                  "vertical slice responde de verdade no portal."), color=COLORS["orange"])

    m = p.terminal("Maestro · scaffold", role="Scaffold Maestro", manager=True, command=CMD_FABLE)
    pos = grid_positions(4, cols=4, gx=940, y0=820)
    arch = p.terminal("Keel · esqueleto", role="Skeleton Architect", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    setup = p.terminal("Bolt · setup", role="Setup Engineer", command=CMD_OPUS, x=pos[1][0], y=pos[1][1])
    slice_ = p.terminal("Rivet · slice", role="Vertical Slice Builder", command=CMD_OPUS, x=pos[2][0], y=pos[2][1])
    wd = p.terminal("Argus · warden", role="Setup Warden", command=CMD_CODEX, x=pos[3][0], y=pos[3][1])

    spec = p.note("feature-spec.md",
                  "# feature-spec — scaffold\n\nO Arquiteto define aqui: estrutura de pastas, "
                  "ferramentas escolhidas (com versão), convenções de nomes, o contrato do "
                  "vertical slice (uma rota de front → um endpoint → uma tabela) e o critério de "
                  "pronto: `install/build/test/dev` verdes e o slice respondendo.",
                  x=1300, y=-360, color="blue")
    board = p.note("workboard.md", R.WORKBOARD_EMPTY, x=1880, y=-360, color="green")
    portal = p.portal("Dev", "http://localhost:5173", x=-1420, y=-1050)

    hub_layout(p, m, [arch, setup, slice_, wd], note_nodes=[spec, board])
    p.connect_portal(p.portal_node_id("Dev"), m)
    p.connect_portal(p.portal_node_id("Dev"), wd)
    return save(p, "Scaffold")


# ===========================================================================
# FAMÍLIA 5 — Validação BFF (padrão KYC, por domínio)
# ===========================================================================

def fam_bff_validation(domain):
    name_short, desc, ck, icon = domain
    p = Partitura(
        name=f"Validação BFF · {name_short}",
        description=(f"Valida {desc}. O Maestro é dono do runtime; o Arquiteto escreve o "
                     f"contrato de validação; dois validadores checam front e BFF em paralelo; "
                     f"o Warden confirma vivo no portal. Achados, não correções."),
        icon=icon, color=COLORS[ck],
    )
    repos = (f"Topologia: uma SPA e o BFF que ela consome via HTTP externo, sem proxy no "
             f"front. Contratos duplicados (não compartilhados): o lado da API é a fonte de "
             f"verdade; o front é uma cópia manual guardada só por um teste de paridade. "
             f"Suspeitas que este run existe para resolver: base URL que precisa resolver e "
             f"terminar TLS localmente, e cookie cross-origin com withCredentials que exige "
             f"origin ecoado (nunca wildcard), SameSite e Secure que o browser aceite.")
    p.role("Runtime Maestro", R.maestro(f"validação de fronteira BFF ({name_short})",
           repos_desc=repos,
           extra="\nAchados são reportados, não corrigidos. Traga a lista de divergências ao "
                 "usuário e obtenha aprovação explícita antes de deixar qualquer validador editar código."),
           color=COLORS["pink"])
    p.role("Contract Architect", R.architect(
        f"validação de {name_short}: paridade de schema e fronteira HTTP",
        contract_note="kyc-contract", board_note="kyc-workboard",
        extra="\nÉ um contrato de VALIDAÇÃO, não um spec de feature: para cada endpoint que o "
              "front consome, escreva request, resposta de sucesso, resposta de erro, o schema do "
              "lado da API que o define e a cópia do lado do front que o espelha; e qual fluxo de "
              "UI exercita cada endpoint, para a verificação viva ter uma rota."),
        color=COLORS["purple"])
    p.role("Surface Validator", R.warden(
        f"a superfície de {name_short} (front e BFF)",
        board_note="kyc-workboard", contract_note="kyc-contract",
        extra="\nVocê valida uma superfície por vez: o front consome o contrato como escrito? o "
              "BFF responde como o contrato diz? Divergências viram achados por severidade."),
        color=COLORS["orange"])
    p.role("Boundary Warden", R.warden(
        f"a fronteira de {name_short}: CORS, cookie credenciado, base URL, paridade",
        board_note="kyc-workboard", contract_note="kyc-contract",
        extra="\nVocê recusa passar: um cookie cross-origin que o browser não armazena de fato; um "
              "CORS com wildcard sob credentials; uma base URL que não resolve; um mirror de schema "
              "entre repos sem nada guardando contra drift."),
        color=COLORS["red"])

    m = p.terminal("Maestro · runtime", role="Runtime Maestro", manager=True, command=CMD_FABLE)
    pos = grid_positions(4, cols=4, gx=920, y0=800)
    arch = p.terminal("Meridian · contrato", role="Contract Architect", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    v1 = p.terminal("Rivet · front", role="Surface Validator", command=CMD_OPUS, x=pos[1][0], y=pos[1][1])
    v2 = p.terminal("Wren · bff", role="Surface Validator", command=CMD_OPUS, x=pos[2][0], y=pos[2][1])
    wd = p.terminal("Argus · fronteira", role="Boundary Warden", command=CMD_OPUS, x=pos[3][0], y=pos[3][1])

    contract = p.note("kyc-contract.md",
                      f"# contract — validação de {name_short}\n\n{desc}\n\n"
                      "## Status\nNão escrito ainda. O Arquiteto preenche antes de qualquer validador começar.\n\n"
                      "## Endpoint contracts\n(um bloco por endpoint: request, sucesso, erro, schema da API, schema do front)\n\n"
                      "## UI flows per endpoint\n(qual rota e qual interação exercita cada endpoint)\n\n"
                      "## Slice breakdown e posse de arquivos\n(uma fatia por validador; nenhuma fatia cruza repos)\n\n"
                      "## Pass criteria\n(por fatia, para o revisor dizer passa/não passa sem interpretar)\n\n"
                      "## Perguntas em aberto\n(qual ambiente, como o hostname resolve localmente)",
                      x=1300, y=-380, color="blue")
    board = p.note("kyc-workboard.md",
                   "# workboard\n\n## Slices\n- [ ] Superfície front — dono: não atribuído — não iniciado\n"
                   "- [ ] Superfície BFF — dono: não atribuído — não iniciado\n"
                   "As superfícies de fronteira (paridade, CORS, cookie, base URL) NÃO são fatia: "
                   "pertencem ao Arquiteto adjudicar e ao Warden verificar.\n\n"
                   "## Runtime\n(o Maestro é dono de cada linha desta seção)\n\n"
                   "## Decisions\n\n## Verdicts\n\n## Findings\n(divergências por severidade; nada é corrigido até o usuário aprovar)",
                   x=1880, y=-380, color="green")
    portal = p.portal("Proving Ground", "http://localhost:5174", x=-1420, y=-1050)

    hub_layout(p, m, [arch, v1, v2, wd], note_nodes=[contract, board])
    p.connect_portal(p.portal_node_id("Proving Ground"), m)
    p.connect_portal(p.portal_node_id("Proving Ground"), wd)
    return save(p, "Validação BFF")


# ===========================================================================
# FAMÍLIA 6 — Pipeline Completo 30 camadas (padrão Money Send, por produto)
# ===========================================================================

def fam_full_pipeline(product):
    name_short, desc, ck, icon, financial = product
    p = Partitura(
        name=f"Pipeline Completo · {name_short}",
        description=(f"Pipeline completo para {desc}: orquestrador, arquiteto, três builders de "
                     f"superfície (web desktop, web mobile, mobile híbrido), sentinela de "
                     f"segurança, engenheiro de plataforma e um stack warden validando 30 camadas."),
        icon=icon, color=COLORS[ck], origin=(9000, 8000),
    )
    money = ("\nDuas consequências que superam o gosto de engenharia normal quando há dinheiro: "
             "(1) dinheiro nunca é float, nunca é reconstruído de string de exibição e nunca se "
             "move sem chave de idempotência e entrada de ledger — um retry nunca envia duas vezes. "
             "(2) Identidade, triagem de sanções e trilha de auditoria são requisito de produto, "
             "não papelada.") if financial else ""
    p.role("Pipeline Maestro", R.maestro(f"produto: {desc}",
           repos_desc="Três repositórios lado a lado (dashboard web, API, mobile híbrido); o "
                      "parent NÃO é um repositório git — rode git dentro de cada repo.",
           extra=money + "\nToda fatia que toca dinheiro, identidade ou segredo passa pela regra "
                 "de corte da stack-checklist antes de ser dada como pronta."),
           color=COLORS["pink"])
    p.role("System Architect", R.architect(f"pipeline de {name_short} em quatro superfícies",
           contract_note="contract", board_note="workboard",
           extra="\nO contrato cobre as quatro superfícies (web desktop, web mobile, iOS, Android) "
                 "e a fronteira de API compartilhada. Interfaces que cruzam superfície são exatas."),
           color=COLORS["indigo"])
    p.role("Web Surface Builder", R.implementer("web desktop (SPA + SSR)",
           contract_note="contract", board_note="workboard"), color=COLORS["blue"])
    p.role("Mobile Web Builder", R.implementer("web mobile (responsivo, PWA)",
           contract_note="contract", board_note="workboard"), color=COLORS["teal"])
    p.role("Hybrid Mobile Builder", R.implementer("mobile híbrido (React Native/Expo)",
           contract_note="contract", board_note="workboard"), color=COLORS["green"])
    p.role("Security Sentinel", R.security_reviewer(), color=COLORS["red"])
    p.role("Platform Engineer", R.platform_engineer(
        "Você cuida de infra, deploy, secrets, filas, observabilidade e as camadas de "
        "plataforma da stack-checklist (11-26)."), color=COLORS["orange"])
    p.role("Stack Warden", R.warden(f"as 30 camadas de {name_short}",
           board_note="workboard", contract_note="contract",
           extra="\nVocê é dono da nota `stack-checklist`: uma camada só fica verde quando você viu "
                 "evidência. Aplique a regra de corte financeira sem exceção."), color=COLORS["yellow"])

    m = p.terminal("Maestro · pipeline", role="Pipeline Maestro", manager=True, command=CMD_FABLE, x=0, y=0)
    pos = grid_positions(7, cols=4, gx=940, gy=780, y0=820)
    arch = p.terminal("Meridian · arquiteto", role="System Architect", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    web = p.terminal("Rivet · web", role="Web Surface Builder", command=CMD_OPUS, x=pos[1][0], y=pos[1][1])
    mweb = p.terminal("Wren · web mobile", role="Mobile Web Builder", command=CMD_OPUS, x=pos[2][0], y=pos[2][1])
    hyb = p.terminal("Tide · mobile híbrido", role="Hybrid Mobile Builder", command=CMD_OPUS, x=pos[3][0], y=pos[3][1])
    sec = p.terminal("Palisade · segurança", role="Security Sentinel", command=CMD_CODEX, x=pos[4][0], y=pos[4][1])
    plat = p.terminal("Anvil · plataforma", role="Platform Engineer", command=CMD_OPUS, x=pos[5][0], y=pos[5][1])
    wd = p.terminal("Ledger · stack warden", role="Stack Warden", command=CMD_OPUS, x=pos[6][0], y=pos[6][1])

    contract = p.note("contract.md",
                      f"# contract — {name_short}\n\n{desc}\n\nO Arquiteto preenche: fatias por "
                      "superfície, interface de API compartilhada (exata), posse de arquivos, "
                      "critério de pronto por fatia.", x=1300, y=-420, color="blue", h=280)
    board = p.note("workboard.md", R.WORKBOARD_EMPTY, x=1880, y=-420, color="green", h=280)
    checklist = p.note("stack-checklist.md", R.STACK_CHECKLIST_30, x=1300, y=-100, color="slate", w=1100, h=560)
    portal_web = p.portal("Web · Desktop", "http://localhost:5173", x=-1500, y=-1150, w=1300, h=760)
    portal_api = p.portal("API · health", "http://localhost:8080/health", x=-1500, y=-320, w=1300, h=380)

    hub_layout(p, m, [arch, web, mweb, hyb, sec, plat, wd],
               note_nodes=[contract, board, checklist])
    p.connect_portal(p.portal_node_id("Web · Desktop"), m)
    p.connect_portal(p.portal_node_id("Web · Desktop"), wd)
    p.connect_portal(p.portal_node_id("API · health"), m)
    p.connect_portal(p.portal_node_id("API · health"), sec)
    return save(p, "Pipeline Completo")


# ===========================================================================
# Famílias de infra/dados/AI — padrão maestro + arquiteto + 2 especialistas + warden
# ===========================================================================

def _team_pipeline(name, description, icon, ck, maestro_domain, arch_domain,
                   specialists, warden_domain, category, contract_note="feature-spec",
                   board_note="workboard", portal_url="http://localhost:5173",
                   portal_name="Proving Ground", extra_maestro="", checklist=False,
                   reviewer_cmd=CMD_CODEX):
    """Monta um time genérico: Maestro (fable) + Arquiteto (opus) + N especialistas
    (opus) + Warden (codex), com contrato + workboard + portal. `specialists` é uma
    lista de (role_name, prompt, colorkey, terminal_name)."""
    p = Partitura(name=name, description=description, icon=icon, color=COLORS[ck])
    p.role("Maestro", R.maestro(maestro_domain, extra=extra_maestro), color=COLORS["pink"])
    p.role("Architect", R.architect(arch_domain, contract_note=contract_note, board_note=board_note),
           color=COLORS["indigo"])
    for rn, pr, cc, _tn in specialists:
        p.role(rn, pr, color=COLORS[cc])
    p.role("Warden", R.warden(warden_domain, contract_note=contract_note, board_note=board_note),
           color=COLORS["orange"])

    workers = len(specialists) + 2  # arquiteto + especialistas + warden = workers
    m = p.terminal("Maestro", role="Maestro", manager=True, command=CMD_FABLE)
    pos = grid_positions(workers, cols=4, gx=940, gy=780, y0=820)
    tids = []
    arch = p.terminal("Meridian · contrato", role="Architect", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    tids.append(arch)
    for i, (rn, _pr, _cc, tn) in enumerate(specialists, start=1):
        tids.append(p.terminal(tn, role=rn, command=CMD_OPUS, x=pos[i][0], y=pos[i][1]))
    wd = p.terminal("Argus · warden", role="Warden", command=reviewer_cmd,
                    x=pos[workers - 1][0], y=pos[workers - 1][1])
    tids.append(wd)

    notes = []
    spec = p.note(f"{contract_note}.md", R.FEATURE_SPEC_EMPTY if contract_note == "feature-spec"
                  else f"# {contract_note}\n\nO Arquiteto escreve o contrato aqui antes de qualquer implementação.",
                  x=1300, y=-360, color="blue")
    board = p.note(f"{board_note}.md", R.WORKBOARD_EMPTY, x=1880, y=-360, color="green")
    notes = [spec, board]
    if checklist:
        cl = p.note("stack-checklist.md", R.STACK_CHECKLIST_30, x=1300, y=-40, color="slate", w=1100, h=560)
        notes.append(cl)
    portal = p.portal(portal_name, portal_url, x=-1460, y=-1080)

    hub_layout(p, m, tids, note_nodes=notes)
    p.connect_portal(p.portal_node_id(portal_name), m)
    p.connect_portal(p.portal_node_id(portal_name), wd)
    return save(p, category)


def fam_cloud(cloud):
    name_short, desc, ck, icon = cloud
    return _team_pipeline(
        name=f"Cloud & Infra · {name_short}",
        description=(f"Provisiona e opera infraestrutura em {name_short} ({desc}) com rede, "
                     f"compute, dados, CDN e mensageria — seguro por padrão, sob revisão."),
        icon=icon, ck=ck,
        maestro_domain=f"infraestrutura em {name_short}",
        arch_domain=f"arquitetura de infra em {name_short}: {desc}",
        specialists=[
            ("Network & Compute Engineer", R.specialist("Network & Compute Engineer",
                f"Você desenha rede e compute em {name_short}: {desc}. Menor privilégio, "
                f"segmentação, alta disponibilidade.",
                rules="- Nada de 0.0.0.0/0 sem justificativa; nada de secret em texto claro."),
             "blue", "Circuit · rede/compute"),
            ("Data & Storage Engineer", R.specialist("Data & Storage Engineer",
                f"Você desenha dados e armazenamento em {name_short}: bancos gerenciados, "
                f"buckets, cache, backup e retenção.",
                rules="- Criptografia em repouso e em trânsito; backups testados, não só configurados."),
             "green", "Vault · dados/storage"),
        ],
        warden_domain=f"a infra de {name_short}: segurança de rede, IAM, custo e resiliência",
        category="Cloud & Infra",
        portal_url="http://localhost:3000", portal_name="Console/Grafana",
        extra_maestro="\nInfra é código: nada de mudança manual no console que não volte pro repo.",
    )


def fam_iac(tool):
    name_short, desc, ck, icon = tool
    return _team_pipeline(
        name=f"IaC · {name_short}",
        description=(f"Infraestrutura como código com {name_short} ({desc}): módulos, plan/apply "
                     f"revisados, policy-as-code e testes de infra. Nada aplicado sem revisão."),
        icon=icon, ck=ck,
        maestro_domain=f"IaC com {name_short}",
        arch_domain=f"módulos e estado de {name_short}: {desc}",
        specialists=[
            ("Module Author", R.specialist("Module Author",
                f"Você escreve módulos {name_short} reutilizáveis e compõe ambientes. "
                f"Estado remoto com lock; sem recurso órfão.",
                rules="- `plan` limpo e revisado antes de qualquer `apply`; nunca aplique você mesmo em prod."),
             "purple", "Forge · módulos"),
            ("Policy Engineer", R.specialist("Policy Engineer",
                f"Você escreve policy-as-code ({desc.split('+')[-1].strip()}) e testes de infra "
                f"que barram config insegura antes do apply.",
                rules="- Toda policy tem um teste que prova que ela bloqueia o caso ruim."),
             "red", "Gate · políticas"),
        ],
        warden_domain=f"o IaC de {name_short}: drift, segurança de estado, blast radius do apply",
        category="IaC", portal_url="http://localhost:3000", portal_name="Plan/CI",
        extra_maestro="\nO `apply` em produção é decisão do usuário; o time entrega o plan revisado.",
        reviewer_cmd=CMD_CODEX,
    )


def fam_database(db):
    name_short, desc, ck, icon = db
    return _team_pipeline(
        name=f"Database · {name_short}",
        description=(f"Modela, indexa, migra e tuna {name_short} ({desc}): schema, migrações "
                     f"expand-contract, índices sob evidência e revisão de performance."),
        icon=icon, ck=ck,
        maestro_domain=f"trabalho de banco de dados em {name_short}",
        arch_domain=f"modelagem e migração em {name_short}: {desc}",
        specialists=[
            ("Schema & Migration Engineer", R.specialist("Schema & Migration Engineer",
                f"Você modela e migra {name_short} com segurança: expand-contract, migrações "
                f"reversíveis, sem lock longo em tabela quente.",
                rules="- Toda migração é testada num dump realista antes de tocar produção."),
             "blue", "Schema · modelagem"),
            ("Query & Index Tuner", R.specialist("Query & Index Tuner",
                f"Você tuna queries e índices em {name_short} com base em planos de execução "
                f"reais, não palpite.",
                rules="- Cite EXPLAIN/plano antes e depois; um índice novo precisa de justificativa por evidência."),
             "green", "Index · performance"),
        ],
        warden_domain=f"o banco {name_short}: integridade, segurança de migração, regressão de performance",
        category="Database", portal_url="http://localhost:8081", portal_name="DB Console",
    )


def fam_data_pipeline(pipe):
    name_short, desc, ck, icon = pipe
    return _team_pipeline(
        name=f"Data Pipeline · {name_short}",
        description=(f"Constrói um pipeline de dados {name_short} ({desc}) com qualidade de "
                     f"dados, idempotência, backfill seguro e observabilidade."),
        icon=icon, ck=ck,
        maestro_domain=f"pipeline de dados {name_short}",
        arch_domain=f"desenho do pipeline {name_short}: {desc}, contratos de dados e SLAs",
        specialists=[
            ("Ingestion Engineer", R.specialist("Ingestion Engineer",
                f"Você constrói ingestão e transformação em {name_short}: idempotente, "
                f"reprocessável, com contratos de schema.",
                rules="- Reprocessar não pode duplicar; toda etapa é idempotente por design."),
             "orange", "Intake · ingestão"),
            ("Data Quality Engineer", R.specialist("Data Quality Engineer",
                f"Você garante qualidade de dados no {name_short}: testes de dados, detecção de "
                f"anomalia, freshness e lineage.",
                rules="- Um teste de qualidade que nunca falha não prova nada; teste os casos ruins."),
             "purple", "Assay · qualidade"),
        ],
        warden_domain=f"o pipeline {name_short}: corretude dos dados, idempotência, custo e SLA",
        category="Data Pipeline", portal_url="http://localhost:8080", portal_name="Orchestrator UI",
    )


def fam_ai(feature):
    name_short, desc, ck, icon = feature
    return _team_pipeline(
        name=f"AI Feature · {name_short}",
        description=(f"Constrói uma feature de IA {name_short} ({desc}) com avaliação (evals) de "
                     f"primeira classe, guardrails e verificação viva — não só 'parece bom'."),
        icon=icon, ck=ck,
        maestro_domain=f"feature de IA: {name_short}",
        arch_domain=f"arquitetura da feature de IA {name_short}: {desc}, incluindo o plano de avaliação",
        specialists=[
            ("AI Engineer", R.specialist("AI Engineer",
                f"Você implementa {name_short}: {desc}. Prompts versionados, saídas estruturadas "
                f"validadas, custo e latência sob controle.",
                rules="- Nada de alegar qualidade sem eval; toda mudança de prompt passa pelo conjunto de avaliação."),
             "indigo", "Synapse · IA"),
            ("Eval & Guardrails Engineer", R.specialist("Eval & Guardrails Engineer",
                f"Você constrói o conjunto de avaliação e os guardrails de {name_short}: dataset de "
                f"referência, métricas, testes adversariais, mitigação de injeção de prompt.",
                rules="- Um eval que só mede casos fáceis é teatro; inclua os casos difíceis e adversariais."),
             "pink", "Rubric · evals"),
        ],
        warden_domain=f"a feature de IA {name_short}: qualidade medida, segurança de prompt, custo, alucinação",
        category="AI Feature", portal_url="http://localhost:5173", portal_name="AI Playground",
        extra_maestro="\nNunca alegue qualidade de modelo sem evidência de eval. 'Parece bom' não é métrica.",
    )


def fam_migration(mig):
    name_short, desc, ck, icon = mig
    return _team_pipeline(
        name=f"Migração · {name_short}",
        description=(f"Executa a migração {name_short} ({desc}) de forma incremental e reversível, "
                     f"com paridade verificada a cada passo e rollback sempre possível."),
        icon=icon, ck=ck,
        maestro_domain=f"migração: {name_short}",
        arch_domain=f"estratégia de migração {name_short}: {desc}, com fatias reversíveis e ordem segura",
        specialists=[
            ("Migration Engineer", R.specialist("Migration Engineer",
                f"Você executa a migração {name_short} em incrementos pequenos e reversíveis, "
                f"mantendo o velho e o novo funcionando lado a lado enquanto durar.",
                rules="- Cada passo é reversível e mantém a suíte verde; nada de big-bang."),
             "indigo", "Shift · migração"),
            ("Parity Verifier", R.specialist("Parity Verifier",
                f"Você prova paridade entre o comportamento antigo e o novo a cada passo de "
                f"{name_short}: testes de característica, comparação de saída, sem regressão.",
                rules="- Paridade é provada com evidência (diff de saída, testes), não assumida."),
             "green", "Mirror · paridade"),
        ],
        warden_domain=f"a migração {name_short}: reversibilidade, paridade e ausência de regressão",
        category="Migração", portal_url="http://localhost:5173", portal_name="Antes/Depois",
    )


def fam_mobile(platform):
    name_short, desc, ck, icon = platform
    return _team_pipeline(
        name=f"Ship Mobile · {name_short}",
        description=(f"Entrega uma feature mobile em {name_short} ({desc}) com verificação viva "
                     f"em simulador/emulador via portal de dispositivo, acessibilidade e release."),
        icon=icon, ck=ck,
        maestro_domain=f"entrega mobile em {name_short}",
        arch_domain=f"feature mobile em {name_short}: {desc}, navegação, estado e camada de dados",
        specialists=[
            ("Mobile Engineer", R.implementer(f"{desc}",
                extra="\nAtenção a ciclo de vida, offline, e diferenças de plataforma."),
             "pink", "Rivet · app"),
            ("Mobile QA & A11y", R.specialist("Mobile QA & A11y",
                f"Você verifica a feature em {name_short} no portal de dispositivo: fluxos reais, "
                f"acessibilidade (VoiceOver/TalkBack), alvos de toque, estados de erro.",
                rules="- Verifique no dispositivo/simulador de verdade, não só no código."),
             "orange", "Argus · QA/a11y"),
        ],
        warden_domain=f"a feature mobile em {name_short}: correção, a11y e prontidão de release",
        category="Ship Mobile", portal_url="http://localhost:19000", portal_name="Device",
    )


def fam_docs(kind):
    name_short, desc, ck, icon = kind
    return _team_pipeline(
        name=f"Documentação · {name_short}",
        description=(f"Produz {name_short.lower()} ({desc}) verificada contra o código: nada de "
                     f"doc que mente. Escritor redige, verificador confirma cada afirmação."),
        icon=icon, ck=ck,
        maestro_domain=f"documentação: {name_short}",
        arch_domain=f"estrutura da documentação {name_short}: {desc}, público-alvo e escopo",
        specialists=[
            ("Doc Writer", R.specialist("Doc Writer",
                f"Você escreve {name_short.lower()}: {desc}. Claro, com exemplos que rodam, "
                f"organizado para quem vai usar.",
                rules="- Todo exemplo de código foi executado; nada de trecho que você não rodou."),
             "blue", "Quill · escrita"),
            ("Doc Verifier", R.specialist("Doc Verifier",
                f"Você confere cada afirmação da doc contra o código real: nomes, flags, endpoints, "
                f"comportamento. Divergência é achado.",
                rules="- Uma afirmação não verificável contra o código é marcada como tal, não publicada."),
             "green", "Fact · verificação"),
        ],
        warden_domain=f"a documentação {name_short}: exatidão contra o código e utilidade",
        category="Documentação", portal_url="http://localhost:3000", portal_name="Docs preview",
        reviewer_cmd=CMD_GEMINI,
    )


def fam_cicd(tool):
    name_short, desc, ck, icon = tool
    return _team_pipeline(
        name=f"CI/CD · {name_short}",
        description=(f"Desenha um pipeline de CI/CD em {name_short} ({desc}): rápido, seguro e "
                     f"reproduzível, com gates de qualidade e deploy progressivo."),
        icon=icon, ck=ck,
        maestro_domain=f"CI/CD com {name_short}",
        arch_domain=f"pipeline {name_short}: {desc}, estágios, gates e estratégia de deploy",
        specialists=[
            ("Pipeline Engineer", R.specialist("Pipeline Engineer",
                f"Você constrói o pipeline {name_short}: {desc}. Rápido por cache e paralelismo, "
                f"seguro por OIDC e menor privilégio.",
                rules="- Sem segredo de longa duração no CI; credenciais são efêmeras (OIDC) onde der."),
             "blue", "Loop · pipeline"),
            ("Release & Rollback Engineer", R.specialist("Release & Rollback Engineer",
                f"Você desenha deploy progressivo e rollback em {name_short}: canário, health "
                f"gates, rollback automático, migração segura.",
                rules="- Todo deploy tem um rollback testado; um deploy sem volta não sobe."),
             "green", "Cutover · deploy"),
        ],
        warden_domain=f"o pipeline {name_short}: segurança de supply chain, reprodutibilidade, segurança de rollback",
        category="CI/CD", portal_url="http://localhost:3000", portal_name="CI Dashboard",
    )


def fam_k8s(work):
    name_short, desc, ck, icon = work
    return _team_pipeline(
        name=f"Kubernetes · {name_short}",
        description=(f"Trabalho de Kubernetes: {name_short} ({desc}). Manifestos revisados, "
                     f"segurança de pod e rede, e verificação viva no cluster."),
        icon=icon, ck=ck,
        maestro_domain=f"Kubernetes: {name_short}",
        arch_domain=f"desenho de {name_short} em Kubernetes: {desc}",
        specialists=[
            ("Platform Engineer", R.specialist("Platform Engineer",
                f"Você implementa {name_short} em K8s: {desc}. Requests/limits sãos, health "
                f"probes reais, rollout seguro.",
                rules="- Sem `latest` em imagem; requests/limits e probes em todo workload."),
             "blue", "Helm · manifestos"),
            ("Cluster Security Engineer", R.specialist("Cluster Security Engineer",
                f"Você endurece a superfície de {name_short}: PSA, NetworkPolicy, RBAC mínimo, "
                f"OPA/Gatekeeper, imagens sem root.",
                rules="- NetworkPolicy default-deny; nenhum container roda como root sem justificativa."),
             "red", "Bastion · segurança"),
        ],
        warden_domain=f"o trabalho de K8s ({name_short}): segurança, resiliência e correção do rollout",
        category="Kubernetes", portal_url="http://localhost:8001", portal_name="K8s Dashboard",
    )


def fam_a11y(surface):
    name_short, desc, ck, icon = surface
    return _team_pipeline(
        name=f"Acessibilidade · {name_short}",
        description=(f"Auditoria e correção de acessibilidade de {desc}, contra WCAG 2.2 AA, com "
                     f"verificação viva no portal (teclado, foco, leitor de tela)."),
        icon=icon, ck=ck,
        maestro_domain=f"acessibilidade de {name_short}",
        arch_domain=f"plano de acessibilidade para {desc}: fluxos críticos e critérios WCAG 2.2 AA",
        specialists=[
            ("A11y Engineer", R.specialist("A11y Engineer",
                f"Você conserta acessibilidade de {desc}: HTML semântico, ARIA só onde precisa, "
                f"teclado completo, foco visível e gerenciado, contraste.",
                rules="- ARIA só onde a semântica nativa não alcança; nada de div clicável sem papel/teclado."),
             "green", "Access · correção"),
            ("Assistive Tech Verifier", R.specialist("Assistive Tech Verifier",
                f"Você verifica {desc} com tecnologia assistiva de verdade no portal: navegação por "
                f"teclado, ordem de foco, anúncios de leitor de tela, reduced motion.",
                rules="- Verifique com AT real no portal; um 'acho que lê certo' não conta."),
             "purple", "Echo · verificação"),
        ],
        warden_domain=f"a acessibilidade de {name_short} contra WCAG 2.2 AA",
        category="Acessibilidade", portal_url="http://localhost:5173", portal_name="A11y target",
        reviewer_cmd=CMD_GEMINI,
    )


def fam_api(style):
    name_short, desc, ck, icon = style
    return _team_pipeline(
        name=f"API Contract · {name_short}",
        description=(f"Desenha um contrato de API {name_short} ({desc}) design-first, com testes de "
                     f"contrato, versionamento e evolução sem quebrar consumidores."),
        icon=icon, ck=ck,
        maestro_domain=f"contrato de API {name_short}",
        arch_domain=f"design-first do contrato {name_short}: {desc}",
        contract_note="api-contract",
        specialists=[
            ("API Designer", R.specialist("API Designer",
                f"Você desenha o contrato {name_short}: {desc}. Consistente, versionável, com erros "
                f"e paginação bem definidos.",
                rules="- Design-first: o contrato existe e é revisado antes da implementação."),
             "blue", "Draft · design"),
            ("Contract Test Engineer", R.specialist("Contract Test Engineer",
                f"Você escreve testes de contrato para {name_short} que barram breaking changes "
                f"antes que cheguem a um consumidor.",
                rules="- Um breaking change tem que quebrar um teste de contrato, não um cliente em produção."),
             "green", "Pact · contract tests"),
        ],
        warden_domain=f"o contrato {name_short}: compatibilidade retroativa e consistência",
        category="API Contract", portal_url="http://localhost:8080", portal_name="API Explorer",
    )


def fam_perf(layer):
    name_short, desc, ck, icon = layer
    return _team_pipeline(
        name=f"Performance · {name_short}",
        description=(f"Otimiza performance de {name_short} ({desc}) guiado por medição: profile "
                     f"primeiro, otimize o gargalo real, prove o ganho com número."),
        icon=icon, ck=ck,
        maestro_domain=f"performance de {name_short}",
        arch_domain=f"plano de performance para {name_short}: {desc}, orçamento e métricas-alvo",
        specialists=[
            ("Performance Engineer", R.specialist("Performance Engineer",
                f"Você otimiza {name_short}: {desc}. Meça antes de mexer; ataque o gargalo real, "
                f"não o que parece lento.",
                rules="- Nenhuma otimização entra sem número antes/depois que prova o ganho."),
             "blue", "Throttle · otimização"),
            ("Benchmark & Profiling Engineer", R.specialist("Benchmark & Profiling Engineer",
                f"Você monta benchmarks e profiling reproduzíveis para {name_short} e guarda contra "
                f"regressão de performance.",
                rules="- Benchmark reproduzível e estável; ruído de medição vira achado, não conclusão."),
             "purple", "Gauge · benchmark"),
        ],
        warden_domain=f"a performance de {name_short}: ganho real provado e ausência de regressão",
        category="Performance", portal_url="http://localhost:5173", portal_name="Profiler/Metrics",
    )


# ===========================================================================
# FAMÍLIA — Red Team (SOMENTE escopo autorizado)
# ===========================================================================

def fam_pentest(scope):
    name_short, toolkit, ck, icon = scope
    p = Partitura(
        name=f"Red Team · {name_short}",
        description=(f"Engajamento de segurança ofensiva AUTORIZADO na superfície {name_short} "
                     f"({toolkit}). Só escopo autorizado, nunca produção, nunca dados de pessoas "
                     f"reais — achados com evidência, nunca correções ou dano."),
        icon=icon, color=COLORS[ck],
    )
    p.role("Red Team Lead", R.redteam_lead(f"superfície {name_short} ({toolkit})"), color=COLORS["red"])
    p.role("Recon Operator", R.redteam_operator(f"{name_short} — recon e enumeração", toolkit), color=COLORS["orange"])
    p.role("Validation Operator", R.redteam_operator(f"{name_short} — validação de vulnerabilidades", toolkit), color=COLORS["pink"])
    p.role("Reporting Analyst", R.specialist("Reporting Analyst",
        "Você consolida achados do engajamento AUTORIZADO em um relatório acionável: severidade, "
        "impacto no escopo, reprodução e remediação. Você não ataca; você organiza e comunica.",
        rules="- Só dados sintéticos na evidência; nenhum dado real de pessoa. Sem exploit weaponizado."),
        color=COLORS["purple"])

    m = p.terminal("Lead · red team", role="Red Team Lead", manager=True, command=CMD_FABLE)
    pos = grid_positions(3, cols=3, gx=980, y0=820)
    recon = p.terminal("Scout · recon", role="Recon Operator", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    val = p.terminal("Pry · validação", role="Validation Operator", command=CMD_OPUS, x=pos[1][0], y=pos[1][1])
    rep = p.terminal("Scribe · relatório", role="Reporting Analyst", command=CMD_OPUS, x=pos[2][0], y=pos[2][1])

    roe = p.note("rules-of-engagement.md", R.RULES_OF_ENGAGEMENT_EMPTY, x=1320, y=-400, color="red", h=460)
    plan = p.note("engagement-plan.md", R.ENGAGEMENT_PLAN_EMPTY, x=1900, y=-400, color="orange", h=460)
    findings = p.note("findings.md", R.FINDINGS_EMPTY, x=1320, y=100, color="yellow", w=1180, h=300)
    portal = p.portal("Alvo (autorizado)", "http://localhost:8080", x=-1460, y=-1080)

    hub_layout(p, m, [recon, val, rep], note_nodes=[roe, plan, findings])
    p.connect_portal(p.portal_node_id("Alvo (autorizado)"), m)
    p.connect_portal(p.portal_node_id("Alvo (autorizado)"), val)
    return save(p, "Red Team")


# ===========================================================================
# FAMÍLIA — Solo (um especialista por vez)
# ===========================================================================

def fam_solo(spec):
    name_short, focus, ck, icon = spec
    p = Partitura(
        name=f"Solo · {name_short}",
        description=(f"Um único especialista ({name_short}) trabalhando sozinho: {focus}. "
                     f"Planeja, executa e verifica você mesmo, com um portal para checar o resultado."),
        icon=icon, color=COLORS[ck],
    )
    p.role(name_short, R.solo_specialist(name_short, f"Foco: {focus}."), color=COLORS[ck])
    t = p.terminal(f"{name_short}", role=name_short, manager=False, command=CMD_OPUS)
    scratch = p.note("scratchpad.md",
                     f"# scratchpad — {name_short}\n\nSeu caderno: plano, decisões, o que verificou e o "
                     "que ficou em aberto. É a fonte de verdade entre sessões.",
                     x=1120, y=-40, color="yellow")
    portal = p.portal("Proving Ground", "http://localhost:5173", x=1120, y=380)
    p.connect_note(scratch, t)
    p.connect_portal(p.portal_node_id("Proving Ground"), t)
    return save(p, "Solo")


# ===========================================================================
# FAMÍLIA — Duelo de Agentes (claude × codex × gemini)
# ===========================================================================

def fam_duel(duel):
    name_short, focus, ck, icon = duel
    p = Partitura(
        name=f"Duelo de Agentes · {name_short}",
        description=(f"Três modelos diferentes atacam o mesmo problema ({focus}) em paralelo; um "
                     f"Juiz escolhe, combina e entrega. Modelos distintos erram distinto — o "
                     f"melhor de cada um vence."),
        icon=icon, color=COLORS[ck],
    )
    p.role("Juiz", R.judge(focus), color=COLORS["yellow"])
    p.role("Duelista · Claude", R.duelist("Claude/Opus", focus), color=COLORS["blue"])
    p.role("Duelista · Codex", R.duelist("Codex", focus), color=COLORS["gray"])
    p.role("Duelista · Gemini", R.duelist("Gemini", focus), color=COLORS["green"])

    m = p.terminal("Juiz", role="Juiz", manager=True, command=CMD_FABLE)
    pos = grid_positions(3, cols=3, gx=980, y0=820)
    d1 = p.terminal("Claude · duelista", role="Duelista · Claude", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    d2 = p.terminal("Codex · duelista", role="Duelista · Codex", command=CMD_CODEX, x=pos[1][0], y=pos[1][1])
    d3 = p.terminal("Gemini · duelista", role="Duelista · Gemini", command=CMD_GEMINI, x=pos[2][0], y=pos[2][1])

    arena = p.note("arena.md",
                   f"# arena — {name_short}\n\n## Problema\n{focus}\n\n## Critério de aceite\n"
                   "(o Juiz define, igual para todos)\n\n## Soluções\n- Claude:\n- Codex:\n- Gemini:\n\n"
                   "## Veredito\n(quem ganhou, o que foi combinado, risco residual)",
                   x=1300, y=-360, color="purple")
    portal = p.portal("Bancada", "http://localhost:5173", x=-1440, y=-1060)
    hub_layout(p, m, [d1, d2, d3], note_nodes=[arena])
    p.connect_portal(p.portal_node_id("Bancada"), m)
    return save(p, "Duelo de Agentes")


# ===========================================================================
# FAMÍLIA — War Room (incidentes)
# ===========================================================================

def fam_incident(inc):
    name_short, desc, ck, icon = inc
    p = Partitura(
        name=f"War Room · {name_short}",
        description=(f"Sala de guerra para {desc}. Comandante organiza a resposta; trilhas de "
                     f"investigação, mitigação e comunicação em paralelo. Mitigar primeiro, "
                     f"causa raiz depois, post-mortem sem culpa."),
        icon=icon, color=COLORS[ck],
    )
    p.role("Incident Commander", R.incident_commander(desc), color=COLORS["red"])
    p.role("Investigator", R.specialist("Investigador de Incidente",
        f"Você acha o que quebrou em {desc}: logs, métricas, mudanças recentes, correlação. Você "
        "reporta hipóteses testadas com evidência, não palpites.",
        rules="- Separe confirmado de suspeito; toda hipótese descartada fica registrada na timeline."),
        color=COLORS["orange"])
    p.role("Mitigation Engineer", R.specialist("Engenheiro de Mitigação",
        f"Você para o sangramento de {desc} agora: rollback, feature-flag, escala, isolamento — "
        "mesmo que feio. Elegância vem depois.",
        rules="- Estabilizar antes de embelezar; registre toda ação com hora e prove que reduziu a dor."),
        color=COLORS["blue"])
    p.role("Comms Lead", R.specialist("Líder de Comunicação",
        f"Você mantém quem precisa saber informado sobre {desc}: status claro, honesto, sem jargão, "
        "no ritmo certo. Você não conserta; você comunica.",
        rules="- Comunicação externa passa por aprovação humana via `maestri notify`."),
        color=COLORS["purple"])

    m = p.terminal("IC · comando", role="Incident Commander", manager=True, command=CMD_FABLE)
    pos = grid_positions(3, cols=3, gx=980, y0=820)
    inv = p.terminal("Trace · investigação", role="Investigator", command=CMD_OPUS, x=pos[0][0], y=pos[0][1])
    mit = p.terminal("Clamp · mitigação", role="Mitigation Engineer", command=CMD_OPUS, x=pos[1][0], y=pos[1][1])
    com = p.terminal("Herald · comunicação", role="Comms Lead", command=CMD_OPUS, x=pos[2][0], y=pos[2][1])

    timeline = p.note("incident-timeline.md", R.INCIDENT_TIMELINE_EMPTY, x=1300, y=-380, color="red", h=440)
    portal = p.portal("Dashboards", "http://localhost:3000", x=-1440, y=-1060)
    hub_layout(p, m, [inv, mit, com], note_nodes=[timeline])
    p.connect_portal(p.portal_node_id("Dashboards"), m)
    p.connect_portal(p.portal_node_id("Dashboards"), inv)
    return save(p, "War Room")


# ===========================================================================
# ÁREAS DE NEGÓCIO — times genéricos (não-código) inspirados nas divisões de
# catálogos de agentes como o agency-agents, adaptados ao Maestri.
# ===========================================================================

def _area_team(area, name, description, icon, ck, orchestrator_domain, deliverable,
               strategist_focus, specialists, reviewer_lane, category,
               portal_url="https://example.com", portal_name="Verificação",
               reviewer_cmd=CMD_CODEX, extra_orch=""):
    """Monta um time de área: Maestro (fable) + Estrategista (opus) + N
    especialistas (opus) + Revisor (codex/gemini), com briefing + board + findings
    e um portal para verificação viva na web. `specialists` é uma lista de
    (role_name, prompt, colorkey, terminal_name)."""
    p = Partitura(name=name, description=description, icon=icon, color=COLORS[ck])
    area_label = AREAS[area][0]
    p.role("Maestro", R.area_orchestrator(area_label.lower(), deliverable, extra=extra_orch),
           color=COLORS["pink"])
    p.role("Estrategista", R.area_strategist(area_label.lower(), strategist_focus),
           color=COLORS["indigo"])
    for rn, pr, cc, _tn in specialists:
        p.role(rn, pr, color=COLORS[cc])
    p.role("Revisor", R.area_reviewer(area_label.lower(), reviewer_lane), color=COLORS["orange"])

    n_workers = len(specialists) + 2
    m = p.terminal("Maestro", role="Maestro", manager=True, command=CMD_FABLE)
    pos = grid_positions(n_workers, cols=4, gx=940, gy=780, y0=820)
    tids = [p.terminal("Estrategista · briefing", role="Estrategista", command=CMD_OPUS,
                       x=pos[0][0], y=pos[0][1])]
    for i, (rn, _pr, _cc, tn) in enumerate(specialists, start=1):
        tids.append(p.terminal(tn, role=rn, command=CMD_OPUS, x=pos[i][0], y=pos[i][1]))
    wd = p.terminal("Revisor · achados", role="Revisor", command=reviewer_cmd,
                    x=pos[n_workers - 1][0], y=pos[n_workers - 1][1])
    tids.append(wd)

    brief = p.note("briefing.md", R.AREA_BRIEF_EMPTY, x=1300, y=-380, color="blue")
    board = p.note("board.md", R.AREA_BOARD_EMPTY, x=1880, y=-380, color="green")
    findings = p.note("findings.md", R.AREA_FINDINGS_EMPTY, x=1300, y=-40, color="yellow")
    portal = p.portal(portal_name, portal_url, x=-1460, y=-1080)

    hub_layout(p, m, tids, note_nodes=[brief, board, findings])
    p.connect_portal(p.portal_node_id(portal_name), m)
    p.connect_portal(p.portal_node_id(portal_name), wd)
    return save(p, category, area=area)


def _sp(area, title, focus, cc, tn, rules=""):
    return (title, R.area_specialist(area, title, focus, rules=rules), cc, tn)


# ---- Design & UX ----------------------------------------------------------
DESIGN = [
    ("Design System", "biblioteca de componentes, tokens e documentação viva", "purple", "square.grid.2x2"),
    ("Redesign de Fluxo", "repensar um fluxo confuso ponta a ponta com base em evidência", "blue", "arrow.triangle.branch"),
    ("Pesquisa de UX", "entrevistas, testes de usabilidade e síntese de insights", "teal", "person.2"),
    ("Landing Page", "página de conversão: proposta de valor, prova, CTA", "orange", "rectangle.on.rectangle"),
    ("Auditoria de UI", "auditar consistência visual, hierarquia e acessibilidade", "pink", "magnifyingglass"),
]


def fam_design(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "design", f"Design & UX · {name_short}",
        f"Time de design para {desc}. Estrategista escreve o briefing, especialistas produzem, "
        f"o revisor confere consistência e acessibilidade ao vivo no portal.",
        icon, ck, f"design ({name_short})", "um design pronto e verificado",
        f"design de {name_short}: {desc}",
        [
            _sp("design", "UI Designer", f"Você desenha a interface de {name_short}: {desc}. "
                "Hierarquia visual, tokens, estados, consistência.", "blue", "Pixel · UI",
                rules="- Acessibilidade (contraste, foco, alvos de toque) é requisito, não enfeite."),
            _sp("design", "UX Researcher", f"Você embasa {name_short} em evidência de usuário: "
                "hipóteses, testes, síntese. Sem inventar dado de pesquisa.", "teal", "Lens · UX",
                rules="- Todo insight rastreia até uma observação real; opinião é marcada como opinião."),
        ],
        "consistência visual e acessibilidade", "Design & UX",
        portal_url="http://localhost:5173", portal_name="Preview/Figma",
        reviewer_cmd=CMD_GEMINI,
    )


# ---- Produto --------------------------------------------------------------
PRODUTO = [
    ("Discovery", "descobrir o problema certo antes de construir a solução", "indigo", "sparkles"),
    ("Roadmap & Priorização", "priorizar por impacto e esforço com critério explícito", "blue", "list.number"),
    ("PRD / Spec", "escrever o documento de requisitos que o time constrói sem drift", "green", "doc.text"),
    ("Síntese de Feedback", "transformar feedback bruto em temas e decisões", "orange", "bubble.left.and.bubble.right"),
    ("Análise de Concorrência", "mapear concorrentes, lacunas e posicionamento", "purple", "chart.bar.doc.horizontal"),
]


def fam_product(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "produto", f"Produto · {name_short}",
        f"Time de produto para {desc}. Do problema ao documento, com evidência e revisão adversarial.",
        icon, ck, f"produto ({name_short})", "uma decisão de produto sustentada",
        f"produto: {name_short} — {desc}",
        [
            _sp("produto", "Product Manager", f"Você conduz {name_short}: {desc}. Foca no problema, "
                "no usuário e no resultado, não na feature favorita.", "blue", "Compass · PM",
                rules="- Toda prioridade tem um porquê explícito (impacto × esforço × risco)."),
            _sp("produto", "Product Analyst", f"Você traz os dados de {name_short}: métricas, "
                "feedback, concorrência. Números com fonte, não palpite.", "green", "Signal · dados",
                rules="- Nenhuma afirmação de mercado sem fonte; o que não dá pra sustentar vira pergunta."),
        ],
        "clareza do problema e sustentação por evidência", "Produto",
        portal_url="https://news.ycombinator.com", portal_name="Mercado/Concorrência",
    )


# ---- Marketing & Conteúdo -------------------------------------------------
MARKETING = [
    ("Campanha de Lançamento", "planejar e executar um lançamento multicanal", "orange", "megaphone"),
    ("SEO & Conteúdo", "estratégia de conteúdo orientada a busca e intenção", "green", "magnifyingglass"),
    ("Social Media", "calendário e peças para redes, por plataforma", "pink", "bubble.left"),
    ("E-mail de Ciclo de Vida", "sequências de onboarding, ativação e retenção", "blue", "envelope"),
    ("Blog Técnico", "artigo técnico correto, útil e verificado contra o código", "indigo", "doc.richtext"),
]


def fam_marketing(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "marketing", f"Marketing · {name_short}",
        f"Time de marketing/conteúdo para {desc}. Briefing de mensagem, produção em paralelo, "
        f"revisão de marca e fato, verificação viva no portal.",
        icon, ck, f"marketing ({name_short})", "conteúdo pronto e alinhado à marca",
        f"marketing: {name_short} — {desc}",
        [
            _sp("marketing", "Content Strategist", f"Você define ângulo e estrutura de {name_short}: "
                f"{desc}. Mensagem clara para o público certo.", "orange", "Angle · estratégia",
                rules="- O ângulo serve ao público e ao objetivo, não ao hype."),
            _sp("marketing", "Copywriter", f"Você escreve as peças de {name_short}: claras, honestas, "
                "no tom da marca. Sem promessa que o produto não cumpre.", "pink", "Ink · copy",
                rules="- Nada de claim sem lastro; afirmação factual passa pelo revisor."),
        ],
        "alinhamento de marca e exatidão factual", "Marketing & Conteúdo",
        portal_url="https://example.com", portal_name="Peça publicada",
        reviewer_cmd=CMD_GEMINI,
    )


# ---- Vendas ---------------------------------------------------------------
VENDAS = [
    ("Prospecção Outbound", "sequências multicanal baseadas em sinal", "green", "paperplane"),
    ("Proposta / RFP", "resposta a RFP com temas de ganho e prova", "blue", "doc.text"),
    ("Sales Enablement", "materiais que ajudam o time a vender melhor", "orange", "books.vertical"),
    ("Preparo de Discovery", "roteiro de descoberta e qualificação (SPIN/MEDDPICC)", "purple", "list.bullet.clipboard"),
]


def fam_sales(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "vendas", f"Vendas · {name_short}",
        f"Time de vendas para {desc}. Mensagem sob medida, produção em paralelo, revisão de "
        f"precisão e conformidade.",
        icon, ck, f"vendas ({name_short})", "material de vendas pronto e preciso",
        f"vendas: {name_short} — {desc}",
        [
            _sp("vendas", "Account Strategist", f"Você desenha a abordagem de {name_short}: {desc}. "
                "Foco no problema do cliente, não no seu produto.", "blue", "Reach · estratégia",
                rules="- Personalização por sinal real; nada de spray-and-pray."),
            _sp("vendas", "Sales Writer", f"Você escreve as peças de {name_short}: diretas, "
                "específicas, honestas. Sem promessa fora do que foi aprovado.", "orange", "Pitch · copy",
                rules="- Nenhum número ou caso de cliente sem aprovação e fonte."),
        ],
        "precisão da mensagem e conformidade", "Vendas",
        portal_url="https://example.com", portal_name="Conta/Concorrente",
    )


# ---- Dados & Analytics ----------------------------------------------------
DADOS = [
    ("Dashboard de BI", "painel confiável com métricas definidas e testadas", "blue", "chart.bar"),
    ("Análise Exploratória", "explorar dados para responder uma pergunta de negócio", "purple", "chart.xyaxis.line"),
    ("Modelagem de Métricas", "definir métricas em dbt/semantic layer, sem ambiguidade", "green", "function"),
    ("Experimento A/B", "desenhar, rodar e ler um experimento com rigor estatístico", "orange", "flask"),
]


def fam_analytics(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "dados", f"Dados & Analytics · {name_short}",
        f"Time de dados para {desc}. Definição antes de número, análise em paralelo, revisão "
        f"estatística adversarial. Nenhum número sem fonte e definição.",
        icon, ck, f"analytics ({name_short})", "uma análise confiável e reprodutível",
        f"analytics: {name_short} — {desc}",
        [
            _sp("dados", "Data Analyst", f"Você produz {name_short}: {desc}. Toda métrica tem "
                "definição escrita e query reproduzível.", "blue", "Query · análise",
                rules="- Nenhum número no dashboard sem definição e fonte rastreável."),
            _sp("dados", "Analytics Engineer", f"Você modela e testa os dados de {name_short}: "
                "camada semântica, testes de dados, freshness.", "green", "Model · dbt",
                rules="- Um teste de dados que nunca falha não prova nada; teste os casos ruins."),
        ],
        "corretude estatística e reprodutibilidade", "Dados & Analytics",
        portal_url="http://localhost:3000", portal_name="Dashboard/Notebook",
    )


# ---- Segurança & Compliance (governança, distinto do Red Team técnico) ----
SEGURANCA = [
    ("Auditoria LGPD", "mapear dados pessoais, bases legais e direitos do titular", "red", "lock.shield"),
    ("Prontidão SOC 2", "levantar controles, gaps e evidências para SOC 2", "orange", "checkmark.shield"),
    ("Threat Modeling", "modelar ameaças de um sistema (STRIDE) e mitigações", "pink", "exclamationmark.shield"),
    ("Resposta a Incidente (SecOps)", "playbook e condução de um incidente de segurança", "purple", "bell.badge"),
]


def fam_compliance(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "seguranca", f"Segurança & Compliance · {name_short}",
        f"Time de segurança/governança para {desc}. Levanta, documenta e recomenda — achados com "
        f"evidência, nunca alegação sem lastro. Só escopo autorizado.",
        icon, ck, f"segurança e compliance ({name_short})", "um relatório de conformidade acionável",
        f"segurança/compliance: {name_short} — {desc}",
        [
            _sp("seguranca", "Compliance Analyst", f"Você conduz {name_short}: {desc}. Mapeia contra "
                "o framework, aponta gaps com evidência e recomenda remediação.", "red", "Ledger · controles",
                rules="- Um controle só é 'atendido' com evidência; intenção não conta. Só escopo autorizado."),
            _sp("seguranca", "Security Architect", f"Você avalia o desenho de {name_short} por risco: "
                "superfícies, confiança, dados sensíveis, mitigações.", "orange", "Bastion · risco",
                rules="- Nunca exponha exploit; o produto é achado + mitigação, não dano."),
        ],
        "rastreabilidade de evidência e escopo", "Segurança & Compliance",
        portal_url="https://example.com", portal_name="Sistema (autorizado)",
    )


# ---- Financeiro -----------------------------------------------------------
FINANCEIRO = [
    ("Fechamento Mensal", "conciliação e fechamento com trilha de auditoria", "green", "calendar"),
    ("Modelagem Financeira", "modelo de projeção com premissas explícitas e cenários", "blue", "chart.line.uptrend.xyaxis"),
    ("FP&A / Orçamento", "orçamento, forecast e análise de variação", "orange", "chart.pie"),
    ("Due Diligence", "análise de valuation e riscos de um investimento", "purple", "doc.text.magnifyingglass"),
]


def fam_finance(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "financeiro", f"Financeiro · {name_short}",
        f"Time financeiro para {desc}. Premissa antes de número, análise em paralelo, revisão "
        f"adversarial de premissas e aritmética. Nenhum número sem fonte.",
        icon, ck, f"financeiro ({name_short})", "uma análise financeira sustentada",
        f"financeiro: {name_short} — {desc}",
        [
            _sp("financeiro", "Financial Analyst", f"Você produz {name_short}: {desc}. Premissas "
                "explícitas, cenários, aritmética conferível.", "blue", "Model · análise",
                rules="- Toda premissa é declarada; nenhum número aparece sem fonte ou cálculo mostrado."),
            _sp("financeiro", "Controller", f"Você garante a integridade contábil de {name_short}: "
                "conciliação, trilha de auditoria, conformidade com a norma.", "green", "Ledger · controle",
                rules="- O que não fecha vira achado, não é arredondado para fechar."),
        ],
        "integridade de premissas e aritmética", "Financeiro",
        portal_url="http://localhost:3000", portal_name="Planilha/Painel",
    )


# ---- Jurídico -------------------------------------------------------------
JURIDICO = [
    ("Revisão de Contrato", "revisar cláusulas, riscos e desvios do padrão", "indigo", "doc.text"),
    ("Intake de Cliente", "qualificar e triar um novo caso com checagem de conflito", "blue", "person.badge.plus"),
    ("Análise de Risco & Compliance", "avaliar exposição regulatória e recomendar mitigação", "red", "exclamationmark.triangle"),
]


def fam_legal(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "juridico", f"Jurídico · {name_short}",
        f"Time jurídico de apoio para {desc}. Analisa, sinaliza risco e recomenda — não substitui "
        f"parecer de advogado responsável. Achados com base, nunca invenção.",
        icon, ck, f"jurídico ({name_short})", "uma análise jurídica de apoio, sinalizada",
        f"jurídico: {name_short} — {desc}",
        [
            _sp("juridico", "Legal Analyst", f"Você conduz {name_short}: {desc}. Aponta cláusulas, "
                "riscos e desvios com referência ao texto e ao padrão.", "indigo", "Clause · análise",
                rules="- Toda sinalização cita o trecho; nada de interpretação sem âncora no documento. "
                      "Isto é apoio, não parecer final: recomende revisão humana."),
            _sp("juridico", "Compliance Reviewer", f"Você checa {name_short} contra a norma aplicável: "
                "o que exige atenção, o que é bloqueante.", "red", "Statute · compliance",
                rules="- Não invente jurisprudência nem artigo; o que não confirmar, marca a confirmar."),
        ],
        "fundamentação e sinalização de risco", "Jurídico",
        portal_url="https://example.com", portal_name="Fonte legal",
    )


# ---- Suporte & Sucesso ----------------------------------------------------
SUPORTE = [
    ("Base de Conhecimento", "artigos de ajuda claros e verificados contra o produto", "teal", "questionmark.circle"),
    ("Triagem de Tickets", "classificar, priorizar e rotear tickets com playbook", "blue", "tray.full"),
    ("Onboarding de Cliente", "levar o cliente ao primeiro valor rápido", "green", "figure.walk"),
    ("Health Score & Churn", "medir saúde da conta e agir antes do churn", "orange", "heart.text.square"),
]


def fam_support(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "suporte", f"Suporte & Sucesso · {name_short}",
        f"Time de suporte/sucesso para {desc}. Playbook antes de resposta, execução em paralelo, "
        f"revisão de exatidão e tom. Nada de resposta que o produto não sustenta.",
        icon, ck, f"suporte e sucesso ({name_short})", "uma resposta/artefato de suporte confiável",
        f"suporte/sucesso: {name_short} — {desc}",
        [
            _sp("suporte", "Support Specialist", f"Você produz {name_short}: {desc}. Empático, claro "
                "e correto; verifica o comportamento real antes de afirmar.", "teal", "Aid · suporte",
                rules="- Nenhuma instrução que você não verificou no produto; passo a passo é testado."),
            _sp("suporte", "Customer Success Manager", f"Você olha {name_short} pela lente de "
                "retenção: valor, saúde da conta, próximos passos.", "orange", "Anchor · sucesso",
                rules="- Sinal de churn é achado acionável, não observação solta."),
        ],
        "exatidão da resposta e tom", "Suporte & Sucesso",
        portal_url="http://localhost:5173", portal_name="Produto/Central de ajuda",
        reviewer_cmd=CMD_GEMINI,
    )


# ---- Gestão de Projetos ---------------------------------------------------
GESTAO = [
    ("Planejamento de Sprint", "converter objetivos em um sprint realista e priorizado", "blue", "calendar.badge.clock"),
    ("Coordenação Multi-time", "alinhar dependências entre times com donos e datas", "indigo", "point.3.connected.trianglepath.dotted"),
    ("Ata de Reunião", "transformar uma reunião em decisões e ações com dono", "green", "text.badge.checkmark"),
    ("Retrospectiva", "conduzir uma retro que gera ações concretas, sem culpa", "purple", "arrow.triangle.2.circlepath"),
]


def fam_pmo(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "gestao", f"Gestão · {name_short}",
        f"Time de gestão de projetos para {desc}. Plano antes de execução, coordenação em paralelo, "
        f"revisão de realismo e clareza. Toda ação tem dono e data.",
        icon, ck, f"gestão de projetos ({name_short})", "um plano/artefato de gestão acionável",
        f"gestão: {name_short} — {desc}",
        [
            _sp("gestao", "Project Manager", f"Você conduz {name_short}: {desc}. Escopo realista, "
                "dependências mapeadas, cada item com dono e critério de pronto.", "blue", "Plan · PM",
                rules="- Nada de tarefa órfã; toda ação tem dono, data e definição de pronto."),
            _sp("gestao", "Scrum Facilitator", f"Você facilita {name_short} sem virar dono do "
                "trabalho: remove impedimento, mantém o ritmo, protege o foco.", "purple", "Cadence · facilitação",
                rules="- Facilita, não decide pelo time; decisões ficam registradas na nota."),
        ],
        "realismo do plano e clareza de posse", "Gestão de Projetos",
        portal_url="http://localhost:3000", portal_name="Board/Jira",
    )


# ---- Pesquisa & Conteúdo Técnico ------------------------------------------
PESQUISA = [
    ("Estado da Arte", "levantar e sintetizar o que já existe sobre um tema", "indigo", "books.vertical"),
    ("Síntese de Pesquisa", "transformar muitas fontes em uma síntese confiável e citada", "blue", "doc.on.doc"),
    ("Análise de Mercado", "mapear um mercado, players e tendências com fontes", "green", "chart.bar.doc.horizontal"),
]


def fam_research(v):
    name_short, desc, ck, icon = v
    return _area_team(
        "pesquisa", f"Pesquisa · {name_short}",
        f"Time de pesquisa para {desc}. Pergunta antes de coleta, síntese em paralelo, revisão "
        f"crítica de fontes. Toda afirmação é citada; nada de fonte inventada.",
        icon, ck, f"pesquisa ({name_short})", "uma síntese confiável e citada",
        f"pesquisa: {name_short} — {desc}",
        [
            _sp("pesquisa", "Researcher", f"Você conduz {name_short}: {desc}. Fontes primárias "
                "quando dá, cada afirmação com citação, sem extrapolar.", "indigo", "Cite · pesquisa",
                rules="- Nenhuma fonte inventada; distinga o que a fonte diz do que você infere."),
            _sp("pesquisa", "Synthesist", f"Você organiza {name_short} numa síntese útil: "
                "estrutura, contradições entre fontes, lacunas.", "blue", "Weave · síntese",
                rules="- Contradição entre fontes é registrada, não escondida atrás de uma média."),
        ],
        "qualidade e rastreabilidade das fontes", "Pesquisa & Conteúdo Técnico",
        portal_url="https://scholar.google.com", portal_name="Fontes",
        reviewer_cmd=CMD_GEMINI,
    )


NEW_AREA_FAMILIES = [
    (DESIGN, fam_design), (PRODUTO, fam_product), (MARKETING, fam_marketing),
    (VENDAS, fam_sales), (DADOS, fam_analytics), (SEGURANCA, fam_compliance),
    (FINANCEIRO, fam_finance), (JURIDICO, fam_legal), (SUPORTE, fam_support),
    (GESTAO, fam_pmo), (PESQUISA, fam_research),
]


# ===========================================================================
# Runner
# ===========================================================================

def main():
    for st in STACKS:
        fam_ship_feature(st)
        fam_debug(st)
        fam_release_gate(st)
        fam_scaffold(st)
    for d in BFF_DOMAINS:
        fam_bff_validation(d)
    for prod in FULL_PRODUCTS:
        fam_full_pipeline(prod)
    for c in CLOUDS:
        fam_cloud(c)
    for t in IAC:
        fam_iac(t)
    for db in DATABASES:
        fam_database(db)
    for pipe in DATA_PIPES:
        fam_data_pipeline(pipe)
    for ai in AI_FEATURES:
        fam_ai(ai)
    for mig in MIGRATIONS:
        fam_migration(mig)
    for plat in MOBILE:
        fam_mobile(plat)
    for kind in DOCS_KINDS:
        fam_docs(kind)
    for tool in CICD:
        fam_cicd(tool)
    for work in K8S:
        fam_k8s(work)
    for surface in A11Y:
        fam_a11y(surface)
    for style in API_CONTRACT:
        fam_api(style)
    for layer in PERF:
        fam_perf(layer)
    for scope in PENTEST:
        fam_pentest(scope)
    for spec in SOLO_SPECIALISTS:
        fam_solo(spec)
    for duel in DUELS:
        fam_duel(duel)
    for inc in INCIDENTS:
        fam_incident(inc)

    # Áreas de negócio (não-código)
    for variants, fam in NEW_AREA_FAMILIES:
        for v in variants:
            fam(v)

    # Pacotes coletivos por área + catálogos + índice mestre
    _write_packs()
    for area in AREAS:
        _write_area_catalog(area)
    _write_master_catalog()

    print(f"Gerados {len(CATALOG)} templates de partitura em {len({c[0] for c in CATALOG})} áreas.")
    per_area = Counter(c[0] for c in CATALOG)
    for area in AREAS:
        if per_area.get(area):
            print(f"  {per_area[area]:3d}  {AREAS[area][0]}")
    return CATALOG


def _write_packs():
    """Um pacote .maestripartituras por área + um pacote mestre com tudo."""
    everything = []
    for area, (_label, _emoji, packfile, _d) in AREAS.items():
        parts = []
        for row in CATALOG:
            if row[0] != area:
                continue
            with open(os.path.join(BASE, area, row[3] + ".maestripartitura"), encoding="utf-8") as f:
                obj = json.load(f)
            parts.append(obj)
            everything.append(obj)
        if parts:
            with open(os.path.join(BASE, area, packfile), "w", encoding="utf-8") as f:
                json.dump(pack(parts), f, ensure_ascii=False, indent=2)
    with open(os.path.join(BASE, "Guia-do-Maestri.maestripartituras"), "w", encoding="utf-8") as f:
        json.dump(pack(everything), f, ensure_ascii=False, indent=2)


_MODELS_NOTE = (
    "**Política de modelos:** Fable rege, Opus executa, Codex/Gemini contestam. Os maestros "
    "sobem em `--model fable`; os especialistas em `--model opus`; a revisão adversarial usa "
    "`codex`/`gemini` de propósito — um modelo diferente pega o que o outro deixou passar.\n"
)

_SAFETY_NOTE = (
    "> ⚠️ Adicionar uma partitura ao canvas **inicia os terminais dela e executa os comandos na "
    "sua máquina** (`claude`, `codex`, `gemini`). Leia os comandos na tela de revisão antes de "
    "importar e só aceite de fontes confiáveis. Red team e qualquer engajamento ofensivo só "
    "operam em **escopo autorizado**, nunca em produção e nunca com dados de pessoas reais.\n"
)


def _rows_for_area(area):
    return [r for r in CATALOG if r[0] == area]


def _write_area_catalog(area):
    rows = _rows_for_area(area)
    if not rows:
        return
    label, emoji, packfile, area_desc = AREAS[area]
    by_cat = defaultdict(list)
    for _a, cat, name, slug, icon, color, desc, roles, nn in rows:
        by_cat[cat].append((name, slug, desc, roles, nn))
    lines = [f"# {emoji} Catálogo · {label}\n", f"> {area_desc}\n",
             f"> **{len(rows)} partituras** nesta área, prontas para arrastar para o canvas do "
             "Maestri. Cada uma traz os terminais com responsabilidades embutidas, as notas "
             "compartilhadas, os portais de verificação e todas as conexões.\n",
             f"Importar tudo desta área: pacote [`{packfile}`](./{packfile}) "
             "(painel de Partituras → ⋯ → **Importar Partituras…**). Um template só: arraste o "
             "`.maestripartitura` para o canvas.\n",
             _SAFETY_NOTE, "## Famílias\n"]
    for cat in sorted(by_cat):
        lines.append(f"- [{cat}](#{slugify(cat)}) — {len(by_cat[cat])} templates")
    lines.append("")
    lines.append(_MODELS_NOTE)
    for cat in sorted(by_cat):
        lines.append(f"\n## {cat}\n")
        lines.append("| Partitura | Responsabilidades | Nós | Arquivo |")
        lines.append("|---|---|---|---|")
        for name, slug, desc, roles, nn in sorted(by_cat[cat]):
            lines.append(f"| **{name}**<br><sub>{desc}</sub> | {' · '.join(roles)} | {nn} | "
                         f"[`{slug}`](./{slug}.maestripartitura) |")
    with open(os.path.join(BASE, area, "CATALOGO.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def _write_master_catalog():
    total = len(CATALOG)
    per_area = Counter(c[0] for c in CATALOG)
    fams_per_area = {a: len({r[1] for r in CATALOG if r[0] == a}) for a in AREAS}
    lines = ["# 🎼 Catálogo de Partituras — por área\n",
             f"> **{total} partituras** de Maestri, divididas em "
             f"**{sum(1 for a in AREAS if per_area.get(a))} áreas**. Cada área tem o seu próprio "
             "catálogo detalhado e um pacote coletivo para importar de uma vez.\n",
             "Importar **tudo** (todas as áreas): pacote "
             "[`Guia-do-Maestri.maestripartituras`](./Guia-do-Maestri.maestripartituras).\n",
             _SAFETY_NOTE, "## Áreas\n",
             "| Área | Partituras | Famílias | Catálogo | Pacote |",
             "|---|:--:|:--:|---|---|"]
    for area, (label, emoji, packfile, _d) in AREAS.items():
        if not per_area.get(area):
            continue
        lines.append(f"| {emoji} **{label}** | {per_area[area]} | {fams_per_area[area]} | "
                     f"[abrir](./{area}/CATALOGO.md) | [`{packfile}`](./{area}/{packfile}) |")
    lines.append("")
    lines.append(_MODELS_NOTE)
    lines.append("## O que cada área cobre\n")
    for area, (label, emoji, _pf, area_desc) in AREAS.items():
        if not per_area.get(area):
            continue
        cats = sorted({r[1] for r in CATALOG if r[0] == area})
        lines.append(f"### {emoji} {label}")
        lines.append(f"{area_desc}")
        lines.append(f"Famílias: {', '.join(cats)}.")
        lines.append(f"→ [Catálogo de {label}](./{area}/CATALOGO.md)\n")
    with open(os.path.join(BASE, "CATALOGO.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
