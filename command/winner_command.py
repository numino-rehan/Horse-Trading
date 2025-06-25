from command_core import BaseCommand, CommandContext
from exceptions import InvalidCommandException
from exceptions.horse_exceptions import InvalidHorseNumberException
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

logger = setup_logger("command.winner_command")


class WinnerCommand(BaseCommand):
    """
    Handles the 'winner' command to declare the winning horse.
    """

    @log_and_handle_errors("WinnerCommand execution failed")
    def execute(self, args: str, context: CommandContext) -> None:
        args = args.split()
        if len(args) != 1 or not args[0].isdigit():
            raise InvalidCommandException(
                f"Invalid winner command arguments: {' '.join(args)}"
            )

        horse_id = int(args[0])

        if horse_id < 1 or horse_id > len(context.horse_manager.horse_data):
            raise InvalidHorseNumberException(f"Invalid horse ID: {horse_id}")

        logger.info(f"Setting horse ID {horse_id} as the winner.")
        context.horse_manager.set_winner(horse_id)
        logger.info(f"Horse ID {horse_id} has been declared the winner.")
