import pygame
import global_variables as gv


# define player class
class Pacman:

    def __init__(self):
        self.movement_direction = [0, 0]
        x = 100
        y = 100
        self.position = [x, y]
        self.movement_speed = 5  # (movement_speed = pixels/tick)
        gv.pacman_position = self.position
    # define every direction

    # moves the pacman up by "movement_speed"
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

    # loops through the events and calls the appropriate movement function upon an event
    def pacman_event_handler(events):
        pass
