from human import Human
from ai import Ai
import random


class Gameboard:
    def __init__(self):
        self.ai = Ai()

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        player_input = int(input("Press 1 to play multiplayer or 2 to play against the computer."))
        if player_input == 1:
            self.human = Human(input("Enter Player One name: "))
            self.human2 = Human(input("Enter Player Two name: "))
            print(f"{self.human}")
            print(f"{self.human2}")
            return self.game_human_vs_human()
        elif player_input == 2:
            self.human = Human(input("Enter Player One name: "))
            return self.game_human_vs_ai()
        else:
            return player_input


            
        

        

    def display_rules(self):
        print("Rules for RPSLS: As a user you will pick a gesture from the list of gestures displayed to you. The user or AI will select a gesture as well. \n After both gestures are picked and displayed there will be declared a winner of that round. The best of three rounds will win the game. \n the following combinations for RSPLS are as follows: \n Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, \n Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. ")
        

    def display_welcome(self):
       print("WELCOME TO RPSLS")
       

    def human_one_pick(self): 
        self.display_gestures()
        selected_gesture = int(input(f"Chose Your Gesture {self.human}: "))
        if selected_gesture >= 0 and selected_gesture <= 4:
            print(f"{self.human} Chose: ", self.human.gestures[selected_gesture])
            return selected_gesture
        else:
            print("Invalid Selection")
            return self.human_one_pick()
    
    def human_two_pick(self):
        self.display_gestures()
        selected_gesture = int(input(f"Chose Your Gesture {self.human2}: "))
        if selected_gesture >= 0 and selected_gesture <= 4:
            print(f"{self.human2} Chose: ", self.human.gestures[selected_gesture])
            return selected_gesture
        else:
            print("Invalid Selection")
            return self.human_two_pick()

    def ai_pick(self):
        ai_number = random.randrange(0,4)
        if ai_number != len(self.ai.gestures):
            print("AI Chose: ", self.ai.gestures[ai_number])
            return ai_number
     
      
    def game_human_vs_ai(self):
        human_wins = 0
        ai_wins = 0
        while human_wins < 2 and ai_wins < 2:
            result = (self.human_one_pick() - self.ai_pick()) % 5
            if result == 0:
                print ("This Round is a Tie")
            elif result <= 2:
                print(f"{self.human} Wins This Round!")
                human_wins += 1
            elif result >= 3:
                print("AI Wins This Round!")
                ai_wins += 1
        if human_wins == 2:
            print(f"Congrats {self.human}!")
        else:
            print("Congrats AI!")
    
    def game_human_vs_human(self):
        human_one_wins = 0
        human_two_wins = 0
        while human_one_wins < 2 and human_two_wins < 2:
            result = (self.human_one_pick() - self.human_two_pick()) % 5
            if result == 0:
                print ("This Round is a Tie")
            elif result <= 2:
                print(f"{self.human} Wins This Round!")
                human_one_wins += 1
            elif result >= 3:
                print(f"{self.human2} Wins This Round!")
                human_two_wins += 1
        if human_one_wins == 2:
            print(f"Congrats {self.human}!")
        else:
            print(f"Congrats {self.human2}!")
                

    def display_gestures(self):
        print("Available gestures to be played:")
        i = 0
        for gesture in self.human.gestures:
            print(f"Press {i} to select {gesture}")
            i += 1
        


  

        

