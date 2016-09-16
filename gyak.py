import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
is_blue = True
green = (0, 255, 0)
red = (255, 0, 0)
x = 150
y = 150
x_change = 0
y_change = 0
z = 300
q = 300
z_change = 0
q_change = 0

clock = pygame.time.Clock()


done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -10
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = 10
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -10
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = 10
                        x_change = 0
                    if event.key == pygame.K_a:
                        z_change = -10
                        q_change = 0
                    elif event.key == pygame.K_d:
                        z_change = 10
                        q_change = 0
                    elif event.key == pygame.K_w:
                        z_change = -10
                        q_change = 0
                    elif event.key == pygame.K_s:
                        z_change = 10
                        q_change = 0
        # pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP]:
        #     y -= 1
        # if pressed[pygame.K_DOWN]:
        #     y += 1
        # if pressed[pygame.K_LEFT]:
        #     x_change -= 10
        # if pressed[pygame.K_RIGHT]:
        #     x_change += 10
        # if pressed[pygame.K_w]:
        #     q -= 1
        # if pressed[pygame.K_s]:
        #     q += 1
        # if pressed[pygame.K_a]:
        #     z -= 1
        # if pressed[pygame.K_d]:
        #     z += 1
        x += x_change
        y += y_change
        pygame.draw.rect(screen, green, pygame.Rect(x, y, 10, 10))
        pygame.draw.rect(screen, red, pygame.Rect(z, q, 10, 10))

        pygame.display.update()
        clock.tick(20)
