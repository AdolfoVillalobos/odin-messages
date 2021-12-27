from typing import Array
from pydantic import BaseModel


class BaseEventMessage(BaseModel):
    event: str
    time: float
    strategy_id: str

class BaseEventMessageArray(BaseModel):
    event: str
    time: float
    strategy_id: str
    messages: Array[BaseEventMessage]