class BetException(Exception):
    """Base class for all betting-related exceptions."""
    pass

class InvalidBetAmountException(BetException):
    """Exception raised when a bet amount is invalid.

    This exception is used when a bet amount violates the game rules,
    such as negative amounts, zero amounts, or amounts exceeding the player's balance.

    Args:
        amount: The invalid bet amount that caused the exception.

    Attributes:
        message (str): The error message containing the invalid amount.
    """
    def __init__(self, amount: str | int):
        self.message = f"Invalid Bet: {amount}"
        super().__init__(self.message)

