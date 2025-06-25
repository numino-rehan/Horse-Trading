import pytest

from config.constants import DENOMINATIONS, MAX_STOCK
from exceptions import InsufficientFundsException
from model import CashDispenser, InventoryManager


class MockInventoryManager(InventoryManager):
    def __init__(self):
        super().__init__()
        self.inventory = {denominations: MAX_STOCK for denominations in DENOMINATIONS}


@pytest.fixture
def cash_dispenser():
    inventory_manager = MockInventoryManager()
    return CashDispenser(inventory_manager)


def test_can_dispense(cash_dispenser):
    amount = 15
    dispensed, updated_inventory = cash_dispenser.can_dispense(amount)
    
    assert sum(denom * count for denom, count in dispensed.items()) == amount
    for denom, count in dispensed.items():
        assert updated_inventory[denom] == MAX_STOCK - count


def test_dispense_cash(cash_dispenser):
    amount = 15
    initial_inventory = cash_dispenser.inventory_manager.inventory.copy()
    
    cash_dispenser.dispense_cash(amount)
    
    updated_inventory = cash_dispenser.inventory_manager.inventory
    for denom, count in updated_inventory.items():
        assert initial_inventory[denom] - count == sum(1 for d, c in cash_dispenser.can_dispense(amount)[0].items() if d == denom)
    
    assert updated_inventory != initial_inventory


def test_insufficient_funds_error(cash_dispenser):
    amount = 99999 
    with pytest.raises(InsufficientFundsException):
        cash_dispenser.dispense_cash(amount)
