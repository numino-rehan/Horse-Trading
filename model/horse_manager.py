from config.constants import HORSE_DATA
from exceptions.horse_exceptions import InvalidHorseNumberError
from colorama import Fore, Style

class HorseManager:
    def __init__(self):
        self.horse_data = self.generate_horse_data()

    def generate_horse_data(self):
        return HORSE_DATA

    def set_winner(self, horse_id, won=True):
        if horse_id < 1 or horse_id > len(self.horse_data):
            raise InvalidHorseNumberError(horse_id)
        self.horse_data[horse_id]["won"] = won
        print(Fore.GREEN + f'Set "{self.horse_data[horse_id]["name"]}" (Horse #{horse_id}) as the winning horse.')
        print()

    def __str__(self):
        lines = [Fore.BLUE + Style.BRIGHT + "HORSES:"]
        for horse_id, data in self.horse_data.items():
            name = data["name"]
            odds = data.get("odds", "N/A")
            won = data.get("won", False)

            status_color = Fore.GREEN if won else Fore.RED
            status_text = "WON" if won else "LOST"

            lines.append(f"{Fore.YELLOW}{horse_id}{Style.RESET_ALL}, "
                  f"{Fore.CYAN}{name}{Style.RESET_ALL}, "
                  f"{Fore.WHITE}{odds}{Style.RESET_ALL}, "
                  f"{status_color}{status_text}")
        return "\n".join(lines)
    
    def show_horse_data(self):
        print(self)
        print()
   