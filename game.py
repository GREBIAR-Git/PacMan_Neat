import pygame
import player
import terrain
import ghost

class Game:
    def __init__(self, width, height):
        self.Restart(width, height)

    def Restart(self,width, height):
        self.map = terrain.Map(width, height)
        self.pacMan = player.PacMan(self.map.XSizeCell()*1.5,self.map.YSizeCell()*1.5,9)
        self.goustRed = ghost.Ghost(self.map.XSizeCell()*11 ,self.map.YSizeCell()*12.5, (255, 0, 0))
        self.goustPink = ghost.Ghost(self.map.XSizeCell()*12,self.map.YSizeCell()*12.5, (255, 192, 203))
        self.goustBlue = ghost.Ghost(self.map.XSizeCell()*13,self.map.YSizeCell()*12.5, (0, 255, 255))
        self.goustOrange = ghost.Ghost(self.map.XSizeCell()*14,self.map.YSizeCell()*12.5, (255, 165, 0))
        self.direction = "RIGHT"

    def Start(self,screen):
        font = pygame.font.SysFont("Verdana", 15)
        fontForVictory = pygame.font.SysFont("Verdana", 40)
        while True:
            self.Events()
            if(self.map.score == self.map.scoreWin):
                victory_text = fontForVictory.render("Победа", True, (255,255,255))
                screen.blit(victory_text, (198, 245))
            else:
                self.pacMan.Run(self.direction,self.map)
                screen.fill((0, 0, 0))
                self.map.Display(screen)
                self.pacMan.Display(screen,self.map)
                self.goustRed.Display(screen)
                self.goustPink.Display(screen)
                self.goustBlue.Display(screen)
                self.goustOrange.Display(screen)
                score_text = font.render(str(self.map.score)+"/"+str(self.map.scoreWin), True, (255,255,255))
                screen.blit(score_text, (21, 208))
            pygame.display.update()

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pacMan.Alive = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if(event.key == 119 or event.key == 1073741906):
                    self.direction = "TOP"
                elif(event.key == 100 or event.key == 1073741903):
                    self.direction = "RIGHT"
                elif(event.key == 115 or event.key == 1073741905):
                    self.direction = "BOT"
                elif(event.key == 97 or event.key == 1073741904):
                    self.direction = "LEFT"
                elif(event.key == 113):
                    self.pacMan.step = 0
                elif(event.key == 101):
                    self.pacMan.step = 0.01
                elif(event.key == 114):
                    self.pacMan.step = 0.3
                elif(event.key == 116):
                    self.pacMan.step = 0.5
                self.pacMan.stop = False
                if event.key == pygame.K_RETURN:
                    self.Restart(self.map.width, self.map.height)