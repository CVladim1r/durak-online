from pydantic import BaseSettings

class Settings(BaseSettings):
    authjwt_secret_key: str = ""
    mongo_url: str = "mongodb://localhost:27017"

settings = Settings()
