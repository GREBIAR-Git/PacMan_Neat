import pygame
import player
import terrain
import redGhost
import blueGhost
import pinkGhost
import orangeGhost

class Game:
    def __init__(self, width, height):
        self.Restart(width, height)
    
    def CloseThreads(self):
        pass
        #self.pacMan.t1
        #self.goustRed.t1
        #self.goustPink.t1
        #self.goustBlue.t1
        #self.goustOrange.t1

    def Restart(self,width, height):
        self.direction = ""
        self.map = terrain.Map(width, height)
        self.pacMan = player.PacMan(self.map.XSizeCell()*12.5,self.map.YSizeCell()*19.5,9)
        self.goustRed = redGhost.GhostRed(self.map.XSizeCell()*11.5 ,self.map.YSizeCell()*12.5, (255, 0, 0))
        self.goustPink = pinkGhost.GhostPink(self.map.XSizeCell()*11.5,self.map.YSizeCell()*13.5, (255, 192, 203))
        self.goustBlue = blueGhost.GhostBlue(self.map.XSizeCell()*13.5,self.map.YSizeCell()*12.5, (0, 255, 255))
        self.goustOrange = orangeGhost.GhostOrange(self.map.XSizeCell()*13.5,self.map.YSizeCell()*13.5, (255, 165, 0))

    def Start(self,screen):
        font = pygame.font.SysFont("Verdana", 15)
        fontForVictory = pygame.font.SysFont("Verdana", 40)
        fontForDefeat = pygame.font.SysFont("Verdana", 25)
        
        while True:
            self.Events()
            if(self.map.score == self.map.scoreWin):
                victory_text = fontForVictory.render("Победа", True, (255,255,255))
                screen.blit(victory_text, (198, 245))
            elif (not self.pacMan.isAlive):
                victory_text = fontForDefeat.render("Поражение", True, (255,255,255))
                screen.blit(victory_text, (200, 255))
            else:
                self.pacMan.Run(self.direction,self.goustRed,self.goustPink,self.goustBlue,self.goustOrange, self.map)
                self.goustRed.Action(self.pacMan, self.map)
                if(self.map.score>=30):
                    self.goustPink.Action(self.pacMan, self.map)
                if(self.map.score>=60):
                    self.goustBlue.Action(self.pacMan, self.goustRed, self.map)
                if(self.map.score>=180):
                    self.goustOrange.Action(self.pacMan, self.map)
                self.pacMan.IsAlive(self.goustRed,self.goustPink,self.goustBlue,self.goustOrange,self.map)
                
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
                self.pacMan.isAlive = False
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
                    self.pacMan.isAlive = False
                    self.Restart(self.map.width, self.map.height)