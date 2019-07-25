# ghost moving randomly
import pygame
import random
import isStripmoveable as IS
import global_variables as gv




class Ghost:
    def __init__(self,ghost_type, starting_position):  # ghost_type
        ENEMY_SOURCE_IMAGES = ["Graphics\enemys\GeistBlau.png", "Graphics\enemys\GeistOrange.png",
                               "Graphics\enemys\GeistRot.png", "Graphics\enemys\GeistTürkis.png"]
        self.image = pygame.image.load(ENEMY_SOURCE_IMAGES[ghost_type])  # ghost_type
        self.rect = self.image.get_rect()
        self.movement_direction = [0, 0]
        self.movement_speed = 4
        self.position = starting_position

    def set_random_direction(self):
        # change direction every 90 ticks on average
        tick_interval = 90
        change_direction = random.randint(0, tick_interval + 1)
        if change_direction == tick_interval:
            gv.ran_x = random.randint(-1, 1)
            gv.ran_y = 0
            if gv.ran_x == 0:
                y_directions = [-1, 1]
                gv.ran_y = y_directions[random.randint(0, 1)]
            self.movement_direction = [gv.ran_x, gv.ran_y]


    def move(self):  # updating position
        self.set_random_direction()
        x = self.position[0] + (self.movement_speed * self.movement_direction[0])
        y = self.position[1] + (self.movement_speed * self.movement_direction[1])
        self.position = [x, y]
        print(x, y)

    def blit_ghost(self, surface):
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        surface.blit(self.image, self.rect)