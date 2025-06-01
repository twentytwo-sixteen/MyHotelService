from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # prod base
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://postgres:postgres@db:5432/hotel_db",
        env="DATABASE_URL",
    )

    class Config:
        env_file = ".env"


settings = Settings()
