from typing import Dict, Optional

from utils.loger_config import setup_logger

from .base_command import BaseCommand

logger = setup_logger("command_core.command_registry")


class CommandRegistry:
    """
    A registry for mapping command keywords to their corresponding command objects.
    """

    def __init__(self) -> None:
        """
        Initialize an empty command registry.
        """
        try:
            self.commands: Dict[str, BaseCommand] = {}
            logger.debug("CommandRegistry initialized with empty command map.")
        except Exception:
            logger.error("Failed to initialize CommandRegistry.", exc_info=True)
            raise

    def register(self, keyword: str, command_obj: BaseCommand) -> None:
        """
        Register a command with its keyword.

        Args:
            keyword (str): The keyword used to invoke the command.
            command_obj (BaseCommand): The command object to be registered.
        """
        try:
            if keyword in self.commands:
                logger.warning(
                    f"Overwriting existing command for keyword '{keyword}'."
                )

            self.commands[keyword] = command_obj
            logger.info(
                f"Command registered: '{keyword}' -> {command_obj.__class__.__name__}"
            )
        except Exception:
            logger.error(
                f"Failed to register command '{keyword}'.", exc_info=True
            )
            raise

    def get(self, keyword: str) -> Optional[BaseCommand]:
        """
        Retrieve a command object by its keyword.

        Args:
            keyword (str): The keyword of the command to retrieve.

        Returns:
            Optional[BaseCommand]: The corresponding command object, or None if not found.
        """
        try:
            command = self.commands.get(keyword)
            if command:
                logger.debug(
                    f"Retrieved command for keyword '{keyword}': {command.__class__.__name__}"
                )
            else:
                logger.warning(f"No command found for keyword: '{keyword}'")
            return command
        except Exception:
            logger.error(
                f"Failed to retrieve command for keyword '{keyword}'.", exc_info=True
            )
            raise
