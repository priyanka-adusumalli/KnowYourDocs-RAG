from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware


from app.api import upload, query

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="RAG QA System")

app.state.limiter = limiter

# ✅ ADD THIS (CORS FIX)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],  # allows OPTIONS
    allow_headers=["*"],
)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return PlainTextResponse(
        "Rate limit exceeded. Try again later.",
        status_code=429,
    )

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(query.router, prefix="/ask", tags=["Ask"])
