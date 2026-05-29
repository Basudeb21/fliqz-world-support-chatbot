from app.schemas.ticket import TICKET_CATEGORIES


class TicketService:

    def detect_ticket_type(self, message: str):

        msg = message.lower()

        if "payment" in msg:
            return "Payment Issue"

        elif "refund" in msg:
            return "Refund Request"

        elif "login" in msg or "account" in msg:
            return "Account Access Issue"

        elif "order" in msg and "not" in msg:
            return "Order Not Delivered"

        return "Other"

    def should_create_ticket(self, message: str):

        msg = message.lower()

        trigger_words = [
            "not working",
            "angry",
            "frustrated",
            "refund",
            "payment",
            "human",
            "support",
            "issue",
            "problem",
            "complaint"
        ]

        return any(word in msg for word in trigger_words)

    def create_ticket(self, user_id: int, message: str):

        category = self.detect_ticket_type(message)

        return {
            "ticket_id": 1001,
            "category": category,
            "status": "open"
        }


ticket_service = TicketService()