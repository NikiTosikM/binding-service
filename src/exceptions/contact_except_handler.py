from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from src.exceptions.phone_address_exception import PhoneNotFound, PhoneNumberAlreadyLinked, PhoneFormatNotCorrect


def contact_error_handler(app: FastAPI):
    @app.exception_handler(PhoneNotFound)
    def phone_not_fount(request: Request, exc: PhoneNotFound):
        return ORJSONResponse(
            status_code=404,
            content={
                "message": "Данный номер телефона не найден"
            }
        )
        
    @app.exception_handler(PhoneNumberAlreadyLinked)
    def phone_number_already_linked(request: Request, exc: PhoneNumberAlreadyLinked):
        return ORJSONResponse(
            status_code=409,
            content={
                "message": "Нельзя привязать два адреса к одному номеру телефона"
            }
        )
        
    @app.exception_handler(PhoneFormatNotCorrect)
    def phone_number_not_correct(request: Request, exc: PhoneNumberAlreadyLinked):
        return ORJSONResponse(
            status_code=422,
            content={
                "message": "Неверный формат номера телефона",
                "detail": "Исправь значение в поле - phone. Пример - '79275052132' (11 цифр). "
            }
        )