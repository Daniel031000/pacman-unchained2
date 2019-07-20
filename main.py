import pygame
import sys
import global_variables as gv
import game_logic as gl
import animation as ani
pygame.init()

BLACK = (0, 0, 0)
screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel`s PacMan")
# call pay_man
pacman = gl.pacman()
pacman_position_Up = [pacman.up().position[0], pacman.up().position[1]]

while 1:
    # event loop
    gv.pygame_events = pygame.event
    for event in gv.pygame_events.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic loop


    # animation
    level_1 = pygame.image.load("Graphics/levels/level1.png")
    level_1_rect =level_1.get_rect()
    screen.blit(level_1, level_1_rect)
    pygame.display.flip()
