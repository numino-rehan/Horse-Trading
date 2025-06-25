import sys

from command_core import BaseCommand, CommandContext
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

logger = setup_logger("command.quit_command")


class QuitCommand(BaseCommand):
    """
    Handles the 'quit' command to exit the application.
    """

    @log_and_handle_errors("QuitCommand execution failed")
    def execute(self, args: str, context: CommandContext) -> None:
        logger.info("Quit command received. Exiting application now.")
        print("Thank you for using the application. Goodbye!")
        sys.exit(0)
