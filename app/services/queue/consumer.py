import json

from app.db.redis import redis_client
from app.core.config import settings


class QueueConsumer:

    async def create_group(self):

        try:

            await redis_client.xgroup_create(
                settings.REDIS_CHAT_STREAM,
                settings.REDIS_CONSUMER_GROUP,
                id="0",
                mkstream=True
            )

        except Exception:
            pass

    async def consume(self):

        while True:

            response = await redis_client.xreadgroup(
                groupname=settings.REDIS_CONSUMER_GROUP,
                consumername=settings.REDIS_CONSUMER_NAME,
                streams={
                    settings.REDIS_CHAT_STREAM: ">"
                },
                count=1,
                block=5000
            )

            if not response:
                continue

            yield response


queue_consumer = QueueConsumer()