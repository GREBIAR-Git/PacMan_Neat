from entities.ghosts.ghost import Ghost

class GhostBlue(Ghost):
    def Scatter(self, map):
        self.GoTo(25*map.XSizeCell(), 25*map.YSizeCell(), map)
    
    def Chase(self, pm, rg, map):
        x2 = rg.x + (pm.x - rg.x)*2
        y2 = rg.y + (pm.y - rg.y)*2
        self.GoTo(x2, y2, map)
    
    def Action(self, pm, rg, map):
        if(self.state == 0):
            self.Scatter(map)
        elif(self.state == 1):
            self.Chase(pm,rg, map)
        elif(self.state == 4):
            self.State4(map)
        else:
            self.Frightened(map)