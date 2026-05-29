import json

from app.db.redis import redis_client
from app.core.config import settings


class QueueProducer:

    async def publish_message(
        self,
        user_id: int,
        message: str
    ):

        payload = {
            "user_id": user_id,
            "message": message
        }

        response = await redis_client.xadd(
            settings.REDIS_CHAT_STREAM,
            {
                "data": json.dumps(payload)
            }
        )

        return response


queue_producer = QueueProducer()