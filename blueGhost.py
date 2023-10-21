import ghost

class GhostBlue(ghost.Ghost):
    def Scatter(self, map):
        self.GoTo(25*map.XSizeCell(), 25*map.YSizeCell(), map)