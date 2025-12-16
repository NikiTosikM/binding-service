from contextlib import asynccontextmanager
from typing import AsyncGenerator

from redis.asyncio import Redis, ConnectionPool, ConnectionError

from src.core.config import settings
from src.exceptions.server_except_handler import server_error_handler


class RedisCore:
    """Основной класс настройки ядра Redis"""

    _conn_pool: ConnectionPool | None = None

    @classmethod
    def _create_connection_pool(cls) -> None:
        cls.conn_pool = ConnectionPool.from_url(
            url=settings.redis.get_redis_url, max_connections=10
        )

    @classmethod
    @asynccontextmanager
    async def create_client(cls) -> AsyncGenerator[Redis, None]:
        try:
            if not cls._conn_pool:
                cls._create_connection_pool()

            client: Redis = Redis(connection_pool=cls.conn_pool)

            yield client
        except ConnectionError:
            raise server_error_handler
        finally:
            await client.aclose()

    @classmethod
    async def close_pool(cls):
        """Закрытие пула соединений"""
        if cls._conn_pool:
            await cls._conn_pool.disconnect()
            cls._conn_pool = None

    @classmethod
    async def test_request(cls) -> None:
        """Тестовый запрос к Redis для проверки соединения"""

        async with cls.create_client() as client:
            request_ping: bool = await client.ping()

        if not request_ping:
            raise server_error_handler