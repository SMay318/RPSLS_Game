from human import Human
from ai import Ai
import random

class Gameboard:
    def __init__(self):
        self.human = Human()
        self.ai = Ai()

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.game()

        

    def display_rules(self):
        print("Rules for RPSLS: As a user you will pick a gesture from the list of gestures displayed to you. The user or AI will select a gesture as well. \n After both gestures are picked and displayed there will be declared a winner of that round. The best of three rounds will win the game. \n the following combinations for RSPLS are as follows: \n Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, \n Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. ")
        

    def display_welcome(self):
       print("WELCOME TO RPSLS")
       

    def human_pick(self):
        self.display_gestures()
        selected_gesture = int(input("Chose Your Gesture: "))
        if selected_gesture >= len(self.human.gestures):
            print("Choose a number from 0-4")
            return self.human_pick()
        else:
            print(f"{self.human.name} Chose: ", self.human.gestures[selected_gesture])
            return selected_gesture

    def ai_pick(self):
        ai_number = random.randrange(0,4)
        if ai_number != len(self.ai.gestures):
            print("AI Chose: ", self.ai.gestures[ai_number])
            return ai_number
     
      
    def game(self):
        human_wins = 0
        ai_wins = 0
        while human_wins < 2 and ai_wins < 2:
            result = (self.human_pick() - self.ai_pick()) % 5
            if result == 0:
                print ("This Round is a Tie")
            elif result <= 2:
                print(f"{self.human.name} Wins This Round!")
                human_wins += 1
            elif result >= 3:
                print("AI Wins This Round!")
                ai_wins += 1
        if human_wins == 2:
            print(f"Congrats {self.human.name}!")
        else:
            print("Congrats AI!")
                

    def display_gestures(self):
        print("Available gestures to be played:")
        i = 0
        for gesture in self.human.gestures:
            print(f"Press {i} to select {gesture}")
            i += 1
        


  

        

