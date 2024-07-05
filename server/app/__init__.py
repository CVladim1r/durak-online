from fastapi import FastAPI
from app.routers import auth, users, rooms, games, transactions, websocket
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Durak Online API",
        version="1.0.0",
        description="API for the Durak online game",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.openapi = custom_openapi

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(games.router, prefix="/games", tags=["games"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(websocket.router, prefix="/ws", tags=["websockets"])
