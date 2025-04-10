from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich


class MenuBase(BaseModel):
    sandwich_name: str
    ingredients: Optional[list] = None
    price: int
    calories: int
    food_category: str


class MenuCreate(MenuBase):
    sandwich_id: int
    resource_id: int

class MenuUpdate(BaseModel):
    sandwich_name: str
    ingredients: Optional[list] = None
    price: int
    calories: int
    food_category: str
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class Menu(MenuBase):
    id: int
    sandwich: Sandwich = None
    resource: Resource = None
    ingredients: Optional[list] = None

    class ConfigDict:
        from_attributes = True