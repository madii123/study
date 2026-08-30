class ATMServiceException(Exception):
    pass


class InvalidPinException(ATMServiceException):
    pass


class InvalidCardException(ATMServiceException):
    pass


class InvalidAccountException(ATMServiceException):
    pass


class CardDoesNotExistException(ATMServiceException):
    pass


class CardAlreadyExistException(ATMServiceException):
    pass


class CardAlreadyExistsException(ATMServiceException):
    pass


class InsertPinException(ATMServiceException):
    pass


class PinAlreadyInsertedException(ATMServiceException):
    pass


class OperationNotSupportedException(ATMServiceException):
    pass
