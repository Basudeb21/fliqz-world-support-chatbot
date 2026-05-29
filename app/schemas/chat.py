from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_id: int
    message: str


class ChatResponse(BaseModel):
    success: bool
    type: str
    response: str
    ticket_id: int | None = None