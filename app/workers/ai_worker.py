import asyncio
import json

from app.services.queue.consumer import (
    queue_consumer
)

from app.services.chat.chat_service import (
    chat_service
)

from app.db.redis import redis_client
from app.core.config import settings


async def start_worker():

    await queue_consumer.create_group()

    print("AI Worker Started...")

    async for messages in queue_consumer.consume():

        for stream_name, entries in messages:

            for message_id, data in entries:

                try:

                    payload = json.loads(data["data"])

                    user_id = payload["user_id"]
                    message = payload["message"]

                    print(f"Processing: {message}")

                    response = await (
                        chat_service.process_message(
                            user_id=user_id,
                            message=message
                        )
                    )

                    print("AI Response:", response)

                    await redis_client.xack(
                        settings.REDIS_CHAT_STREAM,
                        settings.REDIS_CONSUMER_GROUP,
                        message_id
                    )

                except Exception as e:

                    print("Worker Error:", e)


if __name__ == "__main__":

    asyncio.run(start_worker())