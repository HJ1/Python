import os, sys
import pygame
from pygame.locals import *

def draw_colors(screen,x,y):
    #Colors
    White = [255, 255, 255]
    Blue = [0, 0, 255]
    Green = [0, 255, 0]
    Red = [255, 0, 0]
    Yellow = [255, 255, 0]
    Purple = [255, 0, 255]

    #Drawing the shapes
    pygame.draw.rect(screen, Blue, [0+x, 0+y, 25, 25], 2)
    pygame.draw.rect(screen, Green, [55+x, 0+y, 25, 25], 2)
    pygame.draw.rect(screen, Red, [110+x, 0+y, 25, 25], 2)
    pygame.draw.rect(screen, Yellow, [165+x, 0+y, 25, 25], 2)
    pygame.draw.rect(screen, Purple, [220+x, 0+y, 25, 25], 2)
    pygame.draw.rect(screen, White, [270+x, 0+y, 25, 25], 2)

    pygame.draw.arc(screen, Blue, [0+x, 45+y,25,25], 90, 180, 2)
    pygame.draw.arc(screen, Green, [55+x, 45+y,25,25], 90, 180, 2)
    pygame.draw.arc(screen, Red, [110+x, 45+y,25,25], 90, 180, 2)
    pygame.draw.arc(screen, Yellow, [165+x, 45+y,25,25], 90, 180, 2)
    pygame.draw.arc(screen, Purple, [220+x, 45+y,25,25], 90, 180, 2)
    pygame.draw.arc(screen, White, [270+x, 45+y,25,25], 90, 180, 2)
    
    pygame.draw.circle(screen, Blue, [12+x, 100+y], 12)
    pygame.draw.circle(screen, Green, [67+x, 100+y], 12)
    pygame.draw.circle(screen, Red, [122+x, 100+y], 12)
    pygame.draw.circle(screen, Yellow, [177+x, 100+y], 12)
    pygame.draw.circle(screen, Purple, [232+x, 100+y], 12)
    pygame.draw.circle(screen, White, [282+x, 100+y], 12)

    pygame.draw.ellipse(screen, Blue, [0+x, 130+y, 25, 50], 2)
    pygame.draw.ellipse(screen, Green, [55+x, 130+y, 25, 50], 2)
    pygame.draw.ellipse(screen, Red, [110+x, 130+y, 25, 50], 2)
    pygame.draw.ellipse(screen, Yellow, [165+x, 130+y, 25, 50], 2)
    pygame.draw.ellipse(screen, Purple, [220+x, 130+y, 25, 50], 2)
    pygame.draw.ellipse(screen, White, [270+x, 130+y, 25, 50], 2)

    pygame.draw.ellipse(screen, Blue, [0+x, 195+y, 25, 50])
    pygame.draw.ellipse(screen, Green, [55+x, 195+y, 25, 50])
    pygame.draw.ellipse(screen, Red, [110+x, 195+y, 25, 50])
    pygame.draw.ellipse(screen, Yellow, [165+x, 195+y, 25, 50])
    pygame.draw.ellipse(screen, Purple, [220+x, 195+y, 25, 50])
    pygame.draw.ellipse(screen, White, [270+x, 195+y, 25, 50])

    pygame.draw.line(screen, Blue, (11+x, 270+y), (11+x, 300+y), 2)
    pygame.draw.line(screen, Green, (66+x, 270+y), (66+x, 300+y), 2)
    pygame.draw.line(screen, Red, (121+x, 270+y), (121+x, 300+y), 2)
    pygame.draw.line(screen, Yellow, (176+x, 270+y), (176+x, 300+y), 2)
    pygame.draw.line(screen, Purple, (231+x, 270+y), (231+x, 300+y), 2)
    pygame.draw.line(screen, White, (281+x, 270+y), (281+x, 300+y), 2)

def app():
    pygame.init()    
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.display.set_caption("Shapes and Colors")
    screen = pygame.display.set_mode((320, 340)) 
    pygame.mouse.set_visible(0)
    running = True
    draw_colors(screen, 10, 10)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False, sys.exit(0)
            if not hasattr(event, 'key'): continue
            if event.key == K_ESCAPE: sys.exit(0)
            
if __name__=="__main__":
    app()

# end.


