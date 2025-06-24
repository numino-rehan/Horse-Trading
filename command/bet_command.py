from colorama import Fore

from command_core import BaseCommand, CommandContext
from exceptions import (InvalidBetAmountException, InvalidCommandException,
                        InvalidHorseNumberException)
from utils.loger_config import setup_logger

logger = setup_logger("command.bet_command")


class BetCommand(BaseCommand):
    """
    Handles the 'bet' command to place a bet on a horse.

    Validates the horse number and bet amount, and calculates the payout if the horse has won.
    """

    def execute(self, args: str, context: CommandContext) -> None:
        try:
            logger.debug(f"Executing BetCommand with args: '{args}'")

            args_list = args.split()
            if len(args_list) != 2:
                message = f"Invalid number of arguments for bet command: '{args}'"
                logger.error(message)
                raise InvalidCommandException(message)

            horse_id_str, amount_str = args_list

            if not horse_id_str.isdigit():
                message = f"Horse ID is not numeric: '{horse_id_str}'"
                logger.error(message)
                raise InvalidHorseNumberException(message)

            if not amount_str.isdigit():
                message = f"Bet amount is not numeric: '{amount_str}'"
                logger.error(message)
                raise InvalidBetAmountException(message)

            horse_id = int(horse_id_str)
            amount = int(amount_str)

            if horse_id not in context.horse_manager.horse_data:
                message = (
                    f"Invalid horse number: {horse_id}. "
                    f"Must be between 1 and {len(context.horse_manager.horse_data)}"
                )
                logger.error(message)
                raise InvalidHorseNumberException(message)

            if amount <= 0:
                message = f"Invalid bet amount: {amount}. Must be positive."
                logger.error(message)
                raise InvalidBetAmountException(message)

            horse = context.horse_manager.horse_data[horse_id]
            logger.info(
                f"Placing bet: Horse ID={horse_id}, Horse Name='{horse['name']}', Amount=${amount}"
            )

            if horse["won"]:
                winnings = amount * horse["odds"]
                logger.info(
                    f"Bet won! Horse '{horse['name']}' won with odds {horse['odds']}. Winnings: ${winnings}"
                )
                print(f"Payout: {horse['name']}, ${winnings}")
                context.cash_dispenser.dispense_cash(winnings)
                logger.debug(f"Dispensed ${winnings} to the user.")
            else:
                logger.info(f"Bet lost. Horse '{horse['name']}' did not win.")
                print(Fore.YELLOW + f"No Payout: {horse['name']}\n")

            logger.debug("BetCommand execution finished.")

        except (InvalidHorseNumberException, InvalidBetAmountException, InvalidCommandException):
            raise  # Let custom, known exceptions bubble up to be handled by caller

        except Exception:
            logger.error(
                "Unexpected error in BetCommand execution.", exc_info=True)
            raise
