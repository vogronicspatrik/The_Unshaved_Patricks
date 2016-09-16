import os
import sys
import random
import pygame


# Class for the orange dude
class Player(object):

    def __init__(self, player_num, px, py, sx, sy):
        self.player_num = player_num
        self.rect = pygame.Rect(px, py, sx, sy)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        Wall(self.player_num, (self.rect.x + dx, self.rect.y + dy))

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy


# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, player_num, pos):
        walls[player_num].append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 1, 1)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Me get red square!")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
# walls for 2 players: lists in list
walls = [[], []]
player = Player(0, 32, 32, 16, 16)
player2 = Player(1, 16, 16, 16, 16)

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
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # PLAYER 2
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player2.move(-2, 0)
    if key[pygame.K_d]:
        player2.move(2, 0)
    if key[pygame.K_w]:
        player2.move(0, -2)
    if key[pygame.K_s]:
        player2.move(0, 2)

    # Just added this to make it slightly fun ;)
    # if player.rect.colliderect(end_rect):
    #    raise SystemExit

    # Draw the scene
    screen.fill((0, 0, 0))
    # Player 1 walls
    for wall in walls[0]:
        if player.rect.colliderect(wall.rect):
            running = False
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # Player 2 walls
    for wall in walls[1]:
        if player2.rect.colliderect(wall.rect):
            running = False
        pygame.draw.rect(screen, (0, 255, 255), wall.rect)

    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.draw.rect(screen, (255, 200, 0), player2.rect)
    pygame.display.flip()


screen.fill((255, 255, 255))
pygame.display.flip()

pygame.quit()
sys.exit(0)
