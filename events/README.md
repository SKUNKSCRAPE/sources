# SkunkScrape Webhook (`/events`)

Receives POSTed scrape events and leads at `/events`.

## Quickstart (local)

```bash
python -m venv .venv && . .venv/Scripts/activate  # Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app:app --reload --port 8080
```
Test:

```bash
Copy code
curl -X POST http://localhost:8080/events \
  -H "Content-Type: application/json" \
  -d '{"event":"lead_found","timestamp":"2025-09-09T21:15:30Z","source":"AutoTrader ZA","data":{"name":"John Doe","phone":"+27821234567","employment":"Self-employed","vehicle":"Toyota Hilux","location":"Johannesburg","status":"hlr_valid"}}'
```

### Environment
See .env.example—notable vars:

- EVENTS_DIR (default: ./data/events) — where NDJSON is written
- SIGNING_SECRET — optional HMAC to verify X-Signature
- ALLOW_ORIGINS — CORS allowlist
- MAX_BODY_BYTES — payload size guard (default 1MB)

### Deploy with Docker
```bash
Copy code
docker build -t skunkscrape-events .
docker run -p 8080:8080 --env-file .env -v %cd%/data:/app/data skunkscrape-events
```

### Endpoints

- POST /events — ingest event/lead
- GET /healthz — liveness
- GET /readyz — readiness (checks writable storage path)

### Payloads

- event: string (e.g., lead_found, scrape_progress)
- timestamp: ISO8601
- source: string
- data | stats: object (free-form per event type)

See models.py for schemas.

### Signatures (optional)
If SIGNING_SECRET is set, sender must include header:
```makefile
Copy code
X-Signature: sha256=<hex_hmac_of_raw_body>
```

### Tests
```bash
Copy code
pytest -q
```
---
