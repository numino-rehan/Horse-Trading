from .inventory_manager import InventoryManager
from .horse_manager import HorseManager
from .cash_dispenser import CashDispenser
from .commands.command_context import CommandContext
from .commands.registry_command import CommandRegistry
from .commands.quit_command import QuitCommand
from .commands.restock_command import RestockCommand
from .commands.show_inventory_command import ShowInventory

from model.commands.winner_command import WinnerCommand
from model.commands.bet_command import BetCommand
from exceptions.command_exceptions import InvalidCommandError
from colorama import Fore

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
        self.registry.register("q", QuitCommand())
        self.registry.register("r", RestockCommand())
        self.registry.register("w", WinnerCommand())
        self.registry.register("bet", BetCommand()) 
        self.registry.register("s",ShowInventory())
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
                raise InvalidCommandError(command)

            command_obj.execute(args, self.context)

        except Exception as e:
            print(Fore.RED + str(e))
            print()
