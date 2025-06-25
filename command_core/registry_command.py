from typing import Dict, Optional

from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

from .base_command import BaseCommand

logger = setup_logger("command_core.command_registry")


class CommandRegistry:
    """
    A registry for mapping command keywords to their corresponding command objects.
    """

    def __init__(self) -> None:
        self.commands: Dict[str, BaseCommand] = {}
        logger.debug("CommandRegistry initialized with empty command map.")

    @log_and_handle_errors("Failed to register command")
    def register(self, keyword: str, command_obj: BaseCommand) -> None:
        if keyword in self.commands:
            logger.warning(
                f"Overwriting existing command for keyword '{keyword}'.")

        self.commands[keyword] = command_obj
        logger.info(
            f"Command registered: '{keyword}' -> {command_obj.__class__.__name__}"
        )

    @log_and_handle_errors("Failed to retrieve command")
    def get(self, keyword: str) -> Optional[BaseCommand]:
        command = self.commands.get(keyword)
        if command:
            logger.debug(
                f"Retrieved command for keyword '{keyword}': {command.__class__.__name__}"
            )
        else:
            logger.warning(f"No command found for keyword: '{keyword}'")
        return command
