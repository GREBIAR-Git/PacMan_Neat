import ghost

class GhostOrange(ghost.Ghost):
    def Scatter(self, map):
        self.GoTo(0, 25*map.YSizeCell(), map)
    
    def Chase(self, pm, map):
        distance = self.EuclideanDistances(pm.x, self.x, pm.y, self.y)
        if(distance/map.XSizeCell()>8):
            self.GoTo(pm.x, pm.y, map)
        else:
            self.Scatter(map)