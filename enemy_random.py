# ghost moving randomly
import random
import time

class Ghost_random_turquoise:  # blue ghost
    def __init__(self):
        self.ENEMY_TURQUOISE_SOURCE_IMAGE = ["Graphics/enemys/GeistTürkis.png"]
        self.movement_direction = [0,0]
        self.movement_speed = 4
        x = 960
        y = 560
        self.position = [x, y]
        self.PACMAN_LOADED_IMAGES = self.ENEMY_TURQUOISE_SOURCE_IMAGE

    def moving_randomly(self):
        self.movement_direction[random(0, 1)] = random(-1, 1)  # randomise the directions
        if self.movement_direction[0] == 1:
            self.movement_direction[1] = 0  # after multiple changes the ghost still moves in a straight line
            time.sleep(5)  # keeps moving for 5 seconds

        elif self.movement_direction[0] == -1:
            self.movement_direction[1] = 0
            time.sleep(5)

        elif self.movement_direction[1] == 1:
            self.movement_direction[0] = 0
            time.sleep(5)

        elif self.movement_direction[1] == -1:
            self.movement_direction[0] = 0
            time.sleep(5)

        else:
            pass  # if self.movement[0 or 1] = 0 than try again

    def move(self):  # updating position
        x = self.position[0] + (self.movement_speed * self.movement_direction[0])
        y = self.position[1] + (self.movement_speed * self.movement_direction[1])
        self.position = [x, y]

    def blit_enemy_turquoise(self, surface):
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        surface.blit(self.image, self.rect)

class Ghost_random_blue:  # blue ghost
    def __init__(self):
        self.ENEMY_BLUE_SOURCE_IMAGE = ["Graphics/enemys/GeistBlau.png"]
        self.movement_direction = [0, 0]
        self.movement_speed = 4
        x = 30
        y = 30
        self.position = [x, y]
        self.PACMAN_LOADED_IMAGES = self.ENEMY_BLUE_SOURCE_IMAGE

    def moving_randomly(self):
        self.movement_direction[random(0, 1)] = random(-1, 1)  # randomise the directions
        if self.movement_direction[0] == 1:
            self.movement_direction[1] = 0  # after multiple changes the ghost still moves in a straight line
            time.sleep(5)  # keeps moving for 5 seconds

        elif self.movement_direction[0] == -1:
            self.movement_direction[1] = 0
            time.sleep(5)

        elif self.movement_direction[1] == 1:
            self.movement_direction[0] = 0
            time.sleep(5)

        elif self.movement_direction[1] == -1:
            self.movement_direction[0] = 0
            time.sleep(5)

        else:
            pass  # if self.movement[0 or 1] = 0 than try again

    def move(self):  # updating position
        x = self.position[0] + (self.movement_speed * self.movement_direction[0])
        y = self.position[1] + (self.movement_speed * self.movement_direction[1])
        self.position = [x, y]

    def blit_enemy_blue(self, surface):
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        surface.blit(self.image, self.rect)
