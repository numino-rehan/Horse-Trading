from .inventory_manager import InventoryManager
from .horse_manager import HorseManager
from .cash_dispenser import CashDispenser
from utils.exceptions import InvalidCommandError, InvalidBetAmountError,InvalidHorseNumberError
import sys
from colorama import Fore

class CommandProcessor:
    def __init__(self):
        self.inventory_manager = InventoryManager()
        self.horse_manager = HorseManager()
        self.cash_dispenser = CashDispenser(self.inventory_manager)

    def process_commands(self, command):
        command = command.strip().lower()
        if not command:
            return

        cmd = command.split()

        try:
            if command == "q":
                sys.exit()

            elif command == "r":
                self.inventory_manager.restock()

            elif command.startswith("w"):
                if len(cmd) != 2:
                    raise InvalidCommandError(command)
                else:
                    horse_id = cmd[1]
                    if horse_id.isdigit():
                        horse_id = int(horse_id)
                        self.horse_manager.set_winner(horse_id)
                    else:
                        raise InvalidHorseNumberError(horse_id)

            elif command[0].isdigit():
                if len(cmd) != 2:
                    raise InvalidCommandError(command)
                else:
                    horse_id, amount = cmd[0], cmd[1]
                    if horse_id.isdigit():
                        horse_id = int(horse_id)
                        if 1 <= horse_id <= len(self.horse_manager.horse_data):
                            if amount.isdigit():
                                amount = int(amount)
                                if amount <= 0:
                                    raise InvalidBetAmountError(amount)
                                elif self.horse_manager.horse_data[horse_id]["won"]:
                                    winnings = amount * self.horse_manager.horse_data[horse_id]["odds"]
                                    print(f"Payout: {self.horse_manager.horse_data[horse_id]['name']}, ${winnings}")
                                    self.cash_dispenser.dispense_cash(winnings)
                                else:
                                    print(Fore.YELLOW + f"No Payout: {self.horse_manager.horse_data[horse_id]['name']}")
                                    print()
                            else:
                                raise InvalidBetAmountError(amount)
                        else:
                            raise InvalidHorseNumberError(horse_id)
                    else:
                        raise InvalidHorseNumberError(horse_id)

            else:
                raise InvalidCommandError(command)

        except Exception as e:
            print(Fore.RED + str(e))
            print()
