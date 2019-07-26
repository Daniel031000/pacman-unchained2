import pygame
import random
import global_variables as gv

'''I was unable to design a code which follows the pacman so I made every ghost random'''
class Ghost:
    def __init__(self, ghost_type, starting_position):
        self.image = pygame.image.load(gv.GHOST_SOURCE_IMAGES[ghost_type][0])  # load all images
        self.rect = self.image.get_rect()  # draw a rectangle around the ghosts
        self.movement_direction = [0, 0]
        self.movement_speed = 4
        self.position = starting_position  # starting position is defined in the main file

    def set_random_direction(self):  # let them move randomly
        # change direction every 90 ticks on average
        tick_interval = 30
        change_direction = random.randint(0, tick_interval + 1)
        if change_direction == tick_interval:
            gv.ran_x = random.randint(-1, 1)  # random x-direction
            gv.ran_y = 0
            if gv.ran_x == 0:
                y_directions = [-1, 1]  # random y-direction
                gv.ran_y = y_directions[random.randint(0, 1)]
            self.movement_direction = [gv.ran_x, gv.ran_y]

    def next_move_is_possible(self):  # sets the active pixel which is checked in the for-loop in the right direction
        offset = []  # the offset describes the shift of the pixel depending on the direction
        ap_direction = []
        if self.movement_direction == gv.directions[0]:  # up
            offset = [0, self.movement_speed * (-1)]
            ap_direction = gv.directions[3]
        elif self.movement_direction == gv.directions[1]:  # down
            offset = [0, 25 + self.movement_speed]
            ap_direction = gv.directions[3]
        elif self.movement_direction == gv.directions[2]:  # left
            offset = [self.movement_speed * (-1), 0]
            ap_direction = gv.directions[1]
        elif self.movement_direction == gv.directions[3]:  # right
            offset = [25 + self.movement_speed, 0]
            ap_direction = gv.directions[1]
        elif self.movement_direction == gv.directions[4]:  # stationary
            return True

        for i in range(25):  # the active pixel evolves to a whole string
            x = self.position[0] + offset[0] + ap_direction[0] * i
            y = self.position[1] + offset[1] + ap_direction[1] * i
            if gv.screen.get_at([x, y]) == (0, 18, 255, 255):  # check if the next step involves a blue pixel
                return False

        return True

    def teleport(self):  # if they randomly walk into the portal, they are teleported as well
        if self.position[0] < 18:
            self.position[0] = 965
        elif self.position[0] > 965:
            self.position[0] = 25

    def move(self):  # updating position
        self.set_random_direction()  # load the direction and the teleport function
        self.teleport()
        possible_directions = gv.directions.copy()
        del possible_directions[4]
        if self.movement_direction != gv.directions[4]:  # deletes the [0,0] direction and the old direction
            del possible_directions[possible_directions.index(self.movement_direction)]
        if not self.next_move_is_possible():  # if the ghost is stuck it changes the direction right away
            self.movement_direction = possible_directions[random.randint(0, 2)]
        x = self.position[0] + (self.movement_speed * self.movement_direction[0])
        y = self.position[1] + (self.movement_speed * self.movement_direction[1])
        self.position = [x, y]

    def blit_ghost(self, surface):  # draw the ghosts onto the surface
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        surface.blit(self.image, self.rect)