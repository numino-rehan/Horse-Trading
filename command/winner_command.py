from command_core import BaseCommand, CommandContext
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
        try:
            args = args.split()
            if len(args) != 1 or not args[0].isdigit():
                message = f"Invalid winner command arguments: {' '.join(args)}"
                logger.error(message)
                raise InvalidCommandException(message)

            horse_id = int(args[0])

            if horse_id < 1 or horse_id > len(context.horse_manager.horse_data):
                message = f"Invalid horse ID: {horse_id}"
                logger.error(message)
                raise InvalidHorseNumberException(message)

            logger.info(f"Setting horse ID {horse_id} as the winner.")
            context.horse_manager.set_winner(horse_id)
            logger.info(f"Horse ID {horse_id} has been declared the winner.")

        except (InvalidCommandException, InvalidHorseNumberException):
            raise  # Let known errors bubble up to be handled by outer layers

        except Exception:
            logger.error("Unexpected error in WinnerCommand.", exc_info=True)
            raise
