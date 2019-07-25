<<<<<<< HEAD
# MOMS SPAGHETTIZ
=======

>>>>>>> ca739dc8f04a64049b13a5b03207f8080bc251bd
import pygame
import sys
import global_variables as gv
import pacman as pm
import animation as ani
import ghost as gh


pygame.init()

# constants
BLACK = (0, 0, 0)
reached_second_level = False
reached_third_level = False
in_first_level = True

x = 0

# generating a screen
gv.screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel's PacMan")
gv.screen.fill(BLACK)

# counter for the pacman animation
gv.pacman_tick_counter = 0

# create pacman and ghost objects
gv.pacman = pm.Pacman()
ghost_starting_positions = [[950, 450], [950, 450], [950, 450], [950, 450]]
for ghost_type in range(4):
    gv.ghosts.append(gh.Ghost(ghost_type, ghost_starting_positions[ghost_type]))   # ghost_type

# relevant for the game loop
ani.read_pellet_images()
clock = pygame.time.Clock()


while 1:
    '''gv.screen.fill(BLACK)

    if gv.keys_pressed[pygame.K_SPACE]:
        gameRunning = True
        while gameRunning:   # event loop'''

    gv.keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic loop
    gv.pacman.pacman_event_handler(gv.keys_pressed)
    gv.pacman.move()
    for ghost in gv.ghosts:
        ghost.move()


    # animation
    if gv.score == 594 and in_first_level:  # changes to 2nd level
        gv.pacman.position[0] = 480  # reset pacman position
        gv.pacman.position[1] = 200
        in_first_level = False
        gv.current_level = 1
        gv.score = 0
        reached_second_level = True
        x = 1  # new level path

    elif gv.score == 422 and reached_second_level:  # changes to 3rd level
        gv.pacman.position[0] = 480  # reset pacman position
        gv.pacman.position[1] = 200
        gv.current_level = 2
        reached_third_level = True
        x = 2  # new level path
        gv.x = 480  # reset pacman position
        gv.y = 200
    elif gv.score == 340 and reached_third_level:
        pass

    ani.blit_level(gv.LEVEL_PATHS[x], gv.screen)
    ani.draw_pellets(gv.screen, gv.current_level)


    gv.pacman.ani_tick_counter = gv.pacman.ani_tick_counter + 1
    if gv.pacman.ani_tick_counter >= gv.pacman.ANI_DURATION - 1:
        gv.pacman.ani_tick_counter = 0

    gv.pacman.blit_pacman(gv.screen)
    for ghost in gv.ghosts:
        ghost.blit_ghost(gv.screen)



    pygame.display.flip()
    clock.tick(30)