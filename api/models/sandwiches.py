from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    resource_id = Column(Integer, ForeignKey("resources.id"))
    resource_amount = Column(Integer, nullable=False, default=1)

    resource = relationship("Resource", back_populates="sandwiches")
    ratings = relationship("Rating", back_populates="sandwich")

    menu = relationship("Menu", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")

