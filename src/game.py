import pygame
from entities.player import PacMan
from maps.terrain import Map
from entities.ghosts.redGhost import GhostRed
from entities.ghosts.blueGhost import GhostBlue
from entities.ghosts.pinkGhost import GhostPink
from entities.ghosts.orangeGhost import GhostOrange
import sys
import datetime

#from pygame import quit

class Game:
    def __init__(self, width, height):
        self.rrr = True
        self.Restart(width, height)
    
    def CloseProcess(self):
        pass
        # self.pacMan.t1.terminate()
        # self.goustRed.t1.terminate()
        # self.goustPink.t1.terminate()
        # self.goustBlue.t1.terminate()
        # self.goustOrange.t1.terminate()

                    
    def Restart1(self):
        self.rrr = False

    def Restart(self,width, height):
        self.rrr = True
        self.direction = ""
        self.map = Map(width, height)
        self.pacMan = PacMan(self.map.XSizeCell()*12.5,self.map.YSizeCell()*19.5,9,self.map)
        self.goustRed = GhostRed(self.map.XSizeCell()*11.5 ,self.map.YSizeCell()*12.5, (255, 0, 0), self.map.YSizeCell())
        self.goustPink = GhostPink(self.map.XSizeCell()*11.5,self.map.YSizeCell()*13.5, (255, 192, 203), self.map.YSizeCell())
        self.goustBlue = GhostBlue(self.map.XSizeCell()*13.5,self.map.YSizeCell()*12.5, (0, 255, 255), self.map.YSizeCell())
        self.goustOrange = GhostOrange(self.map.XSizeCell()*13.5,self.map.YSizeCell()*13.5, (255, 165, 0), self.map.YSizeCell())

    def Start(self,screen,game_end_callback, game_update_callback, eat, data):
        
        font = pygame.font.SysFont("Verdana", 15)
        fontForVictory = pygame.font.SysFont("Verdana", 40)
        fontForDefeat = pygame.font.SysFont("Verdana", 25)
        first = datetime.datetime.now()
        firstE = datetime.datetime.now()
        while self.rrr:
            current = datetime.datetime.now()
            
            tempScore = self.map.score

            tempDirection = self.pacMan.LocalCoordinates(self.map)
            screen.fill((0, 0, 0))
            self.map.Display(screen)
            game_update_callback()
            self.Events()
            if(self.map.score == self.map.scoreWin):
                victory_text = fontForVictory.render("Победа", True, (255,255,255))
                screen.blit(victory_text, (198, 245))
            elif (not self.pacMan.isAlive):
                victory_text = fontForDefeat.render("Поражение", True, (255,255,255))
                screen.blit(victory_text, (200, 255))
                game_end_callback()
            else:
                self.pacMan.RunAI(self.goustRed,self.goustPink,self.goustBlue,self.goustOrange, self.map,eat)

                self.pacMan.IsAlive(self.goustRed,self.goustPink,self.goustBlue,self.goustOrange,self.map)
                if(data['EnableGhost']):
                    self.goustRed.Action(self.pacMan, self.map)
                    if(self.map.score>=30):
                        self.goustPink.Action(self.pacMan, self.map)
                    if(self.map.score>=60):
                        self.goustBlue.Action(self.pacMan, self.goustRed, self.map)
                    if(self.map.score>=180):
                        self.goustOrange.Action(self.pacMan, self.map)
                self.pacMan.IsAlive(self.goustRed,self.goustPink,self.goustBlue,self.goustOrange,self.map)
                
                
                self.pacMan.Display(screen,self.map)
                self.goustRed.Display(screen)
                self.goustPink.Display(screen)
                self.goustBlue.Display(screen)
                self.goustOrange.Display(screen)
                score_text = font.render(str(self.map.score)+"/"+str(self.map.scoreWin), True, (255,255,255))
                screen.blit(score_text, (21, 208))

            if(self.map.score == tempScore):
                time_diff = current - firstE
                # if(time_diff.seconds>=(1)):
                if(time_diff.microseconds>=(100000)):
                    self.isAlive = False 
                    game_end_callback()
            else:
                firstE = datetime.datetime.now()
            pygame.display.update()

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pacMan.isAlive = False
                pygame.quit()
                sys.exit()
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
                    self.pacMan.step = 10
                    self.goustRed.step = 10
                    self.goustBlue.step = 10
                    self.goustOrange.step = 10
                    self.goustPink.step = 10
                elif(event.key == 101):
                    self.pacMan.step = 50
                    self.goustRed.step = 50
                    self.goustBlue.step = 50
                    self.goustOrange.step = 50
                    self.goustPink.step = 50
                elif(event.key == 114):
                    self.pacMan.step = 5
                    self.goustRed.step = 5
                    self.goustBlue.step = 5
                    self.goustOrange.step = 5
                    self.goustPink.step = 5
                elif(event.key == 116):
                    self.pacMan.step = 1
                    self.goustRed.step = 1
                    self.goustBlue.step = 1
                    self.goustOrange.step = 1
                    self.goustPink.step = 1
                self.pacMan.stop = False
                if event.key == pygame.K_RETURN:
                    self.pacMan.isAlive = False
                    self.Restart(self.map.width, self.map.height)