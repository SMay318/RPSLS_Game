from player import Player

class Human(Player):
    def __init__(self):
        self.name = input ("Enter your Name:")
        super().__init__()

    def __str__(self) -> str:
        return f"Player1 - {self.name}"