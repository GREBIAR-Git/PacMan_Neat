from entities.ghosts.ghost import Ghost

class GhostRed(Ghost):
    def Scatter(self, map):
        self.GoTo(26*map.XSizeCell(), 0, map)