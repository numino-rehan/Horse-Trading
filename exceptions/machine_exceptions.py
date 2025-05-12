 
class InsufficientFundsError(Exception):
    def __init__(self):
        self.message = "Insufficient funds in machine."
        super().__init__(self.message)

class RestockError(Exception):
    def __init__(self):
        self.message = "Error during restocking."
        super().__init__(self.message)
