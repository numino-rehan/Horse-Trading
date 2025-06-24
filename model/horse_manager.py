"""
horse_manager.py

Handles management of horse data including race outcomes, display, and validation.
"""

from typing import Any, Dict

from colorama import Fore, Style

from config.constants import HORSE_DATA
from exceptions import InvalidHorseNumberException
from utils.loger_config import setup_logger

logger = setup_logger("model.horse_manager")


class HorseManager:
    """
    Manages horse data and race outcomes.
    """

    def __init__(self) -> None:
        """
        Initialize the HorseManager with predefined horse data.
        """
        try:
            self.horse_data: Dict[int, Dict[str, Any]
                                  ] = self.generate_horse_data()
            logger.debug(
                "HorseManager initialized with predefined horse data.")
        except Exception:
            logger.error("Failed to initialize HorseManager.", exc_info=True)
            raise

    def generate_horse_data(self) -> Dict[int, Dict[str, Any]]:
        """
        Generate and return the initial horse data.

        Returns:
            Dict[int, Dict[str, Any]]: Mapping of horse IDs to their data.
        """
        try:
            logger.debug("Generating horse data from constants.")
            return HORSE_DATA
        except Exception:
            logger.error("Failed to generate horse data.", exc_info=True)
            raise

    def set_winner(self, horse_id: int, won: bool = True) -> None:
        """
        Set the winning status of a horse.

        Args:
            horse_id (int): The ID of the horse to set as winner or not.
            won (bool): Whether the horse has won. Defaults to True.

        Raises:
            InvalidHorseNumberException: If the horse_id is invalid.
        """
        try:
            if horse_id not in self.horse_data:
                message = f"Invalid horse ID: {horse_id}"
                logger.error(message)
                raise InvalidHorseNumberException(message)

            for hid in self.horse_data:
                self.horse_data[hid]["won"] = False  # Reset all to lost
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

        except InvalidHorseNumberException:
            raise
        except Exception:
            logger.error(
                f"Error setting winner for Horse #{horse_id}.", exc_info=True)
            raise

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the horse data.

        Returns:
            str: Formatted horse data with colors for terminal display.
        """
        try:
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
        except Exception:
            logger.error("Failed to format horse data output.", exc_info=True)
            raise

    def show_horse_data(self) -> None:
        """
        Print the current horse data to the console.
        """
        try:
            logger.debug("Displaying horse data to console.")
            print(self)
            print()
        except Exception:
            logger.error("Failed to display horse data.", exc_info=True)
            raise
