from config.constants import DENOMINATIONS, MAX_STOCK
from exceptions import (RestockException)
from colorama import Fore, Style

class InventoryManager:
    def __init__(self):
        self.inventory = {denominations: MAX_STOCK for denominations in sorted(DENOMINATIONS)}

    def restock(self):
        try:
            self.inventory = {denominations: MAX_STOCK for denominations in sorted(DENOMINATIONS)}
            print(Fore.GREEN + "Restocking Complete\n")
        except Exception as e:
            raise RestockException from e

    def __str__(self):
        lines = [Fore.BLUE + Style.BRIGHT + "INVENTORY:"]
        for den, qty in self.inventory.items():
            lines.append(Fore.YELLOW + f"${den:.2f}" + Fore.WHITE + f" x {qty}")
        return "\n".join(lines)

    def show_inventory(self):
        print(self)  # Calls __str__()
        print()
