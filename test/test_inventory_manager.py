
from config.constants import DENOMINATIONS, MAX_STOCK
from model import InventoryManager


def test_initial_inventory():
    manager = InventoryManager()
    expected_inventory = {den: MAX_STOCK for den in sorted(DENOMINATIONS)}
    assert manager.inventory == expected_inventory

def test_restock_inventory():
    manager = InventoryManager()
    manager.inventory = {den: 0 for den in sorted(DENOMINATIONS)}
    manager.restock()
    assert manager.inventory == {den: MAX_STOCK for den in sorted(DENOMINATIONS)}
