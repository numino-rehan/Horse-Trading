from abc import ABC, abstractmethod
from .command_context import CommandContext
from utils.loger_config import setup_logger

logger = setup_logger("command_core.base_command")


class BaseCommand(ABC):
    """
    Abstract base class for all commands in the application.

    Subclasses must override the `execute` method to define the command's behavior.
    """

    @abstractmethod
    def execute(self, args: str, context: CommandContext) -> None:
        """
        Execute the command with the given arguments and context.

        Args:
            args (str): Arguments required to execute the command.
            context (CommandContext): Context or state for execution.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError(
            "Each command must implement the execute method.")
