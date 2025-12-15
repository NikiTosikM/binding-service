import re
from pydantic import BaseModel, ConfigDict, Field, field_validator


class PhoneAddressSchema(BaseModel):
    """ Схема, которая хранит номер телефона клиента и его адрес """
    
    phone: str
    address: str = Field(min_length=5, max_length=250)
    
    @field_validator("phone")
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", values):
            raise ValueError("Неверный номер телефона")
        return values
    
    model_config = ConfigDict(
        str_strip_whitespace=True
    )
    
    