import pygame
import sys
import math

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing App with GUI")
clock = pygame.time.Clock()

# Drawing settings
radius = 10
color = (0, 0, 255)  # Default: Blue
mode = 'draw'  # Default drawing mode
start_pos = None  # Store initial position for shapes
objects = []  # Stores drawn objects

# GUI Buttons for Tools
buttons = {
    "draw": pygame.Rect(50, 10, 50, 50),    # Pen
    "eraser": pygame.Rect(150, 10, 50, 50),  # Eraser
    "rectangle": pygame.Rect(250, 10, 50, 50),  # Rectangle
    "circle": pygame.Rect(350, 10, 50, 50),   # Circle
    "square": pygame.Rect(450, 10, 50, 50),   # Square
    "right_triangle": pygame.Rect(550, 10, 50, 50),  # Right Triangle
    "equilateral_triangle": pygame.Rect(650, 10, 50, 50),  # Equilateral Triangle
    "rhombus": pygame.Rect(750, 10, 50, 50)  # Rhombus
}

# Color Selection Buttons
color_buttons = {
    "red": pygame.Rect(50, 70, 50, 50),
    "green": pygame.Rect(110, 70, 50, 50),
    "blue": pygame.Rect(170, 70, 50, 50),
    "black": pygame.Rect(230, 70, 50, 50)
}

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Mapping color names to actual RGB values
color_map = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
    "black": BLACK
}

# Helper functions to draw different shapes
def draw_rectangle(screen, color, start, end, width=0):
    """Draws a rectangle given two corner points."""
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(screen, color, rect, width)

def draw_square(screen, color, start, end):
    """Draws a square using the shortest side as reference."""
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], side, side)
    pygame.draw.rect(screen, color, rect, 2)

def draw_circle(screen, color, center, radius, width=0):
    """Draws a circle given a center and radius."""
    pygame.draw.circle(screen, color, center, radius, width)

def draw_right_triangle(screen, color, start, end):
    """Draws a right triangle given two points."""
    pygame.draw.polygon(screen, color, [start, (start[0], end[1]), end], 2)

def draw_equilateral_triangle(screen, color, start, end):
    """Draws an equilateral triangle based on the given base width."""
    base = abs(end[0] - start[0])
    height = (math.sqrt(3) / 2) * base
    top_vertex = (start[0] + base // 2, start[1] - int(height))
    pygame.draw.polygon(screen, color, [start, end, top_vertex], 2)

def draw_rhombus(screen, color, start, end):
    """Draws a rhombus given two opposite corner points."""
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)

    points = [
        (center[0], start[1]),  # Top
        (end[0], center[1]),  # Right
        (center[0], end[1]),  # Bottom
        (start[0], center[1])  # Left
    ]
    pygame.draw.polygon(screen, color, points, 2)

# Function to draw the GUI buttons
def draw_buttons():
    """Draws the buttons for selecting tools and colors."""
    for key, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)

    # Draw tool icons
    pygame.draw.line(screen, BLACK, (60, 30), (90, 30), 5)  # Pen
    pygame.draw.circle(screen, BLACK, (175, 35), 15)  # Eraser
    pygame.draw.rect(screen, BLACK, (260, 20, 30, 30))  # Rectangle
    pygame.draw.circle(screen, BLACK, (375, 35), 20, 3)  # Circle
    pygame.draw.rect(screen, BLACK, (460, 20, 30, 30))  # Square
    pygame.draw.polygon(screen, BLACK, [(560, 50), (550, 20), (590, 50)], 2)  # Right Triangle
    pygame.draw.polygon(screen, BLACK, [(660, 50), (650, 20), (690, 50)], 2)  # Equilateral Triangle
    pygame.draw.polygon(screen, BLACK, [(750, 30), (770, 50), (750, 70), (730, 50)], 2)  # Rhombus

    # Draw color selection buttons
    for name, rect in color_buttons.items():
        pygame.draw.rect(screen, color_map[name], rect)

# Main loop
while True:
    screen.fill(WHITE)
    draw_buttons()

    # Draw all stored shapes
    for item in objects:
        shape = item["type"]
        if shape == "square":
            draw_square(screen, item["color"], item["start"], item["end"])
        elif shape == "right_triangle":
            draw_right_triangle(screen, item["color"], item["start"], item["end"])
        elif shape == "equilateral_triangle":
            draw_equilateral_triangle(screen, item["color"], item["start"], item["end"])
        elif shape == "rhombus":
            draw_rhombus(screen, item["color"], item["start"], item["end"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Check tool selection
            for tool, rect in buttons.items():
                if rect.collidepoint(x, y):
                    mode = tool
                    break

            # Check color selection
            for color_name, rect in color_buttons.items():
                if rect.collidepoint(x, y):
                    color = color_map[color_name]

            else:
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos
            objects.append({"type": mode, "start": start_pos, "end": end_pos, "color": color})
            start_pos = None

    pygame.display.flip()
    clock.tick(60)
