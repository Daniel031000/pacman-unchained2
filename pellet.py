import pygame
import global_variables as gv


class Pellet:
    def __init__(self, position):
        self.position = position
        self.color = (255, 242, 0)

    def __str__(self):
        return "<Pellet, c: " + str(self.color) + "; p:" + str(self.position)

    def draw_pellet(self, surface):
        pellet_rect = (self.position[0], self.position[1], 2, 2)
        pygame.draw.rect(surface, self.color, pellet_rect, 0)  # 0 -> filled

    '''def disappear(self, screen, player_position_x, player_position_y, height, lenght):
        pygame.draw.rect(screen,(0, 0, 0), (player_position_x, player_position_y, lenght, height))'''



