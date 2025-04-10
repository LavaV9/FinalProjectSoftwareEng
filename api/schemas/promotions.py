from pydantic import BaseModel
from datetime import date
from typing import Optional

class PromotionBase(BaseModel):
    code: str
    discount_percentage: int
    expiration_date: date

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount_percentage: Optional[int] = None
    expiration_date: Optional[date] = None

class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
