from pydantic import BaseModel


class BaseEventMessage(BaseModel):
    event: str
    time: float
    strategy_id: str