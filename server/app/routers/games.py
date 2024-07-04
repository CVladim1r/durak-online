from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import GameAction, GameResponse
from app.db import get_database
from app.services.game import process_game_action

router = APIRouter()

@router.post('/{room_id}/action', response_model=GameResponse)
async def game_action(room_id: str, action: GameAction, db: AsyncIOMotorClient = Depends(get_database)):
    return await process_game_action(room_id, action, db)
