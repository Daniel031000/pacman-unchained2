import pygame
import global_variables as gv



class Pacman:
    def __init__(self, starting_position):
        self.PACMAN_SOURCE_LEFT = ["graphics/pacman/left/pacman0.png", "graphics/pacman/left/pacman1.png",
                                   "graphics/pacman/left/pacman2.png", "graphics/pacman/left/pacman3.png"]
        self.PACMAN_SOURCE_RIGHT = ["graphics/pacman/right/pacman0.png", "graphics/pacman/right/pacman1.png",
                                    "graphics/pacman/right/pacman2.png", "graphics/pacman/right/pacman3.png"]
        self.PACMAN_SOURCE_UP = ["graphics/pacman/up/pacman0.png", "graphics/pacman/up/pacman1.png",
                                 "graphics/pacman/up/pacman2.png", "graphics/pacman/up/pacman3.png"]
        self.PACMAN_SOURCE_DOWN = ["graphics/pacman/down/pacman0.png", "graphics/pacman/down/pacman1.png",
                                   "graphics/pacman/down/pacman2.png", "graphics/pacman/down/pacman3.png"]
        self.ANI_DURATION = 16
        self.movement_direction = gv.directions[4]
        self.ani_tick_counter = 0  # animation tick counter used to slow down pacman animation
        self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_LEFT  # starting picture is to the left
        self.image = pygame.image.load(self.PACMAN_LOADED_IMAGES[0])
        self.rect = self.image.get_rect()
        self.position = starting_position
        self.movement_speed = 4  # (movement_speed = pixels/tick)

    def change_direction(self, direction):  # changes animation of the pacman and updates the direction
        if direction == 0:
            self.movement_direction = gv.directions[0]
            self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_UP
        elif direction == 1:
            self.movement_direction = gv.directions[1]
            self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_DOWN
        elif direction == 2:
            self.movement_direction = gv.directions[2]
            self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_LEFT
        elif direction == 3:
            self.movement_direction = gv.directions[3]
            self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_RIGHT

    def next_move_is_possible(self):
        offset = []  # describes the shift of the active pixel
        ap_direction = []
        # every single if looks for the right active pixel
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
        elif self.movement_direction == gv.directions[4]:
            return True

        for i in range(25):  # active pixel -> active string
            x = self.position[0] + offset[0] + ap_direction[0] * i
            y = self.position[1] + offset[1] + ap_direction[1] * i
            if gv.screen.get_at([x, y]) == (0, 18, 255, 255):  # checks if the pixels are blue
                return False

        return True

    def teleport(self):  # teleports if he hits a certain x
        if self.position[0] < 20:
            self.position[0] = 965
        elif self.position[0] > 970:
            self.position[0] = 25

    def move(self):
        # updating its position
        self.teleport()
        if not self.next_move_is_possible():
            self.movement_direction = gv.directions[4]
        x = self.position[0] + (self.movement_speed * self.movement_direction[0])
        y = self.position[1] + (self.movement_speed * self.movement_direction[1])
        self.position = [x, y]
        self.eat_pellet()

    # loops through the events and calls the appropriate movement function upon an event
    def pacman_event_handler(self, keys_pressed):
        for i in range(len(keys_pressed)):
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                self.change_direction(0)
            elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                self.change_direction(1)
            elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                self.change_direction(2)
            elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                self.change_direction(3)

    # draws the pacman to the screen and makes sure the animations looks moving
    def blit_pacman(self, surface):
        image_nr = int(gv.pacman.ani_tick_counter / (int(gv.pacman.ANI_DURATION / 4)))
        self.image = pygame.image.load(self.PACMAN_LOADED_IMAGES[image_nr - 1])
        self.rect = self.image.get_rect()
        self.rect.x = gv.pacman.position[0]
        self.rect.y = gv.pacman.position[1]
        surface.blit(self.image, self.rect)

    def eat_pellet(self):  # if the pacman eats the pellet it will be deleted from the list and disappear from the screen
        counter = 0
        while counter < len(gv.level_pellets[gv.current_level]):
            pellet = gv.level_pellets[gv.current_level][counter]
            if gv.pacman.rect.contains(pellet.rect):
                gv.score = gv.score + 1
                del gv.level_pellets[gv.current_level][counter]
            counter = counter + 1

    def test_ghost_collision(self):  # tests if the rectangle of the ghost touches the pacmans rectangle
        for ghost in gv.ghosts:
            if self.rect.colliderect(ghost.rect):
                gv.lose = True
                break






