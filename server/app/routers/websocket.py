from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from motor.motor_asyncio import AsyncIOMotorClient
from app.db import get_database
from app.game_logic import process_game_action

router = APIRouter()

@router.websocket('/game/{room_id}')
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response = await process_game_action(room_id, data)
            await websocket.send_text(response)
    except WebSocketDisconnect:
        await websocket.close()
