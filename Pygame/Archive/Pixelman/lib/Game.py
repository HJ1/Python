#! usr/bin/env python

import os, sys
import random

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

import Menu, Level_Select, Credits
from Player import *
from Game_Objects import *
from Helper import *
from Level import *

SCORE = 0
COINS = 0
LEVEL = 1
LEVEL_UP = False
DEAD = False
DIALOGUE = False
DIAL_PROG = 0
LETTER = 0
PAUSED = False
dialogue = ''
messages = []
TICKS = 0

unl_levels = os.path.expanduser('~/levels.pixelman')
if os.path.exists(unl_levels):
    unl_levels = int(open(unl_levels).read())
else:
    unl_levels = open(unl_levels, 'w').write(str(1))
UNLOCKED = unl_levels

def Game(screen, level):

    pygame.init()
    pygu.display.center_window()
    
    font = pygu.font.Font(None, 20*Locals.scale)
    font2 = pygu.font.BitmapFont('data/Font%d.bmp' % (1*Locals.scale), WHITE, 6*Locals.scale, 9*Locals.scale,
                                 '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!?:;/[]()+-*=\'" ')
    font3 = pygu.font.BitmapFont('data/Font%d.bmp' % (1*Locals.scale), BLACK, 6*Locals.scale, 9*Locals.scale,
                                 '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!?:;/[]()+-*=\'" ')

    platforms = pygame.sprite.Group()
    spikes = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    bombers = pygame.sprite.Group()
    booms = pygame.sprite.Group()
    virus = pygame.sprite.Group()

    for s in sprites: s.kill()
    for v in virus: v.kill()

    Player.containers = innerlayer, sprites
    Platform.containers = innerlayer, platforms, sprites
    Spikes.containers = innerlayer, spikes, sprites
    Coin.containers = innerlayer, coins, sprites
    Boom.containers = innerlayer, booms, sprites
    Bomber.containers = innerlayer, bombers, sprites
    Bomber.platforms = platforms
    VIRUS.containers = innerlayer, virus, sprites
    VIRUS_DIE.containers = innerlayer, booms, sprites
    VIRUS.platforms = platforms

    global SCORE, COINS, LEVEL_UP, LEVEL, DEAD, TICKS, messages
    global PAUSED, UNLOCKED, DIALOGUE, DIAL_PROG, LETTER, dialogue
    SCORE = COINS = LEVEL_UP = DEAD = 0
    clock = pygame.time.Clock()

    SCORE = 0
    COINS = 0
    LEVEL_UP = False
    DEAD = False
    DIALOGUE = False
    DIAL_PROG = 0
    LETTER = 0
    PAUSED = False
    dialogue = ''
    messages = []
    lastmsg = ''
    TICKS = 0
    key_grabbed = False

    LEVEL = level

    unl_levels = os.path.expanduser('~/levels.pixelman')
    if os.path.exists(unl_levels):
        unl_levels = int(open(unl_levels).read())
    else:
        unl_levels = open(unl_levels, 'w').write(str(1))
    UNLOCKED = unl_levels
    DIAL_PROG = 0
    DIALOGUE = True


    for s in sprites: s.kill()
    for v in virus: v.kill()

    level = Level('data/floor %d.lvl' % LEVEL)
    player = level.player
    camera = pygu.camera.Camera(screen, player, (640*Locals.scale, 240*Locals.scale))

    screen.fill((0,0,0))
    dialogue_screen = load_image('Dialogue Menu.bmp')
    boom_sound = pygu.sound.load_sound('data/Boom.wav')

    nextlevel_img = load_image('Next Level!.bmp')
    crashed_img = load_image('You Crashed!.bmp')

    ren = font.render('Level ' + str(LEVEL), 1, WHITE)
    screen.blit(ren, (96*Locals.scale - ren.get_width()/2, 70*Locals.scale - ren.get_height()/2))

    ren = font2.render(level.name)
    screen.blit(ren, (96*Locals.scale - ren.get_width()/2, 90*Locals.scale - ren.get_height()/2))
    pygame.display.flip()
    pygame.time.wait(2000)

    you_win = False

    pygame.mixer.stop()
    if LEVEL < 10:
        pygu.sound.play_sound('data/Ingame.ogg', 1.0, True)
    if LEVEL == 10:
        pygu.sound.play_sound('data/Boss.ogg', 1.0, True)


    while 1:

        Bomber.platforms = platforms

        "Cap the framerate."
        clock.tick(60)
        TICKS += 1


        "Update the sprites."
        if not PAUSED:
            pygu.display.update_sprites(screen)

        "Get input."
        event = pygame.event.poll()

        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Level_Select.Level_Select(screen, LEVEL)

            if event.key == K_SPACE:
                key_grabbed = True
                TICKS = 2
                if not PAUSED:
                    player.jump()
            if event.key == K_RETURN:
                DIALOGUE = False
                PAUSED = False
            if event.key == K_p:
                PAUSED = not PAUSED
        if event.type == KEYUP:
            key_grabbed = False

        keystate = pygame.key.get_pressed()
        moving = keystate[K_RIGHT] - keystate[K_LEFT]
        if not PAUSED: player.step(moving)

        if player.jump_speed > player.max_fallspeed:
            if keystate[K_SPACE]:
                player.jump_speed -= player.kdown_fall_speed
            else:
                player.jump_speed -= player.kup_fall_speed

        for platform in platforms:
            if player.rect.colliderect(platform.rect):
                if platform.check_fall:
                    player.check_fall(platform)
                if platform.check_ceiling:
                    player.check_jump(platform)
                if platform.check_sides:
                    player.check_leftwalk(platform, moving)
                    player.check_rightwalk(platform, moving)

        for spike in spikes:
            if player.rect.colliderect(spike.rect):
                player.check_fall_on_spikes(spike)
                player.check_jump(spike)
                player.check_leftwalk(spike, moving)
                player.check_rightwalk(spike, moving)

        if player.rect.top >= camera.world_size[1] and player.alive():
            player.kill()
            camera.center_sprite = False
            DEAD = True

        for v in pygu.sprite.spritecollide(player, virus, 1):
            if player.jump_speed < 0 and player.jumping:
                player.jump_speed = 5*Locals.scale
                player.jumping = True
                boom_sound.play()
                if v.hp <= 0:
                    you_win = True
            else:
                boom_sound.play()
                player.image = load_image('Pixelman 4.bmp', True)
                DEAD = True

        if pygu.sprite.spritecollide(player, coins, 1):
            player.coin_sound.play()
            SCORE += 25
            COINS += 1

        for b in pygu.sprite.spritecollide(player, bombers, 1):
            if player.jump_speed < 0 and player.jumping:
                player.jump_speed = 3*Locals.scale
                boom_sound.play()
                Boom(b.rect.center)
            else:
                boom_sound.play()
                Boom(b.rect.center)
                player.image = load_image('Pixelman 4.bmp', True)
                DEAD = True


        if LEVEL_UP == True:
            for s in sprites: s.kill()
            screen.blit(nextlevel_img, (0, 0))
            pygame.display.flip()
            pygame.time.wait(1250)
            Level_Select.Level_Select(screen, LEVEL)


        "Draw the scene."
        screen.fill((0, 0, 0))

        camera.draw_group(platforms)
        camera.draw_group(spikes)
        camera.draw_group(coins)
        camera.draw_group(bombers)
        camera.draw_group(booms)
        camera.draw_group(virus)
        camera.draw_sprite(player)

        ren = font2.render('SCORE: %06d' % SCORE)
        screen.blit(ren, (10, 10))

        messages = [lastmsg]

        if TICKS >= 3:
            TICKS = 0


        "Draw the dialogue to the screen. (This is REALLY complicated)."
        if DIALOGUE:
            try:
                PAUSED = True
                d = level.dialogue[DIAL_PROG]
                dial = d[LETTER]
                if TICKS == 2 and not keystate[K_SPACE]:
                    LETTER += 1
                    dialogue += dial
                if event.type == KEYDOWN and event.key == K_SPACE:
                    LETTER = 100
                    dialogue = d
                ren = font2.render(dialogue)
                screen.blit(dialogue_screen, (0, 0))
                screen.blit(ren, (7*Locals.scale, 70*Locals.scale - ren.get_height()/2))
            except:
                if dialogue == '':
                    DIALOGUE = False
                    PAUSED = False
                if event.type == KEYDOWN and event.key == K_SPACE:
                    lastmsg = dialogue
                    DIAL_PROG += 1
                    LETTER = 0
                    dialogue = ''
                ren = font2.render(dialogue)
                screen.blit(dialogue_screen, (0, 0))
                screen.blit(ren, (7*Locals.scale, 70*Locals.scale - ren.get_height()/2))
            pygame.draw.rect(screen, (255, 255, 255), [2*Locals.scale, 50*Locals.scale, 186*Locals.scale, 30*Locals.scale], 1*Locals.scale)
            ren = font2.render(lastmsg)
            screen.blit(ren, (7*Locals.scale, 60*Locals.scale - ren.get_height()/2))
            pygame.draw.line(screen, WHITE, (60*Locals.scale, 80*Locals.scale), (50*Locals.scale, 90*Locals.scale), 1*Locals.scale)

        "Lose."
        if DEAD:
            screen.blit(crashed_img, (0, 0))
            pygame.display.flip()
            pygame.time.wait(1250)
            Level_Select.Level_Select(screen, LEVEL)

        "Win."
        if player.rect.left >= camera.world_size[0] and player.alive():
            LEVEL += 1
            if LEVEL > UNLOCKED:
                UNLOCKED = open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(LEVEL))
            if LEVEL > 10:
                UNLOCKED = open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(10))
            LEVEL_UP = True
            player.kill()


        if you_win and not booms and not player.jumping:
            for s in sprites: s.kill()
            player.kill()
            pygame.display.flip()
            screen.fill((0, 0, 0))
            ren = font.render('Congratulations!', 1, WHITE)
            screen.blit(ren, (96*Locals.scale - ren.get_width()/2, 70*Locals.scale - ren.get_height()/2))
            ren = font.render('You beat the game!', 1, WHITE)
            screen.blit(ren, (96*Locals.scale - ren.get_width()/2, 90*Locals.scale - ren.get_height()/2))
            pygame.display.flip()
            pygame.time.wait(1500)
            Credits.Credits(screen)
            Menu.Menu(screen)


        if not PAUSED: camera.update()

        #pygame.draw.rect(screen, WHITE, [0, 0, 192, 160], 1)
        
        pygame.display.flip()


if __name__ == '__main__':
    Game()
