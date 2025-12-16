import re
from pydantic import BaseModel, ConfigDict, Field, field_validator



def validate_phone_number(phone: str) -> str:
    """Общая функция для валидации номера телефона"""
    if not re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", phone):
        raise ValueError("Неверный номер телефона")
    return phone

class PhoneAddressSchema(BaseModel):
    """ Схема, которая хранит номер телефона клиента и его адрес """
    
    phone: str
    address: str = Field(min_length=5, max_length=250)
    
    @field_validator("phone")
    def phone_validator(cls, values: str) -> str:
        return validate_phone_number(phone=values)
    
    model_config = ConfigDict(
        str_strip_whitespace=True
    )
    
class PhoneSchema(BaseModel):
    """ Схема для получения номера телефона """
    
    phone: str
    
    @field_validator("phone")
    def validate_phone_number(cls, values: str) -> str:
        return validate_phone_number(phone=values)
    
    model_config = ConfigDict(
        str_strip_whitespace=True
    )
    

class AddressSchema(BaseModel):
    """ Схема для получения адреса"""
    
    address: str