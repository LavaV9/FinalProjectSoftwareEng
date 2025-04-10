from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False) #don't touch
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String(50), nullable=False, default="pending")
    description = Column(String(50), nullable=False, default="no Description")
    tracking_number = Column(Integer, nullable=True)
    total_price = Column(DECIMAL(10, 2), nullable=False, default=0.00)

    customers = relationship("Customers", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payments", uselist=False, back_populates="order")