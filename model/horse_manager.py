from typing import Any, Dict

from colorama import Fore, Style

from config.constants import HORSE_DATA
from exceptions import InvalidHorseNumberException
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

logger = setup_logger("model.horse_manager")


class HorseManager:
    def __init__(self) -> None:
        self.horse_data: Dict[int, Dict[str, Any]] = self.generate_horse_data()
        logger.debug("HorseManager initialized with predefined horse data.")

    @log_and_handle_errors("Failed to generate horse data")
    def generate_horse_data(self) -> Dict[int, Dict[str, Any]]:
        logger.debug("Generating horse data from constants.")
        return HORSE_DATA

    @log_and_handle_errors("Failed to set winning horse")
    def set_winner(self, horse_id: int, won: bool = True) -> None:
        if horse_id not in self.horse_data:
            raise InvalidHorseNumberException(f"Invalid horse ID: {horse_id}")

        for hid in self.horse_data:
            self.horse_data[hid]["won"] = False
        self.horse_data[horse_id]["won"] = won

        logger.info(
            f'Horse #{horse_id} ("{self.horse_data[horse_id]["name"]}") '
            f'marked as {"winner" if won else "not winner"}.'
        )

        print(
            Fore.GREEN +
            f'Set "{self.horse_data[horse_id]["name"]}" (Horse #{horse_id}) as the winning horse.'
        )
        print(Style.RESET_ALL)

    @log_and_handle_errors("Failed to format horse data output")
    def __str__(self) -> str:
        lines = [Fore.BLUE + Style.BRIGHT + "HORSES:" + Style.RESET_ALL]
        for horse_id, data in self.horse_data.items():
            name = data.get("name", "Unknown")
            odds = data.get("odds", "N/A")
            won = data.get("won", False)

            status_color = Fore.GREEN if won else Fore.RED
            status_text = "WON" if won else "LOST"

            lines.append(
                f"{Fore.YELLOW}{horse_id}{Style.RESET_ALL}, "
                f"{Fore.CYAN}{name}{Style.RESET_ALL}, "
                f"{Fore.WHITE}{odds}{Style.RESET_ALL}, "
                f"{status_color}{status_text}{Style.RESET_ALL}"
            )
        return "\n".join(lines)

    @log_and_handle_errors("Failed to display horse data")
    def show_horse_data(self) -> None:
        logger.debug("Displaying horse data to console.")
        print(self)
        print()
