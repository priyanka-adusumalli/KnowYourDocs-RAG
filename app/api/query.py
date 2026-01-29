from fastapi import APIRouter, Request
from app.models.schemas import QuestionRequest
from app.services.vector_store import search
from app.services.llm import generate_answer

router = APIRouter()

@router.post("/")
async def ask_question(request: Request, payload: QuestionRequest):
    limiter = request.app.state.limiter
    limiter.limit("5/minute")(ask_question)

    chunks = search(payload.question, payload.top_k)
    answer = generate_answer(payload.question, chunks)

    return {"answer": answer}
