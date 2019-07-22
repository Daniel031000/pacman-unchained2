import pygame

screensize = (1000, 500)
keys_pressed = []
pacman = 0


pixel_colour = []
level_pellets = []
current_level = 0


def isStripmoveable(player_position, keys_pressed, movement_speed):
    strip_is_trevirsible = True
    size = 25
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:  # left
        strip_starting_point=[player_position[0]-movement_speed,player_position[1]]  # starting point
        for i in range(5, 20):  # test all 25 pixels
            active_pixel = [strip_starting_point[0], strip_starting_point[1] + i]  # find pixel pacman
            print(active_pixel)
            if pygame.display.get_surface().get_at(active_pixel) == (63, 72, 204, 255):  # testen, ob dieser gleicg blau ist
                strip_is_trevirsible = False
    elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:  # right
        strip_starting_point = [player_position[0] + movement_speed, player_position[1]]
        for i in range(5, 20):
            active_pixel = [strip_starting_point[0], strip_starting_point[1] + i + size]
            if pygame.display.get_surface().get_at(active_pixel) == (63, 72, 204,255):
                strip_is_trevirsible = False
    elif keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:  # Up
        strip_starting_point = [player_position[0], player_position[1] - movement_speed]
        for i in range(5, 20):
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            if pygame.display.get_surface().get_at(active_pixel) == (63, 72, 204):
                strip_is_trevirsible = False
    elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:  # Down
        strip_starting_point = [player_position[0], player_position[1] + size]
        for i in range(5, 20):  # Alle 25 Pixel testen
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            if pygame.display.get_surface().get_at(active_pixel) == (63, 72, 204):
                strip_is_trevirsible = False

    return strip_is_trevirsible
'''def pixel_colour_detection(player_position, pygame_events, movement_speed):  # detecting the next upcoming colour
    size = 25
    if keys_pressed == pygame.K_LEFT:  # left
        strip_starting_point = [player_position[0] - movement_speed, player_position[1]]  # starting point
        for i in range(25):  # test all 25 pixels
            active_pixel = [strip_starting_point[0], strip_starting_point[1] + i]  # define pixel in front of pacman
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)  # get pixel colour
            return pixel_colour
    elif keys_pressed == pygame.K_RIGHT:  # right
        strip_starting_point = [player_position[0] + movement_speed, player_position[1]]
        for i in range(25):
            active_pixel = [strip_starting_point[0], strip_starting_point[1] + i + size]
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)
            return pixel_colour
    elif keys_pressed == pygame.K_UP:  # Up
        strip_starting_point = [player_position[0], player_position[1] - movement_speed]
        for i in range(25):
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)
            return pixel_colour
    elif keys_pressed == pygame.K_DOWN:  # Down
        strip_starting_point = [player_position[0], player_position[1] + size]
        for i in range(25):
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)
            return pixel_colour'''


