import os
import sys
import random
import pygame
import time


# Class for the orange dude
class Player(object):

    def __init__(self, player_num, px, py, sx, sy):
        self.player_num = player_num
        self.rect = pygame.Rect(px, py, sx, sy)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            if dx < 0:
                Wall(self.player_num, (self.rect.centerx + dx + (self.rect.width / 2), self.rect.centery), True)
            else:
                Wall(self.player_num, (self.rect.centerx + dx - (self.rect.width / 2), self.rect.centery), True)
            self.move_single_axis(dx, 0)
        if dy != 0:
            if dy < 0:
                Wall(self.player_num, (self.rect.centerx, self.rect.centery + dy + (self.rect.height / 2)), True)
            else:
                Wall(self.player_num, (self.rect.centerx, self.rect.centery + dy - (self.rect.height / 2)), True)
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy


# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, player_num, pos, is_passible):
        walls[player_num].append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 2, 2)
        self.is_passible = True

    def set_unpassible(self):
        if not player.rect.colliderect(wall.rect) or not player2.rect.colliderect(wall.rect):
            self.is_passible = False

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("HECA_TRON!")
screen = pygame.display.set_mode((1280, 1024))

clock = pygame.time.Clock()
# walls for 2 players: lists in list
walls = [[], []]
player = Player(0, 32, 32, 62, 24)
player2 = Player(1, 16, 16, 62, 24)

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

    for new_wall in walls[0][-1:-3]:
        new_wall.set_unpassible()

    for new_wall in walls[1][-1:-10]:
        new_wall.set_unpassible()

    # Draw the scene
    screen.fill((0, 0, 0))
    # Player 1 walls
    for wall in walls[0]:
        if player.rect.colliderect(wall.rect):
            if not wall.is_passible:
                running = False
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # Player 2 walls
    for wall in walls[1]:
        if player2.rect.colliderect(wall.rect):
            if not wall.is_passible:
                running = False
        pygame.draw.rect(screen, (0, 255, 255), wall.rect)

    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.draw.rect(screen, (255, 200, 0), player2.rect)
    pygame.display.flip()



screen.fill((255, 255, 255))
pygame.display.flip()

pygame.quit()
sys.exit(0)
