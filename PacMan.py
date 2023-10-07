import pygame
import Player
import Terrain
import numpy as np 

def Start(screen):
    PacMan = Player.PacMan(100,100,10)
    #Map = Terrain.Map(640, 480)
    direction = "RIGHT"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PacMan.Alive = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if(event.key == 119):
                    direction = "TOP"
                elif(event.key == 100):
                    direction = "RIGHT"
                elif(event.key == 115):
                    direction = "BOT"
                elif(event.key == 97):
                    direction = "LEFT"
                if event.key == pygame.K_RETURN:
                    pass 
        
        screen.fill((0, 0, 0))
        PacMan.Display(screen, direction)
        pygame.display.update()

    #score_text = font.render("text", True, white)
    #screen.blit(score_text, (10, 10))