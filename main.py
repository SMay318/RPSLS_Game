from gameboard import Gameboard
from player import Player

# mygesture = Player()

# print(f"{mygesture.gestures}")

game = Gameboard()
game.display_welcome()
# game.human_pick()

# game.ai_pick()
game.display_rules()
game.game()
