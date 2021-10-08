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
        self.display_gestures()
        selected_gesture = int(input("Select your gesture: "))
        if selected_gesture == 0: 
            print(f"You chose: ROCK")
            return "Rock"
        elif selected_gesture == 1: 
            print(f"You chose: SPOCK")
            return "Spock"
        elif selected_gesture == 2: 
            print(f"You chose: PAPER")
            return "Paper"
        elif selected_gesture == 3: 
            print(f"You chose: LIZARD")
            return "Lizard"
        elif selected_gesture == 4: 
            print(f"You chose: SCISSORS")
            return "Scissors"
        else:
            print("Choose a nuber from 0-4")

            return(self.human_pick)

    def ai_pick(self):
        pass

    def game(self):
        pass

    def display_gestures(self):
        print("Available gestures to be played:")
        i = 0
        for gesture in self.human.gestures:
            print(f"Press {i} to select {gesture}")
            i += 1
        


    def declare_winner(self):
        pass
