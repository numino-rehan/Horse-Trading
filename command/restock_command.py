from command_core import CommandContext, BaseCommand
from exceptions.machine_exceptions import RestockException
from utils.loger_config import setup_logger

logger = setup_logger("command.restock_command")


class RestockCommand(BaseCommand):
    """
    Handles the 'restock' command to replenish inventory levels.
    """

    def execute(self, args: str, context: CommandContext) -> None:
        """
        Execute the restock command to replenish all ingredients.

        Args:
            args (str): Command-line arguments (not used).
            context (CommandContext): The application context containing the inventory manager.
        """
        logger.info("Restock command received.")
        try:
            context.inventory_manager.restock()
            logger.info("Inventory restocked successfully.")
            print("Inventory has been restocked to max levels.")
        except Exception as e:
            logger.error(f"Error during restock: {e}")
            print(f"Failed to restock inventory: {e}")
            raise RestockException from e
