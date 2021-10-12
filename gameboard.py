from human import Human
from ai import Ai


class Gameboard:
    def __init__(self):
        self.ai = Ai()
        self.player_one = Human('')
        self.player_two = Human('')

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        player_input = int(input("Press 1 to play multiplayer or 2 to play against the computer."))
        if player_input == 1:
            self.player_one.name = input("Enter Player One name: ")
            self.player_two.name = input("Enter Player Two name: ")
            print(f"{self.player_one.name}")
            print(f"{self.player_two.name}")
            return self.game_human_vs_human()
        elif player_input == 2:
            self.player_one.name = input("Enter Player One name: ")
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
      
    def game_human_vs_ai(self):
        while self.player_one.wins < 2 and self.ai.wins < 2:
            result = (self.player_one.choose_gesture() - self.ai.ai_pick()) % 5
            if result == 0:
                print ("This Round is a Tie")
            elif result <= 2:
                print(f"{self.player_one.name} Wins This Round!")
                self.player_one.wins += 1
            elif result >= 3:
                print("AI Wins This Round!")
                self.ai.wins += 1
        if self.player_one.wins == 2:
            print(f"Congrats {self.player_one.name}!")
        else:
            print("Congrats AI!")
    
    def game_human_vs_human(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            result = (self.player_one.choose_gesture() - self.player_two.choose_gesture()) % 5
            if result == 0:
                print ("This Round is a Tie")
            elif result <= 2:
                print(f"{self.player_one.name} Wins This Round!")
                self.player_one.wins += 1
            elif result >= 3:
                print(f"{self.player_two.name} Wins This Round!")
                self.player_two.wins += 1
        if self.player_one == 2:
            print(f"Congrats {self.player_one.name}!")
        else:
            print(f"Congrats {self.player_two.name}!")
                

    


  

        

