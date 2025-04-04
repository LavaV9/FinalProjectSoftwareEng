from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentsBase(BaseModel):
    payment_type: str  # cash / card
    transaction_status: str
    card_last4: Optional[str] = None
    amount: float


class PaymentCreate(PaymentsBase):
    order_id: int


class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    card_last4: Optional[str] = None
    amount: Optional[float] = None


class Payment(PaymentsBase):
    id: int
    order_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
