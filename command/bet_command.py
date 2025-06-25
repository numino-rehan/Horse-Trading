from colorama import Fore

from command_core import BaseCommand, CommandContext
from exceptions import (InvalidBetAmountException, InvalidCommandException,
                        InvalidHorseNumberException)
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

logger = setup_logger("command.bet_command")


class BetCommand(BaseCommand):
    """
    Handles the 'bet' command to place a bet on a horse.
    """

    @log_and_handle_errors("BetCommand execution failed")
    def execute(self, args: str, context: CommandContext) -> None:
        logger.debug(f"Executing BetCommand with args: '{args}'")

        args_list = args.split()
        if len(args_list) != 2:
            raise InvalidCommandException(
                f"Invalid number of arguments for bet command: '{args}'"
            )

        horse_id_str, amount_str = args_list

        if not horse_id_str.isdigit():
            raise InvalidHorseNumberException(
                f"Horse ID is not numeric: '{horse_id_str}'"
            )

        if not amount_str.isdigit():
            raise InvalidBetAmountException(
                f"Bet amount is not numeric: '{amount_str}'"
            )

        horse_id = int(horse_id_str)
        amount = int(amount_str)

        if horse_id not in context.horse_manager.horse_data:
            raise InvalidHorseNumberException(
                f"Invalid horse number: {horse_id}. "
                f"Must be between 1 and {len(context.horse_manager.horse_data)}"
            )

        if amount <= 0:
            raise InvalidBetAmountException(
                f"Invalid bet amount: {amount}. Must be positive."
            )

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
        else:
            logger.info(f"Bet lost. Horse '{horse['name']}' did not win.")
            print(Fore.YELLOW + f"No Payout: {horse['name']}\n")

        logger.debug("BetCommand execution finished.")
