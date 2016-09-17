import os
import sys
import random
import pygame
import time
from pygame import locals

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024


class Moto(pygame.sprite.Sprite):

    def __init__(self, player_num, start_direction):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("motor" + str(player_num) + ".png").convert()
        self.orig_image = self.image

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.direction = start_direction

    def move_single_axis(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

    def moveRight(self):
        self.direction = 0
        self.image = pygame.transform.rotate(self.orig_image, 0)

    def moveLeft(self):
        self.direction = 1
        self.image = pygame.transform.rotate(self.orig_image, 0)

    def moveUp(self):
        self.direction = 2
        self.image = pygame.transform.rotate(self.orig_image, 90)

    def moveDown(self):
        self.direction = 3
        self.image = pygame.transform.rotate(self.orig_image, 90)


# Class for the orange dude
class Player(object):

    def __init__(self, player_num, px, py, sx, sy, start_direction):
        self.player_num = player_num
        self.rect = pygame.Rect(px, py, sx, sy)
        self.direction = start_direction
        self.moto = Moto(player_num, start_direction)
        self.moto.rect.x = px
        self.moto.rect.y = py

    def moveRight(self):
        if self.direction != 1:
            self.direction = 0
            self.moto.moveRight()

    def moveLeft(self):
        if self.direction != 0:
            self.direction = 1
            self.moto.moveLeft()

    def moveUp(self):
        if self.direction != 3:
            self.direction = 2
            self.moto.moveUp()

    def moveDown(self):
        if self.direction != 2:
            self.direction = 3
            self.moto.moveDown()

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

    def __init__(self, player_num, pos):
        Game.walls[player_num].append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 3, 3)


# MAIN
class Game:

    walls = [[], []]

    def main(self):

        winner = 0

        # Initialise pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        # Set up the display
        pygame.display.set_caption("HECA_TRON!")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        clock = pygame.time.Clock()
        # walls for 2 players: lists in list
        Game.walls = [[], []]
        # starting positions
        player = Player(0, SCREEN_WIDTH - 1, int(SCREEN_HEIGHT / 2), 2, 16, 1)
        player2 = Player(1, 0, int(SCREEN_HEIGHT / 2), 2, 16, 0)

        # JOYSTICK
        try:
            pygame.joystick.init()
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            joysticks[0].init()
            joysticks[1].init()
            player1_joystick = joysticks[0]
            player2_joystick = joysticks[1]
        except IndexError:
            player1_joystick = None
            player2_joystick = None

        # background music
        sound = pygame.mixer.Sound('ttron.wav')
        sound.play(loops=0, maxtime=0, fade_ms=0)

        end = pygame.image.load('three.png')
        screen.fill((0, 0, 0))
        screen.blit(end, (500, 200))
        pygame.display.flip()
        pygame.time.wait(1000)

        end = pygame.image.load('two.png')
        screen.fill((0, 0, 0))
        screen.blit(end, (500, 200))
        pygame.display.flip()
        pygame.time.wait(1000)

        end = pygame.image.load('one.png')
        screen.fill((0, 0, 0))
        screen.blit(end, (500, 200))
        pygame.display.flip()
        pygame.time.wait(1000)

        end = pygame.image.load('start.png')
        screen.fill((0, 0, 0))
        screen.blit(end, (500, 350))
        pygame.display.flip()
        pygame.time.wait(1000)



        running = True
        while running:

            clock.tick(60)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    running = False

                # JOYSTICK
                try:
                    if e.type == pygame.locals.JOYAXISMOTION:
                        player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
                        if player1jx < 0:
                            player2.moveLeft()
                        if player1jx > 0:
                            player2.moveRight()
                        if player1jy < 0:
                            player2.moveUp()
                        if player1jy > 0:
                            player2.moveDown()
                        player2jx, player2jy = player2_joystick.get_axis(0), player2_joystick.get_axis(1)
                        if player2jx < 0:
                            player.moveLeft()
                        if player2jx > 0:
                            player.moveRight()
                        if player2jy < 0:
                            player.moveUp()
                        if player2jy > 0:
                            player.moveDown()
                except:
                    pass

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

            # check borders
            if player.moto.rect.x < 0 or player2.moto.rect.x < 0:
                running = False
            if player.moto.rect.x > SCREEN_WIDTH or player2.moto.rect.x > SCREEN_WIDTH:
                running = False
            if player.moto.rect.y < 0 or player2.moto.rect.y < 0:
                running = False
            if player.moto.rect.y > SCREEN_HEIGHT or player2.moto.rect.y > SCREEN_HEIGHT:
                running = False

            # Draw the scene
            screen.fill((0, 0, 0))
            # Player 1 walls
            counter1 = 0
            counter2 = 0
            coll_range = len(Game.walls[0]) - (player.moto.rect.width / 2 + 10)
            coll_range_2 = len(Game.walls[1]) - (player2.moto.rect.width / 2 + 10)
            for wall in Game.walls[0]:
                if player2.moto.rect.colliderect(wall.rect):
                    winner = 1
                    running = False
                if (counter1 < coll_range) and player.moto.rect.colliderect(wall.rect):
                    winner = 2
                    running = False
                counter1 += 1
                pygame.draw.rect(screen, (255, 255, 255), wall.rect)
            # Player 2 walls
            for wall in Game.walls[1]:
                if player.moto.rect.colliderect(wall.rect):
                    winner = 2
                    running = False
                if (counter2 < coll_range_2) and player2.moto.rect.colliderect(wall.rect):
                    winner = 1
                    running = False
                counter2 += 1
                pygame.draw.rect(screen, (0, 255, 255), wall.rect)

            # Player 1
            pygame.draw.rect(screen, (255, 200, 0), player.rect)
            screen.blit(player.moto.image, (player.moto.rect.x, player.moto.rect.y))

            # Player 2
            pygame.draw.rect(screen, (255, 200, 0), player2.rect)
            screen.blit(player2.moto.image, (player2.moto.rect.x, player2.moto.rect.y))

            pygame.display.flip()

        return self.game_over(winner)

    # END SCREEN
    def game_over(self, winner):

        print("Winner: ", winner)
        running = True
        clock = pygame.time.Clock()
        sound = pygame.mixer.Sound('blast.wav')
        sound.play(loops=0, maxtime=0, fade_ms=0)

        while running:

            clock.tick(60)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    print("QUIT 1")
                    running = False
                    pygame.quit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    print("QUIT 2")
                    running = False
                    pygame.quit()
                if e.type == pygame.KEYDOWN:
                    running = False
                    print("BACK TO MENU")
                    return True

            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            end = pygame.image.load('gameover.png')

            screen.fill((0, 0, 0))
            screen.blit(end, (10, 10))
            pygame.display.flip()
