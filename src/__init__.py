from fastapi import FastAPI


def create_app() -> FastAPI:
    """ Создание и базовая настройка приложения """
    
    app = FastAPI()
    
    return app