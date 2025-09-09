import json
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def sample_lead():
    return {
        "event": "lead_found",
        "timestamp": "2025-09-09T21:15:30Z",
        "source": "AutoTrader ZA",
        "data": {
            "name": "Jane Doe",
            "phone": "+27821234567",
            "employment": "Employed",
            "vehicle": "VW Polo",
            "location": "Cape Town",
            "status": "hlr_valid"
        },
        "meta": {"runtime":"skunkscrape-1.0.0"}
    }

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.text == "ok"

def test_events_ok():
    r = client.post("/events", json=sample_lead())
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_invalid_payload():
    r = client.post("/events", data="not-json", headers={"Content-Type":"application/json"})
    assert r.status_code == 400
