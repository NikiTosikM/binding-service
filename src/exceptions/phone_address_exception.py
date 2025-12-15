from src.exceptions.server_expection import BaseException


class PhoneNotFound(BaseException):
    """ Номер телефона не найден """
    
class PhoneNumberAlreadyLinked(BaseException):
    """ Данный номер телефона уже првязан """