import pygame
import sys
import global_variables as gv
import pacman as pm
import animation as ani
pygame.init()


# constants
BLACK = (0, 0, 0)
#LEVEL_PATHS = ["Graphics/levels/level1.png", "Graphics/levels/level2.png", "Graphics/levels/level3.png"]

gv.screen = pygame.display.set_mode(gv.screensize)

pygame.display.set_caption("Daniel's PacMan")
clock = pygame.time.Clock()

# instantiate pacman class
gv.pacman = pm.Pacman()
gv.pacman_tick_counter = 0

#
ani.read_pellet_images()



while 1:
    # event loop
    gv.keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic loop
    gv.pacman.pacman_event_handler(gv.keys_pressed)
    gv.pacman.move()

    # animation
    ani.blit_level(gv.LEVEL_PATHS[0], gv.screen)
    '''if gv.score == 587:
        ani.blit_level(LEVEL_PATHS[1], gv.screen]
        gv.current_level = 1
        gv.score = 0
        Reachedsecondlevel = True
        elif score == 23 and reachedsecondlevel=True
        ani.blit_counter_level(LEVEL_PATHS[2, gv.screen]
        gv.current_level = 2 
        reachedthird level = True
        if score==23 and reachedthird level = true 
        gv.current_level = 2
        gv.score = 0'''
    ani.draw_pellets(gv.screen, gv.current_level)

    gv.pacman.ani_tick_counter = gv.pacman.ani_tick_counter + 1
    if gv.pacman.ani_tick_counter >= gv.pacman.ANI_DURATION - 1:
        gv.pacman.ani_tick_counter = 0

    gv.pacman.blit_pacman(gv.screen)

    #print(gv.score)

    pygame.display.flip()
    clock.tick(30)