from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float
    ingredients: Optional[list] = None


class SandwichCreate(SandwichBase):
    sandwich_id: int
    resource_id: int


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None
    ingredients: Optional[list] = None


class Sandwich(SandwichBase):
    id: int

    ingredients: Optional[list] = None
    class ConfigDict:
        from_attributes = True