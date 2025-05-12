 
class InvalidCommandException(Exception):
    def __init__(self, command):
        self.message = f"Invalid Command: {command}"
        super().__init__(self.message)
