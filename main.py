import pygame
import game


pygame.init()

screen_width = 550 
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pacman simulation")
pygame.time.Clock().tick(60)

game.Game(screen_width,screen_height).Start(screen)