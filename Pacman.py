import pygame
import global_variables as gv


# define player class
class Pacman:
    def __init__(self):
        self.ANI_DURATION = 16
        self.movement_direction = [0, 0]
        self.ani_tick_counter = 0  # animation tick counter used to slow down pacman animation
        x = 100
        y = 100
        self.position = [x, y]
        self.movement_speed = 1  # (movement_speed = pixels/tick)


    # define every direction

    # moves the pacman up by "movement_speed"
    def up(self):
        self.movement_direction[1] = -1
        self.movement_direction[0] = 0
        # update position when moving
        self.position = [self.position[0], self.position[1] - self.movement_speed]

    def down(self):
        self.movement_direction[1] = 1
        self.movement_direction[0] = 1
        self.position = [self.position[0], self.position[1] + self.movement_speed]

    def left(self):
        self.movement_direction[0] = -1
        self.movement_direction[1] = 0
        self.position = [self.position[0] - self.movement_speed, self.position[1]]

    def right(self):
        self.movement_direction[0] = 1
        self.movement_direction[1] = 0
        self.position = [self.position[0] + self.movement_speed, self.position[1]]

    # loops through the events and calls the appropriate movement function upon an event
    def pacman_event_handler(self, keys_pressed):
        for i in range(len(keys_pressed)):
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                self.up()
            elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                self.down()
            elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                self.left()
            elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                self.right()

