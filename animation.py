import pygame
import global_variables as gv
def load_image (path, surface):
    level = pygame.image.load(path)
    surface.blit(level, gv.screensize)
