from .base_command import BaseCommand
from exceptions import (InvalidCommandException)


class WinnerCommand(BaseCommand):
    def execute(self, args, context):
        if len(args) != 1 or not args[0].isdigit():
            raise InvalidCommandException("w " + " ".join(args))
        horse_id = int(args[0])
        context.horse_manager.set_winner(horse_id)
