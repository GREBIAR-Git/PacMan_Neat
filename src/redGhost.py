import ghost

class GhostRed(ghost.Ghost):
    def Scatter(self, map):
        self.GoTo(26*map.XSizeCell(), 0, map)