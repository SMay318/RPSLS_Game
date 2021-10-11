from human import Human
from ai import Ai
import random

class Gameboard:
    def __init__(self):
        self.human = Human()
        self.ai = Ai()

    def run_game(self):
        pass

    def display_rules(self):
        print("Rules for RPSLS: As a user you will pick a gesture from the list of gestures displayed to you. The user or AI will select a gesture as well. \n After both gestures are picked and displayed there will be declared a winner of that round. The best of three rounds will win the game. \n the following combinations for RSPLS are as follows: \n Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, \n Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. ")
        

    def display_welcome(self):
        pass    

    def human_pick(self):
        self.display_gestures()
        selected_gesture = int(input("Select your gesture: "))
        if selected_gesture != len(self.human.gestures):
            print("Human chose: ", self.human.gestures[selected_gesture])
            return selected_gesture

    def ai_pick(self):
        ai_number = random.randrange(0,4)
        if ai_number != len(self.ai.gestures):
            print("AI chose: ", self.ai.gestures[ai_number])
            return ai_number
      
    def game(self):
        human_wins = 0
        ai_wins = 0
        while human_wins < 2 and ai_wins < 2:
            result = (self.human_pick() - self.ai_pick()) % 5
            if result == 0:
                print ("this round is a tie")
            elif result <= 2:
                print("human wins this round!")
                human_wins += 1
            elif result >= 3:
                print("AI wins this round!")
                ai_wins += 1
        if human_wins == 2:
            print("Congrats Human!")
        else:
            print("Congrats AI!")
                

    def display_gestures(self):
        print("Available gestures to be played:")
        i = 0
        for gesture in self.human.gestures:
            print(f"Press {i} to select {gesture}")
            i += 1
        


  

        

