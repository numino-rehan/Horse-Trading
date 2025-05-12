from .base_command import BaseCommand
from exceptions.command_exceptions import InvalidCommandError
from exceptions.bet_exceptions import InvalidBetAmountError
from exceptions.horse_exceptions import InvalidHorseNumberError
from colorama import Fore

class BetCommand(BaseCommand):
    def execute(self, args, context):
        if len(args) != 2:
            raise InvalidCommandError(" ".join(args))

        horse_id, amount = args
        if not horse_id.isdigit() or not amount.isdigit():
            raise InvalidCommandError(" ".join(args))

        horse_id = int(horse_id)
        amount = int(amount)

        if horse_id < 1 or horse_id > len(context.horse_manager.horse_data):
            raise InvalidHorseNumberError(horse_id)
        if amount <= 0:
            raise InvalidBetAmountError(amount)

        horse = context.horse_manager.horse_data[horse_id]
        if horse["won"]:
            winnings = amount * horse["odds"]
            print(f"Payout: {horse['name']}, ${winnings}")
            context.cash_dispenser.dispense_cash(winnings)
        else:
            print(Fore.YELLOW + f"No Payout: {horse['name']}\n")
