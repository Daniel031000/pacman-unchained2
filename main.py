import pygame
import sys
import global_variables as gv
import pacman as pm
import animation as ani
import ghost as gh

# initialize pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# game logic variables
reached_second_level = False
reached_third_level = False
in_first_level = True
in_menu = True
win = False
ran_once = False
x = 0

# animation variables
flash_text_counter = 0
gv.pacman_tick_counter = 0

# generating a screen
gv.screen = pygame.display.set_mode(gv.screensize)
pygame.display.set_caption("Daniel's PacMan")

# create pacman and ghost objects
gv.pacman = pm.Pacman([480, 200])
ghost_starting_positions = [[30, 30], [950, 30], [30, 450], [950, 450]]
ghost_second_level_positions = [[30, 30], [950, 30], [30, 450], [950, 450]]
ghost_third_level_positions = [[30, 30], [950, 30], [30, 450], [950, 450]]
for ghost_type in range(4):
    gv.ghosts.append(gh.Ghost(ghost_type, ghost_starting_positions[ghost_type]))

# create pellet lists
ani.read_pellet_images()

# menu loop
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

# main game loop
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
    if gv.score == 587 and in_first_level:  # changes to 2nd level
        gv.pacman.position[0] = 480  # reset pacman position
        gv.pacman.position[1] = 200
        in_first_level = False
        gv.current_level = 1
        gv.score = 0
        reached_second_level = True
        x = 1  # new level path
        for j in range(4):  # reset the position of the ghosts
            gv.ghosts[j].position = ghost_second_level_positions[j]

    # changes to 3rd level
    elif gv.score == 422 and reached_second_level:
        gv.pacman.position[0] = 480  # reset pacman position
        gv.pacman.position[1] = 200
        gv.current_level = 2
        gv.score = 0
        reached_third_level = True
        reached_second_level = False
        x = 2  # new level path
        for j in range(4):  # reset the position of the ghosts
            gv.ghosts[j].position = ghost_second_level_positions[j]

    elif gv.score == 340 and reached_third_level:
        win = True

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

    # the end screen if you win (same system as in menu loop)
    while win:
        gv.screen.fill((0, 0, 0))
        if flash_text_counter == 0:
            flash_text_counter = 1
        else:
            flash_text_counter = 0
            ani.draw_hint2(gv.screen)
        gv.keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if gv.keys_pressed[pygame.K_SPACE]:
            gv.game_over = True
            win = False
        ani.draw_win(gv.screen)  # showing the text
        pygame.display.flip()
        clock.tick(5)

    # the end screen if you lose (same system as in menu loop)
    while gv.lose:
        gv.screen.fill((0, 0, 0))
        if flash_text_counter == 0:
            flash_text_counter = 1
        else:
            flash_text_counter = 0
            ani.draw_hint2(gv.screen)

        gv.keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if gv.keys_pressed[pygame.K_SPACE]:
            gv.game_over = True
            gv.lose = False
        ani.draw_lost(gv.screen)  # showing the text
        pygame.display.flip()
        clock.tick(5)
