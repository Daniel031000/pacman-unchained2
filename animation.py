import pygame
import global_variables as gv

PACMAN_IMAGES = []

def blit_level(path, surface):
    level = pygame.image.load(path)
    surface.blit(level, level.get_rect())


def blit_player(surface):

    surface.blit()
