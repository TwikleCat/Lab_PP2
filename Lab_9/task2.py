import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size and cell size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Grid dimensions
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Font for score and level
font = pygame.font.SysFont('Arial', 24)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Directions dictionary
directions = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

# Function to create border walls
def create_walls():
    walls = set()
    for x in range(COLS):
        walls.add((x, 0))  # Top wall
        walls.add((x, ROWS - 1))  # Bottom wall
    for y in range(ROWS):
        walls.add((0, y))  # Left wall
        walls.add((COLS - 1, y))  # Right wall
    return walls

walls = create_walls()

# Function to draw a cell at given position with a color
def draw_cell(position, color):
    x, y = position
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to generate food that doesn't appear on wall or snake
def generate_food(snake, walls):
    while True:
        pos = (random.randint(1, COLS - 2), random.randint(1, ROWS - 2))
        if pos not in snake and pos not in walls:
            weight = random.randint(1, 3)  # Food weight = 1 to 3
            return pos, weight

# Main Game Loop
def main():
    snake = [(COLS // 2, ROWS // 2)]  # Initial snake position
    direction = "RIGHT"  # Initial direction
    food, food_weight = generate_food(snake, walls)  # Initial food
    food_timer = pygame.time.get_ticks()  # Start food timer
    FOOD_LIFETIME = 5000  # Food disappears after 5 seconds

    score = 0
    level = 1
    speed = 10

    running = True
    while running:
        screen.fill(BLACK)  # Clear screen

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Move snake
        dx, dy = directions[direction]
        head = (snake[0][0] + dx, snake[0][1] + dy)

        # Collision with wall or self
        if head in walls or head in snake:
            print("Game Over! Final Score:", score)
            pygame.quit()
            sys.exit()

        # Add new head
        snake.insert(0, head)

        # Check if food eaten
        if head == food:
            score += food_weight  # Add weighted score
            food, food_weight = generate_food(snake, walls)  # Generate new food
            food_timer = pygame.time.get_ticks()  # Reset food timer

            # Level up every 5 points
            if score >= level * 5:
                level += 1
                speed += 2
        else:
            # Remove tail if no food eaten
            snake.pop()

        # Handle timed food disappearance
        if pygame.time.get_ticks() - food_timer > FOOD_LIFETIME:
            food, food_weight = generate_food(snake, walls)
            food_timer = pygame.time.get_ticks()  # Reset timer

        # Draw snake
        for segment in snake:
            draw_cell(segment, GREEN)

        # Draw food
        draw_cell(food, RED)

        # Draw walls
        for wall in walls:
            draw_cell(wall, BLUE)

        # Draw score and level
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display and limit FPS
        pygame.display.flip()
        clock.tick(speed)

# Run game
if __name__ == "__main__":
    main()
