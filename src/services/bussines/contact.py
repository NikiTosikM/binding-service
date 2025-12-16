from redis import Redis

from src.repositories.redis import RedisRepository
from src.schemas.phone_address import PhoneAddressSchema
from src.exceptions.phone_address_exception import (
    PhoneNotFound,
    PhoneNumberAlreadyLinked,
)


class ContactService:
    """Сервис для работы с данными клиента"""

    def __init__(self, redis_client: Redis):
        self._repository = RedisRepository(client=redis_client)

    async def verify_existence_phone_number(self, phone: str) -> None:
        """ Проверяем существует ли номер телефона в БД """
        
        exist_phone_number = await self._repository.get_value(phone)
        if not exist_phone_number:
            raise PhoneNotFound

    async def bundle_phone_to_address(self, data: PhoneAddressSchema) -> None:
        """Привязываем адрес к номеру телефона клиента"""

        phone, address = data.phone, data.address
        verify_existence_phone_number = await self._repository.get_value(phone)
        
        if verify_existence_phone_number:
            raise PhoneNumberAlreadyLinked

        await self._repository.create_an_entry(phone, address)

    async def get_address_by_phone(self, phone: str) -> str:
        """Получаем адрес по номеру телефона"""

        await self.verify_existence_phone_number(phone)

        address: str = await self._repository.get_value(phone)

        return address

    async def update_address(self, data: PhoneAddressSchema) -> None:
        """Обновляем адрес"""
        
        phone, address = data.phone, data.address
        await self.verify_existence_phone_number(phone)
        await self._repository.update(phone, address)

    async def delete_address_linked_to_phone(self, phone: str) -> None:
        """Удаляем адрес, привязанный к номеру телефона"""

        await self.verify_existence_phone_number(phone)
        await self._repository.delete(phone)
