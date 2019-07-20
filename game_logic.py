import pygame
import global_variables as gv

# define player class
class pacman:

    def __init__(self):
        self.movement_direction = [0, 0]
        self.position = [100, 100]
        self.movement_speed = 5

    # define every direction
    def up(self):
        for event in gv.pygame_events:
            if gv.pygame_events == pygame.K_w:
                self.movement_direction[1] = -1
                self.movement_direction[0] = 0

    def down(self):
        for event in gv.pygame_events:
            if gv.pygame_events == pygame.K_s:
                self.movement_direction[1] = 1
                self.movement_direction[0] = 1

    def left(self):
        for event in gv.pygame_events:
            if gv.pygame_events == pygame.K_a:
                self.movement_direction[0] = -1
                self.movement_direction[1] = 0

    def right(self):
        for event in gv.pygame_events:
            if gv.pygame_events == pygame.K_d:
                self.movement_direction[0] = 1
                self.movement_direction[1] = 0
