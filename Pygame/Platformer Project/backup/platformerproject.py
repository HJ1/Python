#Platformer Project 2016 Alpha Version
#N64 Controller support
import pygame, sys, os, time, datetime, pygame._view #pygame._view Necessary For setup.py On Some Python Builds
from pygame.locals import *
from gamelib import data
pygame.init()
pygame.joystick.init()

#Screen Variables With Values
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
yellow = (255, 255, 0)
blue = (0, 0, 255)

def main():
    running = True
    game_over = False
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    clock = pygame.time.Clock() 
    pygame.display.set_caption("Platformer Project")
    pygame.mouse.set_visible(0)
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    #Timer
    frame_count = 0
    frame_rate = 60
    #Log
    f = open("log.txt", "w")
    f.flush()
    #Controller Section
    try:
        j = pygame.joystick.Joystick(0)
        j.init()
        print 'Enabled Joystick: ' + j.get_name()
    except:
        print "No Controller Found"
    
    #Player Alpha Version
    class Block(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("data/Block.png").convert()
            self.rect = self.image.get_rect()
            screen = pygame.display.get_surface()
            #Spawn Position
            self.rect.x = 0
            self.rect.y = SCREEN_WIDTH
            #Speed
            self.speed_x = 0
            self.speed_y = 0
            
        def update(self, walls):
            self.gravity()
            #Move (DPAD - KEYBOARD)
            self.rect.x += self.speed_x
            #Player Collision
            block_hit_list = pygame.sprite.spritecollide(self, walls, False)
            for block in block_hit_list:
                if self.speed_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right

            #Move (DPAD - KEYBOARD)
            self.rect.y += self.speed_y
        
            block_hit_list = pygame.sprite.spritecollide(self, walls, False)
            for block in block_hit_list:
                if self.speed_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.speed_y < 0:
                    self.rect.top = block.rect.bottom
                #Collision Detection on Platforms
                self.speed_y = 0
            
        def gravity(self):
            if self.speed_y == 0:
                self.speed_y = 1
            else:
                self.speed_y += .35
                
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.speed_y >= 0:
                self.speed_y = 0
                self.rect.y = SCREEN_HEIGHT - self.rect.height

        def jump(self, walls):
            #Limit Jumping and Enable Jumping on Platforms
            self.rect.y += 2
            enable_jump = pygame.sprite.spritecollide(self, walls, False)
            self.rect.y -= 2
            if len(enable_jump) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
                self.speed_y = -10 #Jump Height

    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height):
            pygame.sprite.Sprite.__init__(self)
            #Create Surface
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.image.fill(white)

    class Room(object):
        wall_list = None

        def __init__(self):
            self.wall_list = pygame.sprite.Group()
            
    class Room1(Room): #Room 0 

        def __init__(self):
            Room.__init__(self)

            #Create Platforms x, y, width, height
            walls = [[0, 0, 10, 800],
                     [790, 100, 790, 800],
                     [0, 700, 100, 10],
                     [150, 700, 100, 10],
                     [240, 700, 10, 70],
                     [380, 640, 80, 10],
                     [0, 480, 100, 10],
                     [160, 480, 100, 10],
                     [320, 480, 70, 10],
                     [415, 580, 10, 40],
                     [380, 480, 10, 100],
                     [415, 650, 10, 200],
                     [380, 580, 80, 10],
                     [415, 790, 380, 10],
                     [415, 580, 150, 10],
                     [700, 580, 100, 10],
                     [615, 670, 40, 20],
                     [615, 520, 40, 20],
                     [730, 90, 70, 10],
                     [0, 350, 50, 10],
                     [185, 300, 70, 10],
                     [360, 250, 30, 10],
                     [520, 190, 20, 10],
                     [640, 130, 30, 10],
                    ]

            for item in walls:
                wall = Wall(item[0], item[1], item[2], item[3])
                self.wall_list.add(wall)

    class Room2(Room): #Room 1

        def __init__(self):
            Room.__init__(self)

            #Create Platforms x, y, width, height
            walls = [[0, 0, 10, 680],
                     [0, 784, 200, 40],
                     [300, 784, 100, 40],
                     [500, 784, 50, 40],
                     [700, 784, 100, 40],
                     [790, 0, 10, 150],
                     [790, 250, 10, 600],
                     [750, 700, 100, 10],
                     [700, 600, 40, 10],
                     [520, 600, 25, 10],
                     [340, 600, 25, 10],
                     [140, 600, 40, 10],
                     [10, 580, 30, 10],
                     [50, 380, 20, 70],
                     [35, 440, 20, 10],
                     [160, 300, 15, 70],
                     [163, 0, 8, 300],
                     [300, 280, 20, 70],
                     [305, 0, 9, 280],
                     [145, 390, 50, 7],
                     [285, 370, 50, 7],
                     [430, 300, 50, 10],
                     [600, 260, 20, 10],
                     [725, 250, 65, 10],
                    ]

            for item in walls:
                wall = Wall(item[0], item[1], item[2], item[3])
                self.wall_list.add(wall)

    class Room3(Room): #Room 2

        def __init__(self):
            Room.__init__(self)

            #Create Platforms x, y, width, height
            walls = [[0, 0, 10, 680],
                    ]

            for item in walls:
                wall = Wall(item[0], item[1], item[2], item[3])
                self.wall_list.add(wall)
                   
    #Groups
    allSprites = pygame.sprite.Group()
    player = Block()
    allSprites.add(player)

    #Room List
    rooms = []
    
    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    #Spawn Position Levels
    if current_room_no == 1:
        player.rect.y = 768
    elif current_room_no == 2:
        player.rect.y = 784
                         
    #Game Loop
    while running == True:
        #Timer
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "{0:02}:{1:02}".format(minutes, seconds)
        if game_over == False:
            frame_count += 1
        else:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #N64
            if event.type == pygame.JOYBUTTONDOWN and event.button == 7:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("A BUTTON \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 6:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("B BUTTON \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("START BUTTON \n"))
                    file.close()
                #Pause
                pause = font.render("Pause", True, (white))
                screen.blit(pause, (435-pause.get_width(), 350))
                pygame.display.update()
                while 1:
                    event = pygame.event.wait()
                    player.speed_x = 0
                    if event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                        break
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 13:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("L BUTTON \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 12:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("R BUTTON \n"))
                    file.close()
                running = False, pygame.quit(), sys.exit()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 5:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("Z BUTTON \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 11:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("C BUTTON UP \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 10:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("C BUTTON DOWN \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("C BUTTON LEFT \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 8:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("C BUTTON RIGHT \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 3:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("DPAD UP \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 2:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("DPAD DOWN \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 1:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("DPAD LEFT \n"))
                    file.close()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 0:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("DPAD RIGHT \n"))
                    file.close()
            #Joystick movement
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    player.speed_x = 3
                elif event.button == 1:
                    player.speed_x = -3
                elif event.button == 7:
                    player.jump(current_room.wall_list)
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    player.speed_x = 0
                elif event.button == 1:
                    player.speed_x = 0

            #Keyboard
            if not hasattr(event, 'key'): continue    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                #Pause
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("KEYBOARD PAUSE \n"))
                    file.close()
                pause = font.render("Pause", True, (white))
                screen.blit(pause, (435-pause.get_width(), 350))
                pygame.display.update()
                while 1:
                    event = pygame.event.wait()
                    player.speed_x = 0
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        break
            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                with open("log.txt", mode='a') as file:
                    file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                    file.write(str("KEYBOARD ESCAPE \n"))
                    file.close()
                running = False, pygame.quit(), sys.exit()
            #Keyboard Movement 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    with open("log.txt", mode='a') as file:
                        file.write('%sms: %s\n' %
                       (datetime.datetime.now(), event))
                        file.write(str("KEYBOARD ARROW RIGHT \n"))
                        file.close()
                    player.speed_x = 3
                elif event.key == pygame.K_LEFT:
                    with open("log.txt", mode='a') as file:
                        file.write('%sms: %s\n' %
                           (datetime.datetime.now(), event))
                        file.write(str("KEYBOARD ARROW LEFT \n"))
                        file.close()
                    player.speed_x = -3
                elif event.key == pygame.K_SPACE:
                    with open("log.txt", mode='a') as file:
                        file.write('%sms: %s\n' %
                           (datetime.datetime.now(), event))
                        file.write(str("KEYBOARD SPACEBAR \n"))
                        file.close()
                    player.jump(current_room.wall_list)
                elif event.key == pygame.K_z:
                    print "x", player.rect.x
                    print "y", player.rect.y
                elif event.key == pygame.K_c: #Controls
                    with open("log.txt", mode='a') as file:
                        file.write('%sms: %s\n' %
                           (datetime.datetime.now(), event))
                        file.write(str("KEYBOARD C \n"))
                        file.close()
                        control = font.render("Move: Arrow Keys", 1, (white))
                        control2 = font.render("Jump: Spacebar", 1, (white))
                        control3 = font.render("Pause: P Key", 1, (white))
                        control4 = font.render("Quit: ESC Key", 1, (white))
                        continuegame = font.render("Press any key to continue...", 1, (white))
                        screen.blit(control, (25, 45))
                        screen.blit(control2, (200, 45))
                        screen.blit(control3, (345, 45))
                        screen.blit(control4, (670, 45))
                        screen.blit(continuegame, (305, 350))
                        pygame.display.update()
                        while 1:
                            event = pygame.event.wait()
                            player.speed_x = 0
                            if event.type == pygame.KEYDOWN:
                                break
                            
            #Keyboard Movement       
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.speed_x = 0
                elif event.key == pygame.K_LEFT:
                    player.speed_x = 0
                                                   
        #Background    
        screen.fill(black)

        #Frame Rate
        clock.tick(60)

        #Draw Player and Rooms
        allSprites.draw(screen)
        current_room.wall_list.draw(screen)

        #Player Collision
        player.update(current_room.wall_list)

        #Next Levels

        #Room 1
        if current_room_no == 0:
            if player.rect.right > SCREEN_WIDTH:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
                player.rect.y = 768
                
        #Room 2
        if current_room_no == 1:
            if player.rect.left < 0:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 784
                player.rect.y = 74
            if player.rect.bottom > 800:
                player.rect.x = 10
                player.rect.y = 768
            if player.rect.right > SCREEN_WIDTH:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
                player.rect.y = 784

        #Room 3
        if current_room_no == 2:
            if player.rect.left < 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 784
                player.rect.y = 234
    
        #Collision with screen
        if player.rect.left < 0:
            player.rect.left = 0
        elif player.rect.top < 0:
            player.rect.top = 0
        elif player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
        elif player.rect.bottom > SCREEN_HEIGHT:
            player.rect.bottom = SCREEN_HEIGHT

        #Font Section
        font = pygame.font.SysFont("Times New Roman", 18)
        version = font.render("Alpha V00.2", 1, (white))
        controls = font.render("Controls = C", 1, (white))
        timer = font.render(output_string, 1, white)
        text_timer = font.render("Timer:", 1, (white))
        fps = font.render("FPS %d" % clock.get_fps(), 1, (white))
        screen.blit(version,(690, 15))
        screen.blit(fps, (25, 15))
        screen.blit(timer, (400, 17))
        screen.blit(text_timer, (345, 15))
        screen.blit(controls, (200, 15))

        #Draw Exit
        if current_room_no == 0:
            room_arrow = font.render("->", False, (yellow))
            screen.blit(room_arrow, (780, 70))
        elif current_room_no == 1:
            room_arrow2 = font.render("->", False, (yellow))
            screen.blit(room_arrow2, (780, 228))
        elif current_room_no == 2:
            room_end = font.render("To be continue..", 1, (white))
            screen.blit(room_end, (350, 400))
            game_over = True
            
        if game_over == True:
            timer = font.render(output_string, 1, yellow)
            screen.blit(timer, (400, 17))
        
        #Draw screen
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
