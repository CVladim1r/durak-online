# backend/app/routes/room.py

from fastapi import APIRouter, HTTPException
from typing import List
from ..models.room import Room, Player, GameStatus
from ..utils.room_manager import RoomManager

router = APIRouter()
room_manager = RoomManager()

@router.post("/room/create", response_model=Room)
def create_room(room_id: int):
    room_manager.create_room(room_id)
    return room_manager.get_room(room_id)

@router.post("/room/{room_id}/join", response_model=Room)
def join_room(room_id: int, player: Player):
    if not room_manager.add_player_to_room(room_id, player):
        raise HTTPException(status_code=404, detail="Room not found or full")
    return room_manager.get_room(room_id)

@router.get("/room/{room_id}", response_model=Room)
def read_room(room_id: int):
    room = room_manager.get_room(room_id)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.post("/room/{room_id}/start-game", response_model=Room)
def start_game(room_id: int):
    try:
        room_manager.start_game(room_id)
        return room_manager.get_room(room_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.post("/room/{room_id}/deal-cards", response_model=Room)
def deal_cards(room_id: int):
    try:
        room_manager.deal_cards(room_id)
        return room_manager.get_room(room_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.post("/room/{room_id}/play-card", response_model=Room)
def play_card(room_id: int, player_id: int, card_index: int):
    try:
        room_manager.play_card(room_id, player_id, card_index)
        return room_manager.get_room(room_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
