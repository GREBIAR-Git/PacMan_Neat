import pygame
import PacMan

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman simulation")

font = pygame.font.SysFont("Verdana", 15)

pygame.time.Clock().tick(60)

PacMan.Start(screen)