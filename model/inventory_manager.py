"""
inventory_manager.py

Handles inventory operations such as restocking and displaying cash denominations.
"""

from typing import Dict
from colorama import Fore, Style

from config.constants import DENOMINATIONS, MAX_STOCK
from exceptions import RestockException
from utils.loger_config import setup_logger

logger = setup_logger("model.inventory_manager")


class InventoryManager:
    """
    Manages the cash inventory with denominations and their quantities.
    """

    def __init__(self) -> None:
        """
        Initialize inventory with max stock for each denomination.
        """
        self.inventory: Dict[float, int] = {
            denomination: MAX_STOCK for denomination in sorted(DENOMINATIONS)
        }
        logger.debug(
            "InventoryManager initialized with full stock for all denominations.")

    def restock(self) -> None:
        """
        Restock all denominations to MAX_STOCK.

        Raises:
            RestockException: If restocking fails unexpectedly.
        """
        try:
            self.inventory = {
                denomination: MAX_STOCK for denomination in sorted(DENOMINATIONS)
            }
            logger.info(
                "Inventory restocked to max levels for all denominations.")
            print(Fore.GREEN + "Restocking complete." + Style.RESET_ALL + "\n")
        except Exception as e:
            logger.exception("Error occurred while restocking inventory.")
            raise RestockException from e

    def __str__(self) -> str:
        """
        Returns a formatted string representing the inventory.

        Returns:
            str: Multi-line string listing each denomination and its quantity.
        """
        lines = [Fore.BLUE + Style.BRIGHT + "INVENTORY:" + Style.RESET_ALL]
        for denomination, quantity in sorted(self.inventory.items(), reverse=True):
            lines.append(
                f"{Fore.YELLOW}${denomination:.2f}{Style.RESET_ALL} x "
                f"{Fore.WHITE}{quantity}{Style.RESET_ALL}"
            )
        return "\n".join(lines)

    def show_inventory(self) -> None:
        """
        Prints the current inventory to the console.
        """
        logger.debug("Displaying current inventory.")
        print(self)
        print()
