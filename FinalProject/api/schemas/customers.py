from typing import Optional
from pydantic import BaseModel


class CustomersBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class CustomerCreate(CustomersBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class Customers(CustomersBase):
    id: int

    class ConfigDict:
        from_attributes = True
