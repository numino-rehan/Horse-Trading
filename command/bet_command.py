from .base_command import BaseCommand

from exceptions import (InvalidCommandException,InvalidBetAmountException,InvalidHorseNumberException)
from colorama import Fore

class BetCommand(BaseCommand):
    def execute(self, args, context):
        if len(args) != 2:
            raise InvalidCommandException(" ".join(args))

        horse_id, amount = args
        if not horse_id.isdigit() or not amount.isdigit():
            raise InvalidCommandException(" ".join(args))

        horse_id = int(horse_id)
        amount = int(amount)

        if horse_id < 1 or horse_id > len(context.horse_manager.horse_data):
            raise InvalidHorseNumberException(horse_id)
        if amount <= 0:
            raise InvalidBetAmountException(amount)

        horse = context.horse_manager.horse_data[horse_id]
        if horse["won"]:
            winnings = amount * horse["odds"]
            print(f"Payout: {horse['name']}, ${winnings}")
            context.cash_dispenser.dispense_cash(winnings)
        else:
            print(Fore.YELLOW + f"No Payout: {horse['name']}\n")
