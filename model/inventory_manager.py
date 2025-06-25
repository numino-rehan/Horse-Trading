from typing import Dict

from colorama import Fore, Style

from config.constants import DENOMINATIONS, MAX_STOCK
from exceptions import RestockException
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

logger = setup_logger("model.inventory_manager")


class InventoryManager:
    def __init__(self) -> None:
        self.inventory: Dict[float, int] = {
            denomination: MAX_STOCK for denomination in sorted(DENOMINATIONS)
        }
        logger.debug(
            "InventoryManager initialized with full stock for all denominations.")

    @log_and_handle_errors("Failed to restock inventory")
    def restock(self) -> None:
        try:
            self.inventory = {
                denomination: MAX_STOCK for denomination in sorted(DENOMINATIONS)
            }
            logger.info(
                "Inventory restocked to max levels for all denominations.")
            print(Fore.GREEN + "Restocking complete." + Style.RESET_ALL + "\n")
        except Exception as e:
            logger.error(
                "Error occurred while restocking inventory.", exc_info=True)
            raise RestockException("Restock operation failed.") from e

    @log_and_handle_errors("Failed to format inventory display")
    def __str__(self) -> str:
        lines = [Fore.BLUE + Style.BRIGHT + "INVENTORY:" + Style.RESET_ALL]
        for denomination, quantity in sorted(self.inventory.items(), reverse=True):
            lines.append(
                f"{Fore.YELLOW}${denomination:.2f}{Style.RESET_ALL} x "
                f"{Fore.WHITE}{quantity}{Style.RESET_ALL}"
            )
        return "\n".join(lines)

    @log_and_handle_errors("Failed to display inventory")
    def show_inventory(self) -> None:
        logger.debug("Displaying current inventory.")
        print(self)
        print()
