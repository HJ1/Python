#Platformer Project 2016
import pygame, pygame._view, sys, os
from pygame.locals import *
pygame.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.display.set_caption("Platformer Project")
pygame.mouse.set_visible(0)
window_height = 800
window_length = 800
pygame.display.set_mode((window_height, window_length))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()

pygame.quit()
