import pygame
import global_variables as gv

# define player class
class pacman:

    def __init__(self):
        x = 100
        y = 100

        self.position = [x, y]
        self.movement_speed = 5

    # define every direction
    def up(self):
        self.movement_direction[1] = -1
        self.movement_direction[0] = 0
        # update position when moving   
        self.position = [self.position[0], self.position[1] - self.movement_speed]
        gv.pacman_position = self.position
    def down(self):
        self.movement_direction[1] = 1
        self.movement_direction[0] = 1
        self.position = [self.position[0], self.position[1] + self.movement_speed]
        gv.pacman_position = self.position
    def left(self):
        self.movement_direction[0] = -1
        self.movement_direction[1] = 0
        self.position = [self.position[0] - self.movement_speed, self.position[1]]
        gv.pacman_position= self.position
    def right(self):
        self.movement_direction[0] = 1
        self.movement_direction[1] = 0
        self.position = [self.position[0] + self.movement_speed, self.position[1]]
        gv.pacman_position = self.position
