import pygame
import psycopg2
from datetime import datetime
import random


conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'Database',
    user = 'postgres',
    password = 'Pass@STU2015',
    port = 1671 
)
cur = conn.cursor()

def create_tables():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()

def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def get_latest_score(user_id):
    cur.execute(
        "SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1",
        (user_id,)
    )
    return cur.fetchone()

def save_game(user_id, score, level):
    cur.execute(
        "INSERT INTO user_score (user_id, score, level, saved_at) VALUES (%s, %s, %s, %s)",
        (user_id, score, level, datetime.now())
    )
    conn.commit()

def close_db():
    cur.close()
    conn.close()


pygame.init()
WIDTH, HEIGHT = 400, 400
GRID = 20
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with DB")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(win, GREEN, (*segment, GRID, GRID))

def draw_food(food_pos):
    pygame.draw.rect(win, RED, (*food_pos, GRID, GRID))

def get_username_from_display():
    user_input = ''
    input_active = True
    while input_active:
        win.fill(WHITE)
        txt_surface = font.render("Enter username: " + user_input, True, BLACK)
        win.blit(txt_surface, (50, HEIGHT // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_input.strip() != '':
                    return user_input.strip()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode


create_tables()
username = get_username_from_display()
user_id = get_or_create_user(username)
saved = get_latest_score(user_id)
current_level = saved[1] if saved else 1
current_score = 0
speed = 8 + (current_level - 1) * 2


snake = [[100, 100]]
direction = [GRID, 0]
food = [random.randrange(0, WIDTH, GRID), random.randrange(0, HEIGHT, GRID)]
running = True
paused = False


while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(user_id, current_score, current_level)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != [0, GRID]:
                direction = [0, -GRID]
            elif event.key == pygame.K_DOWN and direction != [0, -GRID]:
                direction = [0, GRID]
            elif event.key == pygame.K_LEFT and direction != [GRID, 0]:
                direction = [-GRID, 0]
            elif event.key == pygame.K_RIGHT and direction != [-GRID, 0]:
                direction = [GRID, 0]
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_game(user_id, current_score, current_level)

    if paused:
        continue

    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

    
    if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        save_game(user_id, current_score, current_level)
        running = False
        break

    snake.insert(0, new_head)

    if new_head == food:
        current_score += 10
        food = [random.randrange(0, WIDTH, GRID), random.randrange(0, HEIGHT, GRID)]

    
        if current_score % 100 == 0 and current_score!=0:
            current_level += 1
            speed += 2
            print(f"Level Up! New Level: {current_level}, Speed: {speed}")

    else:
        snake.pop()

    win.fill(WHITE)
    draw_snake(snake)
    draw_food(food)

    
    score_text = font.render(f"User: {username} | Score: {current_score} | Level: {current_level}", True, BLACK)
    win.blit(score_text, (10, 10))

    pygame.display.update()

close_db()
pygame.quit()
