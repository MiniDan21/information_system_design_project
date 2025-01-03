import uuid
from enum import Enum
from typing import List
from pydantic import BaseModel


class ListIDRequest(BaseModel):
    list_id: List[int]
