from player import Player

class Human(Player):
    def __init__(self):
<<<<<<< HEAD
        self.name = input("Enter your name?")
=======
        self.name = input ("Enter your Name:")
>>>>>>> 81a11eae461743a1cc47f29751753b8d3b26026e
        super().__init__()

    def __str__(self) -> str:
        return f"Player1 - {self.name}"