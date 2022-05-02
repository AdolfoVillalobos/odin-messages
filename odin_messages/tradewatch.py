from typing import Dict, Optional

from odin_messages.balance import CoinBalance
from odin_messages.base import BaseEventMessage


class NewOpenOrderMessage(BaseEventMessage):
    exchange: str
    order_id: str
    market_code: str
    amount: float
    type: str
    selling: str
    status: str
    limit_price: Optional[float]
    custom_id: Optional[str]


class CanceledOrderMessage(BaseEventMessage):
    exchange: str
    order_id: str
    status: str
    market_code: str
    type: str
    selling: str
    custom_id: Optional[str]


class OrderFilledMessage(BaseEventMessage):
    exchange: str
    order_id: str
    status: str
    market_code: str
    type: str
    selling: str
    amount: float
    filled: float
    remaining: float
    limit_price: Optional[float]
    custom_id: Optional[str]


class WebsocketTradeMessage(BaseEventMessage):
    exchange: str
    order_id: str
    transaction_id: str
    market_code: str
    type: str
    selling: str
    amount: float
    limit_price: float
    custom_id: Optional[str]


class WalletBalanceUpdate(BaseEventMessage):
    exchange: str
    currency_code: str
    balance: float
    used_balance: float


class FirstBalance(BaseEventMessage):
    exchange: str
    coins: Dict[str, CoinBalance]


class NewTradeMessage(BaseEventMessage):
    exchange: str
    market_code: str
    type: str
    amount: float
    percentage_of_order: Optional[float]
    price: Optional[float]
    quoted_amount: Optional[float]
    custom_id: Optional[str]
