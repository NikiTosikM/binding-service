from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from src.api.dependencies import RedisClientDep
from src.services.bussines.contact import ContactService
from src.schemas.phone_address import PhoneAddressSchema, AddressSchema


router = APIRouter(
    prefix="/contacts",
    tags=["Работа с данными клиента"],
    default_response_class=ORJSONResponse,
)


@router.get(
    "/{phone_number}",
    description="Получение адреса по номеру телефона",
    responses={
        200: {"description": "Адрес найден"},
        404: {"description": "Данный номер телефона не зарегистрирован"},
    },
)
async def get_client_address(phone_number: str, rd_client: RedisClientDep):
    contract_service = ContactService(redis_client=rd_client)

    address: str = await contract_service.get_address_by_phone(phone=phone_number)

    return {"address": address}


@router.post(
    "/",
    description="Привязываем адрес к номеру телефона",
    status_code=201,
    responses={
        201: {"description": "Запись создана"},
        409: {"description": "Нельзя привязать два адреса к одному номеру телефона"}
    }
)
async def bundle_client_contact(
    client_contact: PhoneAddressSchema, rd_client: RedisClientDep
):
    contract_service = ContactService(redis_client=rd_client)

    await contract_service.bundle_phone_to_address(data=client_contact)

    return {
        "message": "Запись создана",
        "phone": client_contact.phone,
        "address": client_contact.address,
    }


@router.patch(
    "/{phone_number}", 
    description="Обновление адреса",
    responses={
        200: {"description": "Запись обновлена"},
        404: {"description": "Данный номер телефона не зарегистрирован"}
    }
)
async def update_address(
    phone_number: str, address: AddressSchema, rd_client: RedisClientDep
):
    contract_service = ContactService(redis_client=rd_client)

    client_contacts = PhoneAddressSchema(phone=phone_number, address=address.address)

    await contract_service.update_address(data=client_contacts)

    return client_contacts


@router.delete(
    "/{phone_number}", 
    description="Удаляем контакты клиента",
    status_code=204,
    responses={
        204: {"description": "Запись удалена"},
        404: {"description": "Данный номер телефона не зарегистрирован"}
    }
)
async def delete_contact(phone_number: str, rd_client: RedisClientDep):
    contract_service = ContactService(redis_client=rd_client)

    await contract_service.delete_address_linked_to_phone(phone=phone_number)
