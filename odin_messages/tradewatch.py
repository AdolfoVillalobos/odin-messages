from odin_messages.base import BaseEventMessage


class NewTradeInOrderMessage(BaseEventMessage):
    exchange: str
    market_code: str
    order_id: str
    order_status: str
    order_type: str

class CanceledOrderMessage(BaseEventMessage):
    order_id: str
    exchange: str
    


