#! /usr/bin/env python

# PyGU (Python Game Utilities) - A set of python libraries for use with pygame
# Copyright (C) 2007  Michael J. Burns
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#-------------------------------------------



import math

import pygame
from pygame.locals import *



"A basic sprite like the pygame one with some extra functions."
class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)




    def move(self, xspeed, yspeed):
        self.rect.move_ip(xspeed, yspeed)




    def draw(self, surface):
        if self.alive():
            surface.blit(self,image, self.rect)




    def wrap(self, surface):

        if self.rect.left >= surface.get_width():
            self.rect.right = 0

        if self.rect.right < 0:
            self.rect.left = surface.get_width() - 1          


        if self.rect.top >= surface.get_height():
            self.yrect.bottom = 0

        if self.rect.bottom < 0:
            self.rect.top = surface.get_height() - 1




    def clamp(self, surface):
        surf_rect = surface.get_rect()
        self.rect = self.rect.clamp(surf_rect)

     

    def kill_offscreen(self, surface):

        if self.rect.left >= surface.get_width():
            self.kill()
        if self.rect.right < 0:
            self.kill()


        if self.rect.top >= surface.get_height():
            self.kill()
        if self.rect.bottom < 0:
            self.kill()



    def set_pos(self, x, y):
        self.rect.topleft = (x, y)



    def check_top(self, other, y_velocity, y_speed):
        if y_speed < 0 and \
               (self.rect.bottom - y_velocity < other.rect.top <= self.rect.bottom):
            return True
        else:
            return 0

    def check_bottom(self, other, y_velocity, y_speed):
        if y_speed > 0 and \
           (self.rect.top + y_velocity > other.rect.bottom >= self.rect.top):
            return True
        else:
            return 0

    def check_left(self, other, x_speed, y_velocity):
        if other.rect.right < self.rect.right:
            if x_speed < 0 and self.rect.bottom > other.rect.bottom - y_velocity and self.rect.top < other.rect.top + y_velocity + 1:
                return True
        else:
            return 0

    def check_right(self, other, x_speed, y_velocity):
        if other.rect.left > self.rect.left:
            if x_speed > 0 and self.rect.bottom > other.rect.bottom - y_velocity and self.rect.top < other.rect.top + y_velocity + 1:
                return True
        else:
            return 0




"""Unlike the pygame sprite, this sprite will move to floating point numbers.
There are a few limitations right now, but it works pretty good and there
are a few extra features in this sprite that aren't in the pygame sprite."""
class SensitiveSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)




    def move(self, xspeed, yspeed):
        self.x += xspeed
        self.y += yspeed




    def draw(self, surface):
        if self.alive():
            surface.blit(self,image, self.rect)




    def update(self, surface):
        self.rect = self.image.get_rect(center = (self.x, self.y))




    def wrap(self, surface):

        if self.x >= surface.get_width() + self.image.get_width()/2:
            self.x = -self.image.get_width()

        if self.x < -self.image.get_width():
            self.x = surface.get_width() + self.image.get_width()/2 - 1          


        if self.y >= surface.get_height() + self.image.get_height()/2:
            self.y = -self.image.get_height()

        if self.y < -self.image.get_height():
            self.y = surface.get_height() + self.image.get_height()/2 - 1




    def clamp(self, surface):

        if self.x >= surface.get_width() - self.image.get_width()/2:
            self.x = surface.get_width() - self.image.get_width()/2

        if self.x <= self.image.get_width()/2:
            self.x = self.image.get_width()/2


        if self.y >= surface.get_height() - self.image.get_height()/2:
            self.y = surface.get_height() - self.image.get_height()/2

        if self.y <= self.image.get_height()/2:
            self.y = self.image.get_height()/2

     

    def kill_offscreen(self, surface):

        if self.x >= surface.get_width() + self.image.get_width()/2:
            self.kill()
        if self.x < -self.image.get_width():
            self.kill()   

        if self.y >= surface.get_height() + self.image.get_height()/2:
            self.kill()
        if self.y < -self.image.get_height():
            self.kill()



    def set_pos(self, x, y):
        self.x = x
        self.y = y



"""This is an overhead rotatable spaceship sprite, which controls like
the ship in Asteroids. The spaceship sprite moves with inertia only,
so if you want just an overhead rotatable object, use the RotatableSprite
object."""
class RotatableSpaceship(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self, self.containers)

        self.x_velocity = 0
        self.y_velocity = 0

        self.x = 0
        self.y = 0

        self.angle = 0


 
    def draw(self, surface):
        if self.alive():
            surface.blit(self.image, self.rect)
        



    def update(self, surface):

        self.rect = self.image.get_rect(center = (self.x, self.y))
        
        self.key = pygame.key.get_pressed()

        if self.angle > 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360




    def add_inertia(self):

        self.x += float(self.x_velocity)
        self.y += float(self.y_velocity)




    def cap_speed(self, max_speed):

        abs_vel = 0.0
        abs_vel += pow(self.x_velocity,2)+ pow(self.y_velocity,2) 
        if abs_vel > pow(max_speed,2):
            ratio = pow(max_speed,2)/abs_vel 
            self.x_velocity *= ratio
            self.y_velocity *= ratio




    def wrap(self, surface):

        if self.x >= surface.get_width() + self.image.get_width()/2:
            self.x = -self.image.get_width()
        if self.x < -self.image.get_width():
            self.x = surface.get_width() + self.image.get_width()/2 - 1          

        if self.y >= surface.get_height() + self.image.get_height()/2:
            self.y = -self.image.get_height()
        if self.y < -self.image.get_height():
            self.y = surface.get_height() + self.image.get_height()/2 - 1




    def kill_offscreen(self, surface):

        if self.x >= surface.get_width() + self.image.get_width()/2:
            self.kill()
        if self.x < -self.image.get_width():
            self.kill()   

        if self.y >= surface.get_height() + self.image.get_height()/2:
            self.kill()
        if self.y < -self.image.get_height():
            self.kill()




    def rotate(self, amount, original_image):

        self.oldCenter = self.rect.center

        self.angle += amount
        self.image = pygame.transform.rotate(original_image, self.angle)

        self.rect = self.image.get_rect()
        self.rect.center = self.oldCenter




    def accelerate(self, accel_speed):
        self.x_velocity = self.x_velocity + (math.sin(self.angle*2*math.pi/360)*-accel_speed)
        self.y_velocity = self.y_velocity + (math.cos(self.angle*2*math.pi/360)*-accel_speed)




    def deccelerate(self, deccel_speed):
        self.x_velocity = self.x_velocity + (math.sin(self.angle*2*math.pi/360)*deccel_speed)
        self.y_velocity = self.y_velocity + (math.cos(self.angle*2*math.pi/360)*deccel_speed)



    def set_pos(self, x, y):
        self.x = x
        self.y = y



    def set_angle(self, angle):
        self.angle = angle



    def set_image(self, image):
        self.image = image



    def get_pos(self):
        return self.x, self.y



    def get_angle(self):
        return self.angle



    def get_image(self):
        return self.image




"""This is a sprite that makes creating overhead rotatable objects
alot easier."""
class RotatableSprite(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self, self.containers)

 
    def draw(self, surface):
        if self.alive():
            surface.blit(self.image, self.rect)
        


    def update(self, surface):

        self.rect = self.image.get_rect(center = (self.x, self.y))
        
        self.key = pygame.key.get_pressed()

        if self.angle > 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360



    def wrap(self, surface):

        if self.x >= surface.get_width() + self.image.get_width()/2:
            self.x = -self.image.get_width()
        if self.x < -self.image.get_width():
            self.x = surface.get_width() + self.image.get_width()/2 - 1          

        if self.y >= surface.get_height() + self.image.get_height()/2:
            self.y = -self.image.get_height()
        if self.y < -self.image.get_height():
            self.y = surface.get_height() + self.image.get_height()/2 - 1



    def kill_offscreen(self, surface):

        if self.x >= surface.get_width() + self.image.get_width()/2:
            self.kill()
        if self.x < -self.image.get_width():
            self.kill()   

        if self.y >= surface.get_height() + self.image.get_height()/2:
            self.kill()
        if self.y < -self.image.get_height():
            self.kill()



    def rotate(self, amount, original_image):

        self.oldCenter = self.rect.center

        self.angle += amount
        self.image = pygame.transform.rotate(original_image, self.angle)

        self.rect = self.image.get_rect()
        self.rect.center = self.oldCenter



    def move_forward(self, speed, angle):
        self.x = self.x + (math.sin(angle*2*math.pi/360)*-speed)
        self.y = self.y + (math.cos(angle*2*math.pi/360)*-speed)



    def move_backward(self, speed, angle):
        self.x = self.x + (math.sin(angle*2*math.pi/360)*speed)
        self.y = self.y + (math.cos(angle*2*math.pi/360)*speed)


    def init_rect(self):
        return self.image.get_rect(center = (self.x, self.y))



    def set_pos(self, x, y):
        self.x = x
        self.y = y



    def set_angle(self, angle):
        self.angle = angle



    def set_image(self, image):
        self.image = image



    def get_pos(self):
        return self.x, self.y



    def get_angle(self):
        return self.angle



    def get_image(self):
        return self.image



"In alpha right now. Only for MarioWorld style games."
class PlatformJumper(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self, self.containers)

        self.jump_speed = 0
        self.jumping = False
        self.walk_speed = 0
        self.facing = 0



    def check_bottom(self, other, y_velocity):

        if self.jump_speed < 0 and \
               (self.rect.bottom - y_velocity < rect.top <= self.rect.bottom):
            return True
        else:
            return 0


    def check_top(self, other, y_velocity):
        if self.jump_speed > 0 and \
           (self.rect.top + y_velocity > rect.bottom >= self.rect.top):
            return True
        else:
            return 0

    def check_left(self, other):
        if self.walk_speed > 0 and \
           (rect.left > self.rect.left or \
           rect.right < self.rect.right):
            if self.walk_speed < 0:
                return True
        else:
            return 0

    def check_right(self, other):
        if self.walk_speed < 0 and \
           (rect.left > self.rect.left or \
           rect.right < self.rect.right):
            if self.walk_speed > 0:
                return True
        else:
            return 0



"Pixel perfect collision detection."
def PixelPerfectCollisionDetection(sp1, sp2):

    rect1 = sp1.rect;     
    rect2 = sp2.rect;                            
    rect  = rect1.clip(rect2)
            
    x1 = rect.x-rect1.x
    y1 = rect.y-rect1.y
    x2 = rect.x-rect2.x
    y2 = rect.y-rect2.y

    for r in xrange(0, rect.height):      
        for c in xrange(0, rect.width):

            if sp1.image.get_at((c+x1, r+y1))[3] & sp2.image.get_at((c+x2, r+y2))[3]:
                return 1        

    return 0

"Perfect collision detection for a sprite and a group."
def spritecollide_pp(sprite, group, dokill):

    crashed = []
    spritecollide = sprite.rect.colliderect
    ppcollide = PixelPerfectCollisionDetection
    if dokill:
        for s in group.sprites():
            if spritecollide(s.rect):
                if ppcollide(sprite, s):
                    s.kill()
                    crashed.append(s)
    else:
        for s in group.sprites():
            if spritecollide(s.rect):
                if ppcollide(sprite, s):
                    crashed.append(s)
    return crashed

"Perfect collision detection for two groups of sprites."
def groupcollide_pp(groupa, groupb, dokilla, dokillb):

    crashed = {}
    SC = spritecollide_pp
    if dokilla:
        for s in groupa.sprites():
            c = SC(s, groupb, dokillb)
            if c:
                crashed[s] = c
                s.kill()
    else:
        for s in groupa.sprites():
            c = SC(s, groupb, dokillb)
            if c:
                crashed[s] = c
    return crashed


"Same as spritecollideany in pygame but with pixelperfect collisions."
def spritecollideany_pp(sprite, group):

    spritecollide = sprite.rect.colliderect
    ppcollide = PixelPerfectCollisionDetection    
    for s in group.sprites():
        if spritecollide(s.rect):
            if ppcollide(sprite, s):
                return s
    return None


"Perfect collision detection for two single sprites."
def dualspritecollide_pp(sprite1, sprite2):

    spritecollide = sprite1.rect.colliderect
    ppcollide = PixelPerfectCollisionDetection    
    if spritecollide(sprite2.rect):
        if ppcollide(sprite1, sprite2):
            return True
    return None


"Collision detection for a sprite and a group."
def spritecollide(sprite, group, dokill):

    crashed = []
    spritecollide = sprite.rect.colliderect
    ppcollide = PixelPerfectCollisionDetection
    if dokill:
        for s in group.sprites():
            if spritecollide(s.rect):
                s.kill()
                crashed.append(s)
    else:
        for s in group.sprites():
            if spritecollide(s.rect):
                crashed.append(s)
    return crashed


"Collision detection for two groups of sprites."
def groupcollide(groupa, groupb, dokilla, dokillb):

    crashed = {}
    SC = spritecollide
    if dokilla:
        for s in groupa.sprites():
            c = SC(s, groupb, dokillb)
            if c:
                crashed[s] = c
                s.kill()
    else:
        for s in groupa.sprites():
            c = SC(s, groupb, dokillb)
            if c:
                crashed[s] = c
    return crashed


"Same as pygame's spritecollideany."
def spritecollideany(sprite, group):

    spritecollide = sprite.rect.colliderect
    for s in group.sprites():
        if spritecollide(s.rect):
            return s
    return None


"Collision detection for two single sprites."
def dualspritecollide(sprite1, sprite2):

    spritecollide = sprite1.rect.colliderect  
    if spritecollide(sprite2.rect):
        return True
    return None
