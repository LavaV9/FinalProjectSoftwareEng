from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customers(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index = True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(100), nullable=True)
    address = Column(String(200), nullable=True)

    orders = relationship("Order", back_populates="customers")