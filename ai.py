from player import Player

class Ai(Player):
    def __init__(self,name):
        self.name = name
        super().__init__()


    def __str__(self) -> str:
        return f"Ai - {self.name}"