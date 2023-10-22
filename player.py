import pygame
import time
from threading import Thread

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)

class PacMan:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.isOpen = False
        self.isAlive = True
        self.direction = ""
        self.t1 = Thread(target=self.ISOpen)

        self.t1.start()
        self.stop = False
        self.step = 0.3
        self.big = False

    def EndsFrightened(self, rg, pg, bg, og):
        time.sleep(10)
        rgF = self.EndFrightened(rg) 
        pgF = self.EndFrightened(pg)
        bgF = self.EndFrightened(bg)
        ogF = self.EndFrightened(og)
        if(rgF and pgF and bgF and ogF):
            self.big = False

    def EndFrightened(self,ghost):
        if(not ghost.prevState==4 and not ghost.prevState==2):
            ghost.state = ghost.prevState
            return True
        return False

    def SetDirection(self, direction):
        self.direction = direction

    def Debug(self, screen, Map):
        x = int((self.x)/(Map.XSizeCell())) 
        y = int((self.y)/(Map.YSizeCell()))
        x2 = int((self.x-10)/(Map.XSizeCell())) 
        y2 = int((self.y)/(Map.YSizeCell()))

        x4 = int((self.x)/(Map.XSizeCell())) 
        y4 = int((self.y-10)/(Map.YSizeCell()))
        
        x3 = int((self.x+10)/(Map.XSizeCell())) 
        y3 = int((self.y)/(Map.YSizeCell()))

        x5 = int((self.x)/(Map.XSizeCell())) 
        y5 = int((self.y+10)/(Map.YSizeCell()))
        x1 = round((self.x-10)/(Map.XSizeCell())) 
        y1 = round((self.y-10)/(Map.YSizeCell()))

        if(self.direction == "TOP"):
            pygame.draw.rect(screen, BLUE, (Map.XSizeCell()*(x5), Map.YSizeCell()*(y5), Map.XSizeCell(), Map.YSizeCell()))
        elif (self.direction == "RIGHT"):
            pygame.draw.rect(screen, BLUE, (Map.XSizeCell()*(x2), Map.YSizeCell()*(y2), Map.XSizeCell(), Map.YSizeCell()))
        elif (self.direction == "BOT"):
            pygame.draw.rect(screen, BLUE, (Map.XSizeCell()*(x4), Map.YSizeCell()*(y4), Map.XSizeCell(), Map.YSizeCell()))
        elif (self.direction == "LEFT"):
            pygame.draw.rect(screen, BLUE, (Map.XSizeCell()*(x3), Map.YSizeCell()*(y3), Map.XSizeCell(), Map.YSizeCell()))
        pygame.draw.rect(screen, RED, (Map.XSizeCell()*(x)+4, Map.YSizeCell()*(y)+4, Map.XSizeCell()-4, Map.YSizeCell()-4))
        #pygame.draw.rect(screen, (255, 255, 255), (Map.XSizeCell()*(x1)+2, Map.YSizeCell()*(y1)+2, Map.XSizeCell()-2, Map.YSizeCell()-2))


    def Display(self, screen, Map):
        #self.Debug(screen, Map)
        radius = self.radius
        if(self.big):
            radius += 2
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), radius)
        if(not self.isOpen):
            if(self.direction == "TOP"):
                self.DrawMouth(screen, radius, -radius, -radius ,-radius)
            elif (self.direction == "RIGHT"):
                self.DrawMouth(screen, radius, radius, radius ,-radius)
            elif (self.direction == "BOT"):
                self.DrawMouth(screen, radius, radius, -radius ,radius)
            elif (self.direction == "LEFT"):
                self.DrawMouth(screen, -radius, radius, -radius ,-radius)
    
    def DrawMouth(self,screen, x1, y1, x2 ,y2):
        pygame.draw.polygon(screen, BLACK, ((self.x,self.y),(self.x+x1,self.y+y1),(self.x+x2,self.y+y2)))

    def CanPass(self, direction, Map):
        size = 10
        if(direction == "TOP"):
            x1 = int((self.x)/(Map.XSizeCell()))
            x2 = int((self.x+size)/(Map.XSizeCell())) 
            x3 = int((self.x-size)/(Map.XSizeCell()))
            y1 = int((self.y+size)/(Map.YSizeCell())) 
            if(x1>=25 or Map.matrix[y1-1, x1] == 1 or x2>=25 or Map.matrix[y1-1, x2] == 1 or x3>=25 or Map.matrix[y1-1, x3] == 1):
                return False
            else:
                return True
        elif (direction == "BOT"):
            x1 = int((self.x)/(Map.XSizeCell()))
            x2 = int((self.x+size)/(Map.XSizeCell())) 
            x3 = int((self.x-size)/(Map.XSizeCell()))
            y1 = int((self.y-size)/(Map.YSizeCell())) 
            if(y1+1<25 and (x1>=25 or Map.matrix[y1+1, x1] == 1 or x2>=25 or Map.matrix[y1+1, x2] == 1 or x3>=25 or Map.matrix[y1+1, x3] == 1)):
                return False
            else:
                return True
        elif (direction == "RIGHT"):
            x1 = int((self.x-size)/(Map.XSizeCell())) 
            y2 = int((self.y+size)/(Map.YSizeCell())) 
            y3 = int((self.y-size)/(Map.YSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell()))
            if(x1+1<25 and (Map.matrix[y1, x1+1] == 1 or Map.matrix[y2, x1+1] == 1 or Map.matrix[y3, x1+1] == 1)):
                return False
            else:
                return True
        elif (direction == "LEFT"):
            x1 = int((self.x+size)/(Map.XSizeCell())) 
            y2 = int((self.y+size)/(Map.YSizeCell())) 
            y3 = int((self.y-size)/(Map.YSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell()))
            if(Map.matrix[y1, x1-1] == 1 or Map.matrix[y2, x1-1] == 1 or Map.matrix[y3, x1-1] == 1):
                return False
            else:
                return True

    def Run(self, direction,rg, pg, bg, og, Map):
        if(not self.stop):
            if(self.CanPass(direction, Map)):
                self.direction = direction
            self.stop = not self.CanPass(self.direction, Map)
            if(not self.stop):
                if(self.direction == "TOP"):
                    self.y-=self.step
                    if(self.y < (0-self.radius)):
                        self.y = Map.height
                elif (self.direction == "RIGHT"):
                    self.x+=self.step
                    if(self.x > (Map.width+self.radius)):
                        self.x = 0
                elif (self.direction == "BOT"):
                    self.y+=self.step
                    if(self.y > (Map.height+self.radius)):
                        self.y = 0
                elif (self.direction == "LEFT"):
                    self.x-=self.step
                    if(self.x < (0-self.radius)):
                        self.x = Map.width
            x = int((self.x)/(Map.width/25)) 
            y = int((self.y)/(Map.height/25))
            if(not x==25 and not y==25):
                if(Map.matrix[y, x]==0):
                    Map.matrix[y, x] = 3
                    Map.score+=1
                elif(Map.matrix[y, x]==4):
                    Map.matrix[y, x] = 5
                    Map.score+=1
                elif(Map.matrix[y, x]==6):
                    Map.matrix[y, x] = 3
                    Map.score+=1
                    #if(not rg.isHome):
                    self.MegaState(rg)
                   
                    #if(not pg.isHome):
                    self.MegaState(pg)
                    #if(not bg.isHome):
                    self.MegaState(bg)
                    #if(not og.isHome):
                    self.MegaState(og)
                    self.big = True
                    self.t2 = Thread(target=self.EndsFrightened, kwargs={'rg': rg,'pg': pg,'bg': bg,'og': og})
                    self.t2.start()
    
    def MegaState(self, rg):
        if(not rg.state == 2 and not rg.state == 4):
            rg.prevState = rg.state
            rg.state = 2
            rg.Turn()

    def IsAlive(self,rg,pg,bg,og,map):
        
        if(not self.big):
            if(not (self.IsAlive1(rg.x,rg.y,map) and self.IsAlive1(pg.x,pg.y,map) and self.IsAlive1(bg.x,bg.y,map) and self.IsAlive1(og.x,og.y,map))):
                self.isAlive = False
        else:
            if(not self.IsAlive1(rg.x,rg.y,map)):
                if(rg.state == 2):
                    rg.state = 4
                elif(not rg.state == 4):
                    self.isAlive = False
            if(not self.IsAlive1(pg.x,pg.y,map)):
                if(pg.state == 2):
                    pg.state = 4
                elif(not pg.state == 4):
                    self.isAlive = False
            if(not self.IsAlive1(bg.x,bg.y,map)):
                if(bg.state == 2):
                    bg.state = 4
                elif(not bg.state == 4):
                    self.isAlive = False
            if(not self.IsAlive1(og.x,og.y,map)):
                if(og.state == 2):
                    og.state = 4
                elif(not og.state == 4):
                    self.isAlive = False

        return self.isAlive

    def IsAlive1(self,x1,y1,map):
        px = int((self.x)/(map.XSizeCell())) 
        py = int((self.y)/(map.YSizeCell()))
        gx = int((x1)/(map.XSizeCell())) 
        gy = int((y1)/(map.YSizeCell()))
        if(gx==px and gy == py):
            return False
        return True

    def ISOpen(self):
        while(self.isAlive):   
            self.isOpen = not self.isOpen
            time.sleep(0.3)