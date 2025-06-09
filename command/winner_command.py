from command_core import CommandContext, BaseCommand
from exceptions import InvalidCommandException
from exceptions.horse_exceptions import InvalidHorseNumberException
from utils.loger_config import setup_logger

logger = setup_logger("command.winner_command")


class WinnerCommand(BaseCommand):
    """
    Handles the 'winner' command to declare the winning horse.
    """

    def execute(self, args: str, context: CommandContext) -> None:
        """
        Execute the winner command to set the winning horse.

        Args:
            args (str): Command-line arguments containing the winning horse's ID.
            context (CommandContext): The application context with horse manager.

        Raises:
            InvalidCommandException: If the input is not a single valid horse ID.
        """
        args = args.split()
        if len(args) != 1 or not args[0].isdigit():
            logger.error(f"Invalid winner command arguments: {' '.join(args)}")
            raise InvalidCommandException("w " + " ".join(args))

        horse_id = int(args[0])

        if horse_id < 1 or horse_id > len(context.horse_manager.horse_data):
            logger.error(f"Winner command received invalid horse ID: {horse_id}")
            raise InvalidHorseNumberException(horse_id)

        logger.info(f"Setting horse ID {horse_id} as the winner.")
        context.horse_manager.set_winner(horse_id)
        logger.info(f"Horse ID {horse_id} has been declared the winner.")
