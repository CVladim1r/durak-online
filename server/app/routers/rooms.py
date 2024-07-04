from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import Room
from app.schemas import RoomCreate, RoomResponse
from app.db import get_database
from app.services.room import create_room, get_room_by_id

router = APIRouter()

@router.post('/', response_model=RoomResponse)
async def create_new_room(room: RoomCreate, db: AsyncIOMotorClient = Depends(get_database)):
    return await create_room(room, db)

@router.get('/{room_id}', response_model=RoomResponse)
async def get_room(room_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    room = await get_room_by_id(room_id, db)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
