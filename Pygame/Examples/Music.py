import pygame, sys #import modules, we use sys(system) to close the script.
from pygame.locals import * 
pygame.init() #initialize Pygame, get it running.

screen = pygame.display.set_mode((1, 1)) #in my experience we need a screen in order to play music. I add a small screen with 1x1 resolution. this is required to play music far as I know.
print "Now playing music!" #a simple message

#main loop
running = True

#values
loop = -1
volume = 0.7

pygame.mixer.music.load('maintheme.ogg') #load the music, use this if the file is in a folder: "folder/music.mp3"
pygame.mixer.music.set_volume(volume) #value for the volume
pygame.mixer.music.play(loop) #play with a loop

while running == True: #while script is running with main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit script
            running = False
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE: #if we press Escape key we close the script
            running = False, pygame.quit(), sys.exit()

pygame.display.update

pygame.quit()
    
