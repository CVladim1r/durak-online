from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    user_id: str
    amount: float
    currency: str

class TransactionResponse(BaseModel):
    id: str
    user_id: str
    amount: float
    currency: str
    timestamp: datetime
    type: str
