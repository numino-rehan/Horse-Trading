
from model import InventoryManager, HorseManager
from services import CashDispenser
from utils.loger_config import setup_logger

logger = setup_logger("command_core.command_context")


class CommandContext:
    """
    Context container that provides shared managers for executing commands.

    Attributes:
        inventory_manager (InventoryManager): Manages inventory operations.
        horse_manager (HorseManager): Manages horse-related operations.
        cash_dispenser (CashDispenser): Handles cash payout logic.
    """

    def __init__(
        self,
        inventory_manager: InventoryManager,
        horse_manager: HorseManager,
        cash_dispenser: CashDispenser
    ) -> None:
        """
        Initialize the CommandContext with required managers.

        Args:
            inventory_manager (InventoryManager): Instance responsible for inventory control.
            horse_manager (HorseManager): Instance managing horse data and winner state.
            cash_dispenser (CashDispenser): Instance responsible for cash transactions.
        """
        self.inventory_manager = inventory_manager
        self.horse_manager = horse_manager
        self.cash_dispenser = cash_dispenser

        logger.debug(
            "CommandContext initialized with inventory, horse, and cash managers.")

    def __str__(self) -> str:
        """
        String representation for debugging/logging.

        Returns:
            str: Human-readable summary of context components.
        """
        return (
            f"CommandContext("
            f"inventory_manager={self.inventory_manager.__class__.__name__}, "
            f"horse_manager={self.horse_manager.__class__.__name__}, "
            f"cash_dispenser={self.cash_dispenser.__class__.__name__})"
        )
