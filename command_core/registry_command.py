
from typing import Dict, Optional
from .base_command import BaseCommand
from utils.loger_config import setup_logger

logger = setup_logger("command_core.command_registry")


class CommandRegistry:
    """
    A registry for mapping command keywords to their corresponding command objects.
    """

    def __init__(self) -> None:
        """
        Initialize an empty command registry.
        """
        self.commands: Dict[str, BaseCommand] = {}
        logger.debug("CommandRegistry initialized with empty command map.")

    def register(self, keyword: str, command_obj: BaseCommand) -> None:
        """
        Register a command with its keyword.

        Args:
            keyword (str): The keyword used to invoke the command.
            command_obj (BaseCommand): The command object to be registered.
        """
        if keyword in self.commands:
            logger.warning(
                f"Overwriting existing command for keyword '{keyword}'.")

        self.commands[keyword] = command_obj
        logger.info(
            f"Command registered: '{keyword}' -> {command_obj.__class__.__name__}")

    def get(self, keyword: str) -> Optional[BaseCommand]:
        """
        Retrieve a command object by its keyword.

        Args:
            keyword (str): The keyword of the command to retrieve.

        Returns:
            Optional[BaseCommand]: The corresponding command object, or None if not found.
        """
        command = self.commands.get(keyword)
        if command:
            logger.debug(
                f"Retrieved command for keyword '{keyword}': {command.__class__.__name__}")
        else:
            logger.warning(
                f"No command found for keyword: '{keyword}'")
        return command
