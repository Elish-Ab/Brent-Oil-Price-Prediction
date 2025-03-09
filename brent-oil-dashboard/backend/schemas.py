from pydantic import BaseModel
from datetime import datetime

class Price(BaseModel):
    id: int
    price: float
    timestamp: datetime

    class Config:
        orm_mode = True
