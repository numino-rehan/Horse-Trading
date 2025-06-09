
from copy import deepcopy
from typing import Dict, Tuple

from colorama import Fore, Style

from exceptions import InsufficientFundsException
from model.inventory_manager import InventoryManager
from utils.loger_config import setup_logger

logger = setup_logger("services.cash_dispenser")


class CashDispenser:
    """
    Handles cash dispensing operations using an inventory of cash denominations.
    """

    def __init__(self, inventory_manager: InventoryManager) -> None:
        """
        Initialize with an inventory manager that keeps track of cash availability.

        Args:
            inventory_manager (InventoryManager): Manages the inventory of cash denominations.
        """
        self.inventory_manager = inventory_manager
        logger.debug("CashDispenser initialized.")

    def can_dispense(self, amount: float) -> Tuple[Dict[float, int], Dict[float, int]]:
        """
        Simulate dispensing cash to determine if the requested amount can be given.

        Args:
            amount (float): The amount of cash to dispense.

        Raises:
            InsufficientFundsException: If the amount cannot be dispensed with available inventory.

        Returns:
            Tuple:
                - dispensed (Dict[float, int]): Denominations and counts to be dispensed.
                - updated_inventory (Dict[float, int]): Inventory after hypothetical dispensing.
        """
        remaining = round(amount, 2)
        dispensed: Dict[float, int] = {}
        temp_inventory = deepcopy(self.inventory_manager.inventory)

        logger.debug(
            f"Trying to dispense ${remaining:.2f} using inventory: {temp_inventory}")

        for denomination in sorted(temp_inventory.keys(), reverse=True):
            while remaining >= denomination and temp_inventory[denomination] > 0:
                dispensed[denomination] = dispensed.get(denomination, 0) + 1
                temp_inventory[denomination] -= 1
                remaining = round(remaining - denomination, 2)

        if remaining > 0:
            logger.error(
                f"Insufficient funds: cannot dispense ${amount:.2f}. Short by ${remaining:.2f}."
            )
            raise InsufficientFundsException()

        logger.debug(f"Dispense plan: {dispensed}")
        return dispensed, temp_inventory

    def dispense_cash(self, amount: float) -> None:
        """
        Dispense cash for the specified amount, updating the inventory accordingly.

        Args:
            amount (float): The amount of cash to dispense.

        Raises:
            InsufficientFundsException: If cash cannot be dispensed.
        """
        try:
            dispensed, updated_inventory = self.can_dispense(amount)
            self.inventory_manager.inventory = updated_inventory
            logger.info(f"Successfully dispensed: {dispensed}")
        except InsufficientFundsException:
            logger.warning(
                f"Cash dispense failed: Insufficient funds for ${amount:.2f}.")
            raise

        print(Fore.GREEN + "Dispensing Cash:" + Style.RESET_ALL)
        for denom, count in sorted(dispensed.items()):
            print(
                Fore.YELLOW + f"${denom:.2f}:" +
                Fore.WHITE + f" {count}" + Style.RESET_ALL
            )
        print()
