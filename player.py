
class Player:
    def __init__(self):
        self.gestures = []
        self.create_gestures()
        
    def create_gestures(self):
        rock = 0
        spock = 1
        paper = 2
        lizard = 3
        scissors = 4

        self.gestures.extend([rock, spock,paper,lizard,scissors])
