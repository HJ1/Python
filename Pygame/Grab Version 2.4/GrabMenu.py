# Made by HJ. Version 2.3
# Project from 2014-2015
#Game is for PC only
import pygame, os, sys
from pygame.locals import *
pygame.init()
menumusic = ("anot.it")
    
def play_music(name, volume=0.8, loop=-1):
    fullname = os.path.join('data', name)
    try:
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
    except:
        raise SystemExit, "Can't load: " + fullname

def load_sound(name, volume=0.05):
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
        sound.set_volume(volume)
    except:
        raise SystemExit, "Can't load: " + fullname
    return sound

def stop_music():
    pygame.mixer.music.pause() #Pause music

def continue_music():
    pygame.mixer.music.unpause()#Unpause music

def run_game():
    import Grab
    Grab.main()
      
def reset_highscore():
    open("data/highscore.sav", "w").write(str(0))
    print "Grab High Score reset to 0"
    
class GrabMenu(object):
    pygame.mouse.set_visible(0) #make the mouse cursor invisible
    pygame.display.set_caption("Grab") #name the game
    pygame.display.set_icon(pygame.image.load("data/Icon.png")) #set an icon for the game
    screen = pygame.display.set_mode((800, 800)) #screen resolution width and height
    background = pygame.Surface(screen.get_size()) #make the background
    background = pygame.image.load("data/BG.png").convert() #convert background 
    background = pygame.transform.scale(background,(800, 800)) #scale the background down to the screen resulution
    background2 = pygame.Surface(screen.get_size())
    background2 = pygame.image.load("data/BG2.png").convert()
    cursor = pygame.image.load("data/Hand1.png") #make a new cursor inside the game
    pygame.mouse.set_pos(350, 470) # places the player inside the borders before starting
    WHITE = (255, 255, 255) # colors
    YELLOW = (255, 216, 0)
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)
    running = True # value for main loop
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("times new roman", 28, bold=True) # menu font and text.
    fontinstructions = pygame.font.SysFont("times new roman", 19, bold=True)
    fontmenu = pygame.font.SysFont("times new roman", 20, bold=True)
    fontlogo = pygame.font.SysFont("verdana", 150, bold=False, italic=True)
    fontcolor = WHITE
    fontcolor2 = WHITE
    fontcolor3 = WHITE
    fontcolor4 = WHITE
    Key_C = pygame.image.load("data/Key_C.png")
    Key_S = pygame.image.load("data/Key_S.png")
    Key_ESC = pygame.image.load("data/Key_Esc.png")
    Key_P = pygame.image.load("data/Key_P.png")
    Key_Q = pygame.image.load("data/Key_Q.png")
    Mouse = pygame.image.load("data/Mouse.png")
    Clock = pygame.image.load("data/Clock.png")
    Bomb = pygame.image.load("data/Bomb.png")
    Bronzecoin = pygame.image.load("data/Bronzecoin.png")
    Silvercoin = pygame.image.load("data/Silvercoin.png")
    Goldencoin = pygame.image.load("data/Goldencoin.png")
    mousetrigger = False
    mouseclick = load_sound("Click.wav", 3.5) # mouse click
    Menu1 = True #main menu
    Menu2 = False #options menu
    Menu3 = False #reset score menu
    Menu4 = False #how to play
    play_music(menumusic)
    
    #main_loop
    while running == True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False, sys.exit()
                    
            #Keyboard
            if event.type == MOUSEBUTTONDOWN and event.button == 1: # if mouse button is pressed (left mouse key only)
                if Menu1:
                    if ren_r.collidepoint(pygame.mouse.get_pos()): # play the game
                        if Menu1 == False:
                            pass
                        else:
                            mouseclick.play()
                            run_game()
                    elif ren2_r.collidepoint(pygame.mouse.get_pos()): #options
                        if Menu1 == False:
                            pass
                        else:
                            mouseclick.play()
                            Menu1 = False
                            Menu4 = True
                    elif ren3_r.collidepoint(pygame.mouse.get_pos()): #how to play
                        if Menu1 == False:
                            pass
                        else:
                            mouseclick.play()
                            Menu1 = False
                            Menu2 = True
                    elif ren4_r.collidepoint(pygame.mouse.get_pos()): #quit the game
                        if Menu1 == False:
                            pass
                        else:
                            mouseclick.play()
                            running = False, pygame.quit(), sys.exit()
                elif Menu2:
                    if ren5_r.collidepoint(pygame.mouse.get_pos()): #reset high score
                        mouseclick.play()
                        Menu2 = False
                        Menu3 = True
                        
                    elif ren6_r.collidepoint(pygame.mouse.get_pos()): #go back
                        mouseclick.play()
                        Menu1 = True
                        Menu2 = False
                elif Menu3:
                    if ren7_r.collidepoint(pygame.mouse.get_pos()): #reset high score
                        mouseclick.play()
                        reset_highscore()
                        Menu3 = False
                        Menu2 = True
                    elif ren8_r.collidepoint(pygame.mouse.get_pos()): #reset high score
                        mouseclick.play()
                        Menu2 = True
                        Menu3 = False
                elif Menu4:
                    if ren9_r.collidepoint(pygame.mouse.get_pos()): #go back
                        mouseclick.play()
                        Menu4 = False
                        Menu1 = True
                    
            if not hasattr(event, 'key'): continue
            if event.key == K_s: #pause music
                stop_music()
            elif event.key == K_c: #unpause / continue music
                continue_music()

        if Menu4:
            screen.blit(background2, (0, 0))
        else:
            screen.blit(background, (0, 0))
            ren_menu = fontmenu.render("Beta version 2.4", True, (WHITE))
            ren_menu2 = fontmenu.render("Made by HJ", True, (WHITE))
            ren_menu3 = fontmenu.render("Copyright 2014-2015", True, (WHITE))
            ren_logo = fontlogo.render("Grab", True, (0,64,192))
            screen.blit(ren_logo, (220, 190))
            screen.blit(ren_menu, (650, 770))
            screen.blit(ren_menu2, (285, 350))
            screen.blit(ren_menu3, (399, 355))
            screen.blit(cursor, pygame.mouse.get_pos())               
        if Menu1:
            ren = font.render("Play", True, (fontcolor))
            ren_r = ren.get_rect()
            ren_r.x, ren_r.y = 340, 530
            ren2 = font.render("How to Play", True, (fontcolor2))
            ren2_r = ren2.get_rect()
            ren2_r.x, ren2_r.y = 340, 590
            ren3 = font.render("Options", True, (fontcolor3))
            ren3_r = ren3.get_rect()
            ren3_r.x, ren3_r.y = 340, 650
            ren4 = font.render("Quit Game", True, (fontcolor4))
            ren4_r = ren4.get_rect()
            ren4_r.x, ren4_r.y = 340, 710
            screen.blit(ren, (340, 530))
            screen.blit(ren2, (340, 590))
            screen.blit(ren3, (340, 650))
            screen.blit(ren4, (340, 710))
            if ren_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor = YELLOW
            else:
                fontcolor = WHITE

            if ren2_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor2 = YELLOW
            else:
                fontcolor2 = WHITE

            if ren3_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor3 = YELLOW
            else:
                fontcolor3 = WHITE

            if ren4_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor4 = YELLOW
            else:
                fontcolor4 = WHITE
        elif Menu2: #options menu
            options = font.render("Options", 1, (WHITE))
            ren5 = font.render("Reset High Score", True, (fontcolor))
            ren5_r = ren5.get_rect()
            ren5_r.x, ren5_r.y = 340, 590
            ren6 = font.render("Go back", True, (fontcolor2))
            ren6_r = ren6.get_rect()
            ren6_r.x, ren6_r.y = 340, 650
            screen.blit(options, (340, 530))
            screen.blit(ren5, (340, 590))
            screen.blit(ren6, (340, 650))
            if ren5_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor = YELLOW
            else:
                fontcolor = WHITE

            if ren6_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor2 = YELLOW
            else:
                fontcolor2 = WHITE
        elif Menu3: #reset score menu
            resetscore = font.render("Do you want to reset high score?", 1, (WHITE))
            ren7 = font.render("Yes", True, (fontcolor))
            ren7_r = ren7.get_rect()
            ren7_r.x, ren7_r.y = 320, 590
            ren8 = font.render("No", True, (fontcolor2))
            ren8_r = ren8.get_rect()
            ren8_r.x, ren8_r.y = 440, 590
            screen.blit(ren7, (320, 590))
            screen.blit(ren8, (440, 590))
            screen.blit(resetscore, (200, 525))
            if ren7_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor = YELLOW
            else:
                fontcolor = WHITE

            if ren8_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor2 = YELLOW
            else:
                fontcolor2 = WHITE
        elif Menu4:
            #1
            pygame.draw.rect(screen, BLACK, (30, 160, 740, 260))
            pygame.draw.rect(screen, GRAY, (20, 160, 10, 260))
            pygame.draw.rect(screen, GRAY, (770, 160, 10, 260))
            pygame.draw.rect(screen, GRAY, (20, 160, 760, 10))
            pygame.draw.rect(screen, GRAY, (20, 410, 760, 10))
            #2
            pygame.draw.rect(screen, BLACK, (30, 450, 740, 280))
            pygame.draw.rect(screen, GRAY, (20, 450, 10, 280))
            pygame.draw.rect(screen, GRAY, (770, 450, 10, 280))
            pygame.draw.rect(screen, GRAY, (20, 450, 760, 10))
            pygame.draw.rect(screen, GRAY, (20, 720, 760, 10))
            #1
            ren_menu4 = fontlogo.render("HowtoPlay", True, (0,64,192))
            ren2 = font.render("- Mouse for movement", 1, (WHITE))
            ren3 = font.render("- Pause the game", True, (WHITE))
            ren4 = font.render("- Mute music", 1, (WHITE))
            ren5 = font.render("- Unmute music", 1, (WHITE))
            ren6 = font.render("- Game over ~ Give up", 1, (WHITE))
            ren7 = font.render("- Quit game", 1, (WHITE))
            #2
            ren10 = fontinstructions.render("Grab is a simple game where the objective is to collect the highest score.", True, (WHITE))
            ren11 = fontinstructions.render("There are coins falling from the sky. You get score for each coin you manage to grab.", True, (WHITE))
            ren12 = fontinstructions.render("As you progress within the game the levels and difficulty will increase.", True, (WHITE))
            ren13 = fontinstructions.render("There are 3 different types of coins: bronze coin, silver coin and golden coin.", True, (WHITE))
            ren14 = fontinstructions.render("Bronze coin will give you +50 score, a silver coin will give you +100 score and a", True, (WHITE))
            ren15 = fontinstructions.render("Golden coin will give you +200 score. However be aware there are also bombs falling", True, (WHITE))
            ren16 = fontinstructions.render("from the sky. A bomb collision will give you -150 score. For every +1500 score you", True, (WHITE))
            ren17 = fontinstructions.render("advance to a new level. When you reach +10 levels you will get to another world.", True, (WHITE))
            ren18 = fontinstructions.render("Game runs on a time limit 400 seconds, when the time runs out you will get game over.", True, (WHITE))
            ren19 = fontinstructions.render("When the timer reaches 100 seconds left a clock will spawn. Clock will give you +50.", True, (WHITE))
            ren20 = fontinstructions.render("Time. Clocks will respawn until your time is 400 again. Don't let the timer run out.", True, (WHITE))
            ren21 = fontinstructions.render("Good luck!", True, (WHITE))
            ren9 = font.render("Go back", True, (fontcolor))
            ren9_r = ren9.get_rect()
            ren9_r.x, ren9_r.y = 340, 750
            #1
            screen.blit(ren2, (95, 185))
            screen.blit(ren3, (95, 245))
            screen.blit(ren4, (95, 305))
            screen.blit(ren5, (95, 365))
            screen.blit(ren6, (455, 180))
            screen.blit(ren7, (455, 240))
            screen.blit(ren9, (340, 750))
            screen.blit(ren_menu4, (2, -30))
            screen.blit(Mouse, (40, 180))
            screen.blit(Key_P, (40, 240))
            screen.blit(Key_S, (40, 300))
            screen.blit(Key_C, (40, 360))
            screen.blit(Key_Q, (400, 175))
            screen.blit(Key_ESC, (400, 235))
            #2
            screen.blit(ren10, (40, 470))
            screen.blit(ren11, (40, 490))
            screen.blit(ren12, (40, 510))
            screen.blit(ren13, (40, 530))
            screen.blit(ren14, (40, 550))
            screen.blit(ren15, (40, 570))
            screen.blit(ren16, (40, 590))
            screen.blit(ren17, (40, 610))
            screen.blit(ren18, (40, 630))
            screen.blit(ren19, (40, 650))
            screen.blit(ren20, (40, 670))
            screen.blit(ren21, (40, 690))
            screen.blit(cursor, pygame.mouse.get_pos())
            
            if ren9_r.collidepoint(pygame.mouse.get_pos()):
                mousetrigger = True
                fontcolor = YELLOW
            else:
                fontcolor = WHITE
        
        pygame.display.update()
