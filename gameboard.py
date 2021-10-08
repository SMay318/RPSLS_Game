from human import Human
from ai import Ai

class Gameboard:
    def __init__(self):
        self.human = Human()
        self.ai = Ai()

    def run_game(self):
        pass

    def display_rules(self):
        pass

    def display_welcome(self):
        pass    

    def human_pick(self):
        pass

    def ai_pick(self):
        pass

    def game(self):
        pass

    def display_gestures(self):
        print("Available gestures to be played:")
        i = 0
        for gestures in self.human.gestures:
            print(f"Press {i} to select {gestures.name} {self.human.gestures}")
            i += 1
        


    def declare_winner(self):
        pass
