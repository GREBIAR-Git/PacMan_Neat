import pygame
import terrain
import math
import random
import time


from threading import Thread

class Ghost:
    def __init__(self, x, y, color, step = 0.3):   
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.direction = "RIGHT"
        self.step = step
        self.one = False
        self.isHome = True
        self.state = 0
        self.t1 = Thread(target=self.ChangeState)
        
        self.t1.start()
        self.goInHome = False
        self.prevState = -1

    def Turn(self):
        if(self.direction=="LEFT"):
            self.direction = "RIGHT"
        elif(self.direction=="RIGHT"):
            self.direction = "LEFT"
        elif(self.direction=="TOP"):
            self.direction = "BOT"
        else:
            self.direction = "TOP"

    def Action(self, pm, map):
        if(self.state == 0):
            self.Scatter(map)
        elif(self.state == 1):
            self.Chase(pm, map)
        elif(self.state == 4):
            self.State4(map)
        else: 
            self.Frightened(map)

    def State4(self, map):
        if(not self.goInHome):
            self.GoInHome(map)
        else:
            x1 = int((self.x+10)/(map.XSizeCell()))
            y1 = int((self.y)/(map.YSizeCell())) 
            if(x1 == 12 and y1 == 12):
                self.goInHome = False
                self.state = self.prevState
                self.isHome = True
            else:
                self.y+=self.step
                if(self.y < (0-self.radius)):
                    self.y = map.height

    def GoInHome(self, map):
        x1 = int((self.x+10)/(map.XSizeCell()))
        y1 = int((self.y)/(map.YSizeCell())) 
        if(x1 == 12 and y1 == 9):
            self.goInHome = True
        else:
            self.GoTo(13*map.XSizeCell(),9*map.YSizeCell(),map)

    def ChangeState(self):
        time.sleep(7)
        while(self.state==2 or self.state==4):
            time.sleep(1)
        self.state = 1
        time.sleep(20)
        while(self.state==2 or self.state==4):
            time.sleep(1)
        self.state = 0
        time.sleep(7)
        while(self.state==2 or self.state==4):
            time.sleep(1)
        self.state = 1 
        time.sleep(20)
        while(self.state==2 or self.state==4):
            time.sleep(1)
        self.state = 0
        time.sleep(5)
        while(self.state==2 or self.state==4):
            time.sleep(1)
        self.state = 1 
        time.sleep(20)
        while(self.state==2 or self.state==4):
            time.sleep(1)
        self.state = 0
        time.sleep(5)
        while(self.state==2 or self.state==4):
            time.sleep(1)
        self.state = 1


    def EuclideanDistances(self,x1,x2,y1,y2):
        return math.sqrt(math.pow(x2 - x1,2)+math.pow(y2 - y1,2))

    def ExitHome(self, map):
        size = 10
        x1 = int((self.x)/(map.XSizeCell()))
        y1 = int((self.y+size)/(map.YSizeCell())) 
        if(self.isHome and (map.matrix[y1, x1] == 1 or map.matrix[y1, x1] == 2)):
            self.y-=self.step
            if(self.y < (0-self.radius)):
                self.y = map.height
        else:
            self.direction = "LEFT"
            self.isHome = False

    def GoInDirection(self, map):
        if(self.direction == "TOP"):
            self.y-=self.step
            if(self.y < (0-self.radius)):
                self.y = map.height
        elif (self.direction == "RIGHT"):
            self.x+=self.step
            if(self.x > (map.width+self.radius)):
                self.x = 0
        elif (self.direction == "BOT"):
            self.y+=self.step
            if(self.y > (map.height+self.radius)):
                self.y = 0
        elif (self.direction == "LEFT"):
            self.x-=self.step
            if(self.x < (0-self.radius)):
                self.x = map.width

    def GoTo(self, x, y, map):
        if(self.isHome):
            self.ExitHome(map)
        elif(self.CanPass(self.direction, map)): 
            self.one = False
            self.GoInDirection(map)
        elif(self.one):
            self.GoInDirection(map)
        else:
            self.SelectDirection(x,y,map)

    def Chase(self, pm, map):
        self.GoTo(pm.x, pm.y, map)

    def Scatter(self, x, y, map):
        self.GoTo(x, y, map)

    def Frightened(self, map):
        if(self.isHome):
            self.ExitHome(map)
        elif(self.CanPass(self.direction, map)): 
            self.one = False
            self.GoInDirection(map)
        elif(self.one):
            self.GoInDirection(map)
        else:
            self.RandomSelectDirection(map)


    def RandomSelectDirection(self, map):
        self.one = True
        directionList = []
        
        if(self.direction == "TOP"):
            if(self.Test("TOP", map)):
                directionList.append("TOP")
            if(self.Test("LEFT", map)):
                directionList.append("LEFT")
            if(self.Test("RIGHT", map)):
                directionList.append("RIGHT")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

        elif(self.direction == "BOT"):
            if(self.Test("BOT", map)):
                directionList.append("BOT")
            if(self.Test("LEFT", map)):
                directionList.append("LEFT")
            if(self.Test("RIGHT", map)):
                directionList.append("RIGHT")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

        elif(self.direction == "RIGHT"):  
            if(self.Test("TOP", map)):
                directionList.append("TOP")
            if(self.Test("BOT", map)):
                directionList.append("BOT")
            if(self.Test("RIGHT", map)):
                directionList.append("RIGHT")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

        elif(self.direction == "LEFT"):   
            if(self.Test("TOP", map)):
                directionList.append("TOP")
            if(self.Test("BOT", map)):    
                directionList.append("BOT")
            if(self.Test("LEFT", map)):
                directionList.append("LEFT")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

    def SelectDirection(self, xPM, yPM, map):
        self.one = True
        yBot = 1000
        yTop = 1000
        xLeft = 1000
        xRight = 1000
        if(self.direction == "TOP"):
            if(self.Test("TOP", map)):
                yTop = self.EuclideanDistances(self.x,xPM,self.y-map.YSizeCell(),yPM)
            if(self.Test("LEFT", map)):
                xLeft = self.EuclideanDistances(self.x-map.XSizeCell(),xPM,self.y,yPM)
            if(self.Test("RIGHT", map)):
                xRight = self.EuclideanDistances(self.x+map.XSizeCell(),xPM,self.y,yPM)
            
            if(yTop<xLeft and yTop<xRight):
                self.direction = "TOP"
            elif(xLeft<yTop and xLeft<xRight):
                self.direction = "LEFT"
            elif(xRight<yTop and xRight<xLeft):
                self.direction = "RIGHT"

        elif(self.direction == "BOT"):
            if(self.Test("BOT", map)):
                yBot = self.EuclideanDistances(self.x,xPM,self.y+map.YSizeCell(),yPM)
            if(self.Test("LEFT", map)):
                xLeft = self.EuclideanDistances(self.x-map.XSizeCell(),xPM,self.y,yPM)
            if(self.Test("RIGHT", map)):
                xRight = self.EuclideanDistances(self.x+map.XSizeCell(),xPM,self.y,yPM)
            if(yBot<xLeft and yBot<xRight):
                self.direction = "BOT"
            elif(xLeft<yBot and xLeft<xRight):
                self.direction = "LEFT"
            elif(xRight<yBot and xRight<xLeft):
                self.direction = "RIGHT"

        elif(self.direction == "RIGHT"):  
            if(self.Test("TOP", map)):
                yTop = self.EuclideanDistances(self.x,xPM,self.y-map.YSizeCell(),yPM)
            if(self.Test("BOT", map)):
                yBot = self.EuclideanDistances(self.x,xPM,self.y+map.YSizeCell(),yPM)
            if(self.Test("RIGHT", map)):
                xRight = self.EuclideanDistances(self.x+map.XSizeCell(),xPM,self.y,yPM)
            
            if(yTop<xRight and yTop<yBot):
                self.direction = "TOP"
            elif(xRight<yTop and xRight<yBot):
                self.direction = "RIGHT"
            elif(yBot<yTop and yBot<xRight):
                self.direction = "BOT"

        elif(self.direction == "LEFT"):   
            if(self.Test("TOP", map)):
                yTop = self.EuclideanDistances(self.x,xPM,self.y-map.YSizeCell(),yPM)
            if(self.Test("BOT", map)):    
                yBot = self.EuclideanDistances(self.x,xPM,self.y+map.YSizeCell(),yPM)
            if(self.Test("LEFT", map)):
                xLeft = self.EuclideanDistances(self.x-map.XSizeCell(),xPM,self.y,yPM)
            
            if(yTop<xLeft and yTop<yBot):
                self.direction = "TOP"
            elif(xLeft<yTop and xLeft<yBot):
                self.direction = "LEFT"
            elif(yBot<yTop and yBot<xLeft):
                self.direction = "BOT"
            
        
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
                if(Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6):
                    return True
        elif (direction == "BOT"):
            x1 = int((self.x)/(Map.XSizeCell()))
            x2 = int((self.x+size)/(Map.XSizeCell())) 
            x3 = int((self.x-size)/(Map.XSizeCell()))
            y1 = int((self.y-size)/(Map.YSizeCell())) 
            if(y1+1<25 and (x1>=25 or Map.matrix[y1+1, x1] == 1 or x2>=25 or Map.matrix[y1+1, x2] == 1 or x3>=25 or Map.matrix[y1+1, x3] == 1)):
                return False
            else:
                if(Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6):
                    return True
        elif (direction == "RIGHT"):
            x1 = int((self.x-size)/(Map.XSizeCell())) 
            y2 = int((self.y+size)/(Map.YSizeCell())) 
            y3 = int((self.y-size)/(Map.YSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell()))
            if(x1+1<25 and (Map.matrix[y1, x1+1] == 1 or Map.matrix[y2, x1+1] == 1 or Map.matrix[y3, x1+1] == 1)):
                return False
            else:
                if(x1+1<25 and (Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6)):
                    return True
        elif (direction == "LEFT"):
            x1 = int((self.x+size)/(Map.XSizeCell())) 
            y2 = int((self.y+size)/(Map.YSizeCell())) 
            y3 = int((self.y-size)/(Map.YSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell()))
            if(Map.matrix[y1, x1-1] == 1 or Map.matrix[y2, x1-1] == 1 or Map.matrix[y3, x1-1] == 1):
                return False
            else:
                if(x1<25 and ( Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6)):
                    return True
        return False

    def Test(self, direction, map):
        size = 10
        if(direction == "TOP"):
            x1 = int((self.x)/(map.XSizeCell()))
            y1 = int((self.y+size)/(map.YSizeCell())) 
            if(x1>=25 or map.matrix[y1-1, x1] == 1):
                return False
            else:
                return True
        elif (direction == "BOT"):
            x1 = int((self.x)/(map.XSizeCell()))
            y1 = int((self.y-size)/(map.YSizeCell())) 
            if(y1+1<25 and (x1>=25 or map.matrix[y1+1, x1] == 1)):
                return False
            else:
                return True
        elif (direction == "RIGHT"):
            x1 = int((self.x-size)/(map.XSizeCell())) 
            y1 = int((self.y)/(map.YSizeCell()))
            if(x1+1<25 and map.matrix[y1, x1+1] == 1):
                return False
            else:
                return True
        elif (direction == "LEFT"):
            x1 = int((self.x+size)/(map.XSizeCell())) 
            y1 = int((self.y)/(map.YSizeCell()))
            if(map.matrix[y1, x1-1] == 1):
                return False
            else:
                return True
        return False

    def Display(self, screen):
        if(self.state==2):
            pygame.draw.circle(screen, (0,0,255), (self.x, self.y), self.radius)
        elif(self.state==4):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.radius-2)
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

