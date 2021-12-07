from pydantic import BaseModel

from odin_messages.base import BaseEventMessage


class PriceWatchMessage(BaseEventMessage):
    exchange: str
    market_code: str
    ask_price: float
    ask_delta: float
    bid_price: float
    bid_delta: float
