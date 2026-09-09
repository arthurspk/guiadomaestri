<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Maestri ガイド" width="160" height="160">
  </a>
</p>

<h1 align="center">Maestri ガイド</h1>

> **注記:** これは翻訳です。基となるガイドおよび `docs/` 配下の詳細ドキュメントはブラジルポルトガル語で書かれています。

## 🎯 これは何か

> **Maestri** は、**無限のキャンバス**上で**コードエージェントのチームを指揮する** macOS アプリです — Claude Code、Codex、Gemini、OpenCode。ターミナルはエージェント、Markdown ノートは共有された真実の源、ポータルはライブ検証のための埋め込みブラウザ、そして**マエストロ**が委任し調整します。このリポジトリは**ガイド**であり、同時に **Python ジェネレーター**でもあり、キャンバスにドラッグしてすぐ指揮できる **257 のスコア**（`.maestripartitura`）を生成します。各スコアは、責務・ノート・ポータル・接続を内蔵した完全なチームです。重点は**技術**で、さらに 11 のビジネス領域（デザイン、プロダクト、マーケティング、営業、データ、セキュリティ、財務、法務、サポート、プロジェクト管理、リサーチ）があります。

- 🌐 [公式サイト](https://www.themaestri.app) — Maestri のページ：アプリのダウンロード、機能、価格。
- 📖 [公式ドキュメント](https://www.themaestri.app/docs) — アプリのマニュアル：キャンバス、ターミナル、ノート、ポータル、フロア、ルーティン、Wire。

## 💡 本ガイドの構成

> 2 つの影響を組み合わせています。**領域による分割**（AI エージェンシーの部門）は、18 部門・230+ エージェントのカタログ [agency-agents](https://github.com/msitarzewski/agency-agents) に由来します。**レイアウト** — ヘッダー、紹介、アンカー付き目次、セクション — は [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) に倣っています。比較の詳細は [docs/07](docs/07-areas-e-agentes.md)。

## 🌍 翻訳

> 本ガイドを別の言語で読みたい場合は下から選んでください。さらなる言語への翻訳や誤りの修正への協力も歓迎します。コミュニティは感謝します。`docs/` の詳細ドキュメントはポルトガル語です。

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

## ⭐ ここから始める

> テンプレートだけが欲しい場合：カタログを開き、領域を選び、Maestri にドラッグしてください。

- [🎼 **領域別スコアカタログ**](partituras/CATALOGO.md) — 257 スコアのマスター索引。各領域とそのバンドルへのリンク付き。
- [💻 **技術カタログ**](partituras/tecnologia/CATALOGO.md) — 212 のエンジニアリングスコア（ガイドの中核）。
- [📦 **一括インポート**](partituras/Guia-do-Maestri.maestripartituras) — 全領域を含むバンドル（スコアパネル → ⋯ → スコアをインポート…）。

## 📖 ドキュメント

> 9 つのドキュメントとエージェントガイド、いずれもポルトガル語。Maestri が初めてなら 01 から、既に知っているなら 02 と 06 へ。

- 🧭 **01 · コンセプト** ([docs/01](docs/01-conceitos.md)) — キャンバス、ターミナル、ノート、ポータル、接続、マエストロモード、Ombro、Batuta、フロア（Floors）、ルーティン、環境、Wire。
- 🚀 **02 · テンプレートの使い方** ([docs/02](docs/02-como-usar-os-templates.md)) — インポート、実践的な指揮、スコアの選択と調整。
- ⌨️ **03 · ショートカットとコマンド** ([docs/03](docs/03-atalhos.md)) — macOS キーボードショートカットと `maestri` CLI。
- 📐 **04 · `.maestripartitura` 形式** ([docs/04](docs/04-formato-maestripartitura.md)) — 公式ファイルに合わせて較正した JSON 仕様。
- 🛡️ **05 · モデルとセキュリティ** ([docs/05](docs/05-modelos-e-seguranca.md)) — Fable/Opus/Codex、skip-permissions、30 層スタックチェックリスト、認可済みレッドチーム。
- ☀️ **06 · 日常の Maestri** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) — フロア、ポータル、ノート、ルーティン、Ombro を実際の場面で。
- 🗺️ **07 · 領域と利用可能なエージェント** ([docs/07](docs/07-areas-e-agentes.md)) — 領域分割、agency-agents への対応表、レイアウト検証。
- 🏢 **08 · フロア + スコア（レシピ）** ([docs/08](docs/08-andares-e-partituras.md)) — フロアとスコアを併用する方法、場面別レシピと hooks。
- 🌐 **09 · ポータル：Web、モバイル、エミュレーター** ([docs/09](docs/09-portais-mobile-web-emulador.md)) — ブラウザ、モバイル Web、デバイスポータル（iOS シミュレーター / Android エミュレーター）をスコアに追加する方法。
- 📦 **10 · Maestri でのインポートとエクスポート** ([docs/10](docs/10-importar-e-exportar.md)) — ネイティブにインポート/エクスポートできるすべてと、キュレートされたレシピ、そして各要素がハブのどこにあるか。
- 💡 **11 · ヒント** ([docs/11](docs/11-dicas.md)) — Maestri をより活かすための日常の実用ヒント。
- **🎭 · エージェント** ([agentes/README.md](agentes/README.md)) — 責務の原型と専門家の顔ぶれ。
- **📨 · プロンプト** ([prompts](prompts/README.md)) — 既成プロンプトのライブラリ（初期プロンプト、スコア作成）。

## 🗂️ 領域別スコア

> 12 領域にわたる 257 スコア。各領域には詳細カタログと、一括インポート用の `.maestripartituras` バンドルがあります。

- [💻 **技術**](partituras/tecnologia/CATALOGO.md) — 212 · エンドツーエンドのエンジニアリング：機能、バグ、リリース、インフラ、データ、AI、移行、モバイル。
- [🎨 **デザイン & UX**](partituras/design/CATALOGO.md) — 5 · デザインシステム、UX リサーチ、ランディングページ、UI 監査。
- [📦 **プロダクト**](partituras/produto/CATALOGO.md) — 5 · discovery、ロードマップ、PRD、フィードバック統合、競合分析。
- [📢 **マーケティング & コンテンツ**](partituras/marketing/CATALOGO.md) — 5 · キャンペーン、SEO、ソーシャル、ライフサイクルメール、技術ブログ。
- [💼 **営業**](partituras/vendas/CATALOGO.md) — 4 · アウトバウンド、提案/RFP、セールスイネーブルメント、discovery。
- [📊 **データ & 分析**](partituras/dados/CATALOGO.md) — 4 · BI ダッシュボード、探索的分析、指標、A/B。
- [🔒 **セキュリティ & コンプライアンス**](partituras/seguranca/CATALOGO.md) — 4 · GDPR/LGPD、SOC 2、脅威モデリング、インシデント対応。
- [💵 **財務**](partituras/financeiro/CATALOGO.md) — 4 · 決算、モデリング、FP&A、デューデリジェンス。
- [⚖️ **法務**](partituras/juridico/CATALOGO.md) — 3 · 契約レビュー、インテーク、リスク分析。
- [🛟 **サポート & サクセス**](partituras/suporte/CATALOGO.md) — 4 · ナレッジベース、トリアージ、オンボーディング、チャーン。
- [🗂️ **プロジェクト管理**](partituras/gestao/CATALOGO.md) — 4 · スプリント、複数チーム調整、議事録、レトロスペクティブ。
- [🔬 **リサーチ & 技術コンテンツ**](partituras/pesquisa/CATALOGO.md) — 3 · 最新動向、統合、市場分析。

## 📦 インポート/エクスポートできる追加リソース

> Maestri ハブはスコアだけではありません。これらはアプリの他の可搬フォーマット（ロール、テーマ、指示、ノート）を使うか、既成のレシピをまとめます。全体像は [docs/10 · インポートとエクスポート](docs/10-importar-e-exportar.md)。

- [🎭 **責務（`role.json`）**](roles/CATALOGO.md) — ネイティブ形式の再利用可能なロール 30 個。プロジェクトの `.maestri` フォルダに入れ「責務を検出」を使います。
- [🎨 **ターミナルテーマ（Ghostty）**](temas/README.md) — `~/.maestri/terminal/themes/` にインストールする 4 テーマ。
- [🧭 **`CLAUDE.md` / `AGENTS.md` 指示**](instrucoes/README.md) — スタック別テンプレート。ワークスペース開始時にエージェントへ渡されます。
- [📝 **ノートテンプレート**](notas/README.md) — 契約、workboard、playbook、スタックチェックリスト、ケースファイルなど、キャンバスへドラッグ。
- [🧑‍🍳 **キュレートされたレシピ**](receitas/README.md) — フロアフック、定期ルーティン、Maestri Wire クライアント、環境レシピ。
- [📨 **プロンプト**](prompts/README.md) — プロンプトコンポーザー用の既成プロンプト。
- [🗂️ **ワークスペース（`.maestri`）**](workspaces/README.md) — ワークスペースのインポート/共有方法。

## 🧩 23 の技術ファミリー

> 技術領域はカタログ（スタック、ドメイン、プロバイダー）でパラメータ化されています。ファミリー × バリアントは 200 テンプレートを超えます。

- **🚢 Ship Feature**（24）— マエストロ + アーキテクト + ビルダー 2 + warden、スタック別。
- **🐞 デバッグ**（24）— 再現者 → 根本原因 → 修正 → 検証者、スタック別。
- **✅ リリースゲート**（24）— conductor + 4 名の敵対的レビュアー、スタック別。
- **🏗️ Scaffold**（24）— 骨組み + セットアップ + 垂直スライス + warden、スタック別。
- **🔧 移行**（12）— 移行 + 等価検証者、段階的かつ可逆。
- **💸 フルパイプライン**（10）— 4 つの面にわたる 30 層、プロダクト別（金融カットオフ規則）。
- **☁️ クラウド & インフラ**（9）— ネットワーク/コンピュート + データ/ストレージ + warden、プロバイダー別。
- **🗄️ データベース**（9）— スキーマ/移行 + エビデンスに基づくインデックス、DB 別。
- **🔎 BFF 検証**（8）— SPA × BFF：等価性、CORS、Cookie、ドメイン別。
- **🧠 AI 機能**（7）— AI + 評価 & ガードレール。
- **📱 Ship Mobile**（7）— アプリ + デバイスポータルでの QA/アクセシビリティ。
- **🧑‍💻 ソロ**（7）— 単独の専門家。
- **📖 ドキュメント**（5）、**⚔️ エージェント決闘**（5）、**🚨 ウォールーム**（5）。
- **🔗 API Contract**（4）、**♿ アクセシビリティ**（4）、**🔁 CI/CD**（4）、**🔀 Data Pipeline**（4）、**📦 IaC**（4）、**☸️ Kubernetes**（4）、**⚡ パフォーマンス**（4）、**🔴 レッドチーム**（4、認可範囲のみ）。

## ⚡ 日常の Maestri

> スコアは出発点であり、価値はフローにあります。[日常ガイド](docs/06-maestri-no-dia-a-dia.md) は実際の場面で Maestri の機能をどう使うかを示し、[08](docs/08-andares-e-partituras.md) と [09](docs/09-portais-mobile-web-emulador.md) はフロアとポータルを掘り下げます。

- **🏢 フロア（Floors）** — 独自ブランチを持つリポジトリの隔離コピー：`git stash` なしで複数の戦線を並行して進め、Setup/Run/Teardown フックを備えます。スコアと組み合わせれば、1 つのブランチ上に隔離されたチーム全体を立ち上げられます。
- **🌐 ポータル** — ブラウザ、モバイル Web、**デバイス**（iOS シミュレーター / Android エミュレーター / 実機）でのライブ検証：バグの証明、機能の受け入れ、ランディングの確認、ネイティブアプリのテスト。
- **📝 ノート** — セッションを超えて残る真実の源；git に入れるべきものはリポジトリへ移し、マインドマップとして連結し、Ombro に要約させます。
- **⏰ ルーティン** — 反復作業を自動で：CI 番人、デプロイ監視、競合クリッピング、日次決算、チケットのトリアージ。
- **👤 Ombro** — ローカルの注意副操縦士：「私がいない間、エージェントは何をした？」。

## 🤖 モデルポリシー

> Fable が指揮し、Opus が実行し、Codex/Gemini が異議を唱える。

- **🎼 オーケストレーション**（マエストロ、conductor、IC、審判、lead）— `claude --dangerously-skip-permissions --model fable`。
- **🔨 実行**（アーキテクト、ビルダー、専門家）— `--model opus`。
- **🛡️ 敵対的レビュー**（リリース、warden、決闘）— `codex` / `gemini`、意図的に：別のモデルが、もう一方の見逃しを捕らえます。
- 詳細と安全策は [docs/05](docs/05-modelos-e-seguranca.md)。

## 📜 利用可能なスクリプト

> ハブ全体は Python（標準ライブラリのみ）で生成されます。使い方と拡張は [`scripts/README.md`](scripts/README.md)。

| スクリプト | 種別 | 役割 |
|---|---|---|
| [`scripts/maestri_build.py`](scripts/maestri_build.py) | ライブラリ | `Partitura` クラス、`.maestripartitura` シリアライズ、ropePoints、レイアウト、ポータル。 |
| [`scripts/roles_lib.py`](scripts/roles_lib.py) | ライブラリ | 責務プロンプト（pt-BR）とノートテンプレート。 |
| [`scripts/generate_partituras.py`](scripts/generate_partituras.py) | ジェネレーター | 領域別に 257 スコア、バンドル、カタログを生成。 |
| [`scripts/generate_hub.py`](scripts/generate_hub.py) | ジェネレーター | `roles/`（role.json）、`notas/`、`instrucoes/` を生成。 |
| [`tests/validate_partituras.py`](tests/validate_partituras.py) | 検証 | 各スコアを公式リファレンスと比較（差異ゼロ）。 |
| [`tests/validate_hub.py`](tests/validate_hub.py) | 検証 | role.json、ノート、CLAUDE.md/AGENTS.md ペアを検証。 |

## 🛠️ 再生成と検証

> ジェネレーターは Python 3 標準ライブラリ以外に依存しません。決定的 UUID：再生成するとバイト単位で同一のファイルが得られます。

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → 公式スコアに対して "Zero divergências"
python3 tests/validate_hub.py               # → role.json とハブ構造を検証
```

- `scripts/maestri_build.py` — `Partitura` クラス、シリアライズ、ropePoints、レイアウト。
- `scripts/roles_lib.py` — 責務プロンプト（pt-BR）+ ノートテンプレート。
- `scripts/generate_partituras.py` — カタログでパラメータ化され、領域ごとにまとめられたファミリー。
- `tests/validate_partituras.py` — top/payload/ノード/ロールのキーを公式ファイルと比較。

## ⚠️ セキュリティ

> スコアをキャンバスに追加すると、**そのターミナルが起動し、あなたのマシンでコマンドが実行されます**（`claude`、`codex`、`gemini`）。

- インポート前にレビュー画面で**コマンドを読み**、信頼できる出所のスコアだけを受け入れてください。
- **レッドチーム**スコアおよびあらゆる攻撃的活動は、**認可された範囲でのみ**動作し、決して本番環境で、決して実在の人物のデータでは行いません。
- 詳細は [docs/05](docs/05-modelos-e-seguranca.md)。

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=arthurspk/guiadomaestri&type=Date)](https://star-history.com/#arthurspk/guiadomaestri&Date)
