from pydantic import BaseModel
from typing import Dict

from odin_messages.base import BaseEventMessage


class PriceWatchMessage(BaseEventMessage):
    exchange: str
    market_code: str
    ask_price: float
    ask_delta: float
    bid_price: float
    bid_delta: float


class OneSidePriceWatchMessage(BaseEventMessage):
    exchange: str
    market_code: str
    price: float
    delta: float


class NewUSDPriceMessage(BaseEventMessage):
    symbol: str
    ask: float
    bid: float


class NewPriceReferenceMessage(BaseEventMessage):
    prices: Dict[str, float]


class NewPriceMinimumDeltaMessage(BaseEventMessage):
    market_code: str
    minimum_delta: float


class NewOrderBookDephMessage(BaseEventMessage):
    market_code: str
    depth: float
