# SkunkScrape Webhook (`/events`)

Receives POSTed scrape events and leads at `/events`.

## Quickstart (local)

```bash
python -m venv .venv && . .venv/Scripts/activate  # Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app:app --reload --port 8080
