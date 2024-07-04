from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    telegram_id: str

class UserResponse(BaseModel):
    id: str
    username: str
    balance: float
