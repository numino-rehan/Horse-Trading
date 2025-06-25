from copy import deepcopy
from typing import Dict, Tuple

from colorama import Fore, Style

from exceptions import InsufficientFundsException
from model.inventory_manager import InventoryManager
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

logger = setup_logger("services.cash_dispenser")


class CashDispenser:
    def __init__(self, inventory_manager: InventoryManager) -> None:
        self.inventory_manager = inventory_manager
        logger.debug("CashDispenser initialized.")

    @log_and_handle_errors("Failed to simulate cash dispensing")
    def can_dispense(self, amount: float) -> Tuple[Dict[float, int], Dict[float, int]]:
        remaining = round(amount, 2)
        dispensed: Dict[float, int] = {}
        temp_inventory = deepcopy(self.inventory_manager.inventory)

        logger.debug(
            f"Attempting to dispense ${remaining:.2f} using inventory: {temp_inventory}"
        )

        for denomination in sorted(temp_inventory.keys(), reverse=True):
            while remaining >= denomination and temp_inventory[denomination] > 0:
                dispensed[denomination] = dispensed.get(denomination, 0) + 1
                temp_inventory[denomination] -= 1
                remaining = round(remaining - denomination, 2)

        if remaining > 0:
            raise InsufficientFundsException(
                f"Unable to dispense ${amount:.2f}. Short by ${remaining:.2f}."
            )

        logger.debug(f"Dispense plan created: {dispensed}")
        return dispensed, temp_inventory

    @log_and_handle_errors("Failed to dispense cash")
    def dispense_cash(self, amount: float) -> None:
        dispensed, updated_inventory = self.can_dispense(amount)
        self.inventory_manager.inventory = updated_inventory
        logger.info(f"Successfully dispensed: {dispensed}")

        print(Fore.GREEN + "Dispensing Cash:" + Style.RESET_ALL)
        for denom, count in sorted(dispensed.items()):
            print(
                Fore.YELLOW + f"${denom:.2f}:" +
                Fore.WHITE + f" {count}" + Style.RESET_ALL
            )
        print()
