# ghost moving randomly
import random

class Ghost:
    def __init__(self):
        self.movement_direction = [0,0]
        self.movement_speed = 5

    def moving_randomly(self):
        self.movement_direction[random(0, 1)] = random(-1, 1)
        if self.movement_direction[0] == 1:

        elif self.movement_direction[0] == -1:

        elif self.movement_direction[1] == 1:

        elif self.movement_direction[1] == -1:


        else:
            break
