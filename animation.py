import pygame
import global_variables as gv


PACMAN_IMAGES = ["Graphics/pacman/pacman0.png", "Graphics/pacman/pacman1.png", "Graphics/pacman/pacman2.png", "Graphics/pacman/pacman3.png"]


# draws the level
def blit_level(path, surface):
    level_image = pygame.image.load(path)
    surface.blit(level_image, level_image.get_rect())


# takes the position of pacman and draws him to the screen
def blit_player(surface):
    image_nr = int(gv.pacman_tick_counter / (int(gv.PACMAN_ANI_DURATION / 4)))
    pacman_image = pygame.image.load(PACMAN_IMAGES[image_nr - 1])
    pacman_image_rect = pacman_image.get_rect()
    pacman_image_rect.x = gv.pacman_position[0]
    pacman_image_rect.y = gv.pacman_position[1]
    surface.blit(pacman_image, pacman_image_rect)