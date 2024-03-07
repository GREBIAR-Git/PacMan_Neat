import numpy as np 
import pygame
import math

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
DarkPurple = (29, 6, 92)

class Map:
    def __init__(self, width, height):    
        self.nearX = -1000   
        self.nearY = -1000
        self.global1 = 1000
        self.matrix = np.array([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 6, 1, 2, 1, 0, 1, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 1, 0, 1, 2, 1, 6, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 4, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 4, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 4, 0, 4, 1, 2, 2, 2, 2, 2, 2, 2, 1, 4, 0, 4, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1],
            [1, 6, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 6, 1],
            [1, 0, 0, 0, 1, 4, 0, 4, 0, 0, 0, 4, 3, 4, 0, 0, 0, 4, 0, 4, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
        self.width = width
        self.height = height
        self.score = 0
        self.scoreWin = 0
        for x in range(25):
            for y in range(25):
                if(self.matrix[x,y]==0 or self.matrix[x,y]==4 or self.matrix[x,y]==6):
                    self.scoreWin += 1

    def CountHorzontalEats(self, x, y, direction):
        count = 0
        sd = direction
        while(x < 24 and x > 0 and   self.matrix[y,x+sd]!=1):
            if(self.matrix[y,x+sd]==0 or self.matrix[y,x+sd]==4):
                count+=1
            sd += direction
        return count
    
    def CountVertcalEats(self, x, y, direction):
        count = 0
        sd = direction
        while(y < 24 and y > 0 and self.matrix[y+sd,x]!=1):
            if(self.matrix[y+sd,x]==0 or self.matrix[y+sd,x]==4):
                count+=1
            sd += direction
        return count

    def CountEatsSecondLne(self,pm):
        v = []
        x1 = int((pm.x)/(self.XSizeCell())) 
        y1 = int((pm.y)/(self.YSizeCell()))
        if(x1==25 or y1 == 25):
            pass
        left = 0
        right = 0
        top = 0
        bot = 0
        x = x1-1
        while(self.matrix[y1,x]!=1):
            left += self.CountHorzontalEats(x, y1, -1)
            right += self.CountHorzontalEats(x, y1, 1)
            top += self.CountVertcalEats(x, y1, -1)
            bot += self.CountVertcalEats(x, y1, 1)
            x -= 1
        x = x1 +1
        while(self.matrix[y1,x]!=1):
            left += self.CountHorzontalEats(x, y1, -1)
            right += self.CountHorzontalEats(x, y1, 1)
            top += self.CountVertcalEats(x, y1, -1)
            bot += self.CountVertcalEats(x, y1, 1)
            x += 1
        y = y1-1
        while(self.matrix[y,x1]!=1):
            left += self.CountHorzontalEats(x1, y, -1)
            right += self.CountHorzontalEats(x1, y, 1)
            top += self.CountVertcalEats(x1, y, -1)
            bot += self.CountVertcalEats(x1, y, 1)
            y -= 1
        y = y1+1
        while(self.matrix[y,x1]!=1):
            left += self.CountHorzontalEats(x1, y, -1)
            right += self.CountHorzontalEats(x1, y, 1)
            top += self.CountVertcalEats(x1, y, -1)
            bot += self.CountVertcalEats(x1, y, 1)
            y += 1
        
        v.append(left)
        v.append(right)
        v.append(top)
        v.append(bot)
        return v


    def CountGhost(self,pm, g1, g2, g3, g4):
        countGhostTOP = False
        countGhostBOT = False
        countGhostRIGHT = False
        countGhostLEFT = False
        
        v = []
        x = pm[0]
        y1 = pm[1]
        while(True):
            y1-= 1
            if((y1==g1[1] and x == g1[0]) or (y1==g2[1] and x == g2[0])  or (y1==g3[1] and x == g3[0])  or (y1==g4[1] and x == g4[0])):
                countGhostTOP = True
            if(self.matrix[y1,x]==1):
                break
        v.append(countGhostTOP)

        x = pm[0]
        y1 = pm[1]
        while(True):
            y1+= 1
            if((y1==g1[1] and x == g1[0]) or (y1==g2[1] and x == g2[0])  or (y1==g3[1] and x == g3[0])  or (y1==g4[1] and x == g4[0])):
                countGhostBOT = True
            if(self.matrix[y1,x]==1):
                break
        v.append(countGhostBOT)

        x = pm[0]
        y1 = pm[1]
        while(True):
            x += 1
            if((y1==g1[1] and x == g1[0]) or (y1==g2[1] and x == g2[0])  or (y1==g3[1] and x == g3[0])  or (y1==g4[1] and x == g4[0])):
                countGhostRIGHT = True
            if(self.matrix[y1,x]==1):
                break
        v.append(countGhostRIGHT)

        x = pm[0]
        y1 = pm[1]
        while(True):
            x -= 1
            if((y1==g1[1] and x == g1[0]) or (y1==g2[1] and x == g2[0])  or (y1==g3[1] and x == g3[0])  or (y1==g4[1] and x == g4[0])):
                countGhostLEFT = True
            if(self.matrix[y1,x]==1):
                break
        v.append(countGhostLEFT)
        return v



    def AllWall(self):
        v = []
        for y in range(25):
            ts = y*self.XSizeCell()
            for x in range(25):
                if(self.matrix[x,y]==1):
                    v.append(x*self.XSizeCell())
                    v.append(ts)
        print(v)
        return v
    
    def AmountFoodDestination(self,pm):
        v = []
        x1 = int((pm.x)/(self.XSizeCell())) 
        y1 = int((pm.y)/(self.YSizeCell()))
        if(x1 >= 24):
            x1 = 0
        count = 0
        x = x1
        while(True):
            x-= 1
            if(self.matrix[y1,x]==1):
                if(x+1==x1):
                    count = -1
                break
            t = self.matrix[y1,x]
            if(self.matrix[y1,x]==0 or self.matrix[y1,x]==6 or self.matrix[y1,x]==4):
                count += 1
        v.append(count)

        count = 0
        x = x1
        while(True):
            x+= 1
            if(x >= 24):
                x = 0
            if(self.matrix[y1,x]==1):
                if(x-1==x1):
                    count = -1
                break
            if(self.matrix[y1,x]==0 or self.matrix[y1,x]==6 or self.matrix[y1,x]==4):
                count += 1
        v.append(count)
            
        count = 0
        y = y1
        while(True):
            y-= 1
            if(self.matrix[y,x1]==1):
                if(y+1==y1):
                    count = -1
                break
            if(self.matrix[y,x1]==0 or self.matrix[y,x1]==6 or self.matrix[y,x1]==4):
                count += 1
        v.append(count)

        count = 0
        y = y1
        while(True):
            y+= 1
            if(self.matrix[y,x1]==1):
                if(y-1==y1):
                    count = -1
                break
            if(self.matrix[y,x1]==0 or self.matrix[y,x1]==6 or self.matrix[y,x1]==4):
                count += 1
        v.append(count)
        return v
    
    def DistanceToPreferredPoint(self, x1, y1,screen):
        v = []
        x2 = -1
        y2 = -1
        e = 1000
        lr = False
        tb = False
        for y in range(25):
            for x in range(25):
                if(self.matrix[y,x]==0):
                    #print(str(x)+ " " + str(y) + " " +str(x1)+ " " + str(y1) + " "+str(self.EuclideanDistances(x,x1,y,y1)))
                    if(self.EuclideanDistances(24-x,x1,24-y,y1)<e):
                        e = self.EuclideanDistances(24-x,x1,24-y,y1)
                        x2 = x
                        y2 = y

        v.append(x2)
        v.append(y2)
        if(not screen == None):
            pygame.draw.rect(screen, BLUE, (self.XSizeCell()*(x2), self.YSizeCell()*(y2), self.XSizeCell(), self.YSizeCell()))
        return v


    def CoordinatesNearestFood(self, x1, y1,screen):
        v = []
        e = 1000
        for y in range(25):
            for x in range(25):
                if(self.matrix[y,x]==0 or self.matrix[y,x]==4):
                    if((math.fabs(x - x1) + math.fabs(y - y1)) < e):
                        e = math.fabs(x - x1) + math.fabs(y - y1)
                        self.global1 = e
                        self.nearX = x
                        self.nearY = y
        
        v.append(self.nearX - x1)
        v.append(self.nearY - y1)
        if(not screen == None):
            pygame.draw.rect(screen, BLUE, (self.XSizeCell()*(self.nearX), self.YSizeCell()*(self.nearY), self.XSizeCell(), self.YSizeCell()))

        return v

    
    def AllEats(self):
        v = []
        for y in range(25):
            ts = y*self.XSizeCell()
            for x in range(25):
                if(self.matrix[x,y]==0):
                    v.append(x*self.XSizeCell())
                    v.append(ts)
                    v.append(True)
                elif(self.matrix[x,y]==3):
                    v.append(x*self.XSizeCell())
                    v.append(ts)
                    v.append(False)
        return v

    def EuclideanDistances(self,x1,x2,y1,y2):
        return math.sqrt(math.pow(x2 - x1,2)+math.pow(y2 - y1,2))

    def XSizeCell(self):
        return self.width/25
    
    def YSizeCell(self):
        return self.height/25

    def Display(self, screen):
        for x in range(25):
            for y in range(25):
                if(self.matrix[y, x] == 1):
                    pygame.draw.rect(screen, DarkPurple, (self.XSizeCell()*x+0.5, self.YSizeCell()*y+0.5, self.XSizeCell()-0.5, self.YSizeCell()-0.5))
                elif(self.matrix[y, x] == 2):
                    pygame.draw.rect(screen, (0, 0, 0), (self.XSizeCell()*x, self.YSizeCell()*y, self.XSizeCell(), self.YSizeCell()))
                elif(self.matrix[y, x] == 6):
                    pygame.draw.circle(screen, (255, 0, 255), (self.XSizeCell()*(x+0.5), self.YSizeCell()*(y+0.5)), 5)
                elif(self.matrix[y, x] == 0 or self.matrix[y, x] == 4):
                    pygame.draw.circle(screen, (255, 0, 255), (self.XSizeCell()*(x+0.5), self.YSizeCell()*(y+0.5)), 1)