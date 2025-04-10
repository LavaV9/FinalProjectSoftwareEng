from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwich.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    sandwich_name = Column(String)
    price = Column(Integer, index=True, nullable=False, server_default='0.0')
    calories = Column(Integer, index=True, nullable=False, server_default='0.0')
    food_category = Column(String, index=True, nullable=False, server_default='')


    ingredients = relationship("Ingredient", backref="menu")
    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")