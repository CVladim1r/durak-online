from pydantic import BaseModel

class Player(BaseModel):
    id: int
    username: str
    hand: list = []

    def __init__(self, id: int, username: str, hand: list = []):
        self.id = id
        self.username = username
        self.hand = hand
