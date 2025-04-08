from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail

#Note from Pranav: I changed or orders a bit for payment / customer stuff
#  Make sure to include the changes I made in schemas, controller, and routers
#Note from Austin: I added variables for the following: order_date, tracking_number, order_status, total_price,
class OrderBase(BaseModel):
    customer_id: int
    #customer_name: Optional[str] = None
    description: Optional[str] = None
    order_date: Optional[datetime] = None
    tracking_number: Optional[int] = None
    status: Optional[str] = None
    total_price: float


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: int
    #customer_name: Optional[str] = None
    description: Optional[str] = None
    order_date: Optional[datetime] = None
    tracking_number: Optional[int] = None
    status: Optional[str] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    id: int
    order_details: list[OrderDetail] = None


    class ConfigDict:
        from_attributes = True
