
class Player:
    def __init__(self):
        self.gestures = []
        self.create_gestures()
        
    def create_gestures(self):
        rock = "rock"
        spock = "spock"
        paper = "paper"
        lizard = "lizard"
        scissors = "scissors"

        self.gestures.extend([rock, spock, paper, lizard, scissors])
