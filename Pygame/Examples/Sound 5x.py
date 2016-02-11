#Made by HJ - 7 February
#Sound plays from a file 5x times

import pygame, sys #import modules, we use sys(system) to close the script.
from pygame.locals import * 
pygame.init() #initialize Pygame, get it running.
pygame.display.set_caption("Pygame Sound") #add the title of the script

screen = pygame.display.set_mode((1, 1)) #in my experience we need a screen in order to play music. I add a small screen with 1x1 resolution. this is required to play music far as I know.
print "Now playing sound 5x times!" #a simple message

#main loop
running = True

#values
volume = 0.05
loop = 10

sound = pygame.mixer.Sound('data/fireball.ogg') #load the music, use this if the file is in a folder: "folder/music.mp3"
sound.set_volume(volume)
sound.play(loop)

while running == True: #while script is running with main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit script
            running = False
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE: #if we press Escape key we close the script
            running = False, pygame.quit(), sys.exit()

    pygame.display.update()

pygame.quit()
    
