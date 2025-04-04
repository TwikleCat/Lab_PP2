import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing App with Eraser")
clock = pygame.time.Clock()

# Drawing settings
radius = 10
color = (0, 0, 255)
mode = 'draw'
start_pos = None
objects = []  # Stores all drawn shapes

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

# Main loop
while True:
    screen.fill((255, 255, 255))

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

        # Tool & color selection
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_d:
                mode = 'draw'
            elif event.key == pygame.K_s:
                mode = 'rectangle'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_e:
                mode = 'eraser'

        # Start drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
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
