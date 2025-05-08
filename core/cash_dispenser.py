from utils.exceptions import InsufficientFundsError
from colorama import Fore, Style
from copy import deepcopy

class CashDispenser:
    def __init__(self, inventory_manger):
        self.inventory_manager = inventory_manger

    def can_dispense(self, amount):
        """Simulates cash dispensing to check if it's possible."""
        remaining = amount
        dispensed = {}
        temp_inventory = deepcopy(self.inventory_manager.inventory)

        for denomination in sorted(temp_inventory.keys(), reverse=True):
            while remaining >= denomination and temp_inventory[denomination] > 0:
                dispensed[denomination] = dispensed.get(denomination, 0) + 1
                temp_inventory[denomination] -= 1
                remaining = round(remaining - denomination, 2)

        if remaining > 0:
            raise InsufficientFundsError()

        return dispensed, temp_inventory

    def dispense_cash(self, amount):
        """Dispenses cash if sufficient funds exist."""
        try:
            dispensed, updated_inventory = self.can_dispense(amount)
            self.inventory_manager.inventory = updated_inventory
        except InsufficientFundsError:
            raise

        print(Fore.GREEN + "Dispensing Cash:")
        for denom, count in sorted(dispensed.items()):
            print(Fore.YELLOW + f"${denom:.2f}:" + Fore.WHITE + f" {count}")
        print()
