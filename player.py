
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

    def choose_gesture(self):
        self.display_gestures()
        selected_gesture = int(input(f"Chose Your Gesture human one: "))
        if selected_gesture >= 0 and selected_gesture <= 4:
            print(f"Human one Chose: ", self.gestures[selected_gesture])
            return selected_gesture
        else:
            print("Invalid Selection")
            return self.choose_gesture()
            
    
    def display_gestures(self):
        print("Available gestures to be played:")
        i = 0
        for gesture in self.gestures:
            print(f"Press {i} to select {gesture}")
            i += 1
        