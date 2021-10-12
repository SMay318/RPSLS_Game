from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def __str__(self) -> str:
        return f"Player - {self.name}"
    
   