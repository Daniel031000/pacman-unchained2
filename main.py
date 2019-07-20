import pygame
import sys
import global_variables as gv
import animation as ani
pygame.init()

BLACK = (0, 0, 0)
screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel`s PacMan")


while 1:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # game logic loop
    # animation

    level_1 = pygame.image.load("Graphics/levels/level1.png")
    level_1_rect =level_1.get_rect()
    screen.blit(level_1, level_1_rect)
    pygame.display.flip()