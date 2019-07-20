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
    screen.blit(pygame.image.load("Graphics/levels/level1.png"), (1000, 500))
    pygame.display.flip()