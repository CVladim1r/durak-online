from pydantic import BaseModel

class RoomCreate(BaseModel):
    name: str
    is_private: bool

class RoomResponse(BaseModel):
    id: str
    name: str
    code: str
    is_private: bool
