<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Maestri 指南" width="160" height="160">
  </a>
</p>

<h1 align="center">Maestri 指南</h1>

<p align="center">
  <b>在 <a href="https://www.themaestri.app">Maestri</a> 中指挥 AI 智能体团队的指南 —— 侧重技术，并提供一个生成 257 份现成乐谱（按领域组织）的生成器。</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/%E4%B9%90%E8%B0%B1-257-5856D6?style=for-the-badge" alt="257 乐谱"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/%E9%A2%86%E5%9F%9F-12-007AFF?style=for-the-badge" alt="12 领域"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/format-.maestripartitura%20v1-34C759?style=for-the-badge" alt="格式"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/validation-0-FF9500?style=for-the-badge" alt="已验证"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/language-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

> **注意：** 这是译文。基础指南与 `docs/` 下的详细文档使用巴西葡萄牙语撰写。

## 🎯 这是什么

> **Maestri** 是一款 macOS 应用，你在**无限画布**上**指挥一支代码智能体团队** —— Claude Code、Codex、Gemini、OpenCode：终端是智能体，Markdown 笔记是共享的事实来源，门户（portal）是用于实时验证的内嵌浏览器，而**指挥者（maestro）**负责委派与协调。本仓库既是一份**指南**，也是一个 **Python 生成器**，可生成 **257 份乐谱**（`.maestripartitura`），拖到画布上即可指挥 —— 每份都是一个完整团队，内置职责、笔记、门户与连接。重点是**技术**，另有 11 个业务领域（设计、产品、市场、销售、数据、安全、财务、法务、支持、项目管理、研究）。

## 💡 本指南如何组织

> 两种影响的结合。**按领域划分**（AI 机构的各部门）来自 [agency-agents](https://github.com/msitarzewski/agency-agents)，一个涵盖 18 个部门、230+ 智能体的目录。**版式** —— 页眉、简介、带锚点的目录与分节 —— 参照 [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil)。相关对照详见 [docs/07](docs/07-areas-e-agentes.md)。

## 🌍 翻译

> 如果你希望以其他语言阅读本指南，请在下方选择。你也可以协助翻译到更多语言或纠错；社区感谢你。`docs/` 下的详细文档为葡萄牙语。

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

## ⭐ 从这里开始

> 如果你只想要模板：打开目录，选择一个领域，拖入 Maestri。

- [🎼 **按领域的乐谱目录**](partituras/CATALOGO.md) —— 257 份乐谱的主索引，链接到每个领域及其合集包。
- [💻 **技术目录**](partituras/tecnologia/CATALOGO.md) —— 212 份工程乐谱（本指南的核心）。
- [📦 **一次导入全部**](partituras/Guia-do-Maestri.maestripartituras) —— 包含所有领域的合集包（乐谱面板 → ⋯ → 导入乐谱…）。

## 📖 文档

> 九份文档外加智能体指南，均为葡萄牙语。若你初次接触 Maestri 请从 01 开始；若已熟悉可直接看 02 和 06。

- **01 · 概念** ([docs/01](docs/01-conceitos.md)) —— 画布、终端、笔记、门户、连接、指挥模式、Ombro、Batuta、楼层（Floors）、例程、环境、Wire。
- **02 · 使用模板** ([docs/02](docs/02-como-usar-os-templates.md)) —— 导入、实战指挥、挑选与改编一份乐谱。
- **03 · 快捷键与命令** ([docs/03](docs/03-atalhos.md)) —— macOS 快捷键与 `maestri` 命令行。
- **04 · `.maestripartitura` 格式** ([docs/04](docs/04-formato-maestripartitura.md)) —— 对照官方文件校准的 JSON 规范。
- **05 · 模型与安全** ([docs/05](docs/05-modelos-e-seguranca.md)) —— Fable/Opus/Codex、skip-permissions、30 层技术清单、授权红队。
- **06 · Maestri 日常** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) —— 楼层、门户、笔记、例程与 Ombro 的真实场景。
- **07 · 领域与可用智能体** ([docs/07](docs/07-areas-e-agentes.md)) —— 按领域划分、与 agency-agents 的映射、版式验证。
- **08 · 楼层 + 乐谱（配方）** ([docs/08](docs/08-andares-e-partituras.md)) —— 如何将楼层与乐谱结合使用，含分场景配方与 hooks。
- **09 · 门户：网页、移动、模拟器** ([docs/09](docs/09-portais-mobile-web-emulador.md)) —— 如何为乐谱添加浏览器、移动网页与设备门户（iOS 模拟器 / Android 模拟器）。
- **10 · 在 Maestri 中导入与导出** ([docs/10](docs/10-importar-e-exportar.md)) — 所有可原生导入/导出的内容以及精选配方，及其在中心中的位置。
- **🎭 · 智能体** ([agentes/README.md](agentes/README.md)) —— 职责原型与专家阵容。
- **📨 · 提示词** ([prompts](prompts/README.md)) — 现成提示词库（创建乐谱、验证 Maestri 的 Discord）。

## 🗂️ 按领域的乐谱

> 12 个领域共 257 份乐谱。每个领域都有详细目录和一个 `.maestripartituras` 合集包供一次性导入。

- [💻 **技术**](partituras/tecnologia/CATALOGO.md) —— 212 份 · 端到端工程：功能、缺陷、发布、基础设施、数据、AI、迁移、移动。
- [🎨 **设计与 UX**](partituras/design/CATALOGO.md) —— 5 份 · 设计系统、UX 研究、落地页、UI 审计。
- [📦 **产品**](partituras/produto/CATALOGO.md) —— 5 份 · discovery、路线图、PRD、反馈综合、竞品。
- [📢 **市场与内容**](partituras/marketing/CATALOGO.md) —— 5 份 · 活动、SEO、社交、生命周期邮件、技术博客。
- [💼 **销售**](partituras/vendas/CATALOGO.md) —— 4 份 · outbound、提案/RFP、销售赋能、discovery。
- [📊 **数据与分析**](partituras/dados/CATALOGO.md) —— 4 份 · BI 仪表盘、探索性分析、指标、A/B。
- [🔒 **安全与合规**](partituras/seguranca/CATALOGO.md) —— 4 份 · GDPR/LGPD、SOC 2、威胁建模、事件响应。
- [💵 **财务**](partituras/financeiro/CATALOGO.md) —— 4 份 · 结账、建模、FP&A、尽职调查。
- [⚖️ **法务**](partituras/juridico/CATALOGO.md) —— 3 份 · 合同审阅、intake、风险分析。
- [🛟 **支持与成功**](partituras/suporte/CATALOGO.md) —— 4 份 · 知识库、分诊、onboarding、流失。
- [🗂️ **项目管理**](partituras/gestao/CATALOGO.md) —— 4 份 · 冲刺、多团队协调、会议纪要、复盘。
- [🔬 **研究与技术内容**](partituras/pesquisa/CATALOGO.md) —— 3 份 · 现状综述、综合、市场分析。

## 📦 更多可导入/导出的资源

> Maestri 中心不止有乐谱。以下资源使用应用的其他可移植格式（角色、主题、说明、笔记），或汇集现成的配方。完整概览见 [docs/10 · 导入与导出](docs/10-importar-e-exportar.md)。

- [🎭 **职责（`role.json`）**](roles/CATALOGO.md) — 30 个可复用的原生格式角色；放入项目的 `.maestri` 目录并使用「发现职责」。
- [🎨 **终端主题（Ghostty）**](temas/README.md) — 4 个主题，安装到 `~/.maestri/terminal/themes/`。
- [🧭 **`CLAUDE.md` / `AGENTS.md` 说明**](instrucoes/README.md) — 按技术栈的模板，智能体在工作区启动时自动获得。
- [📝 **笔记模板**](notas/README.md) — 合同、workboard、playbook、技术清单、案卷等，拖到画布上。
- [🧑‍🍳 **精选配方**](receitas/README.md) — 楼层钩子、定时例程、Maestri Wire 客户端与环境配方。
- [📨 **提示词**](prompts/README.md) — 面向提示词编排器的现成提示词。
- [🗂️ **工作区（`.maestri`）**](workspaces/README.md) — 如何导入/分享工作区。

## 🧩 23 个技术家族

> 技术领域由目录（技术栈、领域、云商）参数化。家族 × 变体超过 200 个模板。

- **🚢 Ship Feature**（24）—— maestro + 架构师 + 2 名 builder + warden，按技术栈。
- **🐞 调试**（24）—— 复现者 → 根因 → 修复 → 验证者，按技术栈。
- **✅ 发布关卡**（24）—— conductor + 4 名对抗式评审，按技术栈。
- **🏗️ Scaffold**（24）—— 骨架 + 初始化 + 纵切片 + warden，按技术栈。
- **🔧 迁移**（12）—— 迁移 + 一致性验证者，增量且可回退。
- **💸 完整流水线**（10）—— 4 个表面上的 30 层，按产品（金融切断规则）。
- **☁️ 云与基础设施**（9）—— 网络/计算 + 数据/存储 + warden，按云商。
- **🗄️ 数据库**（9）—— schema/迁移 + 有证据支持的索引，按数据库。
- **🔎 BFF 校验**（8）—— SPA × BFF：一致性、CORS、cookie，按域。
- **🧠 AI 功能**（7）—— AI + 评测与护栏。
- **📱 Ship Mobile**（7）—— 应用 + 设备门户上的 QA/无障碍。
- **🧑‍💻 独奏**（7）—— 单个专家。
- **📖 文档**（5）、**⚔️ 智能体对决**（5）、**🚨 作战室**（5）。
- **🔗 API Contract**（4）、**♿ 无障碍**（4）、**🔁 CI/CD**（4）、**🔀 数据流水线**（4）、**📦 IaC**（4）、**☸️ Kubernetes**（4）、**⚡ 性能**（4）、**🔴 红队**（4，仅授权范围）。

## ⚡ Maestri 日常

> 乐谱只是开始，价值在于流程。[日常指南](docs/06-maestri-no-dia-a-dia.md) 展示如何在真实场景中使用 Maestri 的功能，[08](docs/08-andares-e-partituras.md) 与 [09](docs/09-portais-mobile-web-emulador.md) 深入楼层与门户。

- **🏢 楼层（Floors）** —— 仓库的隔离副本，各有自己的分支：无需 `git stash` 即可并行推进多条战线，配有 Setup/Run/Teardown 钩子。与乐谱结合，可在一个分支上直接拉起整支团队。
- **🌐 门户** —— 在浏览器、移动网页与**设备**（iOS 模拟器 / Android 模拟器 / 实体设备）上的实时验证：复现缺陷、验收功能、检查落地页、测试原生应用。
- **📝 笔记** —— 跨会话留存的事实来源；把该进 git 的移入仓库，串成思维导图，让 Ombro 做总结。
- **⏰ 例程** —— 让重复工作自动进行：CI 守护、部署巡查、竞品剪报、每日结账、工单分诊。
- **👤 Ombro** —— 本地的注意力副驾："我离开时智能体做了什么？"

## 🤖 模型策略

> Fable 指挥，Opus 执行，Codex/Gemini 挑战。

- **🎼 编排**（maestro、conductor、IC、裁判、lead）—— `claude --dangerously-skip-permissions --model fable`。
- **🔨 执行**（架构师、builder、专家）—— `--model opus`。
- **🛡️ 对抗式评审**（发布、warden、对决）—— `codex` / `gemini`，刻意为之：换一个模型抓出另一个漏掉的问题。
- 细节与防护见 [docs/05](docs/05-modelos-e-seguranca.md)。

## 🛠️ 重新生成并验证

> 生成器只依赖 Python 3 标准库。确定性 UUID：重新生成会产生逐字节一致的文件。

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → 与官方乐谱对比 "Zero divergências"
python3 tests/validate_hub.py               # → 校验 role.json 与中心结构
```

- `scripts/maestri_build.py` —— `Partitura` 类、序列化、ropePoints、布局。
- `scripts/roles_lib.py` —— 职责提示词（pt-BR）+ 笔记模板。
- `scripts/generate_partituras.py` —— 由目录参数化、按领域分组的家族。
- `tests/validate_partituras.py` —— 将顶层/payload/节点/角色的键与官方文件比对。

## ⚠️ 安全

> 将乐谱加入画布会**启动其终端并在你的机器上执行命令**（`claude`、`codex`、`gemini`）。

- 导入前请在审阅界面**阅读命令**，且仅接受来自可信来源的乐谱。
- **红队**乐谱及任何进攻性活动**仅在授权范围内**运作，绝不用于生产环境，绝不使用真实个人数据。
- 细节见 [docs/05](docs/05-modelos-e-seguranca.md)。

## 🔗 参考

- [Maestri 官方文档](https://www.themaestri.app/pt-br/docs) —— 画布、终端、笔记、门户、楼层、例程、Wire。
- [agency-agents](https://github.com/msitarzewski/agency-agents) —— 18 个部门、230+ 智能体的目录（领域灵感来源）。
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) —— 参考用 pt-BR 指南（版式灵感来源）。

---

<p align="center">
  <sub>为指挥智能体而生。Fable 指挥，Opus 执行，Codex 与 Gemini 挑战。🎻</sub>
</p>
