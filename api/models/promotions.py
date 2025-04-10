from sqlalchemy import Column, Integer, String, Date
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_percentage = Column(Integer, nullable=False)
    expiration_date = Column(Date, nullable=False)
