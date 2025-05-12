import pytest
from model.inventory_manager import InventoryManager
from config.constants import DENOMINATIONS, MAX_STOCK
from exceptions.machine_exceptions import RestockError

def test_initial_inventory():
    manager = InventoryManager()
    expected_inventory = {den: MAX_STOCK for den in sorted(DENOMINATIONS)}
    assert manager.inventory == expected_inventory

def test_restock_inventory():
    manager = InventoryManager()
    # Deplete inventory manually
    manager.inventory = {den: 0 for den in sorted(DENOMINATIONS)}
    manager.restock()
    assert manager.inventory == {den: MAX_STOCK for den in sorted(DENOMINATIONS)}

def test_show_inventory_output(capsys):
    manager = InventoryManager()
    manager.show_inventory()
    captured = capsys.readouterr()
    for den in DENOMINATIONS:
        assert f"${den:.2f}" in captured.out
        assert f"x {MAX_STOCK}" in captured.out
