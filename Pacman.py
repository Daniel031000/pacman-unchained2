import pygame
import global_variables as gv
import animation as ani


PACMAN_IMAGES_LEFT = ["Graphics/pacman/Left/pacman0.png", "Graphics/pacman/Left/pacman1.png", "Graphics/pacman/Left/pacman2.png", "Graphics/pacman/Left/pacman3.png"]
PACMAN_IMAGES_RIGHT = ["Graphics/pacman/Right/pacman0.png", "Graphics/pacman/Right/pacman1.png", "Graphics/pacman/Right/pacman2.png", "Graphics/pacman/Right/pacman3.png"]
PACMAN_IMAGES_UP = ["Graphics/pacman/Up/pacman0.png", "Graphics/pacman/Up/pacman1.png", "Graphics/pacman/Up/pacman2.png", "Graphics/pacman/Up/pacman3.png"]
PACMAN_IMAGES_DOWN = ["Graphics/pacman/Down/pacman0.png", "Graphics/pacman/Down/pacman1.png", "Graphics/pacman/Down/pacman2.png", "Graphics/pacman/Down/pacman3.png"]

# define player class
class Pacman:
    def __init__(self):
        self.ANI_DURATION = 16
        self.movement_direction = [0, 0]
        self.ani_tick_counter = 0  # animation tick counter used to slow down pacman animation
        self.image = pygame.image.load(PACMAN_IMAGES[0])
        x = 100
        y = 100
        self.position = [x, y]
        self.movement_speed = 4  # (movement_speed = pixels/tick)
        self.rotate_direction = 2

    # define every direction

    # moves the pacman up by "movement_speed"
    def up(self):
        self.movement_direction[1] = -1
        self.movement_direction[0] = 0
        # update position when moving

    def down(self):
        self.movement_direction[1] = 1
        self.movement_direction[0] = 0

    def left(self):
        self.movement_direction[0] = -1
        self.movement_direction[1] = 0

    def right(self):
        self.movement_direction[0] = 1
        self.movement_direction[1] = 0

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
        self.image = pygame.image.load(PACMAN_IMAGES[image_nr - 1])
        pygame.transform.rotate(self.image, 45)
        self.rotate_pacman()
        pacman_image_rect = self.image.get_rect()
        pacman_image_rect.x = gv.pacman.position[0]
        pacman_image_rect.y = gv.pacman.position[1]
        surface.blit(self.image, pacman_image_rect)

    def rotate_pacman(self):
        # up
        if self.rotate_direction == 0:
            pass
        # down
        elif self.rotate_direction == 1:

            pass
        # left
        elif self.rotate_direction == 2:
            pass

        # right
        elif self.rotate_direction == 3:
            pygame.transform.flip(self.image, True, False)


    '''def pacman_counter_mocement():
        gv.pacman.ani_tick_counter = gv.pacman.ani_tick_counter + 1
        if gv.pacman.ani_tick_counter >= gv.pacman.ANI_DURATION - 1:
            gv.pacman.ani_tick_counter = 0'''

