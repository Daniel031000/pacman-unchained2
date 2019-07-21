import pygame

screensize = (1000, 500)
keys_pressed = []
pacman = 0
pixel_colour = []


def pixel_colour_detection(player_position, pygame_events, movement_speed):  # detecting the next upcoming colour
    size = 25
    if pygame_events == pygame.K_LEFT:  # left
        strip_starting_point = [player_position[0] - movement_speed, player_position[1]]  # starting point
        for i in range (25):  # test all 25 pixels
            active_pixel = [strip_starting_point[0], strip_starting_point[1] + i]  # define pixel in front of pacman
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)  # get pixel colour
    elif pygame_events == pygame.K_RIGHT:  # right
        strip_starting_point = [player_position[0] + movement_speed, player_position[1]]
        for i in range(25):
            active_pixel = [strip_starting_point[0], strip_starting_point[1] + i + size]
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)
    elif pygame_events == pygame.K_UP:  # Up
        strip_starting_point = [player_position[0], player_position[1] - movement_speed]
        for i in range(25):
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)
    elif pygame_events == pygame.K_DOWN:  # Down
        strip_starting_point = [player_position[0], player_position[1] + size]
        for i in range(25):
            active_pixel = [strip_starting_point[0] + i, strip_starting_point[1]]
            pixel_colour = pygame.display.get_surface().get_at(active_pixel)
    return pixel_colour
