#Platformer Project 2016 Alpha Version
#N64 Controller support
import pygame, sys, os, time, math, random
from pygame.locals import *
pygame.init()
pygame.joystick.init()

#Controller Section
try:
    j = pygame.joystick.Joystick(0)
    j.init()
    print 'Enabled joystick: ' + j.get_name()
except:
    print "No controller found"

#Main
running = True
os.environ["SDL_VIDEO_CENTERED"] = "1"
clock = pygame.time.Clock() 
pygame.display.set_caption("Platformer Project")
pygame.mouse.set_visible(0)
window_height = 800
window_length = 800
screen = pygame.display.set_mode((window_height, window_length))
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
blue = (0, 0, 255)

#Player Alpha Version
class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([16, 16])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        #Current Position
        self.rect.x = 15
        self.rect.y = 770
        #Speed
        self.speed_x = 0
        self.speed_y = 0
        
    def update(self):
        #Joystick
        joystick_count = pygame.joystick.get_count()
        #Check if a controller is connected
        if joystick_count != 0:
            horiz_axis_pos = j.get_axis(0)
            vert_axis_pos = j.get_axis(1)
            self.rect.x = self.rect.x + int(horiz_axis_pos * 6) # 6 = Try to keep same speed as input
            self.rect.y = self.rect.y + int(vert_axis_pos * 6)
                       
#Groups
player = Block()        
allSprites = pygame.sprite.Group()
allSprites.add(player)
        
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
            #pause, sound play
            pause = font.render("Pause", True, (white))
            screen.blit(pause, (435-pause.get_width(), 350))
            pygame.display.update()
            while 1:
                event = pygame.event.wait()
                if event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                    break
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 13:
            print "L BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 12:
            print "R BUTTON"
            running = False, pygame.quit(), sys.exit()
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
        #Joystick movement
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                player.speed_x = 3
            elif event.button == 1:
                player.speed_x -= 3
            elif event.button == 3:
                player.speed_y =- 3
            elif event.button == 2:
                player.speed_y = 3
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                player.speed_x = 0
            elif event.button == 1:
                player.speed_x = 0
            elif event.button == 3:
                player.speed_y = 0
            elif event.button == 2:
                player.speed_y = 0
        #Keyboard
        if not hasattr(event, 'key'): continue    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            #pause, sound play
            pause = font.render("Pause", True, (white))
            screen.blit(pause, (435-pause.get_width(), 350))
            pygame.display.update()
            while 1:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    break
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False, pygame.quit(), sys.exit()
        #Movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.speed_x = 3
            elif event.key == pygame.K_LEFT:
                player.speed_x -= 3
            elif event.key == pygame.K_UP:
                player.speed_y =- 3
            elif event.key == pygame.K_DOWN:
                player.speed_y = 3   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.speed_x = 0
            elif event.key == pygame.K_LEFT:
                player.speed_x = 0
            elif event.key == pygame.K_UP:
                player.speed_y = 0
            elif event.key == pygame.K_DOWN:
                player.speed_y = 0
                                            
    #Background    
    screen.fill(black)
    clock.tick(60)

    allSprites.draw(screen)
    player.update()

    #Move (DPAD - KEYBOARD)
    player.rect.x = player.rect.x + player.speed_x
    player.rect.y = player.rect.y + player.speed_y

    #Collision with screen
    if player.rect.x < 0:
        player.rect.x = 0
    elif player.rect.y < 0:
        player.rect.y = 0
    elif player.rect.x > 784:
        player.rect.x = 784
    elif player.rect.y > 784:
        player.rect.y = 784

    #Font Section
    font = pygame.font.SysFont("Times New Roman", 18)
    version = font.render ("Alpha V00.1", 1, (white))
    fps = font.render("FPS %d" % clock.get_fps(), 1, (white))
    screen.blit(version,(690, 760))
    screen.blit(fps, (10, 0))    

    #Draw screen
    pygame.display.update()

pygame.quit()
