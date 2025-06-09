import pytest
from model import HorseManager
from config.constants import HORSE_DATA
from exceptions import (InvalidHorseNumberException)

def test_initial_horse_data():
    manager = HorseManager()
    assert manager.horse_data == HORSE_DATA

def test_set_winner_valid():
    manager = HorseManager()
    horse_id = 2  # Fort Utopia initially has won=False
    manager.set_winner(horse_id, won=True)
    assert manager.horse_data[horse_id]["won"] is True

def test_set_winner_invalid():
    manager = HorseManager()
    invalid_id = 999
    with pytest.raises(InvalidHorseNumberException):
        manager.set_winner(invalid_id)

def test_show_horse_data_output(capsys):
    manager = HorseManager()
    manager.show_horse_data()
    captured = capsys.readouterr()

    for horse_id, data in HORSE_DATA.items():
        assert str(horse_id) in captured.out
        assert data["name"] in captured.out
        assert str(data["odds"]) in captured.out
        assert "WON" in captured.out or "LOST" in captured.out
