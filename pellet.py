import pygame


class Pellet:
    def __init__(self, position):
        self.position = position  # position
        self.color = (255, 242, 0)  # colour yellow
        self.rect = (self.position[0], self.position[1], 2, 2)  # rectangle around the pellet (important for the
                                                                # collision with pacman)
    # draws the pellet in yellow
    def draw_pellet(self, surface):
        self.rect = (self.position[0], self.position[1], 2, 2)
        pygame.draw.rect(surface, self.color, self.rect, 0)  # 0 -> filled with yellow








