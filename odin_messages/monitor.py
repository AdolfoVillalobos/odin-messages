
from typing import Dict, Any
from odin_messages.base import BaseEventMessage


class CurrentOpenOrdersMessage(BaseEventMessage):
    exchange: str
    open_orders: Dict[str, Any]
