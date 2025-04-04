import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing App with GUI")
clock = pygame.time.Clock()

# Drawing settings
radius = 10
color = (0, 0, 255)  # Default Blue
mode = 'draw'
start_pos = None
objects = []  # Stores all drawn shapes

# GUI Button Areas
buttons = {
    "draw": pygame.Rect(50, 10, 50, 50),    # Pen
    "eraser": pygame.Rect(150, 10, 50, 50),  # Eraser
    "rectangle": pygame.Rect(250, 10, 50, 50),  # Rectangle
    "circle": pygame.Rect(350, 10, 50, 50)   # Circle
}

# Color Selection Buttons
color_buttons = {
    "red": pygame.Rect(500, 10, 50, 50),
    "green": pygame.Rect(560, 10, 50, 50),
    "blue": pygame.Rect(620, 10, 50, 50),
    "black": pygame.Rect(680, 10, 50, 50)
}

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Color mapping
color_map = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
    "black": BLACK
}

# Helper functions
def draw_line(screen, start, end, width, color):
    pygame.draw.line(screen, color, start, end, width)

def draw_rectangle(screen, color, start, end, width=0):
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(screen, color, rect, width)

def draw_circle(screen, color, center, radius, width=0):
    pygame.draw.circle(screen, color, center, radius, width)

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Function to draw the GUI buttons
def draw_buttons():
    # Tool selection buttons
    pygame.draw.rect(screen, GRAY, buttons["draw"])     
    pygame.draw.rect(screen, GRAY, buttons["eraser"])   
    pygame.draw.rect(screen, GRAY, buttons["rectangle"])
    pygame.draw.rect(screen, GRAY, buttons["circle"])   

    # Draw tool icons
    pygame.draw.line(screen, BLACK, (60, 30), (90, 30), 5)  # Pen
    pygame.draw.circle(screen, BLACK, (175, 35), 15)  # Eraser
    pygame.draw.rect(screen, BLACK, (260, 20, 30, 30))  # Rectangle
    pygame.draw.circle(screen, BLACK, (375, 35), 20, 3)  # Circle

    # Color selection buttons
    pygame.draw.rect(screen, RED, color_buttons["red"])  
    pygame.draw.rect(screen, GREEN, color_buttons["green"])  
    pygame.draw.rect(screen, BLUE, color_buttons["blue"])  
    pygame.draw.rect(screen, BLACK, color_buttons["black"])  

# Main loop
while True:
    screen.fill(WHITE)

    # Draw GUI
    draw_buttons()

    # Draw all stored shapes
    for item in objects:
        shape = item["type"]
        if shape == "line":
            pygame.draw.circle(screen, item["color"], item["pos"], item["radius"])
        elif shape == "rect":
            draw_rectangle(screen, item["color"], item["start"], item["end"])
        elif shape == "circle":
            r = int(distance(item["start"], item["end"]))
            draw_circle(screen, item["color"], item["start"], r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if user clicks a button
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Tool selection
            if buttons["draw"].collidepoint(x, y):
                mode = 'draw'
            elif buttons["eraser"].collidepoint(x, y):
                mode = 'eraser'
            elif buttons["rectangle"].collidepoint(x, y):
                mode = 'rectangle'
            elif buttons["circle"].collidepoint(x, y):
                mode = 'circle'
            
            # Color selection
            for color_name, rect in color_buttons.items():
                if rect.collidepoint(x, y):
                    color = color_map[color_name]

            else:
                start_pos = event.pos
                if mode == 'draw':
                    objects.append({"type": "line", "pos": start_pos, "color": color, "radius": radius})
                elif mode == 'eraser':
                    # Erase nearby shapes
                    pos = event.pos
                    objects = [obj for obj in objects if not (
                        (obj["type"] == "line" and distance(obj["pos"], pos) < 15) or
                        (obj["type"] == "rect" and pygame.Rect(min(obj["start"][0], obj["end"][0]),
                                                               min(obj["start"][1], obj["end"][1]),
                                                               abs(obj["end"][0] - obj["start"][0]),
                                                               abs(obj["end"][1] - obj["start"][1])).collidepoint(pos)) or
                        (obj["type"] == "circle" and distance(obj["start"], pos) < distance(obj["start"], obj["end"]))
                    )]

        # Keep drawing on mouse drag (lines)
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == 'draw':
                objects.append({"type": "line", "pos": event.pos, "color": color, "radius": radius})
            elif mode == 'eraser':
                # Erase while moving
                pos = event.pos
                objects = [obj for obj in objects if not (
                    (obj["type"] == "line" and distance(obj["pos"], pos) < 15) or
                    (obj["type"] == "rect" and pygame.Rect(min(obj["start"][0], obj["end"][0]),
                                                           min(obj["start"][1], obj["end"][1]),
                                                           abs(obj["end"][0] - obj["start"][0]),
                                                           abs(obj["end"][1] - obj["start"][1])).collidepoint(pos)) or
                    (obj["type"] == "circle" and distance(obj["start"], pos) < distance(obj["start"], obj["end"]))
                )]

        # Stop drawing rectangle or circle
        if event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos
            if mode == 'rectangle':
                objects.append({"type": "rect", "start": start_pos, "end": end_pos, "color": color})
            elif mode == 'circle':
                objects.append({"type": "circle", "start": start_pos, "end": end_pos, "color": color})
            start_pos = None

    pygame.display.flip()
    clock.tick(60)
