# SkunkScrape Sources

This repo contains curated **data sources** and **UI state configs** for SkunkScrape.
It also includes Python helpers for **MSISDN validation** and **HLR lookups**.

## 🚀 Structure
- `config/` → `sources.json` and `ui_state.json`
- `scripts/` → validation + scraping helpers
- `tests/` → unit tests
- `.env.example` → sample environment file
- `.github/workflows/validate.yml` → CI/CD workflow

## 🔌 Environment
Create a `.env` file in repo root:

```bash
WEBHOOK_URL=https://webhook.skunkscrape.com/events
PROXIES=http://user:password@proxy1:8080
HLR_API=https://api.hlrlookup.com/hlr?msisdn={number}&apikey=YOUR_KEY
```

## ▶️ Usage
Install deps:

```bash
Copy code
pip install -r requirements.txt
Run validation:
```
```bash
Copy code
python scripts/validate_numbers.py
```
Run scrape:

```bash
Copy code
python scripts/scrape_runner.py
```

---

## 📄 .gitignore

```gitignore
# Environment
.env
*.key
*.pem

# Python
__pycache__/
*.pyc
.venv/
```
