import pygame
import global_variables as gv


PACMAN_IMAGES = ["Graphics/pacman/pacman0.png", "Graphics/pacman/pacman1.png", "Graphics/pacman/pacman2.png", "Graphics/pacman/pacman3.png"]


# draws the level
def blit_level(path, surface):
    level_image = pygame.image.load(path)
    surface.blit(level_image, level_image.get_rect())


# takes the position of pacman and draws him to the screen



