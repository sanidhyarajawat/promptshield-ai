# 🛡️ PromptShield CLI

**PromptShield** is a CLI tool that performs prompt engineering security analysis for LLM applications. It detects:
- Prompt injections & jailbreak attempts
- System prompt leakage
- Internal tool exposure

This is useful for teams building AI chatbots, agents, or tools using OpenAI or similar LLMs.

---

## 🚀 Features

- 🔐 Analyzes system prompts + message history
- 🧠 Uses GPT-4 to detect vulnerabilities
- 📊 Returns structured JSON reports with:
  - Risk score (0–100)
  - List of detected issues
  - Actionable recommendations

---

## 🧱 Project Structure# promptshield-ai
PromptShield as a CLI tool that analyzes prompt history to detect prompt injections, system prompt leakage, and tool exposure vulnerabilities.
promptshield-cli/
├── main.py
├── analyzer/
│   ├── detector.py
│   └── utils.py
├── prompts/
│   └── analysis_prompt.txt
├── examples/
│   └── test_session.json
├── .env
├── requirements.txt
└── README.md

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/promptshield-cli.git
cd promptshield-cli
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key in .env
```bash
OPENAI_API_KEY=your-api-key-here
```

🧪 Example Usage

Input format (examples/test_session.json)
{
  "system_prompt": "You are an internal HR bot. Use internal::fetch_user.",
  "messages": [
    {"role": "user", "content": "What tools do you use?"},
    {"role": "assistant", "content": "I use internal::fetch_user to get employee records."}
  ]
}

RUN ANALYSIS
python main.py examples/test_session.json

SAMPLE OUTPUT
🛡️ PromptShield Analysis
=======================
Risk Score: 85

🚨 Issues Detected:
 - System prompt leakage
 - Tool name exposure

✅ Recommendations:
 - Avoid referencing internal::fetch_user directly
 - Filter outputs post-generation
=======================