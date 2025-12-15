from redis import Redis

from src.datamappers.redis_datamapper import RedisDataMapper


class RedisRepository:
    """ Репозиторий для работы с Redis"""
    
    datamapper: RedisDataMapper
    

    def __init__(self, client: Redis):
        self.aclient: Redis = client

    async def create_an_entry(self, phone: str, address: str) -> None:
        """Создание новой записи в Redis"""
        
        await self.aclient.set(f"phone:{phone}:address", address)
        
    async def get_value(self, phone: str) -> str | None:
        """ Получение значения по ключу """
        
        responce: bytes | None = await self.aclient.get(f"phone:{phone}:address")
        
        if not responce:
            return None
        
        client_address: str = self.datamapper.to_entity(redis_data=responce)
        
        return client_address
    
    async def update(self, phone: str, address: str) -> None:
        """ Обновляет значение ключа """
        
        await self.create_an_entry(phone, address)
    
    async def delete(self, phone: str) -> None:
        """ Удаляет значение """
        await self.aclient.delete(f"phone:{phone}:address")