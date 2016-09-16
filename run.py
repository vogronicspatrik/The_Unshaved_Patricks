import pygame
import testmenu as dm
from collision import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024


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


# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#
# BackGround = Background('tron.jpg', [10, 10])
# # screen.fill([255, 255, 255])
# screen.blit(BackGround.image, BackGround.rect)

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
    g = Game()
    winner = g.main()
    g.game_over(winner)
elif choose == 1:
    print ("You choose 'Options'.")
elif choose == 2:
    print ("You choose 'Manual'.")
elif choose == 3:
    print ("You choose 'Show Highscore'.")
elif choose == 4:
    print ("You choose 'Quit Game'.")
