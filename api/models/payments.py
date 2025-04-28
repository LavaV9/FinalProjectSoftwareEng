from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    card_last4 = Column(String(4), nullable=True)
    payment_type = Column(String(50), nullable=False)  # card or cash
    transaction_status = Column(String(50), nullable=False)  # success or failed
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    order = relationship("Order", back_populates="payments")
