class HorseException(Exception):
    """Base class for all horse-related exceptions."""
    pass


class InvalidHorseNumberException(HorseException):
    """Exception raised when an invalid horse number is provided.

    This exception is thrown when a horse identification number does not meet
    the required format or validation criteria.

    Args:
        horse_id: The invalid horse identification number that caused the exception.

    Attributes:
        message: The error message containing details about the invalid horse number.

    Example:
        >>> raise InvalidHorseNumberException("ABC123")
        InvalidHorseNumberException: Invalid Horse Number: ABC123
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
