import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
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

# Fonts
font = pygame.font.SysFont('Arial', 24)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Directions
directions = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

# Create wall positions (you can make more complex patterns)
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

# Function to draw grid objects
def draw_cell(position, color):
    x, y = position
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to generate food at a position not on wall or snake
def generate_food(snake, walls):
    while True:
        pos = (random.randint(1, COLS - 2), random.randint(1, ROWS - 2))
        if pos not in snake and pos not in walls:
            return pos

# Main game loop
def main():
    snake = [(COLS // 2, ROWS // 2)]
    direction = "RIGHT"
    food = generate_food(snake, walls)
    score = 0
    level = 1
    speed = 10

    running = True
    while running:
        screen.fill(BLACK)

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

        # Check for collision with wall or self
        if head in walls or head in snake:
            print("Game Over! Final Score:", score)
            pygame.quit()
            sys.exit()

        # Add new head
        snake.insert(0, head)

        # Check if food is eaten
        if head == food:
            score += 1
            food = generate_food(snake, walls)
            # Level up every 3 points
            if score % 3 == 0:
                level += 1
                speed += 2
        else:
            # Remove tail
            snake.pop()

        # Draw snake
        for segment in snake:
            draw_cell(segment, GREEN)

        # Draw food
        draw_cell(food, RED)

        # Draw walls
        for wall in walls:
            draw_cell(wall, BLUE)

        # Display score and level
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display and tick clock
        pygame.display.flip()
        clock.tick(speed)

if __name__ == "__main__":
    main()
