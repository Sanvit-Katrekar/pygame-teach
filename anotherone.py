import pygame

pygame.init() # Initialie phase

#Screen setup
SCREENX, SCREENY = 500, 500
window = pygame.display.set_mode((SCREENX, SCREENY))

pygame.display.set_caption("Bruh")

x, y, width, height = 100, 100, 50, 50
vel = 10
DELAY_MS = 50

jump = False
JUMP_COUNT_MAX = 7
jumpcount = JUMP_COUNT_MAX # -> 10

run = True

while run:
    pygame.time.delay(DELAY_MS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    elif keys[pygame.K_RIGHT]:
        x += vel
    elif keys[pygame.K_UP]:
        y -= vel
    elif keys[pygame.K_DOWN]:
        y += vel
    elif keys[pygame.K_SPACE]:
        jump = True

    if jump:
        if jumpcount >= -JUMP_COUNT_MAX: # -a <-> a
            if jumpcount < 0:
                sign = -1
            else:
                sign = 1
            y -= sign * jumpcount**2
            jumpcount -=1
        else:
            jump = False
            jumpcount = JUMP_COUNT_MAX
    
    window.fill('black')
    pygame.draw.rect(window, (238, 189, 34), (x, y, width, height))
    pygame.display.update()
pygame.quit()
