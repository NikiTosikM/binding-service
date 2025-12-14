class RedisDataMapper:
    """ DataMapper для работы с данными Redis """
    
    @staticmethod
    def to_entity(redis_data: bytes) -> str | None:
        """ Преобразует байты из Redis в строку """
        
        return redis_data.decode("utf-8")