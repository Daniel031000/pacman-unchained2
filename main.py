import pygame
import sys
import global_variables as gv
import game_logic as gl
import animation as ani
pygame.init()

BLACK = (0, 0, 0)
LEVEL_PATHS = ["Graphics/levels/level1.png", "Graphics/levels/level2.png", "Graphics/levels/level3.png"]

screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel`s PacMan")
clock = pygame.time.Clock()

# call pay_man
pacman = gl.pacman()




while 1:
    # event loop
    gv.pygame_events = pygame.event
    
    for event in gv.pygame_events:
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic loop
    pacman.up()
    print(gv.pacman_position)

    # animation
    ani.blit_level(LEVEL_PATHS[0], screen)

    gv.pacman_ani_counter = gv.pacman_ani_counter + 1
    if gv.pacman_ani_counter >= 5:
        gv.pacman_ani_counter = 0

#    ani.blit_player(screen)

    pygame.display.flip()
    clock.tick(30)