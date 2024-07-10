from typing import Dict
from models.room import Room, Player, GameStatus
from models.game import Game
class GameManager:
    def __init__(self):
        self.rooms: Dict[int, Room] = {}

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

    def defend(self, room_id: int, player_id: int, defending_card_index: int) -> Room:
        room = self.rooms.get(room_id)
        if room is None:
            raise ValueError(f"Room {room_id} not found")

        if room.status != GameStatus.IN_PROGRESS:
            raise ValueError(f"Cannot defend. Game in room {room_id} is not in progress")

        player = next((p for p in room.players if p.id == player_id), None)
        if player is None:
            raise ValueError(f"Player {player_id} not found in room {room_id}")

        if defending_card_index < 0 or defending_card_index >= len(room.attack_cards):
            raise ValueError(f"Invalid defending card index {defending_card_index} in room {room_id}")

        defending_card = player.hand.pop(defending_card_index)
        room.defend_cards.append(defending_card)

        return room

    def end_turn(self, room_id: int) -> Room:
        room = self.rooms.get(room_id)
        if room is None:
            raise ValueError(f"Room {room_id} not found")

        if room.status != GameStatus.IN_PROGRESS:
            raise ValueError(f"Cannot end turn. Game in room {room_id} is not in progress")

        if len(room.players) > 1 and all(not p.hand for p in room.players):
            room.status = GameStatus.FINISHED

        room.current_turn = (room.current_turn + 1) % len(room.players)

        return room


    def create_room(self, room_id: int):
        self.rooms[room_id] = Room(id=room_id, game=Game())

    def add_player_to_room(self, room_id: int, player: Player):
        if room_id in self.rooms:
            room = self.rooms[room_id]
            if len(room.players) < room.max_players:
                room.players.append(player)
                return True
        return False

    def get_room(self, room_id: int):
        return self.rooms.get(room_id)

    async def handle_play_card(self, room_id: int, player_id: int, message: dict):
        card_index = message.get("card_index")

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

        await self.broadcast(room_id, {"action": "update_game_state"})

    async def broadcast(self, room_id: int, message: dict):
        for client in connected_clients.values():
            await client.send_text(json.dumps(message))
