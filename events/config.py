import os
from dotenv import load_dotenv

load_dotenv()

EVENTS_DIR = os.getenv("EVENTS_DIR", "./data/events")
SIGNING_SECRET = os.getenv("SIGNING_SECRET", "").strip()
ALLOW_ORIGINS = [o.strip() for o in os.getenv("ALLOW_ORIGINS", "*").split(",")] if os.getenv("ALLOW_ORIGINS") else ["*"]
MAX_BODY_BYTES = int(os.getenv("MAX_BODY_BYTES", "1048576"))
