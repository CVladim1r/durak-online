from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import UserCreate, UserResponse
from app.models import User
from fastapi_jwt_auth import AuthJWT
from fastapi import HTTPException

async def register_user(user: UserCreate, db: AsyncIOMotorClient):
    user_dict = user.dict()
    await db["users"].insert_one(user_dict)
    return user_dict

async def login_user(telegram_code: str, Authorize: AuthJWT, db: AsyncIOMotorClient):
    # Логика входа через Telegram
    user = await db["users"].find_one({"telegram_id": telegram_code})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    access_token = Authorize.create_access_token(subject=user["_id"])
    return {"access_token": access_token}
