import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame  # it is important to import pygame after that

pygame.init()

SCREENX, SCREENY = 500, 500
window = pygame.display.set_mode((SCREENX, SCREENY))

x, y, width, height = 100, 100, 50, 50
velocity = 10

pygame.display.set_caption("Template code")

run = True

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    
    window.fill('black')
    pygame.draw.rect(window, (255,0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()