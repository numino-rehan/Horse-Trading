import pytest
from exceptions import (InsufficientFundsException)
from config.constants import DENOMINATIONS, MAX_STOCK
from model import (InventoryManager,CashDispenser)


# Mock InventoryManager class for testing
class MockInventoryManager(InventoryManager):
    def __init__(self):
        super().__init__()
        self.inventory = {denominations: MAX_STOCK for denominations in DENOMINATIONS}


@pytest.fixture
def cash_dispenser():
    # Set up CashDispenser with a mock inventory manager
    inventory_manager = MockInventoryManager()
    return CashDispenser(inventory_manager)


def test_can_dispense(cash_dispenser):
    # Testing can_dispense method without updating the inventory
    amount = 15
    dispensed, updated_inventory = cash_dispenser.can_dispense(amount)
    
    # Assert that the amount was correctly dispensed
    assert sum(denom * count for denom, count in dispensed.items()) == amount
    # Assert that the updated inventory has the correct amount of denominations
    for denom, count in dispensed.items():
        assert updated_inventory[denom] == MAX_STOCK - count


def test_dispense_cash(cash_dispenser):
    # Test dispensing cash and updating the inventory
    amount = 15
    initial_inventory = cash_dispenser.inventory_manager.inventory.copy()
    
    # Dispense cash
    cash_dispenser.dispense_cash(amount)
    
    # Assert that the inventory is updated
    updated_inventory = cash_dispenser.inventory_manager.inventory
    for denom, count in updated_inventory.items():
        # Check that the number of each denomination has decreased accordingly
        assert initial_inventory[denom] - count == sum(1 for d, c in cash_dispenser.can_dispense(amount)[0].items() if d == denom)
    
    # Check if the inventory has been correctly updated
    assert updated_inventory != initial_inventory


def test_insufficient_funds_error(cash_dispenser):
    # Test dispensing cash with insufficient funds
    amount = 99999  # Exceeds the available amount
    with pytest.raises(InsufficientFundsException):
        cash_dispenser.dispense_cash(amount)
