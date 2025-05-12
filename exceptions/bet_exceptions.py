class InvalidBetAmountError(Exception):
    def __init__(self, amount):
        self.message = f"Invalid Bet: {amount}"
        super().__init__(self.message)

