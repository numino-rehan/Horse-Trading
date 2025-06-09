from typing import Optional

from colorama import Fore

from config.constants import COMMAND_LIST

from model import InventoryManager, HorseManager
from .cash_dispenser import CashDispenser

from exceptions import InvalidCommandException

from command import BetCommand, QuitCommand, RestockCommand, WinnerCommand
from command_core import CommandContext, CommandRegistry
from utils.loger_config import setup_logger

logger = setup_logger("services.command_processor")


class CommandProcessor:
    """
    Processes user commands by delegating to appropriate command handlers.
    """

    def __init__(self) -> None:
        """
        Initialize CommandProcessor with core components and register commands.
        """
        # Initialize core components
        self.inventory_manager = InventoryManager()
        self.horse_manager = HorseManager()
        self.cash_dispenser = CashDispenser(self.inventory_manager)

        # Setup shared context
        self.context = CommandContext(
            self.inventory_manager,
            self.horse_manager,
            self.cash_dispenser,
        )

        # Setup command registry and register commands
        self.registry = CommandRegistry()
        self.registry.register(COMMAND_LIST["quit"], QuitCommand())
        self.registry.register(COMMAND_LIST["restock"], RestockCommand())
        self.registry.register(COMMAND_LIST["winner"], WinnerCommand())
        self.registry.register(COMMAND_LIST["bet"], BetCommand())

        logger.info("CommandProcessor initialized and commands registered.")

    def process_commands(self, command: str) -> Optional[None]:
        """
        Process a command string by parsing and executing the corresponding command.

        Args:
            command (str): The raw input command string.

        Returns:
            None
        """
        command = command.strip().lower()
        if not command:
            logger.debug("Received empty command; ignoring.")
            return

        cmd_parts = command.split()
        keyword = cmd_parts[0]

        # Special handling: if first part is a digit, treat as 'bet' command
        if keyword.isdigit():
            command_obj = self.registry.get("bet")
            args = cmd_parts
        else:
            command_obj = self.registry.get(keyword)
            args = cmd_parts[1:]
        print(f"Command: {command}, Keyword: {keyword}, Args: {args}")
        if not command_obj:
            raise InvalidCommandException(command)

        logger.debug(f"Executing command '{keyword}' with args: {args}")
        command_obj.execute(" ".join(args), self.context)
