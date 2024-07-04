from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

class Transaction(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    amount: float
    currency: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    type: str  # "deposit" or "withdrawal"
