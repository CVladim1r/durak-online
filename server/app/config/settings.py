from pydantic import BaseSettings

class Settings(BaseSettings):
    authjwt_secret_key: str = ""
    mongo_url: str = "mongodb://localhost:27017"
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 30  # Добавляем значение по умолчанию

    class Config:
        env_file = ".env"

settings = Settings()