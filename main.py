import pygame
import sys
import global_variables as gv
import pacman as gl
import animation as ani

pygame.init()

# constants
BLACK = (0, 0, 0)
LEVEL_PATHS = ["Graphics/levels/level1.png", "Graphics/levels/level2.png", "Graphics/levels/level3.png"]

screen = pygame.display.set_mode(gv.screensize)

pygame.display.set_caption("Daniel's PacMan")
clock = pygame.time.Clock()

# instantiate pacman class
gv.pacman = gl.Pacman()
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
    ani.blit_level(LEVEL_PATHS[0], screen)
    ani.draw_pellets(screen, gv.current_level)

    gv.pacman.ani_tick_counter = gv.pacman.ani_tick_counter + 1
    if gv.pacman.ani_tick_counter >= gv.pacman.ANI_DURATION - 1:
        gv.pacman.ani_tick_counter = 0

    gv.pacman.blit_pacman(screen)

    pygame.display.flip()
    clock.tick(30)