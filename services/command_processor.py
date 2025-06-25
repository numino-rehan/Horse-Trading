from typing import Optional

from command import BetCommand, QuitCommand, RestockCommand, WinnerCommand
from command_core import CommandContext, CommandRegistry
from config.constants import COMMAND_LIST
from exceptions import InvalidCommandException
from model import HorseManager, InventoryManager
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

from .cash_dispenser import CashDispenser

logger = setup_logger("services.command_processor")


class CommandProcessor:
    def __init__(self) -> None:
        self.inventory_manager = InventoryManager()
        self.horse_manager = HorseManager()
        self.cash_dispenser = CashDispenser(self.inventory_manager)

        self.context = CommandContext(
            self.inventory_manager,
            self.horse_manager,
            self.cash_dispenser,
        )

        self.registry = CommandRegistry()
        self.registry.register(COMMAND_LIST["quit"], QuitCommand())
        self.registry.register(COMMAND_LIST["restock"], RestockCommand())
        self.registry.register(COMMAND_LIST["winner"], WinnerCommand())
        self.registry.register(COMMAND_LIST["bet"], BetCommand())

        logger.info(
            "CommandProcessor initialized and commands registered.")

    @log_and_handle_errors("Failed to process command")
    def process_commands(self, command: str) -> Optional[None]:
        command = command.strip().lower()
        if not command:
            logger.debug("Received empty command; ignoring.")
            return

        cmd_parts = command.split()
        keyword = cmd_parts[0]

        if keyword.isdigit():
            command_obj = self.registry.get("bet")
            args = cmd_parts
        else:
            command_obj = self.registry.get(keyword)
            args = cmd_parts[1:]

        logger.info(f"Command: {command}, Keyword: {keyword}, Args: {args}")

        if not command_obj:
            logger.warning(f"Invalid command received: '{command}'")
            raise InvalidCommandException(f"Unrecognized command: '{command}'")

        logger.debug(f"Executing command '{keyword}' with args: {args}")
        command_obj.execute(" ".join(args), self.context)
