from typing import List

from pydantic import BaseModel, Field


class Material(BaseModel):
    name: str
    qty: float = Field(gt=0)
    price_rub: float = Field(gt=0)


class CalcRequest(BaseModel):
    materials: List[Material]


class CalcResponse(BaseModel):
    total_cost_rub: float
