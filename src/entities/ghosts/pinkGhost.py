from entities.ghosts.ghost import Ghost

class GhostPink(Ghost):
    def Scatter(self, map):
        self.GoTo(0, 0, map)
    
    def Chase(self, pm, map):
        offsetX = 0
        offsetY = 0
        if(pm.direction=="TOP"):
            offsetY-4*map.YSizeCell()
        elif(pm.direction == "RIGHT"):
            offsetX+4*map.XSizeCell()
        elif (pm.direction == "BOT"):
            offsetY+4*map.YSizeCell()
        elif ( pm.direction == "LEFT"):
            offsetX-4*map.XSizeCell()
        self.GoTo(pm.x+offsetX, pm.y+offsetY, map)