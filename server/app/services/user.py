from motor.motor_asyncio import AsyncIOMotorClient

async def get_user_by_id(user_id: str, db: AsyncIOMotorClient):
    return await db["users"].find_one({"_id": user_id})
