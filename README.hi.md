<p align="center">
  <a href="https://www.themaestri.app">
    <img src="./images/maestri-logo.png" alt="Maestri गाइड" width="160" height="160">
  </a>
</p>

<h1 align="center">Maestri गाइड</h1>

<p align="center">
  <b><a href="https://www.themaestri.app">Maestri</a> में AI एजेंट टीमों का संचालन करने की गाइड — तकनीक पर ज़ोर, और क्षेत्र के अनुसार व्यवस्थित 257 तैयार स्कोर बनाने वाला जनरेटर।</b>
</p>

<p align="center">
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/scores-257-5856D6?style=for-the-badge" alt="257 scores"></a>
  <a href="partituras/CATALOGO.md"><img src="https://img.shields.io/badge/areas-12-007AFF?style=for-the-badge" alt="12 areas"></a>
  <a href="docs/04-formato-maestripartitura.md"><img src="https://img.shields.io/badge/format-.maestripartitura%20v1-34C759?style=for-the-badge" alt="Format"></a>
  <a href="tests/validate_partituras.py"><img src="https://img.shields.io/badge/validation-0-FF9500?style=for-the-badge" alt="Validated"></a>
  <a href="docs/05-modelos-e-seguranca.md"><img src="https://img.shields.io/badge/language-pt--BR-FFCC00?style=for-the-badge" alt="pt-BR"></a>
</p>

> **नोट:** यह एक अनुवाद है। मूल गाइड और `docs/` के विस्तृत दस्तावेज़ ब्राज़ीली पुर्तगाली में हैं।

## 🎯 यह क्या है

> **Maestri** एक macOS ऐप है जहाँ आप एक **अनंत कैनवास** पर **कोड एजेंटों की टीम का संचालन** करते हैं — Claude Code, Codex, Gemini, OpenCode: टर्मिनल एजेंट हैं, markdown नोट्स साझा सत्य-स्रोत हैं, पोर्टल लाइव सत्यापन के लिए एम्बेडेड ब्राउज़र हैं, और **maestro** कार्य सौंपता व समन्वय करता है। यह रिपॉज़िटरी एक **गाइड** भी है और एक **Python जनरेटर** भी, जो **257 स्कोर** (`.maestripartitura`) बनाता है — कैनवास पर खींचिए और संचालन शुरू कीजिए। हर स्कोर एक पूरी टीम है, जिसमें जिम्मेदारियाँ, नोट्स, पोर्टल और कनेक्शन अंतर्निहित हैं। ज़ोर **तकनीक** पर है, साथ ही 11 और व्यावसायिक क्षेत्र (डिज़ाइन, उत्पाद, मार्केटिंग, बिक्री, डेटा, सुरक्षा, वित्त, क़ानूनी, सपोर्ट, प्रोजेक्ट प्रबंधन, अनुसंधान)।

## 💡 यह गाइड कैसे व्यवस्थित है

> दो प्रेरणाएँ, एक साथ। **क्षेत्र-आधारित विभाजन** (एक AI एजेंसी के विभाग) [agency-agents](https://github.com/msitarzewski/agency-agents) से आता है — 18 विभागों में 230+ एजेंटों का कैटलॉग। **लेआउट** — हेडर, परिचय, एंकर-सहित सूची और अनुभाग — [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) का अनुसरण करता है। विवरण [docs/07](docs/07-areas-e-agentes.md) में।

## 🌍 अनुवाद

> यदि आप इस गाइड को किसी अन्य भाषा में देखना चाहते हैं, नीचे से चुनें। आप और भाषाओं में अनुवाद या त्रुटि-सुधार में भी सहयोग कर सकते हैं; समुदाय आभारी रहेगा। `docs/` के विस्तृत दस्तावेज़ पुर्तगाली में हैं।

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

## ⭐ यहाँ से शुरू करें

> यदि आपको केवल टेम्पलेट चाहिए: कैटलॉग खोलिए, एक क्षेत्र चुनिए, Maestri में खींच दीजिए।

- [🎼 **क्षेत्र के अनुसार स्कोर कैटलॉग**](partituras/CATALOGO.md) — 257 स्कोर का मास्टर इंडेक्स, हर क्षेत्र और उसके बंडल का लिंक।
- [💻 **तकनीक कैटलॉग**](partituras/tecnologia/CATALOGO.md) — 212 इंजीनियरिंग स्कोर (गाइड का हृदय)।
- [📦 **सब कुछ एक साथ आयात करें**](partituras/Guia-do-Maestri.maestripartituras) — सभी क्षेत्रों वाला बंडल (Scores पैनल → ⋯ → Import Scores…)।

## 📖 दस्तावेज़

> नौ दस्तावेज़ और एजेंट गाइड, पुर्तगाली में। यदि Maestri नया है तो 01 से शुरू करें, वरना 02 और 06 पर जाएँ।

- **01 · अवधारणाएँ** ([docs/01](docs/01-conceitos.md)) — कैनवास, टर्मिनल, नोट्स, पोर्टल, कनेक्शन, Maestro मोड, Ombro, Batuta, Floors, Routines, Environments, Wire।
- **02 · टेम्पलेट का उपयोग** ([docs/02](docs/02-como-usar-os-templates.md)) — आयात, व्यावहारिक संचालन, स्कोर चुनना व अनुकूलित करना।
- **03 · शॉर्टकट और कमांड** ([docs/03](docs/03-atalhos.md)) — macOS कीबोर्ड शॉर्टकट और `maestri` CLI।
- **04 · `.maestripartitura` प्रारूप** ([docs/04](docs/04-formato-maestripartitura.md)) — आधिकारिक फ़ाइलों के विरुद्ध कैलिब्रेटेड JSON विनिर्देश।
- **05 · मॉडल और सुरक्षा** ([docs/05](docs/05-modelos-e-seguranca.md)) — Fable/Opus/Codex, skip-permissions, 30-परत स्टैक चेकलिस्ट, अधिकृत रेड टीम।
- **06 · रोज़मर्रा का Maestri** ([docs/06](docs/06-maestri-no-dia-a-dia.md)) — floors, पोर्टल, नोट्स, routines और Ombro वास्तविक स्थितियों में।
- **07 · क्षेत्र और उपलब्ध एजेंट** ([docs/07](docs/07-areas-e-agentes.md)) — क्षेत्र-विभाजन, agency-agents से मानचित्रण, लेआउट सत्यापन।
- **08 · Floors + Scores (रेसिपी)** ([docs/08](docs/08-andares-e-partituras.md)) — floors को scores के साथ उपयोग करना, स्थिति-अनुसार रेसिपी और hooks।
- **09 · पोर्टल: वेब, मोबाइल, एमुलेटर** ([docs/09](docs/09-portais-mobile-web-emulador.md)) — scores में ब्राउज़र, मोबाइल-वेब और डिवाइस पोर्टल (iOS सिम्युलेटर / Android एमुलेटर) कैसे जोड़ें।
- **10 · Maestri में इम्पोर्ट और एक्सपोर्ट** ([docs/10](docs/10-importar-e-exportar.md)) — जो कुछ नेटिव रूप से इम्पोर्ट/एक्सपोर्ट हो सकता है, साथ में क्यूरेटेड रेसिपी, और हब में हर चीज़ कहाँ है।
- **🎭 · एजेंट** ([agentes/README.md](agentes/README.md)) — जिम्मेदारी के आदर्श और विशेषज्ञों की टोली।
- **📨 · प्रॉम्प्ट** ([prompts](prompts/README.md)) — तैयार प्रॉम्प्ट की लाइब्रेरी (स्कोर बनाएं, Maestri का Discord सत्यापित करें)।

## 🗂️ क्षेत्र के अनुसार स्कोर

> 12 क्षेत्रों में 257 स्कोर। हर क्षेत्र का विस्तृत कैटलॉग और एक-साथ आयात हेतु `.maestripartituras` बंडल है।

- [💻 **तकनीक**](partituras/tecnologia/CATALOGO.md) — 212 स्कोर · एंड-टू-एंड इंजीनियरिंग: फ़ीचर, बग, रिलीज़, इंफ़्रा, डेटा, AI, माइग्रेशन, मोबाइल।
- [🎨 **डिज़ाइन & UX**](partituras/design/CATALOGO.md) — 5 स्कोर · डिज़ाइन सिस्टम, UX शोध, लैंडिंग पेज, UI ऑडिट।
- [📦 **उत्पाद**](partituras/produto/CATALOGO.md) — 5 स्कोर · discovery, रोडमैप, PRD, फ़ीडबैक संश्लेषण, प्रतिस्पर्धा।
- [📢 **मार्केटिंग & कंटेंट**](partituras/marketing/CATALOGO.md) — 5 स्कोर · अभियान, SEO, सोशल, लाइफ़साइकल ईमेल, तकनीकी ब्लॉग।
- [💼 **बिक्री**](partituras/vendas/CATALOGO.md) — 4 स्कोर · outbound, प्रस्ताव/RFP, sales enablement, discovery।
- [📊 **डेटा & एनालिटिक्स**](partituras/dados/CATALOGO.md) — 4 स्कोर · BI डैशबोर्ड, अन्वेषी विश्लेषण, मेट्रिक्स, A/B।
- [🔒 **सुरक्षा & अनुपालन**](partituras/seguranca/CATALOGO.md) — 4 स्कोर · GDPR/LGPD, SOC 2, threat modeling, घटना प्रतिक्रिया।
- [💵 **वित्त**](partituras/financeiro/CATALOGO.md) — 4 स्कोर · क्लोज़, मॉडलिंग, FP&A, due diligence।
- [⚖️ **क़ानूनी**](partituras/juridico/CATALOGO.md) — 3 स्कोर · अनुबंध समीक्षा, intake, जोखिम विश्लेषण।
- [🛟 **सपोर्ट & सक्सेस**](partituras/suporte/CATALOGO.md) — 4 स्कोर · नॉलेज बेस, ट्राइएज, onboarding, churn।
- [🗂️ **प्रोजेक्ट प्रबंधन**](partituras/gestao/CATALOGO.md) — 4 स्कोर · स्प्रिंट, बहु-टीम समन्वय, मीटिंग नोट्स, रेट्रो।
- [🔬 **अनुसंधान & तकनीकी कंटेंट**](partituras/pesquisa/CATALOGO.md) — 3 स्कोर · state of the art, संश्लेषण, बाज़ार विश्लेषण।

## 📦 इम्पोर्ट/एक्सपोर्ट के और संसाधन

> Maestri हब सिर्फ़ स्कोर नहीं है। ये संसाधन ऐप के अन्य पोर्टेबल फ़ॉर्मैट (roles, थीम, निर्देश, नोट्स) का उपयोग करते हैं या तैयार रेसिपी समेटते हैं। पूरा अवलोकन [docs/10 · इम्पोर्ट और एक्सपोर्ट](docs/10-importar-e-exportar.md) में।

- [🎭 **जिम्मेदारियाँ (`role.json`)**](roles/CATALOGO.md) — नेटिव फ़ॉर्मैट में 30 पुनःप्रयोज्य roles; प्रोजेक्ट के `.maestri` फ़ोल्डर में रखें और "Descobrir Responsabilidades" का उपयोग करें।
- [🎨 **टर्मिनल थीम (Ghostty)**](temas/README.md) — `~/.maestri/terminal/themes/` में इंस्टॉल करने के लिए 4 थीम।
- [🧭 **`CLAUDE.md` / `AGENTS.md` निर्देश**](instrucoes/README.md) — प्रति-स्टैक टेम्पलेट, जो एजेंट को वर्कस्पेस शुरू होने पर मिलते हैं।
- [📝 **नोट टेम्पलेट**](notas/README.md) — कॉन्ट्रैक्ट, workboard, playbook, स्टैक-चेकलिस्ट, केस-फ़ाइल आदि, कैनवास पर खींचने के लिए।
- [🧑‍🍳 **क्यूरेटेड रेसिपी**](receitas/README.md) — फ़्लोर hooks, शेड्यूल्ड routines, Maestri Wire क्लाइंट और पर्यावरण रेसिपी।
- [📨 **प्रॉम्प्ट**](prompts/README.md) — Compositor के लिए तैयार प्रॉम्प्ट।
- [🗂️ **वर्कस्पेस (`.maestri`)**](workspaces/README.md) — वर्कस्पेस इम्पोर्ट/साझा कैसे करें।

## 🧩 23 तकनीकी परिवार

> तकनीक क्षेत्र कैटलॉग (stacks, डोमेन, प्रोवाइडर) द्वारा पैरामीट्रीकृत है। परिवार × वैरिएंट 200 टेम्पलेट से अधिक।

- **🚢 Ship Feature** (24) — maestro + आर्किटेक्ट + 2 builders + warden, प्रति stack।
- **🐞 डिबगिंग** (24) — reproducer → root cause → fix → verifier, प्रति stack।
- **✅ रिलीज़ गेट** (24) — conductor + 4 प्रतिकूल समीक्षक, प्रति stack।
- **🏗️ Scaffold** (24) — कंकाल + setup + vertical slice + warden, प्रति stack।
- **🔧 माइग्रेशन** (12) — माइग्रेशन + parity verifier, वृद्धिशील व प्रतिवर्ती।
- **💸 पूर्ण पाइपलाइन** (10) — 4 सतहों पर 30 परतें, प्रति उत्पाद (वित्तीय कट-ऑफ़ नियम)।
- **☁️ Cloud & Infra** (9) — नेटवर्क/कंप्यूट + डेटा/स्टोरेज + warden, प्रति प्रोवाइडर।
- **🗄️ डेटाबेस** (9) — schema/माइग्रेशन + साक्ष्य-आधारित इंडेक्स, प्रति डेटाबेस।
- **🔎 BFF सत्यापन** (8) — SPA × BFF: parity, CORS, cookie, प्रति डोमेन।
- **🧠 AI फ़ीचर** (7) — AI + evals & guardrails।
- **📱 Ship Mobile** (7) — ऐप + डिवाइस पोर्टल पर QA/a11y।
- **🧑‍💻 सोलो** (7) — एकल विशेषज्ञ।
- **📖 दस्तावेज़** (5), **⚔️ एजेंट द्वंद्व** (5), **🚨 वॉर रूम** (5)।
- **🔗 API Contract** (4), **♿ सुलभता** (4), **🔁 CI/CD** (4), **🔀 Data Pipeline** (4), **📦 IaC** (4), **☸️ Kubernetes** (4), **⚡ प्रदर्शन** (4), **🔴 रेड टीम** (4, केवल अधिकृत दायरा)।

## ⚡ रोज़मर्रा का Maestri

> स्कोर शुरुआत हैं; मूल्य प्रवाह में है। [रोज़मर्रा गाइड](docs/06-maestri-no-dia-a-dia.md) वास्तविक स्थितियों में Maestri की सुविधाओं का उपयोग दिखाती है, और [08](docs/08-andares-e-partituras.md) व [09](docs/09-portais-mobile-web-emulador.md) floors व पोर्टल को गहराई से समझाते हैं।

- **🏢 Floors** — रिपॉज़िटरी की पृथक प्रतियाँ, अपनी शाखा के साथ: `git stash` के बिना कई मोर्चों पर समानांतर काम, Setup/Run/Teardown hooks के साथ। किसी स्कोर के साथ मिलाकर एक शाखा पर पूरी टीम खड़ी करें।
- **🌐 पोर्टल** — ब्राउज़र, मोबाइल-वेब और **डिवाइस** (iOS सिम्युलेटर / Android एमुलेटर / भौतिक डिवाइस) पर लाइव सत्यापन: बग सिद्ध करना, फ़ीचर स्वीकारना, लैंडिंग जाँचना, नेटिव ऐप परखना।
- **📝 नोट्स** — सत्र के बाद भी बचा रहने वाला सत्य-स्रोत; जो git में जाना चाहिए उसे रिपॉज़िटरी में ले जाएँ, माइंड मैप में जोड़ें, Ombro से सारांश करवाएँ।
- **⏰ Routines** — दोहरावदार काम अपने आप: CI प्रहरी, deploy निगरानी, प्रतिस्पर्धी क्लिपिंग, दैनिक क्लोज़, टिकट ट्राइएज।
- **👤 Ombro** — स्थानीय ध्यान सह-चालक: "मेरे न रहने पर एजेंटों ने क्या किया?"

## 🤖 मॉडल नीति

> Fable संचालन करता है, Opus निष्पादन, Codex/Gemini चुनौती देते हैं।

- **🎼 ऑर्केस्ट्रेशन** (maestro, conductor, IC, judge, lead) — `claude --dangerously-skip-permissions --model fable`।
- **🔨 निष्पादन** (आर्किटेक्ट, builders, विशेषज्ञ) — `--model opus`।
- **🛡️ प्रतिकूल समीक्षा** (release, wardens, द्वंद्व) — `codex` / `gemini`, जानबूझकर: भिन्न मॉडल वही पकड़ता है जो दूसरा चूक गया।
- विवरण व सुरक्षा-उपाय [docs/05](docs/05-modelos-e-seguranca.md) में।

## 🛠️ पुनः जनरेट और सत्यापित करें

> जनरेटर को Python 3 मानक लाइब्रेरी के अलावा कुछ नहीं चाहिए। नियतात्मक UUID: पुनः जनरेट करने पर बाइट-दर-बाइट समान फ़ाइलें।

```bash
python3 scripts/generate_partituras.py     # → "Gerados 257 templates em 12 áreas"
python3 scripts/generate_hub.py            # → roles/ + notas/ + instrucoes/
python3 tests/validate_partituras.py        # → आधिकारिक स्कोर बनाम "Zero divergências"
python3 tests/validate_hub.py               # → role.json और हब संरचना की जाँच
```

- `scripts/maestri_build.py` — `Partitura` क्लास, serialization, ropePoints, layout।
- `scripts/roles_lib.py` — जिम्मेदारी प्रॉम्प्ट (pt-BR) + नोट टेम्पलेट।
- `scripts/generate_partituras.py` — कैटलॉग द्वारा पैरामीट्रीकृत, क्षेत्रवार समूहित परिवार।
- `tests/validate_partituras.py` — top/payload/node/role कुंजियों की आधिकारिक फ़ाइल से तुलना।

## ⚠️ सुरक्षा

> कैनवास में स्कोर जोड़ने पर उसके **टर्मिनल शुरू होते हैं और आपकी मशीन पर कमांड चलते हैं** (`claude`, `codex`, `gemini`)।

- आयात से पहले समीक्षा स्क्रीन पर **कमांड पढ़ें**, और केवल विश्वसनीय स्रोतों से स्कोर स्वीकारें।
- **रेड टीम** स्कोर और कोई भी आक्रामक गतिविधि **केवल अधिकृत दायरे में** चलती है, कभी उत्पादन में नहीं और कभी वास्तविक लोगों के डेटा के साथ नहीं।
- विवरण [docs/05](docs/05-modelos-e-seguranca.md) में।

## 🔗 संदर्भ

- [आधिकारिक Maestri दस्तावेज़](https://www.themaestri.app/pt-br/docs) — कैनवास, टर्मिनल, नोट्स, पोर्टल, floors, routines, Wire।
- [agency-agents](https://github.com/msitarzewski/agency-agents) — 18 विभागों में 230+ एजेंटों का कैटलॉग (क्षेत्रों की प्रेरणा)।
- [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) — संदर्भ pt-BR गाइड (लेआउट की प्रेरणा)।

---

<p align="center">
  <sub>एजेंटों के संचालन हेतु निर्मित। Fable संचालन करता है, Opus निष्पादन, Codex व Gemini चुनौती देते हैं। 🎻</sub>
</p>
