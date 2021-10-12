from player import Player
import random

class Ai(Player):
    def __init__(self):
        self.name = ""
        super().__init__()


    def __str__(self) -> str:
        return f"Ai - {self.name}"

    def ai_pick(self):
        ai_number = random.randrange(0,4)
        if ai_number != len(self.gestures):
            print("AI Chose: ", self.gestures[ai_number])
            return ai_number