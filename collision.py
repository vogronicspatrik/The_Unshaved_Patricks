import os
import sys
import random
import pygame
import time

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 768


class Moto(pygame.sprite.Sprite):

    def __init__(self, player_num):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("motor" + str(player_num) + ".png").convert()

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def move_single_axis(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy


# Class for the orange dude
class Player(object):

    def __init__(self, player_num, px, py, sx, sy, start_direction):
        self.player_num = player_num
        self.rect = pygame.Rect(px, py, sx, sy)
        self.direction = start_direction
        self.moto = Moto(player_num)
        self.moto.rect.x = px
        self.moto.rect.y = py

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def moveOn(self):
        if self.direction == 0:
            self.move(2, 0)
        if self.direction == 1:
            self.move(-2, 0)
        if self.direction == 2:
            self.move(0, -2)
        if self.direction == 3:
            self.move(0, 2)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
            self.moto.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            self.moto.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # Draw a wall (after the movement)
        Wall(self.player_num, (self.rect.centerx, self.rect.centery))


# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, player_num, pos, is_passible = True):
        walls[player_num].append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 2, 2)
        self.is_passible = is_passible

    def set_unpassible(self):
        if not player.rect.colliderect(wall.rect) or not player2.rect.colliderect(wall.rect):
            self.is_passible = False

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("HECA_TRON!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
# walls for 2 players: lists in list
walls = [[], []]
# starting positions
player = Player(0, SCREEN_WIDTH - 1, int(SCREEN_HEIGHT / 2), 2, 16, 1)
player2 = Player(1, 0, int(SCREEN_HEIGHT / 2), 2, 16, 0)

# MAIN

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # PLAYER 1
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.moveLeft()
    if key[pygame.K_RIGHT]:
        player.moveRight()
    if key[pygame.K_UP]:
        player.moveUp()
    if key[pygame.K_DOWN]:
        player.moveDown()

    player.moveOn()

    # PLAYER 2
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player2.moveLeft()
    if key[pygame.K_d]:
        player2.moveRight()
    if key[pygame.K_w]:
        player2.moveUp()
    if key[pygame.K_s]:
        player2.moveDown()

    player2.moveOn()

    # Just added this to make it slightly fun ;)
    # if player.rect.colliderect(end_rect):
    #    raise SystemExit

    for new_wall in walls[0][-1:-3]:
        new_wall.set_unpassible()

    for new_wall in walls[1][-1:-10]:
        new_wall.set_unpassible()

    # Draw the scene
    screen.fill((0, 0, 0))
    # Player 1 walls
    for wall in walls[0]:
        wall.set_unpassible()
        if player2.moto.rect.colliderect(wall.rect):
            running = False
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # Player 2 walls
    for wall in walls[1]:
        wall.set_unpassible()
        if player.moto.rect.colliderect(wall.rect):
            running = False
        pygame.draw.rect(screen, (0, 255, 255), wall.rect)

    # Player 1
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    screen.blit(player.moto.image, (player.moto.rect.x, player.moto.rect.y))

    # Player 2
    pygame.draw.rect(screen, (255, 200, 0), player2.rect)
    screen.blit(player2.moto.image, (player2.moto.rect.x, player2.moto.rect.y))

    pygame.display.flip()


# END SCREEN
screen.fill((255, 255, 255))
pygame.display.flip()

pygame.quit()
sys.exit(0)
