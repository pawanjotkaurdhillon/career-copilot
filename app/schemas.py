from pydantic import BaseModel


class AskRequest(BaseModel):
    query: str
    resume_id: str | None = None