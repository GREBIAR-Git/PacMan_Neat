import ghost

class GhostRed(ghost.Ghost):
    def Scatter(self, map):
        self.GoTo(25*map.XSizeCell(), 0, map)