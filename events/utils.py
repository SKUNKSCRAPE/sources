import hmac, hashlib

def compute_sig(secret: str, body: bytes) -> str:
    return hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()

def safe_int(x, default=0):
    try: return int(x)
    except Exception: return default
