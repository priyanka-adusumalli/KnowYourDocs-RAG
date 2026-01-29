from fastapi import APIRouter, UploadFile, BackgroundTasks
from app.services.vector_store import process_document
import os

router = APIRouter()

@router.post("/")
async def upload_document(
    file: UploadFile,
    background_tasks: BackgroundTasks
):
    os.makedirs("data/documents", exist_ok=True)
    file_path = f"data/documents/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    background_tasks.add_task(process_document, file_path)

    return {"message": "Document uploaded. Processing started."}
