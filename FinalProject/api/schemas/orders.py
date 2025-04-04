from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail

#Note from Pranav: I changed or orders a bit for payment / customer stuff
#  Make sure to include the changes I made in schemas, controller, and routers

class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
