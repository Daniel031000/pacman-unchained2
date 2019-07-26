import pygame
import global_variables as gv


class Pellet:
    def __init__(self, position):
        self.position = position
        self.color = (255, 242, 0)
        self.rect = (self.position[0], self.position[1], 2, 2)

    def __str__(self):
        return "<Pellet, c: " + str(self.color) + "; p:" + str(self.position)

    def draw_pellet(self, surface):
        self.rect = (self.position[0], self.position[1], 2, 2)
        pygame.draw.rect(surface, self.color, self.rect, 0)  # 0 -> filled








