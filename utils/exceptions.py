class InvalidHorseNumberError(Exception):
    def __init__(self, horse_id):
        self.message = f"Invalid Horse Number: {horse_id}"
        super().__init__(self.message)

class InvalidBetAmountError(Exception):
    def __init__(self, amount):
        self.message = f"Invalid Bet: {amount}"
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    def __init__(self):
        self.message = "Insufficient funds in machine."
        super().__init__(self.message)

class InvalidCommandError(Exception):
    def __init__(self, command):
        self.message = f"Invalid Command: {command}"
        super().__init__(self.message)

class RestockError(Exception):
    def __init__(self):
        self.message = "Error during restocking."
        super().__init__(self.message)
