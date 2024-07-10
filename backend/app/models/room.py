# backend/app/models.py

from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class GameStatus(str, Enum):
    WAITING_FOR_PLAYERS = "waiting_for_players"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"

class Card(BaseModel):
    rank: str
    suit: str

class Player(BaseModel):
    id: int
    username: str
    hand: List[Card] = []

class Room(BaseModel):
    id: int
    players: List[Player] = []
    max_players: int = 2
    status: GameStatus = GameStatus.WAITING_FOR_PLAYERS
    deck: List[Card] = []
    current_turn: int = 0
    played_cards: List[Card] = []
    attack_cards: List[Card] = []
    defend_cards: List[Card] = []
    trump_card: Card = None
