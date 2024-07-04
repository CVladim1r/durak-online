from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import GameAction, GameResponse
from app.models import GameSession

async def process_game_action(room_id: str, action: GameAction, db: AsyncIOMotorClient):
    return {"state": {}}
