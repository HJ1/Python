# Made by HJ. Version 2.3
# Project from 2014-2015
#Game has support for N64 controller.
import pygame, time, math, sys, random, os
from pygame.locals import *
from GrabMenu import *
pygame.init()
pygame.joystick.init()
    
def filepath(filename):
    data_dir = os.path.normpath(os.path.join('data'))
    return os.path.join(data_dir, filename)

def load(filename, mode='rb'):
    return open(os.path.join(data_dir, filename), mode)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        raise SystemExit, "Can't load:" + fullname
    return image

def load_sound(name, volume=0.05):
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
        sound.set_volume(volume)
    except:
        raise SystemExit, "Can't load: " + fullname
    return sound

def play_music(name, volume=0.7, loop=-1):
    fullname = os.path.join('data', name)
    try:
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
    except:
        raise SystemExit, "Can't load: " + fullname
    
def stop_music():
    pygame.mixer.music.pause() #Pause music

def continue_music():
    pygame.mixer.music.unpause()#Unpause music

def save_score(score):
    open(filepath("score.sav"), "w").write(str(score))

def save_level(level):
    open(filepath("level.sav"), "w").write(str(level))

def save_world(world):
    open(filepath("world.sav"), "w").write(str(world))

def save_highscore(highscore):
    open(filepath("highscore.sav"), "w").write(str(highscore))

def save_highlevel(highlevel):
    open(filepath("highlevel.sav"), "w").write(str(highlevel))
     
def get_saved_score():
    try:
        return int(open(filepath("score.sav")).read())
    except:
        open(filepath("score.sav"), "w").write(str(1))
        return 1

def get_saved_level():
    try:
        return int(open(filepath("level.sav")).read())
    except:
        open(filepath("level.sav"), "w").write(str(1))
        return 1

def get_saved_world():
    try:
        return int(open(filepath("world.sav")).read())
    except:
        open(filepath("world.sav"), "w").write(str(1))
        return 1

def get_highscore():
    try:
        return int(open(filepath("highscore.sav")).read())
    except:
        open(filepath("highscore.sav"), "w").write(str(1))
        return 1

def get_highlevel():
    try:
        return int(open(filepath("highlevel.sav")).read())
    except:
        open(filepath("highlevel.sav"), "w").write(str(1))
        return 1
                
def main():
    done = False #game loop running
    testmode = False 
    gameover = False 
    screen = pygame.display.set_mode((800, 800)) #screen display size
    music = ("boc.it") #music 1
    music2 = ("ctrm.it") #music 2
    background = pygame.Surface(screen.get_size()) #make the background
    background = pygame.image.load("data/BG.png").convert() 
    background = pygame.transform.scale(background,(800, 800))
    clock_ = pygame.time.Clock() 
    #colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    #values
    time = 400
    score = 0
    highscore = 0
    level = 1
    world = 1
    coins_gathered = 0
    coins_gathered2 = 0
    coins_gathered3 = 0
    #stats images  
    stats_coin = load_image ("Bronzecoin.png")
    stats_coin2 = load_image("Silvercoin.png")
    stats_coin3 = load_image("Goldencoin.png")
    
    class Border(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image ("Border.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()
            self.rect.x = 75 # Border placement
            self.rect.y = 0

    class Hand(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image ("Hand1.png")
            self.rect = self.image.get_rect()
            screen = pygame.display.get_surface()
            self.rect.x = 300
            self.rect.y = 300
            self.grab_sound = load_sound("Coin.ogg")
            self.bomb_explosion = load_sound("Bomb_explosion.wav", 0.150)
            self.bomb_explosion2 = load_sound("Bomb_explosion2.wav", 0.150)
            self.explosion = load_image("Explosion.png")
             
        def update(self):
            pos = pygame.mouse.get_pos()
            collide = pygame.sprite.spritecollide(self, allSprites, False)
            if collide:
                if pos[0] < 640 and pos[0] > 85: # Player crashes with the borders
                    self.rect.x = pos[0] - 5
                if pos[1] > 5 and pos[1] < 770: # Player crashes with top of screen and bottom of screen
                    self.rect.y = pos[1]
            if pygame.sprite.spritecollide(self, Coins_Bronze, False):
                self.grab_sound.play()
            elif pygame.sprite.spritecollide(self, Coins_Silver, False):
                self.grab_sound.play()
            elif pygame.sprite.spritecollide(self, Coins_Golden, False):
                self.grab_sound.play()
            if random.randint(0, 1) == 0:    
                if pygame.sprite.spritecollide(self, BombGroup1, False):
                    screen.blit(self.explosion,(pos), None)
                    self.bomb_explosion.play()
                elif pygame.sprite.spritecollide(self, BombGroup2, False):
                    screen.blit(self.explosion,(pos), None)
                    self.bomb_explosion.play()
                elif pygame.sprite.spritecollide(self, BombGroup3, False):
                    screen.blit(self.explosion,(pos), None)
                    self.bomb_explosion.play()
            else:
                if pygame.sprite.spritecollide(self, BombGroup1, False):
                    screen.blit(self.explosion,(pos), None)
                    self.bomb_explosion2.play()
                elif pygame.sprite.spritecollide(self, BombGroup2, False):
                    screen.blit(self.explosion,(pos), None)
                    self.bomb_explosion2.play()
                elif pygame.sprite.spritecollide(self, BombGroup3, False):
                    screen.blit(self.explosion,(pos), None)
                    self.bomb_explosion2.play()
            
    class Coin_Bronze(pygame.sprite.Sprite): # DIFFERENT TYPES OF COINS
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("Bronzecoin.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()
            
        def reset_pos(self):
            self.rect.x = random.randrange(640)
            self.rect.y = random.randrange(-200, -20) # Respawns the coins at the top
        
        def update(self):
            if self.rect.y > 805: # Coins that hit the bottom is removed
                self.reset_pos()
            if self.rect.x < 100: # Removes coins that spawns outside the left border
                self.reset_pos()
            if level == 1:
                self.rect.y += 4
            elif level == 2:
                self.rect.y += 4
            elif level == 3:
                self.rect.y += 5
            elif level == 4:
                self.rect.y += 6
            elif level == 5:
                self.rect.y += 6
            elif level == 6:
                self.rect.y += 7
            elif level == 7:
                self.rect.y += 8
            else:
                self.rect.y += level + 1
            if time <= 1: # Game over
                self.kill()
    
    class Coin_Silver(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("Silvercoin.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()
            
        def reset_pos(self):
            self.rect.x = random.randrange(640)
            self.rect.y = random.randrange(-200, -20)
        
        def update(self):
            if self.rect.y > 805:
                self.reset_pos()
            if self.rect.x < 100:
                self.reset_pos()
            if testmode == True:
                self.rect.y += 4
            if level == 1:
                pass
            elif level == 2:
                self.rect.y += 5
            elif level == 3:
                self.rect.y += 5
            elif level == 4:
                self.rect.y += 6
            elif level == 5:
                self.rect.y += 7
            elif level == 6:
                self.rect.y += 7
            elif level == 7:
                self.rect.y += 8
            else:
                self.rect.y += level + 1
            if time <= 1:
                self.kill()
        
    class Coin_Golden(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("Goldencoin.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()
        
        def reset_pos(self):
            self.rect.x = random.randrange(640)
            self.rect.y = random.randrange(-200, -20) # Respawns the coins at the top
        
        def update(self):
            
            if self.rect.y > 805:
                self.reset_pos()
            if self.rect.x < 100: # Removes coins that spawns outside the left border
                self.reset_pos()
            if level == 1:
                pass
            elif level == 2:
                pass
            elif level == 3:
                self.rect.y += 6
            elif level == 4:
                self.rect.y += 6
            elif level == 5:
                self.rect.y += 7
            elif level == 6:
                self.rect.y += 8
            elif level == 7:
                self.rect.y += 9
            else:
                self.rect.y += level + 1
            if time <= 1: # Game over
                self.kill()
            if testmode == True:
                self.rect.y += 4
            else:
                if level == 1:
                    self.reset_pos()
            if testmode == True:
                pass
            else:
                if level == 2:
                    self.reset_pos()
                
    class Bomb(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("Bomb.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()
           
        def bomb_spawn(self):
            self.rect.x = random.randrange(640)
            self.rect.y = random.randrange(-200, -20)
     
        def update(self):
            if self.rect.y > 805:
                self.bomb_spawn()
            if self.rect.x < 105:
                self.bomb_spawn()
            if level == 1:
                pass
            elif level == 2:
                pass
            elif level == 3:
                self.rect.y += 5
            elif level == 4:
                self.rect.y += 6
            elif level == 5:
                self.rect.y += 6
            elif level == 6:
                self.rect.y += 7
            elif level == 7:
                self.rect.y += 8
            else:
                self.rect.y += level + 1
            if testmode == True:
                self.rect.y += 4
            else:
                if level == 1:
                    self.bomb_spawn()
            if testmode == True:
                pass
            else:
                if level == 2:
                    self.bomb_spawn()
            if time <= 1: # Game over
                self.kill()
       
    class Bomb2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("Bomb.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()
           
        def bomb2_spawn(self):
            self.rect.x = random.randrange(640)
            self.rect.y = random.randrange(-200, -20)
     
        def update(self):
            if self.rect.y > 805:
                self.bomb2_spawn()
            if self.rect.x < 105:
                self.bomb2_spawn()
            if level == 1:
                pass
            elif level == 2:
                pass
            elif level == 3:
                pass
            elif level == 4:
                pass
            elif level == 5:
                self.rect.y += 6
            elif level == 6:
                self.rect.y += 7
            elif level == 7:
                self.rect.y += 8
            else:
                self.rect.y += level + 1
            if level == 1:
                self.bomb2_spawn()
            elif level == 2:
                self.bomb2_spawn()
            elif level == 3:
                self.bomb2_spawn()
            elif level == 4:
                self.bomb2_spawn()
            if time <= 1: # Game over
                self.kill()
     
    class Bomb3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("Bomb.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()
           
        def bomb3_spawn(self):
            self.rect.x = random.randrange(640)
            self.rect.y = random.randrange(-200, -20)
     
        def update(self):
            if self.rect.y > 805:
                self.bomb3_spawn()
            if self.rect.x < 105:
                self.bomb3_spawn()
            if level == 1:
                pass
            elif level == 2:
                pass
            elif level == 3:
                pass
            elif level == 4:
                pass
            elif level == 5:
                pass
            elif level == 6:
                pass
            elif level == 7:
                self.rect.y += 9
            else:
                self.rect.y += level + 1
            if level == 1:
                self.bomb3_spawn()
            elif level == 2:
                self.bomb3_spawn()
            elif level == 3:
                self.bomb3_spawn()
            elif level == 4:
                self.bomb3_spawn()
            elif level == 5:
                self.bomb3_spawn()
            elif level == 6:
                self.bomb3_spawn()
            elif level == 7:
                self.bomb3_spawn()
            if time <= 1: # Game over
                self.kill()
            
    class Clock(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("Clock.png")
            screen = pygame.display.get_surface()
            self.rect = self.image.get_rect()

        def clock_spawn(self):
            self.rect.x = random.randrange(640)
            self.rect.y = random.randrange(-200, -20) # Respawns the coins at the top
            
        def update(self):  
            if time < 100 and time >= 0:    
                if self.rect.y > 805:
                    self.clock_spawn()
            if self.rect.x < 105:
                self.clock_spawn()
            if level == 1:
                self.rect.y += 3
            elif level == 2:
                self.rect.y += 4
            elif level == 3:
                self.rect.y += 5
            elif level == 4:
                self.rect.y += 6
            elif level == 5:
                self.rect.y += 7
            elif level == 6:
                self.rect.y += 8
            elif level == 7:
                self.rect.y += 9
            else:
                self.rect.y += level + 1
            if time <= 1: # Game over
                self.kill()

    #Sprite groups        
    player = Hand()
    margin = Border()
    allSprites = pygame.sprite.Group()
    allSprites.add(player, margin)
    Coins_Bronze = pygame.sprite.Group()
    Coins_Silver = pygame.sprite.Group()
    Coins_Golden = pygame.sprite.Group()
    ClockGroup = pygame.sprite.Group()
    BombGroup1 = pygame.sprite.Group()
    BombGroup2 = pygame.sprite.Group()
    BombGroup3 = pygame.sprite.Group()

    #Music
    if random.randint(0, 1) == 0:
        play_music(music2)
    else:
        play_music(music)

    #Objects

    for i in range(8): # BRONZE COIN
        coin_bronze = Coin_Bronze()
       
        coin_bronze.rect.x = random.randrange(640)
        coin_bronze.rect.y = random.randrange(-200, -20)
           
        Coins_Bronze.add(coin_bronze)
     
    if random.randint(0, 1) == 0:
        for i in range(5): # SILVER COIN
            coin_silver = Coin_Silver()
           
            coin_silver.rect.x = random.randrange(640)
            coin_silver.rect.y = random.randrange(-200, -20)
           
            Coins_Silver.add(coin_silver)
    else:
        for i in range(6):
            coin_silver = Coin_Silver()
           
            coin_silver.rect.x = random.randrange(640)
            coin_silver.rect.y = random.randrange(-200, -20)
           
            Coins_Silver.add(coin_silver)
         
    if random.randint(0, 1) == 0:
        for i in range(1): # GOLDEN COIN
            coin_golden = Coin_Golden()
           
            coin_golden.rect.x = random.randrange(640)
            coin_golden.rect.y = random.randrange(-200, -20)
         
            Coins_Golden.add(coin_golden)
    else:
        for i in range(2):
            coin_golden = Coin_Golden()
           
            coin_golden.rect.x = random.randrange(640)
            coin_golden.rect.y = random.randrange(-200, -20)
         
            Coins_Golden.add(coin_golden)
                   
    for i in range(1): # CLOCK
        if time > 100:
         
            clock = Clock()
               
            clock.rect.x = 2000
            clock.rect.y = 2000
               
            ClockGroup.add(clock)    
        else:
            pass
          
    #--BOMB 1--
    if random.randint(0, 1) == 0:
        for i in range(3):
            bomb = Bomb()
     
            bomb.rect.x = random.randrange(640)
            bomb.rect.y = random.randrange(-200, -20)
     
            BombGroup1.add(bomb)
    else:
        for i in range(4):
            bomb = Bomb()
     
            bomb.rect.x = random.randrange(640)
            bomb.rect.y = random.randrange(-200, -20)
     
            BombGroup1.add(bomb)
     
    #--BOMB 2--
    if random.randint(0, 1) == 0:
        for i in range(2):
            bomb2 = Bomb2()
     
            bomb2.rect.x = random.randrange(640)
            bomb2.rect.y = random.randrange(-200, -20)
     
            BombGroup2.add(bomb2)
    else:
        for i in range(3):
            bomb2 = Bomb2()
     
            bomb2.rect.x = random.randrange(640)
            bomb2.rect.y = random.randrange(-200, -20)
     
            BombGroup2.add(bomb2)
     
    #--BOMB 3--
    if random.randint(0, 1) == 0:
        for i in range(1):
            bomb3 = Bomb3()
     
            bomb3.rect.x = random.randrange(640)
            bomb3.rect.y = random.randrange(-200, -20)
     
            BombGroup3.add(bomb3)
    else:
        for i in range(2):
            bomb3 = Bomb3()
     
            bomb3.rect.x = random.randrange(640)
            bomb3.rect.y = random.randrange(-200, -20)
     
            BombGroup3.add(bomb3)

    #Main Loop
    while done == False:
        time -= 0.150
        clock_.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
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
            if event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                if gameover == True:
                    done = True
                    main()
                else:
                    while 1:
                        #pause sound play
                        ren15 = font.render("Paused", 1, (WHITE))
                        screen.blit(ren15, (465-ren.get_width(), 350))
                        pygame.display.update()
                        event = pygame.event.wait()
                        if event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                            break
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 6:
                stop_music()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 7:
                continue_music()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 13:
                gameover = True
                testmode = False
                pygame.sprite.groupcollide(allSprites, Coins_Bronze, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.groupcollide(allSprites, Coins_Silver, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.groupcollide(allSprites, Coins_Golden, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.spritecollide(player, allSprites, True) # Removes the remaining sprites (player)
                time = 0 # Keeps the timer at 0
                if highscore == 0:
                    pass
                if highscore < get_highscore():
                    pass
                else:
                    save_highscore(highscore)
                if score == 0:
                    pass
                else:
                    save_score(score)
                save_level(level)
                save_world(world)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 12:
                if highscore == 0:
                    pass
                if highscore < get_highscore():
                    pass
                else:
                    save_highscore(highscore)
                if score == 0:
                    pass
                else:
                    save_score(score)
                save_level(level)
                save_world(world)
                done = True
                pygame.mixer.music.stop()
                play_music(menumusic)
             
            # Keyboard
            if not hasattr(event, 'key'): continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                ren15 = font.render("Paused", 1, (WHITE))
                screen.blit(ren15, (465-ren.get_width(), 350))
                pygame.display.update()
                if gameover == True:
                    pass
                else:
                    while 1:
                        #pause sound play
                        event = pygame.event.wait()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            break
            elif event.key == K_ESCAPE:
                if highscore == 0:
                    pass
                if highscore < get_highscore():
                    pass
                else:
                    save_highscore(highscore)
                if score == 0:
                    pass
                else:
                    save_score(score)
                save_level(level)
                save_world(world)
                done = True
                pygame.mixer.music.stop()
                play_music(menumusic)
            elif event.key == K_s: #pause music
                stop_music()
            elif event.key == K_c: #unpause / continue music
                continue_music()
            elif event.key == K_q:
                gameover = True
                testmode = False
                pygame.sprite.groupcollide(allSprites, Coins_Bronze, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.groupcollide(allSprites, Coins_Silver, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.groupcollide(allSprites, Coins_Golden, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.spritecollide(player, allSprites, True) # Removes the remaining sprites (player)
                time = 0 # Keeps the timer at 0
                if highscore == 0:
                    pass
                if highscore < get_highscore():
                    pass
                else:
                    save_highscore(highscore)
                if score == 0:
                    pass
                else:
                    save_score(score)
                save_level(level)
                save_world(world)
            elif gameover == True and event.key == K_SPACE:
                gameover = False
                testmode = True
                time = 400 # Reset all the values
                score = 0
                level = 1
                world = 1
                coins_gathered = 0
                coins_gathered2 = 0
                coins_gathered3 = 0
                allSprites.add(player, margin)
                Coins_Bronze.add(coin_bronze)
                Coins_Silver.add(coin_silver)
                Coins_Golden.add(coin_golden)
                ClockGroup.add(clock)
                BombGroup1.add(bomb)
            elif gameover == True and event.key == K_g:
                done = True
                main()
                  
        screen.blit(background, (0, 0))

        font = pygame.font.SysFont("times new roman", 22, bold=True)
        font2 = pygame.font.SysFont("times new roman", 17, bold=True) # score last time font
        font2.set_underline(1)
        ren = font.render("Score%06d" % score, 1, (WHITE))
        ren1 = font.render("Time: %d" % time, 1, (WHITE))
        ren2 = font.render("Time: %d" % time, 1, Color("#ffffff"))
        ren3 = font.render("FPS %d" % clock_.get_fps(), 1, (WHITE))
        ren4 = font.render("x% 02d" % coins_gathered, 1, (WHITE))
        ren5 = font.render("Level %d" % level, 1, (WHITE))
        ren6 = font.render("World %d" % world, 1, (WHITE))
        ren7 = font.render("Beta v2.4", 1, (WHITE))
        ren9 = font.render("x% 02d" % coins_gathered2, 1, (WHITE))
        ren10 = font.render("x% 02d" % coins_gathered3, 1, (WHITE))
        ren11 = font2.render("Score Last Time", 18, (WHITE))
        ren12 = font.render("Score%06d" % get_saved_score(), 1, (WHITE))
        ren13 = font.render("Level %d" % get_saved_level(), 1, (WHITE))
        ren14 = font.render("World %d" % get_saved_world(), 1, (WHITE))
        ren16 = font.render("High Score", 1, (WHITE))
        ren17 = font.render("%06d"  % get_highscore(), 1, (WHITE))
        if testmode == True:
            ren15 = font.render("Test Mode", 1, (WHITE))
            screen.blit(ren15, (460-ren.get_width(), 760))
        screen.blit(ren, (798-ren.get_width(), 52))
        screen.blit(ren1, (677, 0))
        screen.blit(ren2, (677, 0))
        screen.blit(ren3, (700, 770))
        screen.blit(ren4, (780-ren4.get_width(), 70))
        screen.blit(ren5, (800-ren.get_width(), 18))
        screen.blit(ren6, (798-ren.get_width(), 35))
        screen.blit(ren7, (820-ren.get_width(), 750))
        screen.blit(ren9, (780-ren4.get_width(), 90))
        screen.blit(ren10, (780-ren4.get_width(), 110))
        screen.blit(ren11, (798-ren11.get_width(), 155))
        screen.blit(ren12, (797-ren12.get_width(), 175))
        screen.blit(ren13, (750-ren5.get_width(), 195))
        screen.blit(ren14, (757-ren14.get_width(), 215))
        screen.blit(ren16, (798-ren.get_width(), 322))
        screen.blit(ren17, (798-ren.get_width(), 342))
        screen.blit(stats_coin, (677, 75))
        screen.blit(stats_coin2, (677, 95))
        screen.blit(stats_coin3, (677, 115))
        allSprites.draw(screen)
        Coins_Bronze.draw(screen)
        Coins_Silver.draw(screen)
        Coins_Golden.draw(screen)
        ClockGroup.draw(screen)
        BombGroup1.draw(screen)
        BombGroup2.draw(screen)
        BombGroup3.draw(screen)
        player.update()
        Coins_Bronze.update()
        Coins_Silver.update()
        Coins_Golden.update()
        ClockGroup.update()
        BombGroup1.update()
        BombGroup2.update()
        BombGroup3.update()

        if testmode == True:
            pass
        else:
            level = int(score/1500) + 1
            world = int(level/10) + 1

        if time >= 400: # Max time limit
            time = 400
            
        if score <= 0:
            score = 0 # Preventing you to go below 0 in score (-)
            
        if highscore <= 0:
            highscore = 0

        Bronze_Coins = pygame.sprite.spritecollide(player, Coins_Bronze, False)
        for Coin_Bronze in Bronze_Coins :
            score += 50
            highscore += 50
            coins_gathered += 1
            Coin_Bronze.reset_pos()

        Silver_Coins = pygame.sprite.spritecollide(player, Coins_Silver, False)
        for Coin_Silver in Silver_Coins:
            score += 100
            highscore += 100
            coins_gathered2 += 1
            Coin_Silver.reset_pos()

        Golden_Coins = pygame.sprite.spritecollide(player, Coins_Golden, False)
        for Coin_Golden in Golden_Coins:
            score += 200
            highscore += 200
            coins_gathered3 += 1
            Coin_Golden.reset_pos()

        Clock_timer = pygame.sprite.spritecollide(player, ClockGroup, False)
        for Clock in Clock_timer:
            time += 50
            Clock.clock_spawn()

        Bomb_collision = pygame.sprite.spritecollide(player, BombGroup1, False)
        for Bomb in Bomb_collision:
            score -= 150
            highscore -= 150
            Bomb.bomb_spawn()
     
        Bomb_collision = pygame.sprite.spritecollide(player, BombGroup2, False)
        for Bomb in Bomb_collision:
            score -= 150
            highscore -= 150
            Bomb.bomb2_spawn()
     
        Bomb_collision = pygame.sprite.spritecollide(player, BombGroup3, False)
        for Bomb in Bomb_collision:
            score -= 150
            highscore -= 150
            Bomb.bomb3_spawn()
        
        if time <= 0: # Game over
                gameover = True
                pygame.sprite.groupcollide(allSprites, Coins_Bronze, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.groupcollide(allSprites, Coins_Silver, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.groupcollide(allSprites, Coins_Golden, True, True) # Removes the coin + allsprites sprites.
                pygame.sprite.spritecollide(player, allSprites, True) # Removes the remaining sprites (player)
                time = 0 # Keeps the timer at 0
                ren = font.render("Your stats", 1, (WHITE))
                screen.blit(ren, (776-ren.get_width(), 130))
                fontGameover = pygame.font.SysFont("times new roman", 28, bold=True)
                ren = fontGameover.render("GAME OVER", 1, (WHITE))
                ren2 = fontGameover.render("Press Esc to exit", 1, (WHITE))
                ren3 = fontGameover.render("Press G to play again", 1, (WHITE))
                screen.blit(ren, (495-ren.get_width(), 355))
                screen.blit(ren2, (485-ren.get_width(), 760))
                screen.blit(ren3, (465-ren.get_width(), 720))
                if highscore == 0:
                    pass
                if highscore < get_highscore():
                    pass
                else:
                    save_highscore(highscore)
                if score == 0:
                    pass
                else:
                    save_score(score)
                save_level(level)
                save_world(world)
        
        pygame.display.update()
