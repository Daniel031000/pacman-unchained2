import pygame

screensize = (1000, 500)
keys_pressed = []
pacman = 0

pixel_colour = []
level_pellets = []
current_level = 0
score = 0
strip_starting_point = []
screen = 0
active_pixel = []



def eating_pellets(player_position, keys_pressed, movement_speed):
    pellet_eatable = False
    size = 25
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:  # left
        strip_starting_point = [player_position[0] - movement_speed, player_position[1]]  # starting point
        for i in range(0, 25):  # test all 25 pixels
            active_pixel = [strip_starting_point[0], strip_starting_point[1] + i]  # find pixel pacman
            print(active_pixel)
            if pygame.display.get_surface().get_at(active_pixel) == (255, 242, 0):  # testen, ob dieser gleicg blau ist
                pellet_eatable = True
    elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:  # right
        strip_starting_point = [player_position[0] + movement_speed, player_position[1]]
        for i in range(0, 25):
            active_pixel = [strip_starting_point[0] + size, strip_starting_point[1] + i]
            if pygame.display.get_surface().get_at(active_pixel) == (255, 242, 0):
                pellet_eatable = True
    elif keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:  # Up
        strip_starting_point = [player_position[0], player_position[1] - movement_speed]
        for i in range(0, 25):
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            if pygame.display.get_surface().get_at(active_pixel) == (255, 242, 0):
                pellet_eatable = True
    elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:  # Down
        strip_starting_point = [player_position[0], player_position[1] + size]
        for i in range(0, 25):
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            if pygame.display.get_surface().get_at(active_pixel) == (255, 242, 0):
                pellet_eatable = True

    return pellet_eatable