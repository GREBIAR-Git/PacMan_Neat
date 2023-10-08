import pygame
import player
import terrain

class Game:
    def __init__(self, width, height):
        self.PacMan = player.PacMan(width/25*1.5,height/25*1.5,9)
        self.Map = terrain.Map(width, height)
        self.direction = "RIGHT"

    def Start(self,screen):
        font = pygame.font.SysFont("Verdana", 15)
        fontWin = pygame.font.SysFont("Verdana", 40)
        while True:
            if(self.Map.score == self.Map.scoreWin):
                score_text = fontWin.render("Победа", True, (255,255,255))
                screen.blit(score_text, (198, 245))
            else:
                self.PacMan.Run(self.direction,self.Map)
                screen.fill((0, 0, 0))
                self.Map.Display(screen)
                self.PacMan.Display(screen)
                score_text = font.render(str(self.Map.score)+"/"+str(self.Map.scoreWin), True, (255,255,255))
                screen.blit(score_text, (21, 208))
            self.Events()
            pygame.display.update()

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.PacMan.Alive = False
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
                self.PacMan.stop = False
                if event.key == pygame.K_RETURN:
                    self.PacMan = player.PacMan(self.Map.width/25*1.5,self.Map.height/25*1.5,9)
                    self.Map = terrain.Map(self.Map.width, self.Map.height)
                    self.direction = "RIGHT"