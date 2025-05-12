class CommandContext:
    def __init__(self, inventory_manager, horse_manager, cash_dispenser):
        self.inventory_manager = inventory_manager
        self.horse_manager = horse_manager
        self.cash_dispenser = cash_dispenser
