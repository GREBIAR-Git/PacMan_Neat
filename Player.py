import pygame
import time
from threading import Thread
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

class PacMan:
    def __init__(self, x, y, radius):
        self.xPacMan = x
        self.yPacMan = y
        self.radiusPacMan = radius
        self.isOpen = False
        self.Alive = True
        self.t1 = Thread(target=self.ISOpen)
        self.t1.start()


    def Display(self, screen, direction):
        pygame.draw.circle(screen, YELLOW, (self.xPacMan, self.yPacMan), self.radiusPacMan)
        if(not self.isOpen):
            if(direction == "TOP"):
                pygame.draw.polygon(screen, BLACK, ((self.xPacMan,self.yPacMan),(self.xPacMan+self.radiusPacMan,self.yPacMan-self.radiusPacMan),(self.xPacMan-self.radiusPacMan,self.yPacMan-self.radiusPacMan)))
            elif (direction == "RIGHT"):
                pygame.draw.polygon(screen, BLACK, ((self.xPacMan,self.yPacMan),(self.xPacMan+self.radiusPacMan,self.yPacMan+self.radiusPacMan),(self.xPacMan+self.radiusPacMan,self.yPacMan-self.radiusPacMan)))
            elif (direction == "BOT"):
                pygame.draw.polygon(screen, BLACK, ((self.xPacMan,self.yPacMan),(self.xPacMan+self.radiusPacMan,self.yPacMan+self.radiusPacMan),(self.xPacMan-self.radiusPacMan,self.yPacMan+self.radiusPacMan))) 
            elif (direction == "LEFT"):
                pygame.draw.polygon(screen, BLACK, ((self.xPacMan,self.yPacMan),(self.xPacMan-self.radiusPacMan,self.yPacMan+self.radiusPacMan),(self.xPacMan-self.radiusPacMan,self.yPacMan-self.radiusPacMan)))
    
    def ISOpen(self):
        while(self.Alive):   
            self.isOpen = not self.isOpen
            time.sleep(0.3)