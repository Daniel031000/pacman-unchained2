import pygame
import global_variables as gv
import pellet

RED = (255, 0, 0)
PELLET_IMAGE_PATHS = ["Graphics/levels/level1_pellets.png", "Graphics/levels/level2_pellets.png", "Graphics/levels/level3_pellets.png"]
pellet_coordinates_array = []


def read_pellet_images():
    for i in range(3):
        gv.level_pellets.append([])
        pellet_image = pygame.image.load(PELLET_IMAGE_PATHS[i])
        pellets_coordinates = []
        for x in range(gv.screensize[0]):
            for y in range(gv.screensize[1] - 1):
                active_pixel = pellet_image.get_at([x, y])
                if active_pixel == RED:
                    gv.level_pellets[i].append(pellet.Pellet([x, y]))


def draw_pellets(surface, current_level):
    for pellet in gv.level_pellets[current_level]:
        pellet.draw_pellet(surface)


# draws the level
def blit_level(path, surface):
    level_image = pygame.image.load(path)
    surface.blit(level_image, level_image.get_rect())

# building the portal

def portal(position):
    if position[0] > 950:
        position = [20, 257]
    elif position[0] < 50:
        position = [993, 257]
    return position


