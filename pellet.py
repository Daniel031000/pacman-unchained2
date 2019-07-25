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


def eating_pellet():  # if the pacman eats the pellet it will be deleted from the list and disappear from the screen
    counter = 0
    while counter < len(gv.level_pellets[gv.current_level]):
        every_single_pellet = gv.level_pellets[gv.current_level][counter]
        if gv.pacman.rect.contains(every_single_pellet.rect):
            gv.score = gv.score + 1
            del gv.level_pellets[gv.current_level][counter]
        counter = counter + 1





