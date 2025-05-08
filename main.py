from core.command_processor import CommandProcessor

def runATMMachine():
    # Create an instance of CommandProcessor which integrates all functionalities
    processor = CommandProcessor()

   

    # Run command loop
    while True:
         # Show initial inventory and horse data
        print(processor.inventory_manager.inventory)
        processor.inventory_manager.show_inventory()
        processor.horse_manager.show_horse_data()
        command = input(
            "Enter a command:\n"
            "'R' or 'r' - restock the cash inventory\n"
            "'Q' or 'q' - quit the application\n"
            "'W' or 'w' [1-7] - set the winning horse number\n"
            "[1-7] <amount> - place a bet of the given amount on a specific horse\n"
        )
        print("______________________________")
        processor.process_commands(command)

if __name__ == "__main__":
    runATMMachine()
