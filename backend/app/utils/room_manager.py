from typing import Dict, List, Optional
from random import shuffle
from ..models.room import Room, Player, Card, GameStatus

class RoomManager:
    def __init__(self):
        self.rooms: Dict[int, Room] = {}

    def create_room(self, room_id: int):
        self.rooms[room_id] = Room(id=room_id)

    def add_player_to_room(self, room_id: int, player: Player) -> bool:
        if room_id in self.rooms:
            if len(self.rooms[room_id].players) < self.rooms[room_id].max_players:
                self.rooms[room_id].players.append(player)
                return True
        return False

    def get_room(self, room_id: int) -> Optional[Room]:
        return self.rooms.get(room_id)

    def start_game(self, room_id: int) -> Room:
        room = self.rooms.get(room_id)
        if room is None:
            raise ValueError(f"Room {room_id} not found")

        if room.status != GameStatus.WAITING_FOR_PLAYERS:
            raise ValueError(f"Room {room_id} cannot start game. Status: {room.status}")

        if len(room.players) < 2:
            raise ValueError(f"Not enough players to start the game in room {room_id}")

        room.deck = self.create_deck()
        self.deal_cards(room_id)
        room.status = GameStatus.IN_PROGRESS
        room.current_turn = 0
        room.played_cards = []
        room.attack_cards = []
        room.defend_cards = []
        room.trump_card = room.deck[-1]
        return room

    def deal_cards(self, room_id: int):
        room = self.rooms.get(room_id)
        if room is None:
            raise ValueError(f"Room {room_id} not found")

        if room.status != GameStatus.IN_PROGRESS:
            raise ValueError(f"Cannot deal cards. Game in room {room_id} is not in progress")

        deck = room.deck
        shuffle(deck)
        num_players = len(room.players)
        for i in range(num_players):
            hand_start = i * 6
            hand_end = hand_start + 6
            room.players[i].hand = deck[hand_start:hand_end]

    def play_card(self, room_id: int, player_id: int, card_index: int) -> Room:
        room = self.rooms.get(room_id)
        if room is None:
            raise ValueError(f"Room {room_id} not found")

        if room.status != GameStatus.IN_PROGRESS:
            raise ValueError(f"Cannot play card. Game in room {room_id} is not in progress")

        player = next((p for p in room.players if p.id == player_id), None)
        if player is None:
            raise ValueError(f"Player {player_id} not found in room {room_id}")

        if player.id != room.current_turn:
            raise ValueError(f"It's not player {player_id}'s turn to play in room {room_id}")

        if card_index < 0 or card_index >= len(player.hand):
            raise ValueError(f"Invalid card index {card_index} for player {player_id} in room {room_id}")

        played_card = player.hand.pop(card_index)
        room.played_cards.append(played_card)

        if not room.attack_cards:
            room.attack_cards.append(played_card)
        elif not room.defend_cards:
            room.defend_cards.append(played_card)

        room.current_turn = (room.current_turn + 1) % len(room.players)
        return room

    def end_turn(self, room_id: int) -> Room:
        room = self.rooms.get(room_id)
        if room is None:
            raise ValueError(f"Room {room_id} not found")

        if room.status != GameStatus.IN_PROGRESS:
            raise ValueError(f"Cannot end turn. Game in room {room_id} is not in progress")

        if len(room.players) > 1 and all(not p.hand for p in room.players):
            room.status = GameStatus.FINISHED

        return room

    def create_deck(self) -> List[Card]:
        ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [Card(rank=rank, suit=suit) for suit in suits for rank in ranks]
        return deck
