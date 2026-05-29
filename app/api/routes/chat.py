from fastapi import APIRouter

from app.schemas.chat import ChatRequest

from app.services.queue.producer import (
    queue_producer
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/send")
async def send_message(data: ChatRequest):

    stream_id = await queue_producer.publish_message(
        user_id=data.user_id,
        message=data.message
    )

    return {
        "success": True,
        "message": "Message queued",
        "stream_id": stream_id
    }