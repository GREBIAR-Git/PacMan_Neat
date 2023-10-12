import pygame

class Ghost:
    def __init__(self, x, y, color):   
        self.xGhost = x
        self.yGhost = y
        self.color = color

    def Display(self, screen):
        pygame.draw.circle(screen, self.color, (self.xGhost, self.yGhost), 10)
