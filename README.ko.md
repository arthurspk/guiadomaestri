<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Maestri 가이드" width="160" height="160">
  </a>
</p>

<h1 align="center">Maestri 가이드</h1>

<p align="center">
  <b><a href="https://www.themaestri.app">Maestri</a>에서 AI 에이전트 팀을 지휘하기 위한 가이드 — 기술 중심이며, 영역별로 정리된 257개의 완성 악보(스코어)를 만드는 생성기를 포함합니다.</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/scores-257-5856D6?style=for-the-badge" alt="257"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/areas-12-007AFF?style=for-the-badge" alt="12"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/format-.maestripartitura%20v1-34C759?style=for-the-badge" alt="format"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/validation-0-FF9500?style=for-the-badge" alt="validated"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/language-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

> **참고:** 이 문서는 번역본입니다. 원본 가이드와 `docs/`의 상세 문서는 브라질 포르투갈어로 작성되어 있습니다.

## 🎯 이것은 무엇인가

> **Maestri**는 **무한 캔버스**에서 **코드 에이전트 팀을 지휘**하는 macOS 앱입니다 — Claude Code, Codex, Gemini, OpenCode. 터미널은 에이전트, 마크다운 노트는 공유된 진실의 원천, 포털은 실시간 검증을 위한 내장 브라우저이며, **마에스트로**가 위임하고 조율합니다. 이 저장소는 **가이드**이자 **Python 생성기**로, 캔버스에 끌어다 놓고 바로 지휘할 수 있는 **257개의 악보**(`.maestripartitura`)를 만듭니다. 각 악보는 책임·노트·포털·연결이 내장된 완결된 팀입니다. 중심은 **기술**이며, 11개의 비즈니스 영역(디자인, 제품, 마케팅, 영업, 데이터, 보안, 재무, 법무, 지원, 프로젝트 관리, 리서치)이 더해집니다.

## 💡 이 가이드의 구성

> 두 가지 영향의 결합입니다. **영역별 구분**(AI 에이전시의 부서들)은 18개 부서에 230+ 에이전트를 담은 카탈로그 [agency-agents](https://github.com/msitarzewski/agency-agents)에서 왔습니다. **레이아웃** — 헤더, 소개, 앵커가 있는 목차, 섹션 — 은 [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil)를 따릅니다. 이 비교의 자세한 내용은 [docs/07](docs/07-areas-e-agentes.md)에 있습니다.

## 🌍 번역

> 이 가이드를 다른 언어로 보고 싶다면 아래에서 선택하세요. 더 많은 언어로의 번역이나 오류 수정에 기여할 수도 있습니다. 커뮤니티가 감사드립니다. `docs/`의 상세 문서는 포르투갈어입니다.

🇧🇷・**Português (Brasil) —** [este arquivo](README.md)<br>
🇺🇸・**English —** [Click Here](README.en.md)<br>
🇪🇸・**Español —** [Clic aquí](README.es.md)<br>
🇨🇳・**中文 —** [点击这里](README.zh.md)<br>
🇮🇳・**हिन्दी —** [यहाँ क्लिक करें](README.hi.md)<br>
🇸🇦・**العربية —** [اضغط هنا](README.ar.md)<br>
🇫🇷・**Français —** [Cliquez ici](README.fr.md)<br>
🇮🇹・**Italiano —** [Clicca qui](README.it.md)<br>
🇰🇷・**한국어 —** [여기 클릭](README.ko.md)<br>
🇷🇺・**Русский —** [Нажмите здесь](README.ru.md)<br>
🇩🇪・**Deutsch —** [Hier klicken](README.de.md)<br>
🇯🇵・**日本語 —** [こちらをクリック](README.ja.md)<br>

## ⭐ 여기서 시작하세요

> 템플릿만 필요하다면: 카탈로그를 열고 영역을 골라 Maestri로 끌어다 놓으세요.

- [🎼 **영역별 악보 카탈로그**](partituras/CATALOGO.md) — 257개 악보의 마스터 인덱스, 각 영역과 번들 링크 포함.
- [💻 **기술 카탈로그**](partituras/tecnologia/CATALOGO.md) — 212개의 엔지니어링 악보(가이드의 핵심).
- [📦 **한 번에 모두 가져오기**](partituras/Guia-do-Maestri.maestripartituras) — 모든 영역을 담은 번들(악보 패널 → ⋯ → 악보 가져오기…).

## 📖 문서

> 9개의 문서와 에이전트 가이드, 모두 포르투갈어. Maestri가 처음이라면 01부터, 이미 안다면 02와 06으로.

- **01 · 개념** ([docs/01](docs/01-conceitos.md)) — 캔버스, 터미널, 노트, 포털, 연결, 마에스트로 모드, Ombro, Batuta, 층(Floors), 루틴, 환경, Wire.
- **02 · 템플릿 사용** ([docs/02](docs/02-como-usar-os-templates.md)) — 가져오기, 실전 지휘, 악보 선택과 조정.
- **03 · 단축키와 명령** ([docs/03](docs/03-atalhos.md)) — macOS 키보드 단축키와 `maestri` CLI.
- **04 · `.maestripartitura` 형식** ([docs/04](docs/04-formato-maestripartitura.md)) — 공식 파일 대비 보정된 JSON 사양.
- **05 · 모델과 보안** ([docs/05](docs/05-modelos-e-seguranca.md)) — Fable/Opus/Codex, skip-permissions, 30계층 스택 체크리스트, 승인된 레드팀.
- **06 · 일상 속 Maestri** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) — 층, 포털, 노트, 루틴, Ombro의 실제 상황.
- **07 · 영역과 사용 가능한 에이전트** ([docs/07](docs/07-areas-e-agentes.md)) — 영역 구분, agency-agents 매핑, 레이아웃 검증.
- **08 · 층 + 악보(레시피)** ([docs/08](docs/08-andares-e-partituras.md)) — 층과 악보를 함께 쓰는 법, 상황별 레시피와 hooks.
- **09 · 포털: 웹, 모바일, 에뮬레이터** ([docs/09](docs/09-portais-mobile-web-emulador.md)) — 악보에 브라우저·모바일웹·기기 포털(iOS 시뮬레이터 / Android 에뮬레이터)을 추가하는 법.
- **10 · Maestri에서 가져오기와 내보내기** ([docs/10](docs/10-importar-e-exportar.md)) — 네이티브로 가져오기/내보내기 가능한 모든 것과 큐레이트 레시피, 그리고 각 항목이 허브의 어디에 있는지.
- **🎭 · 에이전트** ([agentes/README.md](agentes/README.md)) — 책임 원형과 전문가 캐스트.
- **📨 · 프롬프트** ([prompts](prompts/README.md)) — 준비된 프롬프트 라이브러리(스코어 생성, Maestri Discord 검증).

## 🗂️ 영역별 악보

> 12개 영역에 걸친 257개 악보. 각 영역에는 상세 카탈로그와 한 번에 가져오는 `.maestripartituras` 번들이 있습니다.

- [💻 **기술**](partituras/tecnologia/CATALOGO.md) — 212개 · 엔드투엔드 엔지니어링: 기능, 버그, 릴리스, 인프라, 데이터, AI, 마이그레이션, 모바일.
- [🎨 **디자인 & UX**](partituras/design/CATALOGO.md) — 5개 · 디자인 시스템, UX 리서치, 랜딩 페이지, UI 감사.
- [📦 **제품**](partituras/produto/CATALOGO.md) — 5개 · discovery, 로드맵, PRD, 피드백 종합, 경쟁 분석.
- [📢 **마케팅 & 콘텐츠**](partituras/marketing/CATALOGO.md) — 5개 · 캠페인, SEO, 소셜, 라이프사이클 이메일, 기술 블로그.
- [💼 **영업**](partituras/vendas/CATALOGO.md) — 4개 · outbound, 제안/RFP, 세일즈 이네이블먼트, discovery.
- [📊 **데이터 & 분석**](partituras/dados/CATALOGO.md) — 4개 · BI 대시보드, 탐색적 분석, 지표, A/B.
- [🔒 **보안 & 컴플라이언스**](partituras/seguranca/CATALOGO.md) — 4개 · GDPR/LGPD, SOC 2, 위협 모델링, 사고 대응.
- [💵 **재무**](partituras/financeiro/CATALOGO.md) — 4개 · 마감, 모델링, FP&A, 실사.
- [⚖️ **법무**](partituras/juridico/CATALOGO.md) — 3개 · 계약 검토, 인테이크, 리스크 분석.
- [🛟 **지원 & 성공**](partituras/suporte/CATALOGO.md) — 4개 · 지식베이스, 분류, 온보딩, 이탈.
- [🗂️ **프로젝트 관리**](partituras/gestao/CATALOGO.md) — 4개 · 스프린트, 다중 팀 조율, 회의록, 회고.
- [🔬 **리서치 & 기술 콘텐츠**](partituras/pesquisa/CATALOGO.md) — 3개 · 최신 동향, 종합, 시장 분석.

## 📦 가져오기/내보내기 추가 리소스

> Maestri 허브는 스코어만이 아닙니다. 아래 리소스는 앱의 다른 이식 가능한 형식(역할, 테마, 지침, 노트)을 사용하거나 완성된 레시피를 모읍니다. 전체 개요는 [docs/10 · 가져오기와 내보내기](docs/10-importar-e-exportar.md).

- [🎭 **책임(`role.json`)**](roles/CATALOGO.md) — 네이티브 형식의 재사용 가능한 역할 30개; 프로젝트의 `.maestri` 폴더에 넣고 "책임 검색"을 사용하세요.
- [🎨 **터미널 테마(Ghostty)**](temas/README.md) — `~/.maestri/terminal/themes/`에 설치할 4개 테마.
- [🧭 **`CLAUDE.md` / `AGENTS.md` 지침**](instrucoes/README.md) — 스택별 템플릿, 워크스페이스 시작 시 에이전트에게 전달됩니다.
- [📝 **노트 템플릿**](notas/README.md) — 계약, workboard, playbook, 스택 체크리스트, 케이스 파일 등, 캔버스로 끌어다 놓기.
- [🧑‍🍳 **큐레이트 레시피**](receitas/README.md) — 층 훅, 예약 루틴, Maestri Wire 클라이언트, 환경 레시피.
- [📨 **프롬프트**](prompts/README.md) — 프롬프트 컴포저용 준비된 프롬프트.
- [🗂️ **워크스페이스(`.maestri`)**](workspaces/README.md) — 워크스페이스 가져오기/공유 방법.

## 🧩 23개 기술 패밀리

> 기술 영역은 카탈로그(스택, 도메인, 제공자)로 매개변수화됩니다. 패밀리 × 변형은 200개 템플릿을 넘습니다.

- **🚢 Ship Feature** (24) — 마에스트로 + 아키텍트 + 빌더 2 + warden, 스택별.
- **🐞 디버깅** (24) — 재현자 → 근본 원인 → 수정 → 검증자, 스택별.
- **✅ 릴리스 게이트** (24) — conductor + 적대적 리뷰어 4, 스택별.
- **🏗️ Scaffold** (24) — 골격 + 셋업 + 수직 슬라이스 + warden, 스택별.
- **🔧 마이그레이션** (12) — 마이그레이션 + 패리티 검증자, 점진적·되돌림 가능.
- **💸 풀 파이프라인** (10) — 4개 표면에 걸친 30계층, 제품별(금융 컷오프 규칙).
- **☁️ 클라우드 & 인프라** (9) — 네트워크/컴퓨트 + 데이터/스토리지 + warden, 제공자별.
- **🗄️ 데이터베이스** (9) — 스키마/마이그레이션 + 증거 기반 인덱스, DB별.
- **🔎 BFF 검증** (8) — SPA × BFF: 패리티, CORS, 쿠키, 도메인별.
- **🧠 AI 기능** (7) — AI + 평가 & 가드레일.
- **📱 Ship Mobile** (7) — 앱 + 기기 포털에서의 QA/접근성.
- **🧑‍💻 솔로** (7) — 단일 전문가.
- **📖 문서화** (5), **⚔️ 에이전트 대결** (5), **🚨 워룸** (5).
- **🔗 API Contract** (4), **♿ 접근성** (4), **🔁 CI/CD** (4), **🔀 Data Pipeline** (4), **📦 IaC** (4), **☸️ Kubernetes** (4), **⚡ 성능** (4), **🔴 레드팀** (4, 승인된 범위 한정).

## ⚡ 일상 속 Maestri

> 악보는 시작이고, 가치는 흐름에 있습니다. [일상 가이드](docs/06-maestri-no-dia-a-dia.md)는 실제 상황에서 Maestri 기능을 쓰는 법을 보여주고, [08](docs/08-andares-e-partituras.md)과 [09](docs/09-portais-mobile-web-emulador.md)는 층과 포털을 깊이 다룹니다.

- **🏢 층(Floors)** — 자체 브랜치를 가진 저장소의 격리 사본: `git stash` 없이 여러 전선을 병렬로, Setup/Run/Teardown 훅과 함께. 악보와 결합하면 한 브랜치 위에 격리된 팀 전체를 띄울 수 있습니다.
- **🌐 포털** — 브라우저, 모바일웹, **기기**(iOS 시뮬레이터 / Android 에뮬레이터 / 실기기)에서의 실시간 검증: 버그 증명, 기능 수용, 랜딩 확인, 네이티브 앱 테스트.
- **📝 노트** — 세션을 넘어 남는 진실의 원천; git에 들어가야 할 것은 저장소로 옮기고, 마인드맵으로 연결하고, Ombro가 요약하게 하세요.
- **⏰ 루틴** — 반복 작업을 스스로: CI 파수꾼, 배포 감시, 경쟁사 클리핑, 일일 마감, 티켓 분류.
- **👤 Ombro** — 로컬 주의 부조종사: "내가 없는 동안 에이전트들이 뭘 했지?"

## 🤖 모델 정책

> Fable가 지휘하고, Opus가 실행하며, Codex/Gemini가 반박합니다.

- **🎼 오케스트레이션** (마에스트로, conductor, IC, 심판, lead) — `claude --dangerously-skip-permissions --model fable`.
- **🔨 실행** (아키텍트, 빌더, 전문가) — `--model opus`.
- **🛡️ 적대적 리뷰** (릴리스, warden, 대결) — `codex` / `gemini`, 의도적으로: 다른 모델이 놓친 것을 잡습니다.
- 세부 사항과 안전장치는 [docs/05](docs/05-modelos-e-seguranca.md).

## 📜 사용 가능한 스크립트

> 허브 전체가 Python(표준 라이브러리만)으로 생성됩니다. 사용법과 확장은 [`scripts/README.md`](scripts/README.md).

| 스크립트 | 유형 | 하는 일 |
|---|---|---|
| [`scripts/maestri_build.py`](scripts/maestri_build.py) | 라이브러리 | `Partitura` 클래스, `.maestripartitura` 직렬화, ropePoints, 레이아웃, 포털. |
| [`scripts/roles_lib.py`](scripts/roles_lib.py) | 라이브러리 | 책임 프롬프트(pt-BR)와 노트 템플릿. |
| [`scripts/generate_partituras.py`](scripts/generate_partituras.py) | 생성기 | 영역별 257개 스코어, 번들, 카탈로그 생성. |
| [`scripts/generate_hub.py`](scripts/generate_hub.py) | 생성기 | `roles/`(role.json), `notas/`, `instrucoes/` 생성. |
| [`tests/validate_partituras.py`](tests/validate_partituras.py) | 검증 | 각 스코어를 공식 레퍼런스와 비교(차이 0). |
| [`tests/validate_hub.py`](tests/validate_hub.py) | 검증 | role.json, 노트, CLAUDE.md/AGENTS.md 쌍 검증. |

## 🛠️ 재생성과 검증

> 생성기는 Python 3 표준 라이브러리 외에 아무것도 필요로 하지 않습니다. 결정적 UUID: 재생성하면 바이트 단위로 동일한 파일이 나옵니다.

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → 공식 악보 대비 "Zero divergências"
python3 tests/validate_hub.py               # → role.json과 허브 구조 검증
```

- `scripts/maestri_build.py` — `Partitura` 클래스, 직렬화, ropePoints, 레이아웃.
- `scripts/roles_lib.py` — 책임 프롬프트(pt-BR) + 노트 템플릿.
- `scripts/generate_partituras.py` — 카탈로그로 매개변수화되고 영역별로 묶인 패밀리.
- `tests/validate_partituras.py` — top/payload/노드/역할 키를 공식 파일과 비교.

## ⚠️ 보안

> 악보를 캔버스에 추가하면 **그 터미널이 시작되고 사용자의 컴퓨터에서 명령이 실행됩니다**(`claude`, `codex`, `gemini`).

- 가져오기 전에 검토 화면에서 **명령을 읽고**, 신뢰할 수 있는 출처의 악보만 받아들이세요.
- **레드팀** 악보와 모든 공격적 활동은 **승인된 범위에서만** 작동하며, 절대 프로덕션에서, 절대 실제 사람의 데이터로 하지 않습니다.
- 세부 사항은 [docs/05](docs/05-modelos-e-seguranca.md).

## 🔗 참고

- [Maestri 공식 문서](https://www.themaestri.app/pt-br/docs) — 캔버스, 터미널, 노트, 포털, 층, 루틴, Wire.
- [agency-agents](https://github.com/msitarzewski/agency-agents) — 18개 부서에 230+ 에이전트 카탈로그(영역의 영감).
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) — 참조용 pt-BR 가이드(레이아웃의 영감).

---

<p align="center">
  <sub>에이전트를 지휘하기 위해 만들어졌습니다. Fable가 지휘하고, Opus가 실행하며, Codex와 Gemini가 반박합니다. 🎻</sub>
</p>
