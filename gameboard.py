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
        pass

    def display_welcome(self):
        pass    

    def human_pick(self):
        self.display_gestures()
        selected_gesture = int(input("Select your gesture: "))
        if selected_gesture == 0: 
            print("You chose: ROCK")
            return 0
        elif selected_gesture == 1: 
            print("You chose: SPOCK")
            return 1
        elif selected_gesture == 2: 
            print("You chose: PAPER")
            return 2
        elif selected_gesture == 3: 
            print("You chose: LIZARD")
            return 3
        elif selected_gesture == 4: 
            print("You chose: SCISSORS")
            return 4
        else:
            print("Choose a number from 0-4")
            return (self.human_pick)

    def ai_pick(self):
        ai_number = random.randrange(0,4)
        if ai_number == 0: 
            print("AI chose: ROCK")
            return 0
        elif ai_number == 1: 
            print("AI chose: SPOCK")
            return 1
        elif ai_number == 2: 
            print("AI chose: PAPER")
            return 2
        elif ai_number == 3: 
            print("AI chose: LIZARD")
            return 3
        elif ai_number == 4: 
            print("AI chose: SCISSORS")
            return 4
       #print(f"AI chose  + {ai_number}")
       # ai_number = self.display_gestures(ai_rand)
        #print(ai_number)
        
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

    def display_gestures(self):
        print("Available gestures to be played:")
        i = 0
        for gesture in self.human.gestures:
            print(f"Press {i} to select {gesture}")
            i += 1
        


    def declare_winner(self):
        pass
        

