from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RatingBase(BaseModel):
    customer_id: int
    menu_item_id: Optional[int] = None
    review: str
    score: int


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    review: Optional[str] = None
    score: Optional[int] = None


class Rating(RatingBase):
    id: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True
