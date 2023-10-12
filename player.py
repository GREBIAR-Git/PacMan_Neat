import pygame
import time
from threading import Thread

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

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
        self.t1 = Thread(target=self.ISOpen)
        self.t1.start()
        self.stop = False
        self.step = 0.3

    def Debug(self, screen, Map):
        x = int((self.xPacMan)/(Map.XSizeCell())) 
        y = int((self.yPacMan)/(Map.YSizeCell()))
        x2 = int((self.xPacMan-10)/(Map.XSizeCell())) 
        y2 = int((self.yPacMan)/(Map.YSizeCell()))

        x4 = int((self.xPacMan)/(Map.XSizeCell())) 
        y4 = int((self.yPacMan-10)/(Map.YSizeCell()))
        
        x3 = int((self.xPacMan+10)/(Map.XSizeCell())) 
        y3 = int((self.yPacMan)/(Map.YSizeCell()))

        x5 = int((self.xPacMan)/(Map.XSizeCell())) 
        y5 = int((self.yPacMan+10)/(Map.YSizeCell()))
        x1 = round((self.xPacMan-10)/(Map.XSizeCell())) 
        y1 = round((self.yPacMan-10)/(Map.YSizeCell()))

        if(self.direction == "TOP"):
            pygame.draw.rect(screen, (0, 0, 255), (Map.XSizeCell()*(x5), Map.YSizeCell()*(y5), Map.XSizeCell(), Map.YSizeCell()))
        elif (self.direction == "RIGHT"):
            pygame.draw.rect(screen, (0, 0, 255), (Map.XSizeCell()*(x2), Map.YSizeCell()*(y2), Map.XSizeCell(), Map.YSizeCell()))
        elif (self.direction == "BOT"):
            pygame.draw.rect(screen, (0, 0, 255), (Map.XSizeCell()*(x4), Map.YSizeCell()*(y4), Map.XSizeCell(), Map.YSizeCell()))
        elif (self.direction == "LEFT"):
            pygame.draw.rect(screen, (0, 0, 255), (Map.XSizeCell()*(x3), Map.YSizeCell()*(y3), Map.XSizeCell(), Map.YSizeCell()))
        pygame.draw.rect(screen, (255, 0, 0), (Map.XSizeCell()*(x)+4, Map.YSizeCell()*(y)+4, Map.XSizeCell()-4, Map.YSizeCell()-4))
        #pygame.draw.rect(screen, (255, 255, 255), (Map.XSizeCell()*(x1)+2, Map.YSizeCell()*(y1)+2, Map.XSizeCell()-2, Map.YSizeCell()-2))


    def Display(self, screen, Map):
        #self.Debug(screen, Map)
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

    def CanPass(self, direction, Map):
        size = 10
        if(direction == "TOP"):
            x1 = int((self.xPacMan)/(Map.XSizeCell()))
            x2 = int((self.xPacMan+size)/(Map.XSizeCell())) 
            x3 = int((self.xPacMan-size)/(Map.XSizeCell()))
            y1 = int((self.yPacMan+size)/(Map.YSizeCell())) 
            if(x1>=25 or Map.matrix[y1-1, x1] == 1 or x2>=25 or Map.matrix[y1-1, x2] == 1 or x3>=25 or Map.matrix[y1-1, x3] == 1):
                return False
            else:
                return True
        elif (direction == "BOT"):
            x1 = int((self.xPacMan)/(Map.XSizeCell()))
            x2 = int((self.xPacMan+size)/(Map.XSizeCell())) 
            x3 = int((self.xPacMan-size)/(Map.XSizeCell()))
            y1 = int((self.yPacMan-size)/(Map.YSizeCell())) 
            if(y1+1<25 and (x1>=25 or Map.matrix[y1+1, x1] == 1 or x2>=25 or Map.matrix[y1+1, x2] == 1 or x3>=25 or Map.matrix[y1+1, x3] == 1)):
                return False
            else:
                return True
        elif (direction == "RIGHT"):
            x1 = int((self.xPacMan-size)/(Map.XSizeCell())) 
            y2 = int((self.yPacMan+size)/(Map.YSizeCell())) 
            y3 = int((self.yPacMan-size)/(Map.YSizeCell()))
            y1 = int((self.yPacMan)/(Map.YSizeCell()))
            if(x1+1<25 and (Map.matrix[y1, x1+1] == 1 or Map.matrix[y2, x1+1] == 1 or Map.matrix[y3, x1+1] == 1)):
                return False
            else:
                return True
        elif (direction == "LEFT"):
            x1 = int((self.xPacMan+size)/(Map.XSizeCell())) 
            y2 = int((self.yPacMan+size)/(Map.YSizeCell())) 
            y3 = int((self.yPacMan-size)/(Map.YSizeCell()))
            y1 = int((self.yPacMan)/(Map.YSizeCell()))
            if(Map.matrix[y1, x1-1] == 1 or Map.matrix[y2, x1-1] == 1 or Map.matrix[y3, x1-1] == 1):
                return False
            else:
                return True

    def Run(self, direction, Map):
        if(not self.stop):
            if(self.CanPass(direction, Map)):
                self.direction = direction
            self.stop = not self.CanPass(self.direction, Map)
            if(self.direction == "TOP"):
                self.yPacMan-=self.step
                if(self.yPacMan < (0-self.radius)):
                    self.yPacMan = Map.height
            elif (self.direction == "RIGHT"):
                self.xPacMan+=self.step
                if(self.xPacMan > (Map.width+self.radius)):
                    self.xPacMan = 0
            elif (self.direction == "BOT"):
                self.yPacMan+=self.step
                if(self.yPacMan > (Map.height+self.radius)):
                    self.yPacMan = 0
            elif (self.direction == "LEFT"):
                self.xPacMan-=self.step
                if(self.xPacMan < (0-self.radius)):
                    self.xPacMan = Map.width
            x = int((self.xPacMan)/(Map.width/25)) 
            y = int((self.yPacMan)/(Map.height/25))
            if(not x==25 and not y==25 and Map.matrix[y, x]==0):
                Map.matrix[y, x] = 3
                Map.score+=1

    def ISOpen(self):
        while(self.Alive):   
            self.isOpen = not self.isOpen
            time.sleep(0.3)