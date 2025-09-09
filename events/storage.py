import os, datetime, io
from typing import Dict, Any
from config import EVENTS_DIR

# Writes line-delimited JSON (NDJSON) into date-partitioned files
def ensure_dirs() -> None:
    os.makedirs(EVENTS_DIR, exist_ok=True)
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    os.makedirs(os.path.join(EVENTS_DIR, today), exist_ok=True)

def _path_for(event_type: str) -> str:
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"{event_type}.ndjson"
    return os.path.join(EVENTS_DIR, today, filename)

def append_ndjson(event_type: str, json_line: str) -> None:
    ensure_dirs()
    path = _path_for(event_type)
    # atomic-ish append
    with io.open(path, "a", encoding="utf-8") as f:
        f.write(json_line)
        if not json_line.endswith("\n"):
            f.write("\n")

def writable() -> bool:
    try:
        ensure_dirs()
        test_path = os.path.join(EVENTS_DIR, ".probe")
        with open(test_path, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(test_path)
        return True
    except Exception:
        return False
