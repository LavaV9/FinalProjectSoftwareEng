from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float
    resource_id: int


class SandwichCreate(SandwichBase):
    resource_id: int


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None


class Sandwich(SandwichBase):
    id: int
    resource: Resource = None

    class ConfigDict:
        from_attributes = True