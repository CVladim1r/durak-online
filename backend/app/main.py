from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
import json

from utils.room_manager import RoomManager
from utils.game_logic import GameManager
from models.room import Room, Player

app = FastAPI()

# Хранилище подключенных клиентов
connected_clients: Dict[tuple, WebSocket] = {}

# Менеджеры комнат и игровой логики
room_manager = RoomManager()
game_manager = GameManager()

# Обработчик WebSocket соединения
@app.websocket("/ws/{room_id}/{player_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, player_id: int):
    await websocket.accept()
    key = (room_id, player_id)
    connected_clients[key] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            action = message.get("action")

            if action == "create_room":
                room_manager.create_room(room_id)
                await websocket.send_json({"action": "room_created", "room_id": room_id})

            elif action == "add_player":
                player = Player(**message["player"])
                if room_manager.add_player_to_room(room_id, player):
                    await websocket.send_json({"action": "player_added", "player": player.dict()})
                else:
                    await websocket.send_json({"action": "error", "message": f"Room {room_id} not found or already full"})

            elif action == "start_game":
                try:
                    room = room_manager.start_game(room_id)
                    await websocket.send_json({"action": "game_started"})
                except ValueError as e:
                    await websocket.send_json({"action": "error", "message": str(e)})

            elif action == "play_card":
                try:
                    room = await game_manager.play_card(room_id, player_id, message["card_index"])
                    await _broadcast_game_state(room)
                except ValueError as e:
                    await websocket.send_json({"action": "error", "message": str(e)})

            elif action == "end_turn":
                try:
                    room = room_manager.end_turn(room_id)
                    await _broadcast_game_state(room)
                except ValueError as e:
                    await websocket.send_json({"action": "error", "message": str(e)})

            elif action == "get_room_info":
                room = room_manager.get_room(room_id)
                if room:
                    await websocket.send_json({"action": "room_info", "room_id": room.id, "players": [player.dict() for player in room.players]})
                else:
                    await websocket.send_json({"action": "error", "message": f"Room {room_id} not found"})

            elif action == "get_all_rooms":
                await websocket.send_json({"action": "all_rooms", "rooms": [room.id for room in room_manager.rooms.values()]})

            elif action == "chat_message":
                _broadcast_chat_message(room_id, message["message"])

            elif action == "get_player_info":
                room = room_manager.get_room(room_id)
                if room:
                    player = next((p for p in room.players if p.id == player_id), None)
                    if player:
                        await websocket.send_json({"action": "player_info", "player": player.dict()})
                    else:
                        await websocket.send_json({"action": "error", "message": f"Player {player_id} not found in room {room_id}"})
                else:
                    await websocket.send_json({"action": "error", "message": f"Room {room_id} not found"})

            elif action == "delete_room":
                try:
                    del room_manager.rooms[room_id]
                    await _broadcast_room_deleted(room_id)
                except KeyError:
                    await websocket.send_json({"action": "error", "message": f"Room {room_id} not found"})


            elif action == "get_game_state":
                room = room_manager.get_room(room_id)
                if room:
                    await websocket.send_json({"action": "game_state", "current_turn": room.current_turn, "played_cards": room.played_cards, "status": room.status})
                else:
                    await websocket.send_json({"action": "error", "message": f"Room {room_id} not found"})

            elif action == "end_game":
                try:
                    room = game_manager.end_game(room_id)
                    await _broadcast_game_state(room)
                except ValueError as e:
                    await websocket.send_json({"action": "error", "message": str(e)})

            elif action == "defend":
                try:
                    room = game_manager.defend(room_id, player_id, message["defending_card_index"])
                    await _broadcast_game_state(room)
                except ValueError as e:
                    await websocket.send_json({"action": "error", "message": str(e)})

            elif action == "end_turn":
                try:
                    room = game_manager.end_turn(room_id)
                    await _broadcast_game_state(room)
                except ValueError as e:
                    await websocket.send_json({"action": "error", "message": str(e)})

    except WebSocketDisconnect:
        del connected_clients[key]

async def _broadcast_game_state(room: Room):
    for player in room.players:
        key = (room.id, player.id)
        if key in connected_clients:
            await connected_clients[key].send_json({"action": "game_state", "current_turn": room.current_turn, "played_cards": room.played_cards, "status": room.status})

async def _broadcast_chat_message(room_id: int, message: str):
    for client in connected_clients.values():
        await client.send_json({"action": "chat_message", "message": message})

async def _broadcast_room_deleted(room_id: int):
    for client in connected_clients.values():
        await client.send_json({"action": "room_deleted", "room_id": room_id})