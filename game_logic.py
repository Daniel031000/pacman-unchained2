import pygame
import global_variables as gv

# define player class
class pacman:

    def __init__(self):
        x = 100
        y = 100
        self.movement_direction = [0, 0]
        self.position = [x, y]
        self.movement_speed = 5

    # define every direction
    def up(self):
        try:
            for event in gv.pygame_events:
                if gv.pygame_events == pygame.K_w:
                    self.movement_direction[1] = -1
                    self.movement_direction[0] = 0
                    y = y-1
                    gv.pacman_position = [x, y]
        except:
            print("Ed SHeerans's fault")
            pass
    def down(self):
        for event in gv.pygame_events:
            if gv.pygame_events == pygame.K_s:
                self.movement_direction[1] = 1
                self.movement_direction[0] = 1
                y = y+1
                gv.pacman_position = [x, y ]
    def left(self):
        for event in gv.pygame_events:
            if gv.pygame_events == pygame.K_a:
                self.movement_direction[0] = -1
                self.movement_direction[1] = 0
                x = x-1
                gv.pygame_events = [x, y]
    def right(self):
        for event in gv.pygame_events:
            if gv.pygame_events == pygame.K_d:
                self.movement_direction[0] = 1
                self.movement_direction[1] = 0
                x = x+1
                gv.pacman_position = [x, y]
