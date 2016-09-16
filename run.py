import pygame
import testmenu as dm
from collision import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024


class Menu():

    def main(self):

        pygame.init()

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
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        sound = pygame.mixer.Sound('ttron.wav')
        sound.play(loops=0, maxtime=0, fade_ms=0)

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
    option = m.main()
    if option == 1:
        print("Start game...")
        g = Game()
        g.main()
    else:
        pygame.quit()
        break
