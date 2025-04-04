from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id")) #don't touch
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String(50), nullable=False, default="pending")


    customers = relationship("Customers", back_populates="orders") # relationship with customers table
    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payments", uselist=False, back_populates="order") # relationship with payment table
