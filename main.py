import pygame
import sys
import global_variables as gv
import pacman as pm
import animation as ani
import ghost as gh
import time


pygame.init()
pygame.font.init()

# constants
reached_second_level = False
reached_third_level = False
in_first_level = True
in_menu = True

x = 0

# generating a screen
gv.screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel's PacMan")

# counter for the pacman animation
gv.pacman_tick_counter = 0

# create pacman and ghost objects
gv.pacman = pm.Pacman([480, 200])
ghost_starting_positions = [[30, 30], [950, 30], [30, 450], [950, 450]]
for ghost_type in range(4):
    gv.ghosts.append(gh.Ghost(ghost_type, ghost_starting_positions[ghost_type]))

# relevant for the game loop
ani.read_pellet_images()
clock = pygame.time.Clock()


flash_text_counter = 0
while in_menu:
    gv.screen.fill((0, 0, 0))
    if flash_text_counter == 0:
        flash_text_counter = 1
    else:
        flash_text_counter = 0
        ani.draw_hint(gv.screen)  # showing the text
    # ordinary pygame loop which enables closing
    gv.keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # if space pressed than the game starts
    if gv.keys_pressed[pygame.K_SPACE]:
        in_menu = False

    ani.draw_heading(gv.screen)  # showing the text
    pygame.display.flip()
    clock.tick(5)

ran_once = False
while not gv.game_over:
    # event handling
    gv.keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic
    gv.pacman.pacman_event_handler(gv.keys_pressed)
    gv.pacman.move()
    if ran_once:
        gv.pacman.test_ghost_collision()
    for ghost in gv.ghosts:
        ghost.move()

    # switching levels
    if gv.score == 7 and in_first_level:  # changes to 2nd level
        gv.pacman.position[0] = 480  # reset pacman position
        gv.pacman.position[1] = 200
        in_first_level = False
        gv.current_level = 1
        gv.score = 0
        reached_second_level = True
        x = 1  # new level path
        for ghost in gv.ghosts:
            ghost.position = ghost_starting_positions

    elif gv.score == 422 and reached_second_level:  # changes to 3rd level
        gv.pacman.position[0] = 480  # reset pacman position
        gv.pacman.position[1] = 200
        gv.current_level = 2
        gv.score = 0
        reached_third_level = True
        reached_second_level = False
        x = 2  # new level path
        gv.x = 480  # reset pacman position
        gv.y = 200

    elif gv.score == 340 and reached_third_level:
        gv.game_over = True


    # animation
    ani.blit_level(gv.LEVEL_PATHS[x], gv.screen)
    ani.draw_pellets(gv.screen, gv.current_level)
    ani.draw_score(gv.screen)

    gv.pacman.ani_tick_counter = gv.pacman.ani_tick_counter + 1
    if gv.pacman.ani_tick_counter >= gv.pacman.ANI_DURATION - 1:
        gv.pacman.ani_tick_counter = 0

    gv.pacman.blit_pacman(gv.screen)
    for ghost in gv.ghosts:
        ghost.blit_ghost(gv.screen)

    pygame.display.flip()
    clock.tick(30)
    ran_once = True

