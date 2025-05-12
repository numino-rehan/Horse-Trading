from config.constants import COMMAND_LIST
from .inventory_manager import InventoryManager
from .horse_manager import HorseManager
from .cash_dispenser import CashDispenser

from exceptions import (InvalidCommandException)
from colorama import Fore

from command import (BetCommand, QuitCommand, RestockCommand, WinnerCommand)
from command_core import (CommandContext, CommandRegistry)

class CommandProcessor:
    def __init__(self):
        # Initialize core components
        self.inventory_manager = InventoryManager()
        self.horse_manager = HorseManager()
        self.cash_dispenser = CashDispenser(self.inventory_manager)

        # Setup context
        self.context = CommandContext(self.inventory_manager, self.horse_manager, self.cash_dispenser)

        # Setup command registry
        self.registry = CommandRegistry()
        self.registry.register(COMMAND_LIST["quit"], QuitCommand())
        self.registry.register(COMMAND_LIST["restock"], RestockCommand())
        self.registry.register(COMMAND_LIST["winner"], WinnerCommand())
        self.registry.register(COMMAND_LIST["bet"], BetCommand())
         # generic handler for "1 50" style

    def process_commands(self, command):
        command = command.strip().lower()
        if not command:
            return

        try:
            cmd_parts = command.split()
            keyword = cmd_parts[0]

            # Special handling: if first part is a digit, it's a bet (e.g., "1 50")
            if keyword.isdigit():
                command_obj = self.registry.get("bet")
                args = cmd_parts
            else:
                command_obj = self.registry.get(keyword)
                args = cmd_parts[1:]

            if not command_obj:
                raise InvalidCommandException(command)

            command_obj.execute(args, self.context)

        except Exception as e:
            print(Fore.RED + str(e))
            print()
