from config.constants import DENOMINATIONS, MAX_STOCK
from utils.exceptions import RestockError
from colorama import Fore, Style

class InventoryManager:
    def __init__(self):
        self.inventory = {denominations: MAX_STOCK for denominations in sorted(DENOMINATIONS)}

    def restock(self):
        try:
            self.inventory = {denominations: MAX_STOCK for denominations in sorted(DENOMINATIONS)}
            print(Fore.GREEN + "Restocking Complete")
            print()
        except Exception as e:
            raise RestockError from e

    def show_inventory(self):
        print(Fore.BLUE + Style.BRIGHT + "INVENTORY:")
        for den, qty in self.inventory.items():
            print(Fore.YELLOW + f"${den:.2f}" + Fore.WHITE + f" x {qty}")
        print()
