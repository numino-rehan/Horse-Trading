class BetException(Exception):
    """Base class for all betting-related exceptions."""
    pass


class InvalidBetAmountException(BetException):
    """
    Exception raised when a bet amount is invalid.

    Accepts either an amount or a custom message.
    """

    def __init__(self, message: str = None):
        if message:
            self.message = message
        super().__init__(self.message)
