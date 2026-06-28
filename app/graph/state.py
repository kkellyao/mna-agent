import operator
from typing import Annotated

from typing_extensions import TypedDict


class DiligenceState(TypedDict):
    deal_name: str
    status: str
    messages: Annotated[list[str], operator.add]
