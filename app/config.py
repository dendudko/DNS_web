from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_database: str
    db_host: str
    db_port: int
    debug: bool = False

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
