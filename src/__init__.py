from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.contact import router as contact_router
from src.core.redis.config import RedisCore
from src.exceptions.server_except_handler import server_error_handler
from src.exceptions.contact_except_handler import contact_error_handler



@asynccontextmanager
async def livespan(app: FastAPI):
    await RedisCore.test_request() # тестовый запрос в БД
    
    yield
    
    await RedisCore.close_pool()


def create_app() -> FastAPI:
    """ Создание и базовая настройка приложения """
    
    app = FastAPI(lifespan=livespan)
    
    app.include_router(contact_router)
    
    server_error_handler(app)
    contact_error_handler(app)
    
    return app