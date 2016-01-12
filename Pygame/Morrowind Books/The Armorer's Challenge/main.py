#! /usr/bin/env python
import pygame, os, sys
from pygame.locals import *
pygame.init()

# Special thanks to PyMike for making the "cutscenes" file.

os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Morrowind Book: The Armorer's Challenge")
pygame.display.set_icon(pygame.image.load("The Armorer's Challenge.png"))
pygame.mouse.set_visible(0)
pygame.mixer.init()
pygame.mixer.music.load("Morrowind.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0) # 0.0 = Muted - Alt annet styrer Vol

#######################################################################################################################################################

def cutscene(screen, text):
    pygame.font.init()
    font = pygame.font.Font("Magic Cards.ttf", 18, bold=True)
    black = pygame.Surface((800, 800))
    black.fill((0, 0, 0))
    alpha = 255
    intro = True
    outro = False
    image2 = pygame.image.load("The Armorer's Challenge.png")
    height = len(text)*(font.get_height()+3)
    image = pygame.Surface((800, height))
    y = 0
    for line in text:
        ren = font.render(line, 1, (255, 255, 255))
        image.blit(ren, (50-ren.get_width()/2, y*(font.get_height()+3)))
        y += 1
    while 1:
        pygame.time.wait(10)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == K_c:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    return sys.exit(0)
                if e.key in (K_SPACE, K_RETURN):
                    intro = False
                    outro = True
                if e.key == K_s:
                    pygame.mixer.music.stop()
                if e.key == K_p:
                    pygame.mixer.music.play(-1) # restarts the music
        if intro:
            if alpha > 0:
                alpha -= 5
        if outro:
            if alpha < 255:
                alpha += 5
            else:
                return
        black.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(image, (0, 240-image.get_height()/2))
        screen.blit(black, (0, 0))
        screen.blit(image2, (5, 5))
        ren = font.render("Press enter to continue", 1, (255, 255, 255))
        screen.blit(ren, (400-ren.get_width()/2, 775))
        pygame.display.flip()
 
#######################################################################################################################################################

cutscene(screen, ["",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "                                                                                                                     The Armorer's Challenge",
                  "",
                  "                                                                                                                         by Mymophonus",
                  "",
                  "                                                                                                                     A competition between two skilled armorsmiths",
"",
"",
"",
"                                                                                                                       Three hundred years ago, when Katariah became Empress, the first and only Dunmer to rule all of Tamriel,",
"                                                                                                                       she faced opposition from the Imperial Council. Even after she convinced them that she would be",
"                                                                                                                       the best regent to rule the Empire while her husband Pelagius sought treatment for his madness,",
"                                                                                                                       there was still conflict. In particular from the Duke of Vengheto, Thane Minglumire,",
"                                                                                                                       who took a particular delight in exposing all of the Empress's lack of practical knowledge.",
"                                                                                                                       In this particular instance, Katariah and the Council were discussing the unrest",
"                                                                                                                       in Black Marsh and the massacre of Imperial troops outside the village of Armanias.",
"                                                                                                                       The sodden swampland and the sweltering climate, particular in summertide, would endanger the troops",
"                                                                                                                       if they wore their usual armor. I know a very clever armorer, said Katariah,",
"                                                                                                                       His name is Hazadir, an Argonian who knows the environments our army will be facing.",
"                                                                                                                       I knew him in Vivec where he was a slave to the master armorer there,",
"                                                                                                                       before he moved to the Imperial City as a freedman. We should have him design armor and weaponry",
"                                                                                                                       for the campaign. Minglumire gave a short, barking laugh: She wants a slave to design the armor and",
"                                                                                                                      weaponry for our troops! ' Sirollus Saccus is the finest armorer in the Imperial City. Everyone knows that.'",
"                                                                                                                       After much debate, it was finally decided to have both armorers contend for the commission.",
"                                                                                                                       The Council also elected two champions of equal power and prowess, Nandor Beraid and Raphalas Eul,",
"                                                                                                                       to battle using the arms and armaments of the real competitors in the struggle.",
"                                                                                                                       Whichever champion won, the armorer who supplied him would earn the Imperial commission.",
"                                                                                                                       It was decided that Beraid would be outfitted by Hazadir, and Eul by Saccus.",
"                                                                                                                       The fight was scheduled to commence in seven days.",
])

cutscene(screen, ["",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
"                                                                                                                       Sirollus Saccus began work immediately. He would have preferred more time,",
"                                                                                                                       but he recognized the nature of the test. The situation in Armanias was urgent.",
"                                                                                                                       The Empire had to select their armorer quickly, and once selected, the preferred armorer had to act swiftly",
"                                                                                                                       and produce the finest armor and weaponry for the Imperial army in Black Marsh.",
"                                                                                                                       It wasn't just the best armorer they were looking for. It was the most efficient.",
"                                                                                                                       Saccus had only begun steaming the half-inch strips of black virgin oak to bend into",
"                                                                                                                       bands for the flanges of the armor joints when there was a knock at his door.",
"                                                                                                                       His assistant Phandius ushered in the visitor. It was a tall reptilian of common markings, a dull,",
"                                                                                                                       green-fringed hood, bright black eyes, and a dull brown cloak. It was Hazadir, Katariah's preferred armorer.",
"                                                                                                                       I wanted to wish you the best of luck on the - is that ebony?",
"                                                                                                                       It was indeed. Saccus had bought the finest quality ebony weave available in the Imperial City",
"                                                                                                                       as soon as he heard of the competition and had begun the process of smelting it.",
"                                                                                                                       Normally it was a six-month procedure refining the ore, but he hoped that a massive convection oven",
"                                                                                                                       stoked by white flames born of magicka would shorten the operation to three days.",
"                                                                                                                       Saccus proudly pointed out the other advancements in his armory.",
"                                                                                                                       The acidic lime pools to sharpen the blade of the dai-katana",
"                                                                                                                       to an unimaginable degree of sharpness. The Akaviri forge and tongs he would use to fold",
"                                                                                                                       the ebony back and forth upon itself. Hazadir laughed. Have you been to my armory?",                
"                                                                                                                       It's two tiny smoke-filled rooms. The front is a shop.",
"                                                                                                                       The back is filled with broken armor, some hammers, and a forge. That's it.",
"                                                                                                                       That's your competition for the millions of gold pieces in Imperial commission.",
"                                                                                                                       I'm sure the Empress has some reason to trust you to outfit her troops, said Sirollus Saccus, kindly.",
"                                                                                                                       He had, after all, seen the shop and knew that what Hazadir said was true.",
"                                                                                                                       It was a pathetic workshop in the slums, fit only for the lowliest of adventurers",
"                                                                                                                       to get their iron daggers and cuirasses repaired.",
"                                                                                                                       Saccus had decided to make the best quality regardless of the inferiority of his rival.",
"                                                                                                                       It was his way and how he became the best armorer in the Imperial City.",
"                                                                                                                       Out of kindness, and more than a bit of pride, Saccus showed Hazadir how, by contrast,",
"                                                                                                                       things should be done in a real professional armory. The Argonian acted as an apprentice to Saccus,",
"                                                                                                                       helping him refine the ebony ore, and to pound it and fold it when it cooled.",
])

cutscene (screen, ["",
"                                                                                                                       Over the next several days, they worked together to create a beautiful dai-katana",
"                                                                                                                       with an edge honed sharp enough to trim a mosquito's eyebrows, enchanted with flames",
"                                                                                                                       along its length by one of the Imperial Battlemages, as well as a suit of armor",
"                                                                                                                       of bound wood, leather, silver, and ebony to resist the winds of Oblivion.",
"                                                                                                                       On the day of the battle, Saccus, Hazadir, and Phandius finished polishing the armor and brought in",
"                                                                                                                       Raphalas Eul for the fitting. Hazadir left only then, realizing that Nandor Beraid would be",
"                                                                                                                       at his shop shortly to be outfitted. The two warriors met before the Empress and Imperial Council",
"                                                                                                                       in the arena, which had been flooded slightly to simulate the swampy conditions of Black Marsh.",
"                                                                                                                       From the moment Saccus saw Eul in his suit of heavy ebony and blazing dai-katana",
"                                                                                                                       and Beraid in his collection of dusty, rusted lizard-scales and spear from Hazadir's shop,",
"                                                                                                                       he knew who would win. And he was right.",
pygame.display.flip()
])

cutscene (screen, ["",
"                                                                                                                       The first blow from the dai-katana lodged in Beraid's soft shield,",
"                                                                                                                       as there was no metal trim to deflect it. Before Eul could pull his sword back,",
"                                                                                                                       Beraid let go of the now-flaming shield, still stuck on the sword,",
"                                                                                                                       and poked at the joints of Eul's ebony armor with his spear.",
"                                                                                                                       Eul finally retrieved his sword from the ruined shield and slashed at Beraid,",
"                                                                                                                       but his light armor was scaled and angled, and the attacks rolled off into the water, extinguishing",
"                                                                                                                       the dai-katana's flames. When Beraid struck at Eul's feet, he fell into the churned mud",
"                                                                                                                       and was unable to move. The Empress, out of mercy, called a victor.",
"                                                                                                                       Hazadir received the commission and thanks to his knowledge of Argonian battle tactics and weaponry",
"                                                                                                                       and how best to combat them, he designed implements of war that brought down the insurrection",
"                                                                                                                       in Armanias. Katariah won the respect of Council, and even, grudgingly, that of Thane Minglumire.",
"                                                                                                                       Sirollus Saccus went to Morrowind to learn what Hazadir learned there, and was never heard from again.",
"",
"",
"",
"                                                                                                                       The End.",
])
pygame.quit()
