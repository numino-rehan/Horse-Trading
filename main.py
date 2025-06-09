import logging
from exceptions import InvalidBetAmountException, InvalidHorseNumberException, InsufficientFundsException, InvalidCommandException, RestockException
from utils.loger_config import setup_logger
from services import CommandProcessor

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
            logging.info(f"Processing command: {command}")
            processor.process_commands(command)
        except InvalidBetAmountException as e:
            logging.error(f"Invalid bet amount: {e}")
            print(f"Error: {e}\n")
        except InvalidCommandException as e:
            logging.error(f"Invalid command: {e}")
            print(f"Error: {e}\n")
        except InvalidHorseNumberException as e:
            logging.error(f"Invalid horse number: {e}")
            print(f"Error: {e}\n")
        except InsufficientFundsException as e:
            logging.error(f"Insufficient funds: {e}")
            print(f"Error: {e}\n")
        except RestockException as e:
            logging.error(f"Restock failed: {e}")
            print(f"Error: {e}\n")
        except Exception as exc:
            logging.error(f"Error processing command '{command}': {exc}")
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    runATMMachine()
