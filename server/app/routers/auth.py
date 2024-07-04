from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas import UserCreate, UserResponse
from app.models import User
from app.db import get_database
from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from app.services.auth import register_user, login_user

router = APIRouter()
oauth = OAuth()

class Settings(BaseModel):
    authjwt_secret_key: str = ""
    authjwt_algorithm: str = "HS256"

@AuthJWT.load_config
def get_config():
    return Settings()

@router.post('/register', response_model=UserResponse)
async def register(user: UserCreate, db: AsyncIOMotorClient = Depends(get_database)):
    return await register_user(user, db)

@router.post('/login')
async def login(telegram_code: str, Authorize: AuthJWT = Depends(), db: AsyncIOMotorClient = Depends(get_database)):
    return await login_user(telegram_code, Authorize, db)
