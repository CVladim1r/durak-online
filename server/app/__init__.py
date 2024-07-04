from fastapi import FastAPI
from app.routers import auth, users, rooms, games, transactions, websocket

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(games.router, prefix="/games", tags=["games"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(websocket.router, prefix="/ws", tags=["websockets"])
