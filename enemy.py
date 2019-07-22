# ghost moving randomly
import random

class Ghost_random:  # green or blue ghost
    def __init__(self):
        self.movement_direction = [0,0]
        self.movement_speed = 5
        self.position = [x, y]

    def moving_randomly(self):
        self.movement_direction[random(0, 1)] = random(-1, 1)  # randomise the directions
        if self.movement_direction[0] == 1:
            self.movement_direction[1] = 0  # after multiple changes the ghost still moves in a straight line
            self.position = self.position[self.position[0] + self.movement_speed, self.position[1]]  # updating position
        elif self.movement_direction[0] == -1:
            self.movement_direction[1] = 0
            self.position = self.position[self.position[0] - self.movement_speed, self.position[1]]
        elif self.movement_direction[1] == 1:
            self.movement_direction[0] = 0
            self.position = self.position[self.position[0], self.position[1] + self.movement_speed]
        elif self.movement_direction[1] == -1:
            self.movement_direction[0] = 0
            self.position = self.position[self.position[0], self.position[1] - self.movement_speed]
        else:
            pass  # if self.movement[0 or 1] = 0 than tray again

