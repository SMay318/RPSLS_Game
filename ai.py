from player import Player
import random

class Ai(Player):
    def __init__(self):
        self.name = ''
        self.wins = 0
        super().__init__()


    def __str__(self) -> str:
        return f"Ai - {self.name}"

    def ai_pick(self):
        ai_number = random.randrange(0,4)
        if ai_number != len(self.gestures):
            # print("AI Chose: ", self.gestures[ai_number])
            return ai_number
    
    def choose_gesture(self):
        selected_gesture = self.ai_pick()
        if selected_gesture >= 0 and selected_gesture <= 4:
            print(f"AI Chose: ", self.gestures[selected_gesture])
            return selected_gesture
      