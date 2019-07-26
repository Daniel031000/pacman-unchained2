import pygame
import global_variables as gv
import pellet

# constants
RED = (255, 0, 0)
PELLET_IMAGE_PATHS = ["graphics/levels/level_1_pellets.png", "graphics/levels/level_2_pellets.png",
                      "graphics/levels/level_3_pellets.png"]
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


def draw_score(surface):
    score_font = pygame.font.SysFont(None, 24)
    text = score_font.render("Score: " + str(gv.score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.y = 5
    surface.blit(text, text_rect)


def draw_heading(surface):
    heading_font = pygame.font.SysFont(None, 100)
    text = heading_font.render("Pacman Unchained 2", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 200
    text_rect.y = 20
    surface.blit(text, text_rect)


def draw_hint(surface):
    heading_font = pygame.font.SysFont(None, 50)
    text = heading_font.render("Hit Space to Start", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 400
    text_rect.y = 300
    surface.blit(text, text_rect)
