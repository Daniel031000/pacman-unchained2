import pygame
import global_variables as gv
import pellet

# variables used for clarity
RED = (255, 0, 0)  # colour for the red dots
PELLET_IMAGE_PATHS = ["graphics/levels/level_1_pellets.png", "graphics/levels/level_2_pellets.png",
                      "graphics/levels/level_3_pellets.png"]
pellet_coordinates_array = []  # coordinates of the red dots


# The pellets are generated using a second image
# This image contains red pixels at the locations that the pellets should be
def read_pellet_images():  # checking the second level for red dots
    for i in range(3):
        gv.level_pellets.append([])
        pellet_image = pygame.image.load(PELLET_IMAGE_PATHS[i])  # loading each path
        for x in range(gv.screensize[0]):
            for y in range(gv.screensize[1] - 1):
                active_pixel = pellet_image.get_at([x, y])
                if active_pixel == RED:  # saving a coordinate when there is a red dot (filled yellow in pellet.draw)
                    gv.level_pellets[i].append(pellet.Pellet([x, y]))


# draws all pellets to the screen (not draw)
def draw_pellets(surface, current_level):
    for pellet in gv.level_pellets[current_level]:
        pellet.draw_pellet(surface)


# draws the level
def blit_level(path, surface):
    level_image = pygame.image.load(path)
    surface.blit(level_image, level_image.get_rect())


# draws the score in the top right corner
def draw_score(surface):
    score_font = pygame.font.SysFont(None, 24)
    text = score_font.render("Score: " + str(gv.score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.y = 5
    surface.blit(text, text_rect)


# text at the start
def draw_heading(surface):
    heading_font = pygame.font.SysFont(None, 100)
    text = heading_font.render("Pacman Unchained", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 160
    text_rect.y = 20
    surface.blit(text, text_rect)


# flashing text at the start
def draw_hint(surface):
    heading_font = pygame.font.SysFont(None, 50)
    text = heading_font.render("Hit Space to Start", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 340
    text_rect.y = 300
    surface.blit(text, text_rect)


def draw_win(surface):
    heading_font = pygame.font.SysFont(None, 50)
    text = heading_font.render("Congratulations! You won!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 250
    text_rect.y = 20
    surface.blit(text, text_rect)


def draw_lost(surface):
    heading_font = pygame.font.SysFont(None, 50)
    text = heading_font.render("GAME OVER! You lost!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 250
    text_rect.y = 20
    surface.blit(text, text_rect)


def draw_hint2(surface):
    heading_font = pygame.font.SysFont(None, 50)
    text = heading_font.render("Hit Space to End", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = 340
    text_rect.y = 300
    surface.blit(text, text_rect)