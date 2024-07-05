from pydantic import BaseModel, Field
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

class GameSession(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    room_id: PyObjectId
    players: list
    state: dict