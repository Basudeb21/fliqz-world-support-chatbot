from app.services.ticket.ticket_service import ticket_service


class ChatService:

    async def process_message(
        self,
        user_id: int,
        message: str
    ):

        if ticket_service.should_create_ticket(message):

            ticket = ticket_service.create_ticket(
                user_id,
                message
            )

            return {
                "success": True,
                "type": "ticket",
                "response": (
                    f"Your issue has been escalated "
                    f"to support under category: "
                    f"{ticket['category']}"
                ),
                "ticket_id": ticket["ticket_id"]
            }

        return {
            "success": True,
            "type": "chat",
            "response": (
                "This is a temporary AI response."
            ),
            "ticket_id": None
        }


chat_service = ChatService()