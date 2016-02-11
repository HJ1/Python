#Made by HJ - 11 February

import pygame, sys #import modules, we use sys(system) to close the script.
from pygame.locals import * 
pygame.init() #initialize Pygame
pygame.display.set_caption("Pygame Custom Cursor") #add the title of the script
screen = pygame.display.set_mode((500, 500)) #draw a screen we can use the cursor on
cursor = pygame.image.load("data/Hand1.png") #load the cursor image from data folder
black = (0, 0, 0) #black color for our background

#main loop
running = True

while running == True: #while script is running with main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit script
            running = False
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE: #if we press Escape key we close the script
            running = False, pygame.quit(), sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == K_1:
            pygame.mouse.set_visible(0) # make the original mouse invisible
        elif event.type == pygame.KEYUP and event.key == K_1:
            pygame.mouse.set_visible(1) # make cursor appear again
        elif event.type == pygame.KEYDOWN and event.key == K_2:
            pygame.mouse.set_visible(0) # make the original mouse invisible
            
    screen.fill(black) #fill the screen with a color
    screen.blit(cursor, pygame.mouse.get_pos()) #set the cursor image as the new mouse cursor

    pygame.display.update() #draw the screen

pygame.quit()
    
