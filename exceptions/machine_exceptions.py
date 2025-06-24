
class MachineException(Exception):

    pass


class InsufficientFundsException(MachineException):
    """
    Exception raised when the machine does not have sufficient funds.

    This exception is thrown when a machine operation requires more funds
    than what is currently available in the machine.

    Attributes:
        message (str): The error message indicating insufficient funds.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class RestockException(MachineException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
