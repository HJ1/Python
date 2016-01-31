#Platformer Project 2016
#N64 Controller support
import pygame, sys, os
from pygame.locals import *
pygame.init()
pygame.joystick.init()

#Controller Section
try:
    Joystick_N64 = pygame.joystick.Joystick(0)
    Joystick_N64.init()
    Joystick_Name = Joystick_N64.get_name()
    print "Controller Found: " + Joystick_Name
except:
    pass

#Main
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.display.set_caption("Platformer Project")
pygame.mouse.set_visible(0)
window_height = 800
window_length = 800
screen = pygame.display.set_mode((window_height, window_length))
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

#Screen Section
screen.fill(black)

#Loop Variable
running = True

#Loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #N64
        elif event.type == pygame.JOYBUTTONDOWN:
            print event
        elif event.type == pygame.JOYBUTTONUP:
            print event
        if event.type == pygame.JOYBUTTONDOWN and event.button == 7:
            print "A BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 6:
            print "B BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:
            print "START BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 13:
            print "L BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 12:
            print "R BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 5:
            print "Z BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 11:
            print "C BUTTON UP"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 10:
            print "C BUTTON DOWN"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 9:
            print "C BUTTON LEFT"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 8:
            print "C BUTTON RIGHT"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 3:
            print "DPAD UP"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 2:
            print "DPAD DOWN"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 1:
            print "DPAD LEFT"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 0:
            print "DPAD RIGHT"
        #Keyboard
        if event.type == pygame.KEYDOWN and event.key == K_q:
            running = False, pygame.quit(), sys.exit()

    #Font Section
    font = pygame.font.SysFont("Times New Roman", 72)
    text1 = font.render ("YOOOOOOOOOOOOOOOOOOO", True, (white))
    screen.blit(text1,(100, 10))
        
    pygame.display.update()

pygame.quit()
