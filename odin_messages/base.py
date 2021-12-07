from pydantic import BaseModel


class BaseEventMessage(BaseModel):
    event: str
    time: int