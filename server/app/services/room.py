from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import RoomCreate, RoomResponse
from app.models import Room

async def create_room(room: RoomCreate, db: AsyncIOMotorClient):
    room_dict = room.dict()
    room_dict["code"] = "generated_code"  # generate_unique_code() should be implemented
    await db["rooms"].insert_one(room_dict)
    return room_dict

async def get_room_by_id(room_id: str, db: AsyncIOMotorClient):
    return await db["rooms"].find_one({"_id": room_id})
