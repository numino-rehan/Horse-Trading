
from colorama import Fore, Style

from exceptions import (InsufficientFundsException, InvalidBetAmountException,
                        InvalidCommandException, InvalidHorseNumberException,
                        RestockException)
from services import CommandProcessor
from utils.loger_config import setup_logger

logger = setup_logger("main")


def runATMMachine() -> None:
    """
    Main loop to run the ATM betting machine.
    """
    processor = CommandProcessor()

    while True:
        processor.inventory_manager.show_inventory()
        processor.horse_manager.show_horse_data()

        command = input(
            "Enter a command:\n"
            "\n"
            "Available Commands:\n"
            "  R or r            -> Restock the cash inventory\n"
            "  Q or q            -> Quit the application\n"
            "  W or w <number>   -> Set the winning horse number (e.g., W 3)\n"
            "  <number> <amount> -> Place a bet on a horse (e.g., 4 20 for $20 on Horse #4)\n"
            "\n"
            "Examples:\n"
            "  r          - Restock inventory\n"
            "  w 2        - Set Horse #2 as winner\n"
            "  5 10       - Bet $10 on Horse #5\n"
            "  q          - Quit the application\n"
            "\n"
            "> "
        ).strip()

        print("______________________________")

        try:
            if not command:
                raise InvalidCommandException("Command cannot be empty.")
            logger.info(f"Processing command: {command}")
            processor.process_commands(command)
        except InvalidCommandException as e:
            logger.error(f"Invalid command: {e}")
            print(
                Fore.RED + "Invalid command. Please check the format and try again.\n" + Style.RESET_ALL)

        except InvalidHorseNumberException as e:
            logger.error(f"Invalid horse number: {e}")
            print(
                Fore.RED + "Invalid horse number. Please enter a number from the list.\n" + Style.RESET_ALL)

        except InvalidBetAmountException as e:
            logger.error(f"Invalid bet amount: {e}")
            print(
                Fore.RED + "Invalid bet amount. Please enter a positive number.\n" + Style.RESET_ALL)

        except InsufficientFundsException as e:
            logger.error(f"Insufficient funds: {e}")
            print(
                Fore.RED + "Cannot dispense winnings. The machine has insufficient funds.\n" + Style.RESET_ALL)

        except RestockException as e:
            logger.error(f"Restock failed: {e}")
            print(
                Fore.RED + "Error occurred while restocking. Please try again.\n" + Style.RESET_ALL)

        except Exception as exc:
            logger.error(
                f"Unexpected error while processing command '{command}': {exc}",
                exc_info=True
            )
            print(
                Fore.RED + "An unexpected error occurred. Please contact support.\n" + Style.RESET_ALL)


if __name__ == "__main__":
    runATMMachine()
