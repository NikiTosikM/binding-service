from src.exceptions.server_exception import BaseException


class PhoneNotFound(BaseException):
    """ Номер телефона не найден """
    
class PhoneNumberAlreadyLinked(BaseException):
    """ Данный номер телефона уже првязан """
    
class PhoneFormatNotCorrect(BaseException):
    """ Формат номера телефона неверный """