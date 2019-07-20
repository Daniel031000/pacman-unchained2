import pygame
import sys
import global_variables as gv
import animation as ani
pygame.init()

BLACK = (0, 0, 0)
LEVEL_PATHS = ["Graphics/levels/level1.png", "Graphics/levels/level2.png", "Graphics/levels/level3.png"]

screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel`s PacMan")




while 1:


    # event loop
    gv.pygame_events = pygame.event
    for event in gv.pygame_events.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic loop


    # animation
    ani.blit_level(LEVEL_PATHS[2], screen)

    gv.pacman_ani_counter = gv.pacman_ani_counter + 1
    if gv.pacman_ani_counter >= 5:
        gv.pacman_ani_counter = 0

    ani.blit_player()

    pygame.display.flip()
