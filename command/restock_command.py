from command_core import BaseCommand, CommandContext
from utils.decorators import log_and_handle_errors
from utils.loger_config import setup_logger

logger = setup_logger("command.restock_command")


class RestockCommand(BaseCommand):
    """
    Handles the 'restock' command to replenish inventory levels.
    """

    @log_and_handle_errors("RestockCommand execution failed")
    def execute(self, args: str, context: CommandContext) -> None:
        logger.info("Restock command received.")
        context.inventory_manager.restock()
        logger.info("Inventory restocked successfully.")
        print("Inventory has been restocked to max levels.")
