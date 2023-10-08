import pygame
import time
import math
from threading import Thread

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
step = 0.5

class PacMan:
    def __init__(self, x, y, radius):
        self.xPacMan = x
        self.yPacMan = y
        self.x = 1
        self.y = 1
        self.radius = radius
        self.isOpen = False
        self.Alive = True
        self.direction = "RIGHT"
        self.nextDirection = "RIGHT"
        self.t1 = Thread(target=self.ISOpen)
        self.t1.start()
        self.stop = False

    def Display(self, screen):
        #print("x="+ (str)(self.xPacMan)+ "; y=" + (str)(self.yPacMan))
        pygame.draw.circle(screen, YELLOW, (self.xPacMan, self.yPacMan), self.radius)
        if(not self.isOpen):
            if(self.direction == "TOP"):
                self.DrawMouth(screen, self.radius, -self.radius, -self.radius ,-self.radius)
            elif (self.direction == "RIGHT"):
                self.DrawMouth(screen, self.radius, self.radius, self.radius ,-self.radius)
            elif (self.direction == "BOT"):
                self.DrawMouth(screen, self.radius, self.radius, -self.radius ,self.radius)
            elif (self.direction == "LEFT"):
                self.DrawMouth(screen, -self.radius, self.radius, -self.radius ,-self.radius)
    
    def DrawMouth(self,screen, x1, y1, x2 ,y2):
        pygame.draw.polygon(screen, BLACK, ((self.xPacMan,self.yPacMan),(self.xPacMan+x1,self.yPacMan+y1),(self.xPacMan+x2,self.yPacMan+y2)))

    def Run(self, direction, Map):
        if(not self.stop):
            self.direction = direction
            if(self.direction == "TOP"):
                self.yPacMan-=step
                if(self.yPacMan < (0-self.radius)):
                    self.yPacMan = Map.height
            elif (self.direction == "RIGHT"):
                self.xPacMan+=step
                if(self.xPacMan > (Map.width+self.radius)):
                    self.xPacMan = 0
            elif (self.direction == "BOT"):
                self.yPacMan+=step
                if(self.yPacMan > (Map.height+self.radius)):
                    self.yPacMan = 0
            elif (self.direction == "LEFT"):
                self.xPacMan-=step
                if(self.xPacMan < (0-self.radius)):
                    self.xPacMan = Map.width
            x = int((self.xPacMan)/(Map.width/25)) 
            y = int((self.yPacMan)/(Map.height/25))
            if(not x==25 and not y==25 and Map.matrix[y, x]==0):
                Map.matrix[y, x] = 3
                Map.score+=1
        
        if(self.direction == "TOP"):
            x1 = int((self.xPacMan)/(Map.width/25)) 
            y1 = int((self.yPacMan+10)/(Map.height/25)) 
            if(y1-1>=0 and Map.matrix[y1-1, x1] == 1):
                self.stop = True
            else:
                self.stop = False 
        elif (self.direction == "RIGHT"):
            x1 = int((self.xPacMan-10)/(Map.width/25)) 
            y1 = int((self.yPacMan)/(Map.height/25)) 
            if(x1+1<25 and Map.matrix[y1, x1+1] == 1):
                self.stop = True
        elif (self.direction == "BOT"):
            x1 = int((self.xPacMan)/(Map.width/25)) 
            y1 = int((self.yPacMan-10)/(Map.height/25)) 
            if(y1+1<25 and Map.matrix[y1+1, x1] == 1):
                self.stop = True
        elif (self.direction == "LEFT"):
            x1 = int((self.xPacMan+10)/(Map.width/25)) 
            y1 = int((self.yPacMan)/(Map.height/25)) 
            if(x1-1>=0 and Map.matrix[y1, x1-1] == 1):
                self.stop = True

    def ISOpen(self):
        while(self.Alive):   
            self.isOpen = not self.isOpen
            time.sleep(0.3)