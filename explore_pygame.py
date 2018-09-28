import pygame

WIN_HEIGHT = 500

WIN_WIDTH = 500
IMAGE_WIDTH_HEIGHT = 32

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pygame First")
run = True
x = int(WIN_WIDTH / 2)
y = int(WIN_HEIGHT / 2)
width = IMAGE_WIDTH_HEIGHT * 2
height = IMAGE_WIDTH_HEIGHT * 2
velocity = 5
jumpCount = 10
jumping = False
images = pygame.image.load('expl_pygame_resources/playersprites.png')
IMAGE_NB = 16
currImage = 0

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
        #oldY = y
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
    movableRect = (x, y, width, height)

    if currImage >= IMAGE_NB:
        currImage = 0
    else:
        currImage += 1

    pygame.draw.rect(win, (255, 0, 0), movableRect)

    win.blit(images, movableRect, (currImage * IMAGE_WIDTH_HEIGHT, 0, IMAGE_WIDTH_HEIGHT, IMAGE_WIDTH_HEIGHT))
    pygame.display.update()
pygame.quit()