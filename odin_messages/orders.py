from odin_messages.base import BaseEventMessage


class NewLimitOrderMessage(BaseEventMessage):
    exchange: str
    market_code: str
    limit_price: str
    quantity: float
    usd_price: float
    price_delta: float
    selling: bool


class NewSpotOrderMessage(BaseEventMessage):
    exchange: str
    market_code: str
    quantity: float
    usd_price: float
    selling: bool


class CancelOrderMessage(BaseEventMessage):
    order_id: str
    exchange: str
    market_code: str


class UpdateOrderMessage(BaseEventMessage):
    order_id: str
    market_code: str
    exchange: str
    new_limit_price: float
    new_quantity: float
