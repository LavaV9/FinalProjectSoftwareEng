from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))

    sandwich_name = Column(String(100))
    price = Column(DECIMAL(6, 2), nullable=False, server_default='0.0')
    calories = Column(Integer, nullable=False, server_default='0')
    food_category = Column(String(100), nullable=False, server_default='')

    sandwich = relationship("Sandwich", back_populates="menu")

