from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from config import MAX_BODY_BYTES, SIGNING_SECRET
from utils import compute_sig

class BodyLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        if len(body) > MAX_BODY_BYTES:
            return JSONResponse({"error": "payload too large"}, status_code=413)
        # stash body so downstream can reuse it without re-reading
        request.state.raw_body = body
        return await call_next(request)

class SignatureMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method == "POST" and request.url.path.endswith("/events") and SIGNING_SECRET:
            provided = request.headers.get("X-Signature", "")
            if not provided.startswith("sha256="):
                return JSONResponse({"error": "missing or invalid signature"}, status_code=401)
            expected = compute_sig(SIGNING_SECRET, request.state.raw_body)
            if provided != f"sha256={expected}":
                return JSONResponse({"error": "signature mismatch"}, status_code=401)
        return await call_next(request)
