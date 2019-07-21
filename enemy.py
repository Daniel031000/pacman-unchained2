# ghost moving randomly
import random

class Ghost_random:
    def __init__(self):
        self.movement_direction = [0,0]
        self.movement_speed = 5
        self.position = [x,y]

    def moving_randomly(self):
        self.movement_direction[random(0, 1)] = random(-1, 1)
        if self.movement_direction[0] == 1:
            self.movementDirection[1] = 0
            self.position = self.position[self.position[0] + self.movement_speed, self.position[1]]
        elif self.movement_direction[0] == -1:
            self.movementDirection[1] = 0
            self.position = self.position[self.position[0] - self.movement_speed, self.position[1]]
        elif self.movement_direction[1] == 1:
            self.movementDirection[0] = 0
            self.position = self.position[self.position[0], self.position[1] + self.movement_speed]
        elif self.movement_direction[1] == -1:
            self.movementDirection[0] = 0
            self.position = self.position[self.position[0], self.position[1] - self.movement_speed]
        else:
            # if self.movement
            break
