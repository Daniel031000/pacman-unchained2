import pygame
import global_variables as gv


PACMAN_IMAGES = ["Graphics/pacman/pacman0.png"]


def blit_level(path, surface):
    level = pygame.image.load(path)
    surface.blit(level, level.get_rect())


def blit_player(surface):

    surface.blit()