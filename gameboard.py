from human import Human
from ai import Ai


class Gameboard:
    def __init__(self):
        self.ai = Ai()
        self.player_one = None
        self.player_two = None

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
            return self.run_game()

    def display_rules(self):
        print(""" Rules for RPSLS: As a user you will pick a gesture from the list of gestures displayed to you. The user or AI will select a gesture as well. 
        \n After both gestures are picked and displayed there will be declared a winner of that round. The best of three rounds will win the game. 
        \n The following combinations for RSPLS are as follows: 
        \n Rock Crushes Scissors, Scissors Cuts Paper, Paper Covers Rock, Rock Crushes Lizard, Lizard Poisons Spock, 
        \n Spock Smashes Scissors, Scissors Decapitates Lizard, Lizard Eats Paper, Paper Disproves Spock, Spock Vaporizes Rock. """)
    
    def display_welcome(self):
       print("WELCOME TO RPSLS")
       

    def human_one_pick(self): 
        self.human.choose_gesture()
       
    
    def human_two_pick(self):
        self.human.choose_gesture()
        
      
    def game_human_vs_ai(self):
        human_wins = 0
        ai_wins = 0
        while human_wins < 2 and ai_wins < 2:
            result = (self.human.choose_gesture() - self.ai.ai_pick()) % 5
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
            result = (self.human.choose_gesture() - self.human.choose_gesture()) % 5
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
                

    


  

        

