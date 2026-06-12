import uuid
from pathlib import Path

from fastapi import (
    FastAPI,
    UploadFile,
    File
)

from pypdf import PdfReader

from langchain_core.messages import HumanMessage

from app.graph import graph
from app.schemas import AskRequest


UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    exist_ok=True
)


app = FastAPI(
    title="Career Copilot API"
)


@app.post("/ask")
def ask(request: AskRequest):

    initial_state = {
        "messages": [
            HumanMessage(
                content=request.query
            )
        ],

        "resume_id": request.resume_id
    }

    result = graph.invoke(
        initial_state
    )

    return {
        "response":
        result["final_response"]
    }


@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".pdf"):
        return {
            "error":
            "Only PDF files are supported."
        }

    resume_id = str(
        uuid.uuid4()
    )

    pdf_path = (
        UPLOAD_DIR /
        f"{resume_id}.pdf"
    )

    with open(
        pdf_path,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    reader = PdfReader(
        pdf_path
    )

    resume_text = ""

    for page in reader.pages:

        resume_text += (
            page.extract_text()
            or ""
        )

    if not resume_text.strip():

        return {
            "error":
            "Could not extract text from PDF."
        }

    text_path = (
        UPLOAD_DIR /
        f"{resume_id}.txt"
    )

    text_path.write_text(
        resume_text,
        encoding="utf-8"
    )

    return {
        "resume_id": resume_id
    }

@app.get("/")
def health_check():

    return {
        "status": "healthy"
    }    