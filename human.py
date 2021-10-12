from player import Player

class Human(Player):
    def __init__(self,name):
        self.name = name
        self.wins = 0
        super().__init__()

    def __str__(self) -> str:
        return f"Player - {self.name}"
    
  