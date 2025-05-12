from .base_command import BaseCommand

class RestockCommand(BaseCommand):
    def execute(self, args, context):
        context.inventory_manager.restock()
