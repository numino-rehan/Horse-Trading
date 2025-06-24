 
class CommandException(Exception):
    """Base class for all command-related exceptions."""
    pass

class InvalidCommandException(CommandException):
    """
    Exception raised when an invalid command is encountered.

    This exception is thrown when a command is not recognized or cannot be executed
    in the current context.

    Args:
        command: The invalid command that was attempted to be executed.

    Attributes:
        message (str): Error message indicating which command was invalid.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
