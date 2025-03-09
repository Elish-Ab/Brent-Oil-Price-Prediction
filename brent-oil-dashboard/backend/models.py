from sqlalchemy import Column, Integer, Float, DateTime
from database import Base
from datetime import datetime

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
