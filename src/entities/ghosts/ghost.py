import pygame
import maps.terrain
import math
import random
import time


from threading import Thread

class Ghost:
    def __init__(self, x, y, color, step = 2):   
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.direction = "RIGHT"
        self.step = step
        self.slowStep = step 
        self.fastStep = step
        self.isHome = True
        self.state = 0
        speed=25
        self.TScatter = 7/speed# 7 #1 # 7
        self.TChase = 20/speed#20 #3 # 20
        self.TScatter2 =2/speed# 2#0.5 # 2
        self.W =1/speed# 2#0.5 # 2

        self.t1 = Thread(target=self.ChangeState)
        
        self.t1.start()
        self.goInHome = False
        self.prevState = -1
    
    def LocalCoordinates(self, map):
        v = []
        if(not self.isHome and not self.goInHome):
            x = int((self.x)/(map.XSizeCell())) 
            y = int((self.y)/(map.YSizeCell()))
            v.append(x)
            v.append(y)
        else:
            v.append(-1)
            v.append(-1)
        return v

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

    def Step(self):
        if(self.state == 2):
            return self.slowStep
        elif(self.state == 4):
            return self.fastStep
        else:
            return self.step

    def State4(self, map):
        if(not self.goInHome):
            self.GoInHome(map)
        else:
            x1 = int((self.x)/(map.XSizeCell()))
            y1 = int((self.y)/(map.YSizeCell())) 
            if(x1 == 12 and y1 == 12):
                self.goInHome = False
                self.state = self.prevState
                self.isHome = True
            else:
                self.y += self.Step()

    def GoInHome(self, map):
        x1 = int((self.x)/(map.XSizeCell()))
        y1 = int((self.y)/(map.YSizeCell())) 
        if(x1 == 12 and y1 == 9):
            self.goInHome = True
        else:
            self.GoTo(13*map.XSizeCell(),9*map.YSizeCell(),map)

    def ChangeState(self):
        time.sleep(self.TScatter)
        while(self.state==2 or self.state==4):
            time.sleep(self.W)
        self.state = 1
        time.sleep(self.TChase)
        while(self.state==2 or self.state==4):
            time.sleep(self.W)
        self.state = 0
        time.sleep(self.TScatter)
        while(self.state==2 or self.state==4):
            time.sleep(self.W)
        self.state = 1 
        time.sleep(self.TChase)
        while(self.state==2 or self.state==4):
            time.sleep(self.W)
        self.state = 0
        time.sleep(self.TScatter - self.TScatter2)
        while(self.state==2 or self.state==4):
            time.sleep(self.W)
        self.state = 1 
        time.sleep(self.TChase)
        while(self.state==2 or self.state==4):
            time.sleep(self.W)
        self.state = 0
        time.sleep(self.TScatter - self.TScatter2)
        while(self.state==2 or self.state==4):
            time.sleep(self.W)
        self.state = 1


    def EuclideanDistances(self,x1,x2,y1,y2):
        return math.sqrt(math.pow(x2 - x1,2)+math.pow(y2 - y1,2))

    def ExitHome(self, map):
        x1 = int((self.x)/(map.XSizeCell()))
        y1 = int((self.y)/(map.YSizeCell())) 
        if(self.isHome and (map.matrix[y1, x1] == 1 or map.matrix[y1, x1] == 2)):
            self.y -= self.Step()
        else:
            self.direction = "LEFT"
            self.isHome = False

    def GoInDirection(self, map):
        if(self.direction == "TOP"):
            if(self.CanPass(self.direction,map)):
                self.y -= self.Step()
            # if(self.y < (0-self.radius)):
            #     self.y = map.height
        elif (self.direction == "RIGHT"):
            if(self.CanPass(self.direction,map)):
                self.x += self.Step()
            # if(self.x > (map.width+self.radius)):
            #     self.x = 0
        elif (self.direction == "BOT"):
            if(self.CanPass(self.direction,map)):
                self.y += self.Step()
            # if(self.y > (map.height+self.radius)):
            #     self.y = 0
        elif (self.direction == "LEFT"):
            if(self.CanPass(self.direction,map)):
                self.x -= self.Step()
            # if(self.x < (0-self.radius)):
            #     self.x = map.width

    def GoTo(self, x, y, map):
        if(self.isHome):
            self.ExitHome(map)
        else:
            if(self.CanChangeDirection(self.direction, map)):
                self.SelectDirection(x, y, map)
                self.GoInDirection(map)
            else:
                if(self.CanPass(self.direction, map)): 
                    self.GoInDirection(map)

    def Chase(self, pm, map):
        self.GoTo(pm.x, pm.y, map)

    def Scatter(self, x, y, map):
        self.GoTo(x, y, map)

    def Frightened(self, map):
        if(self.isHome):
            self.ExitHome(map)
        else:
            if(self.CanChangeDirection(self.direction, map)):
                self.RandomSelectDirection(map)
                self.GoInDirection(map)
            else:
                if(self.CanPass(self.direction, map)): 
                    self.GoInDirection(map)


    def RandomSelectDirection(self, map):
        directionList = []
        
        if(self.direction == "TOP"):
            if(self.CanPass("TOP", map)):
                directionList.append("TOP")
            if(self.CanPass("LEFT", map)):
                directionList.append("LEFT")
            if(self.CanPass("RIGHT", map)):
                directionList.append("RIGHT")
            # if(len(directionList)==0):
            #     directionList.append("BOT")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

        elif(self.direction == "BOT"):
            if(self.CanPass("BOT", map)):
                directionList.append("BOT")
            if(self.CanPass("LEFT", map)):
                directionList.append("LEFT")
            if(self.CanPass("RIGHT", map)):
                directionList.append("RIGHT")
            # if(len(directionList)==0):
            #     directionList.append("TOP")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

        elif(self.direction == "RIGHT"):  
            if(self.CanPass("TOP", map)):
                directionList.append("TOP")
            if(self.CanPass("BOT", map)):
                directionList.append("BOT")
            if(self.CanPass("RIGHT", map)):
                directionList.append("RIGHT")
            # if(len(directionList)==0):
            #     directionList.append("LEFT")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

        elif(self.direction == "LEFT"):   
            if(self.CanPass("TOP", map)):
                directionList.append("TOP")
            if(self.CanPass("BOT", map)):    
                directionList.append("BOT")
            if(self.CanPass("LEFT", map)):
                directionList.append("LEFT")
            # if(len(directionList)==0):
            #     directionList.append("RIGHT")
            direction = random.randint(1, len(directionList))
            self.direction = directionList[direction-1]

    def SelectDirection(self, xPM, yPM, map):
        yBot = 1000
        yTop = 1000
        xLeft = 1000
        xRight = 1000
        if(self.direction == "TOP"):
            if(self.CanPass("TOP", map)):
                yTop = self.EuclideanDistances(self.x,xPM,self.y-map.YSizeCell(),yPM)
            if(self.CanPass("LEFT", map)):
                xLeft = self.EuclideanDistances(self.x-map.XSizeCell(),xPM,self.y,yPM)
            if(self.CanPass("RIGHT", map)):
                xRight = self.EuclideanDistances(self.x+map.XSizeCell(),xPM,self.y,yPM)
            
            if(yTop<xLeft and yTop<xRight):
                self.direction = "TOP"
            elif(xLeft<yTop and xLeft<xRight):
                self.direction = "LEFT"
            elif(xRight<yTop and xRight<xLeft):
                self.direction = "RIGHT"

        elif(self.direction == "BOT"):
            if(self.CanPass("BOT", map)):
                yBot = self.EuclideanDistances(self.x,xPM,self.y+map.YSizeCell(),yPM)
            if(self.CanPass("LEFT", map)):
                xLeft = self.EuclideanDistances(self.x-map.XSizeCell(),xPM,self.y,yPM)
            if(self.CanPass("RIGHT", map)):
                xRight = self.EuclideanDistances(self.x+map.XSizeCell(),xPM,self.y,yPM)
            if(yBot<xLeft and yBot<xRight):
                self.direction = "BOT"
            elif(xLeft<yBot and xLeft<xRight):
                self.direction = "LEFT"
            elif(xRight<yBot and xRight<xLeft):
                self.direction = "RIGHT"

        elif(self.direction == "RIGHT"):  
            if(self.CanPass("TOP", map)):
                yTop = self.EuclideanDistances(self.x,xPM,self.y-map.YSizeCell(),yPM)
            if(self.CanPass("BOT", map)):
                yBot = self.EuclideanDistances(self.x,xPM,self.y+map.YSizeCell(),yPM)
            if(self.CanPass("RIGHT", map)):
                xRight = self.EuclideanDistances(self.x+map.XSizeCell(),xPM,self.y,yPM)
            
            if(yTop<xRight and yTop<yBot):
                self.direction = "TOP"
            elif(xRight<yTop and xRight<yBot):
                self.direction = "RIGHT"
            elif(yBot<yTop and yBot<xRight):
                self.direction = "BOT"

        elif(self.direction == "LEFT"):   
            if(self.CanPass("TOP", map)):
                yTop = self.EuclideanDistances(self.x,xPM,self.y-map.YSizeCell(),yPM)
            if(self.CanPass("BOT", map)):    
                yBot = self.EuclideanDistances(self.x,xPM,self.y+map.YSizeCell(),yPM)
            if(self.CanPass("LEFT", map)):
                xLeft = self.EuclideanDistances(self.x-map.XSizeCell(),xPM,self.y,yPM)
            
            if(yTop<xLeft and yTop<yBot):
                self.direction = "TOP"
            elif(xLeft<yTop and xLeft<yBot):
                self.direction = "LEFT"
            elif(yBot<yTop and yBot<xLeft):
                self.direction = "BOT"
            
        
    def CanPass(self, direction, Map):
        #if(self.color == (255, 0, 0)):
            #print("noX: " + str((self.x)/(Map.XSizeCell())) + "; int: " + str(int((self.x)/(Map.XSizeCell()))))
            #rint("noY: " + str((self.y)/(Map.XSizeCell())) + "; int: " + str(int((self.y)/(Map.XSizeCell()))))
        if(direction == "TOP"):
            x1 = int((self.x)/(Map.XSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell())) 
            if(Map.matrix[y1-1, x1] == 1):
                return False
            else:
                #if(Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6):
                return True
        elif (direction == "BOT"):
            x1 = int((self.x)/(Map.XSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell())) 
            if(Map.matrix[y1+1, x1] == 1):
                return False
            else:
                #if(Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6):
                return True
        elif (direction == "RIGHT"):
            x1 = int((self.x)/(Map.XSizeCell())) 
            y1 = int((self.y)/(Map.YSizeCell()))
            if(Map.matrix[y1, x1+1] == 1):
                return False
            else:
                #if(x1+1<25 and (Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6)):
                return True
        elif (direction == "LEFT"):
            x1 = int((self.x)/(Map.XSizeCell())) 
            y1 = int((self.y)/(Map.YSizeCell()))
            if(Map.matrix[y1, x1-1] == 1):
                return False
            else:
                #if(x1<25 and ( Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6)):
                return True
        return False

    def CanChangeDirection(self, direction, Map):
        #if(self.color == (255, 0, 0)):
            #print("noX: " + str((self.x)/(Map.XSizeCell())) + "; int: " + str(int((self.x)/(Map.XSizeCell()))))
            #print("noY: " + str((self.y)/(Map.XSizeCell())) + "; int: " + str(int((self.y)/(Map.XSizeCell()))))
        if(direction == "TOP"):
            x1 = int((self.x)/(Map.XSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell())) 
            if(Map.matrix[y1-1, x1] == 1 or Map.matrix[y1, x1] == 4 or Map.matrix[y1, x1] == 5):
                return True
            else:
                #if(Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6):
                return False
        elif (direction == "BOT"):
            x1 = int((self.x)/(Map.XSizeCell()))
            y1 = int((self.y)/(Map.YSizeCell())) 
            if(Map.matrix[y1+1, x1] == 1 or Map.matrix[y1, x1] == 4 or Map.matrix[y1, x1] == 5):
                self.one = True
                return True
            else:
                #if(Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6):
                return False
        elif (direction == "RIGHT"):
            x1 = int((self.x)/(Map.XSizeCell())) 
            y1 = int((self.y)/(Map.YSizeCell()))
            if((Map.matrix[y1, x1+1] == 1) or Map.matrix[y1, x1] == 4 or Map.matrix[y1, x1] == 5):
                self.one = True
                return True
            else:
                #if(x1+1<25 and (Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6)):
                return False
        elif (direction == "LEFT"):
            x1 = int((self.x)/(Map.XSizeCell())) 
            y1 = int((self.y)/(Map.YSizeCell()))
            if(Map.matrix[y1, x1-1] == 1 or Map.matrix[y1, x1] == 4 or Map.matrix[y1, x1] == 5):
                self.one = True
                return True
            else:
                #if(x1<25 and ( Map.matrix[y1, x1] == 3 or Map.matrix[y1, x1] == 0 or Map.matrix[y1, x1] == 6)):
                return False
        return False

    def Display(self, screen):
        if(self.state==2):
            pygame.draw.circle(screen, (0,0,255), (self.x, self.y), self.radius)
        elif(self.state==4):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.radius-2)
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

