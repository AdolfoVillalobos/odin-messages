from typing import List

from odin_messages.base import BaseEventMessageArray
from odin_messages.orders import (
    NewLimitOrderMessage,
    UpdateLimitOrderMessage,
    NewSpotOrderMessage,
)


class NewLimitOrdersArray(BaseEventMessageArray):
    messages: List[NewLimitOrderMessage]


class UpdateLimitOrdersArray(BaseEventMessageArray):
    messages: List[UpdateLimitOrderMessage]


class UpdateLimitOrdersArray(BaseEventMessageArray):
    messages: List[UpdateLimitOrderMessage]


class NewSpotOrdersArray(BaseEventMessageArray):
    messages: List[NewSpotOrderMessage]
