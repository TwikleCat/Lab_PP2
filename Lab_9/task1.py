import pygame
import sys
import random
import time
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen Settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game Variables
SPEED = 1  # Initial speed of enemy
SCORE = 0  # Player's score
COINS = 0  # Player's collected coins
COINS_TO_INCREASE_SPEED = 5  # Number of coins needed to increase enemy speed

# Load Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load Background Image
background = pygame.image.load(r"./Lab_8/AnimatedStreet.png")

# Display Window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"./Lab_8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Random start position
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Move down by SPEED pixels
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1  # Increase score when enemy crosses the screen
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Respawn at top

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"./Lab_8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 540)  # Player's start position
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"./Lab_8/coin.png")
        self.rect = self.image.get_rect()
        self.value = random.randint(1, 3)  # Random weight (1, 2, or 3 points)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # Move slower than enemy
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        """Respawn coin at a random position with a new random weight."""
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.value = random.randint(1, 3)  # Assign a new weight

# Setting up Sprites
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()

# Generating multiple coins with different weights
for _ in range(3):  # Change this number to generate more coins
    coins.add(Coin())

# Creating Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

# Custom Event to Increase Speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Increase enemy speed gradually
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw Background
    DISPLAYSURF.blit(background, (0, 0))
    
    # Display Score and Coins
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))
    
    # Move and Draw all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # Collision Detection - Player hits an Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Collision Detection - Player collects a Coin
    collected_coins = pygame.sprite.spritecollide(P1, coins, dokill=True)
    for coin in collected_coins:
        COINS += coin.value  # Add coin's weight to the total coins
        new_coin = Coin()  # Generate a new coin
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Increase Enemy Speed when Player Collects Enough Coins
    if COINS >= COINS_TO_INCREASE_SPEED:
        SPEED += 1
        COINS_TO_INCREASE_SPEED += 5  # Next speed increase after another 5 coins

    pygame.display.update()
    FramePerSec.tick(FPS)
