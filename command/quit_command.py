import sys

from command_core import BaseCommand, CommandContext
from utils.loger_config import setup_logger

logger = setup_logger("command.quit_command")


class QuitCommand(BaseCommand):
    """
    Handles the 'quit' command to exit the application.
    """

    def execute(self, args: str, context: CommandContext) -> None:
        """
        Execute the quit command and exit the application.

        Args:
            args (str): Command-line arguments (ignored in this command).
            context (CommandContext): The application context (not used here).
        """
        try:
            logger.info("Quit command received. Exiting application now.")
            print("Thank you for using the application. Goodbye!")
            sys.exit(0)
        except Exception:
            logger.error("Failed to exit application gracefully.", exc_info=True)
            raise
