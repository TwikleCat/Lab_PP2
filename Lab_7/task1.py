import pygame
import time
import math
import os

pygame.init()

w, h = 500, 500
c = (w // 2, h // 2)

back = pygame.image.load(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_7\mickeyclock.jpg")  
minute= pygame.image.load(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_7\minute1.png")  
second = pygame.image.load(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_7\second1.png")  

back = pygame.transform.scale(back, (w, h)) 
second = pygame.transform.scale(second, (220, 60))
minute = pygame.transform.scale(minute, (170, 60))

screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

def blit_rotate_center(surf, image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(back, (0, 0))
    
    t = time.localtime()
    seconds = t.tm_sec
    minutes = t.tm_min
    
    
    sec_angle = -seconds * 6  
    min_angle = -minutes * 6 
    
    blit_rotate_center(screen, second, sec_angle, c)
    blit_rotate_center(screen, minute, min_angle, c)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(30)  

pygame.quit()
