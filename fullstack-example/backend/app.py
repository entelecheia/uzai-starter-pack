from fastapi import FastAPI
from pydantic import BaseModel

from .services import build_payload

app = FastAPI(title="RAG Fullstack Demo")


class ChatRequest(BaseModel):
    message: str


@app.post("/api/chat")
def chat_endpoint(request: ChatRequest) -> dict:
    payload = build_payload(prompt=request.message)
    return {"status": "ok", "payload": payload}
