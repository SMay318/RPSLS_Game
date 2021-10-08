from player import Player

class Ai(Player):
    def __init__(self):
        self.name = ""
        super().__init__()


    def __str__(self) -> str:
        return f"Ai - {self.name}"