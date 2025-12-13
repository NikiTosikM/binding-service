from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


SRC_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve().parent.parent.parent


class UvicornConfig(BaseModel):
    """Класс настройки uvicorn"""

    host: str
    port: int
    reload: bool = False


class RedisConfig(BaseModel):
    """Класс настройки Redis"""

    host: str
    port: int = 6379
    db: int = 0

    @property
    def get_redis_url(self):
        return f"redis://{self.host}:{self.port}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{ROOT_DIR}/.env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )
    
    uv: UvicornConfig
    redis: RedisConfig
