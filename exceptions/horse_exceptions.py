 
class InvalidHorseNumberException(Exception):
    def __init__(self, horse_id):
        self.message = f"Invalid Horse Number: {horse_id}"
        super().__init__(self.message)
