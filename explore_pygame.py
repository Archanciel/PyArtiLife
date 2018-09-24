import pygame

WIN_HEIGHT = 500

WIN_WIDTH = 500

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pygame First")
run = True
x = int(WIN_WIDTH / 2)
y = int(WIN_HEIGHT / 2)
width = 20
height = 20
velocity = 5
jumpCount = 10
jumping = False

def limitUp(y):
    if y < 1:
        return 1
    else:
        return y

def limitDown(y):
    if y > WIN_HEIGHT - height - 1:
        y = WIN_HEIGHT - height - 1

    return y

while run:
    pygame.time.delay(50)

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

    if not jumping:
        if keys[pygame.K_UP]:
            y = y - velocity
            y = limitUp(y)

        if keys[pygame.K_DOWN]:
            y = y + velocity
            y = limitDown(y)

        if keys[pygame.K_SPACE]:
            jumping = True
            jumpCount = 10
    else:
        oldY = y
        if jumpCount >= 0:
            y -= jumpCount ** 2 / 2
        elif jumpCount < 0 and jumpCount >= -10:
            y += jumpCount ** 2 / 2
        else:
            jumpCount = 10
            jumping = False
        #print("y: {}, diff: {}".format(y, oldY - y))
        jumpCount -= 1
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), [x, y, width, height])
    pygame.display.update()
pygame.quit()