from typing import List, Optional
from .player import Player
from .card import Card

class Game:
    def __init__(self):
        self.deck: List[Card] = []
        self.players: List[Player] = []
        self.trump_card: Optional[Card] = None
        self.current_player_index: int = 0
        self.attacking_player_index: Optional[int] = None
        self.defending_player_index: Optional[int] = None
        self.table_cards: List[Card] = []

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]

    def deal_cards(self):
        for _ in range(6):
            for player in self.players:
                player.hand.append(self.deck.pop(0))

    def set_trump_card(self, card: Card):
        self.trump_card = card

    def start_game(self):
        self.create_deck()
        self.deal_cards()
        self.trump_card = self.deck.pop(0)

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_card(self, player: Player, card: Card):
        if player.hand.count(card) == 0:
            raise ValueError("Player does not have this card in hand")
        
        if self.attacking_player_index is None:
            self.attacking_player_index = self.current_player_index
        
        if self.current_player_index != self.attacking_player_index:
            if not self.is_defending_card_valid(card):
                raise ValueError("Defending card is not valid")
            self.defending_player_index = self.current_player_index

        self.table_cards.append(card)
        player.hand.remove(card)
        self.next_turn()

    def is_defending_card_valid(self, card: Card):
        if not self.table_cards:
            return False
        
        attacking_card = self.table_cards[-1]
        if attacking_card.rank == card.rank:
            return True
        if card.rank == 'Ace':
            return True
        return False

    def end_turn(self):
        self.attacking_player_index = None
        self.defending_player_index = None
        self.table_cards = []

    def get_game_state(self):
        return {
            "players": [player.dict() for player in self.players],
            "current_player_index": self.current_player_index,
            "attacking_player_index": self.attacking_player_index,
            "defending_player_index": self.defending_player_index,
            "table_cards": [card.dict() for card in self.table_cards],
            "trump_card": self.trump_card.dict() if self.trump_card else None
        }
