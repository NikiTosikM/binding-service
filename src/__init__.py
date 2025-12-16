from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.contact import router as contact_router
from src.core.redis.config import RedisCore



@asynccontextmanager
async def livespan(app: FastAPI):
    RedisCore.test_request() # тестовый запрос в БД
    
    yield
    
    RedisCore.close_pool()


def create_app() -> FastAPI:
    """ Создание и базовая настройка приложения """
    
    app = FastAPI(lifespan=livespan)
    
    app.include_router(contact_router)
    
    return app