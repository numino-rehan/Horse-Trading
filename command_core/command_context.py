from model import HorseManager, InventoryManager
from services import CashDispenser
from utils.loger_config import setup_logger

logger = setup_logger("command_core.command_context")


class CommandContext:
    """
    Context container that provides shared managers for executing commands.
    """

    def __init__(
        self,
        inventory_manager: InventoryManager,
        horse_manager: HorseManager,
        cash_dispenser: CashDispenser
    ) -> None:
        self.inventory_manager = inventory_manager
        self.horse_manager = horse_manager
        self.cash_dispenser = cash_dispenser

        logger.debug(
            "CommandContext initialized with inventory, horse, and cash managers."
        )

    def __str__(self) -> str:
        return (
            f"CommandContext("
            f"inventory_manager={self.inventory_manager.__class__.__name__}, "
            f"horse_manager={self.horse_manager.__class__.__name__}, "
            f"cash_dispenser={self.cash_dispenser.__class__.__name__})"
        )
