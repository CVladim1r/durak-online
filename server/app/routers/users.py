from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import User
from app.schemas import UserResponse
from app.db import get_database

router = APIRouter()

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    user = await db["users"].find_one({"_id": user_id})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
