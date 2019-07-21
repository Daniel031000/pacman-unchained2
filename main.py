import pygame
import sys
import global_variables as gv
import Pacman as gl
import animation as ani
pygame.init()

BLACK = (0, 0, 0)
LEVEL_PATHS = ["Graphics/levels/level1.png", "Graphics/levels/level2.png", "Graphics/levels/level3.png"]

screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel's PacMan")
clock = pygame.time.Clock()

# instantiate pacman class
gv.pacman = gl.Pacman()
gv.pacman_tick_counter = 0

while 1:
    # event loop
    gv.pygame_events = pygame.event.get()
    for event in gv.pygame_events:
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic loop
    gv.pacman.pacman_event_handler(gv.pygame_events)

    # animation
    ani.blit_level(LEVEL_PATHS[0], screen)

    gv.pacman_tick_counter = gv.pacman_tick_counter + 1
    if gv.pacman_tick_counter >= gv.PACMAN_ANI_DURATION - 1:
        gv.pacman_tick_counter = 0

    ani.blit_player(screen)

    pygame.display.flip()
    clock.tick(30)