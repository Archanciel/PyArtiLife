import pygame

WIN_HEIGHT = 100

WIN_WIDTH = 100

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pygame First")
run = True
x = 50
y = 50
width = 20
height = 20
velocity = 5

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - velocity
        if x < 1:
            x = 1

    if keys[pygame.K_RIGHT]:
        x = x + velocity
        if x > WIN_WIDTH - width - 1:
            x = WIN_WIDTH - width - 1

    if keys[pygame.K_UP]:
        y = y - velocity
        if y < 1:
            y = 1

    if keys[pygame.K_DOWN]:
        y = y + velocity
        if y > WIN_HEIGHT - height - 1:
            y = WIN_HEIGHT - height - 1

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), [x, y, width, height])
    pygame.display.update()
pygame.quit()