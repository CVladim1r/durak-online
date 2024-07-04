from pydantic import BaseModel

class GameAction(BaseModel):
    player_id: str
    action: dict

class GameResponse(BaseModel):
    state: dict
