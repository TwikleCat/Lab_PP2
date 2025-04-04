import pygame
import sys
import random
import time
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Settings for screen/framework
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPEED = 1
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("./Lab_8/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # display screen
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite):  # new class, inheriting from the base class “Sprite”
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Lab_8/Enemy.png")
        self.rect = self.image.get_rect()  # automatically create a rectangle of the same size as the image
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # randomized starting point for Enemy

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # move enemy car down by SPEED pixels
        if self.rect.top > SCREEN_HEIGHT:  # checks if enemy car has gone off the bottom of the screen
            SCORE += 1
            self.rect.top = 0  # if so, reset enemy car to the top of the screen
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # at random point on the left of the screen


class Player(pygame.sprite.Sprite):  # Passing pygame.sprite.Sprite into the parameters, makes the Player Class it’s child class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Lab_8/Player.png")
        self.rect = self.image.get_rect()  # automatically create a rectangle of the same size as the image
        self.rect.center = (160, 540)  # position of player(car) in the vector dimension in the framework

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Lab_8/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed_modifier = random.uniform(0.5, 1.5)  # Random weight (coin fall speed)

    def move(self):
        self.rect.move_ip(0, SPEED // 2 * self.speed_modifier)  # Modify speed with the weight of the coin
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.speed_modifier = random.uniform(0.5, 1.5)  # Reset speed modifier when coin is repositioned


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# starting game loop where events occur, update and get drawn until the game is quit
while True:
    for event in pygame.event.get():  # Event occurs when the user performs a specific action
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('./Lab_8/crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # To be run if collision occurs between coins and Player
    if pygame.sprite.spritecollideany(P1, coins):
        COINS =COINS + random.randint(1, 3)
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        # Increase the speed of the enemy every 5 coins
        if COINS % 5 == 0:
            SPEED += 0.5

    pygame.display.update()
    FramePerSec.tick(FPS)
