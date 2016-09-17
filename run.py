import os
import pygame
import testmenu as dm
from collision import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024


class Menu():

    def start(self):

        pygame.init()
        # Initialise pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        # Set up the display
        pygame.display.set_caption("HECA_TRON!")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        sound = pygame.mixer.Sound('ttron.wav')
        sound.play(loops=0, maxtime=0, fade_ms=0)

        for i in range(5):

            pics = ['frame_0_delay-0.04s.png', 'frame_1_delay-0.04s.png', 'frame_2_delay-0.04s.png',
                    'frame_3_delay-0.04s.png', 'frame_4_delay-0.04s.png', 'frame_5_delay-0.04s.png',
                    'frame_6_delay-0.04s.png', 'frame_7_delay-0.04s.png', ]
            for pic in pics:
                end = pygame.image.load(pic)
                end = pygame.transform.scale(end, (1280, 1024))
                screen.fill((0, 0, 0))
                screen.blit(end, (0, 0))
                pygame.display.flip()
                pygame.time.wait(20)

    def main(self):
        # Just a few static variables
        red = 255, 0, 0
        green = 0, 255, 0
        blue = 0, 0, 255

        size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
        screen = pygame.display.set_mode(size)
        # screen.fill(red)
        pygame.display.update()
        pygame.key.set_repeat(5, 30)

        bg = pygame.image.load('tron.jpg')
        bg = pygame.transform.scale(bg, (1280, 1024))
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        pygame.display.flip()
        myfont = pygame.font.SysFont("monospace", 72)
        label = myfont.render('HECA_TRON PRODUCTION', 1, (0, 0, 255))
        screen.blit(label, (300, 800))
        pygame.display.flip()


        choose = dm.dumbmenu(screen, [
                                '            Start Game',
                                '            Options',
                                '            Manual',
                                '            Show Highscore',
                                '            Quit Game'], 64, 64, None, 62, 1.0, green, red)

        if choose == 0:
            return 1
        elif choose == 1:
            print ("You choose 'Options'.")
            return 0
        elif choose == 2:
            print ("You choose 'Manual'.")
            return 0
        elif choose == 3:
            print ("You choose 'Show Highscore'.")
            return 0
        elif choose == 4:
            print ("You choose 'Quit Game'.")
            return 0


while True:
    print("Main LOOP...")
    m = Menu()
    m.start()
    option = m.main()
    if option == 1:
        print("Start game...")
        g = Game()
        g.main()
    else:
        pygame.quit()
        break
