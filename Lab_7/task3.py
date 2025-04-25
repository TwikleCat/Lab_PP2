import pygame

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))

r = 25
x = w // 2
y = h // 2
ball = (255, 0, 0)  
back = (255, 255, 255)  
n = 20  

running = True
while running:
    screen.fill(back)  
    
    pygame.draw.circle(screen, ball, (x, y), r)
    pygame.display.flip()  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - r - n >= 0:
                y -= n
            elif event.key == pygame.K_DOWN and y + r + n <= h:
                y += n
            elif event.key == pygame.K_LEFT and x - r - n >= 0:
                x -= n
            elif event.key == pygame.K_RIGHT and x + r + n <= w:
                x += n

pygame.quit()
