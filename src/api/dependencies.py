from typing import Annotated

from redis.asyncio import Redis
from fastapi import Depends

from src.core.redis.config import RedisCore


async def get_redis_client():
    async with RedisCore.create_client() as aclient:
        yield aclient
        
RedisClientDep = Annotated[Redis, Depends(get_redis_client)]