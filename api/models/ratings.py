from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=True)
    review = Column(String(500))
    score = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    sandwich = relationship("Sandwich", back_populates="ratings")

