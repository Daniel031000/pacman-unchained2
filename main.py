import pygame
import sys

BLACK = (0, 0, 0)
pygame.display.set_caption("Daniel`s PacMan")
screen = pygame.display.set_mode((1000, 500))



while 1:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # game logic loop
    # animation
    screen.fill(BLACK)
    pygame.display.flip()