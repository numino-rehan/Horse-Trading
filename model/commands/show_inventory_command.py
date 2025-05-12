from .base_command import BaseCommand

class ShowInventory(BaseCommand):
    def execute(self, args, context):
        context.inventory_manager.restock()

