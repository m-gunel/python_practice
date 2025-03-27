import pygame
import time

pygame.init()

# Глобальные переменные
window_width = 800
window_height = 600
fon = 'fon.png'  


window = pygame.display.set_mode((window_width, window_height)) 
pygame.display.set_caption("Игра v1.0")

speed = 0  
sdvig_fona = 0  

img1 = pygame.image.load(fon)  
back_fon = pygame.transform.scale(img1, (window_width, window_height))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = 5
            elif event.key == pygame.K_RIGHT:
                speed = -5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                speed = 0

    sdvig_fona = (sdvig_fona + speed) % window_width
    window.blit(back_fon, (sdvig_fona, 0))
    if sdvig_fona != 0:
        window.blit(back_fon, (sdvig_fona - window_width, 0))  

    pygame.display.update() 
    time.sleep(0.02)

pygame.quit()  # закрытие окна крестиком
