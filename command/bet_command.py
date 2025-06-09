from colorama import Fore

from command_core import CommandContext, BaseCommand
from exceptions import (
    InvalidCommandException,
    InvalidBetAmountException,
    InvalidHorseNumberException
)
from utils.loger_config import setup_logger

logger = setup_logger("command.bet_command")


class BetCommand(BaseCommand):
    """
    Handles the 'bet' command to place a bet on a horse.

    Validates the horse number and bet amount, and calculates the payout if the horse has won.
    """

    def execute(self, args: str, context: CommandContext) -> None:
        logger.debug(f"Executing BetCommand with args: '{args}'")
        print("-->", type(args))
        args_list = args.split()
        if len(args_list) != 2:
            logger.error(
                f"Invalid number of arguments for bet command: '{args}'")
            raise InvalidCommandException(" ".join(args_list))

        horse_id_str, amount_str = args_list

        if not horse_id_str.isdigit():
            logger.error(f"Horse ID is not numeric: '{horse_id_str}'")
            raise InvalidHorseNumberException(horse_id_str)
        if not amount_str.isdigit():
            logger.error(f"Bet amount is not numeric: '{amount_str}'")
            raise InvalidBetAmountException(amount_str)

        horse_id = int(horse_id_str)
        amount = int(amount_str)

        if horse_id < 1 or horse_id > len(context.horse_manager.horse_data):
            logger.error(
                f"Invalid horse number: {horse_id}. Must be between 1 and {len(context.horse_manager.horse_data)}")
            raise InvalidHorseNumberException(horse_id)

        if amount <= 0:
            logger.error(f"Invalid bet amount: {amount}. Must be positive.")
            raise InvalidBetAmountException(amount)

        horse = context.horse_manager.horse_data[horse_id]
        logger.info(
            f"Placing bet: Horse ID={horse_id}, Horse Name='{horse['name']}', Amount=${amount}")

        if horse["won"]:
            winnings = amount * horse["odds"]
            logger.info(
                f"Bet won! Horse '{horse['name']}' won with odds {horse['odds']}. Winnings: ${winnings}")
            print(f"Payout: {horse['name']}, ${winnings}")
            context.cash_dispenser.dispense_cash(winnings)
            logger.debug(f"Dispensed ${winnings} to the user.")
        else:
            logger.info(f"Bet lost. Horse '{horse['name']}' did not win.")
            print(Fore.YELLOW + f"No Payout: {horse['name']}\n")

        logger.debug("BetCommand execution finished.")
