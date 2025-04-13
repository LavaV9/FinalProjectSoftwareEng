from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, nullable=False, server_default='0')

    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    sandwich = relationship("Sandwich", back_populates="resources")
