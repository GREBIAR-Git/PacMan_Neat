import pygame
import player
import terrain

#score_text = font.render("text", True, white)
#screen.blit(score_text, (10, 10))

class Game:
    def __init__(self):
        self.PacMan = player.PacMan(100,100,10)
        self.Map = terrain.Map(640, 480)
        self.direction = "RIGHT"

    def Start(self,screen):
        while True:
            self.Events()
            self.PacMan.Run(self.direction,self.Map)
            screen.fill((0, 0, 0))
            self.PacMan.Display(screen)
            pygame.display.update()

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.PacMan.Alive = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if(event.key == 119 or event.key == 1073741906):
                    self.direction = "TOP"
                elif(event.key == 100 or event.key == 1073741903):
                    self.direction = "RIGHT"
                elif(event.key == 115 or event.key == 1073741905):
                    self.direction = "BOT"
                elif(event.key == 97 or event.key == 1073741904):
                    self.direction = "LEFT"
                if event.key == pygame.K_RETURN:
                    pass