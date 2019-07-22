import pygame
import global_variables as gv
import animation as ani


# define player class
class Pacman:
    def __init__(self):
        # loading every image
        self.PACMAN_SOURCE_LEFT = ["Graphics/pacman/Left/pacman0.png", "Graphics/pacman/Left/pacman1.png",
                                   "Graphics/pacman/Left/pacman2.png", "Graphics/pacman/Left/pacman3.png"]
        self.PACMAN_SOURCE_RIGHT = ["Graphics/pacman/Right/pacman0.png", "Graphics/pacman/Right/pacman1.png",
                                    "Graphics/pacman/Right/pacman2.png", "Graphics/pacman/Right/pacman3.png"]
        self.PACMAN_SOURCE_UP = ["Graphics/pacman/Up/pacman0.png", "Graphics/pacman/Up/pacman1.png",
                                 "Graphics/pacman/Up/pacman2.png", "Graphics/pacman/Up/pacman3.png"]
        self.PACMAN_SOURCE_DOWN = ["Graphics/pacman/Down/pacman0.png", "Graphics/pacman/Down/pacman1.png",
                                   "Graphics/pacman/Down/pacman2.png", "Graphics/pacman/Down/pacman3.png"]
        self.ANI_DURATION = 16
        self.movement_direction = [0, 0]
        self.ani_tick_counter = 0  # animation tick counter used to slow down pacman animation
        self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_LEFT
        self.image = pygame.image.load(self.PACMAN_LOADED_IMAGES[0])
        x = 480
        y = 200
        self.position = [x, y]
        self.movement_speed = 4  # (movement_speed = pixels/tick)
        self.rotate_direction = 2

    # define every direction
    # moves the pacman up by "movement_speed"
    def up(self):
        self.movement_direction[1] = -1
        self.movement_direction[0] = 0
        self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_UP  # moving image in the right direction

    def down(self):
        self.movement_direction[1] = 1
        self.movement_direction[0] = 0
        self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_DOWN

    def left(self):
        self.movement_direction[0] = -1
        self.movement_direction[1] = 0
        self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_LEFT

    def right(self):
        self.movement_direction[0] = 1
        self.movement_direction[1] = 0
        self.PACMAN_LOADED_IMAGES = self.PACMAN_SOURCE_RIGHT

    def move(self):
        x = self.position[0] + (self.movement_speed * self.movement_direction[0])
        y = self.position[1] + (self.movement_speed * self.movement_direction[1])
        self.position = [x, y]

    # loops through the events and calls the appropriate movement function upon an event
    def pacman_event_handler(self, keys_pressed):
        for i in range(len(keys_pressed)):
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                self.up()
                self.rotate_direction = 0
            elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                self.down()
                self.rotate_direction = 1
            elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                self.left()
                self.rotate_direction = 2
            elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                self.right()
                self.rotate_direction = 3

    def blit_pacman(self, surface):
        image_nr = int(gv.pacman.ani_tick_counter / (int(gv.pacman.ANI_DURATION / 4)))
        self.image = pygame.image.load(self.PACMAN_LOADED_IMAGES[image_nr - 1])
        pygame.transform.rotate(self.image, 45)
        pacman_image_rect = self.image.get_rect()
        pacman_image_rect.x = gv.pacman.position[0]
        pacman_image_rect.y = gv.pacman.position[1]
        surface.blit(self.image, pacman_image_rect)

    gv.pixel_colour_detection(self.position, gv.keys_pressed, self.movement_speed)
