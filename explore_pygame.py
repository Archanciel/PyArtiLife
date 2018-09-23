import pygame

WIN_WIDTH = 500
WIN_HEIGHT = 500

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pygame First")
run = True
x = 50
y = 50
width = 40
height = 20
velocity = 5

def xLeft(x, width, velocity, winWidth):
    newX = x - velocity
    partialRecOne = None
    partialRecTwo = None

    if newX < 0:
        if newX > -width + 1:
            partialRecOne = (winWidth - 1 + newX, abs(newX))
            partialRecTwo = (1, width + newX)
#            print('x = {}, newX = {} width 1 {} width 2 {}'.format(x, newX, partialRecOne[1], partialRecTwo[1]))
        else:
            partialRecOne = (winWidth - 1 + newX, width)
            newX = winWidth + newX
            partialRecTwo = None
#            print('x = {}, newX = {} width 1 {}'.format(x, newX, partialRecOne[1]))
    elif newX == 0:
        partialRecOne = (1, width)
#        print('x = {}, newX = {} width 1 {}'.format(x, newX, width))
    else:
        partialRecOne = (newX, width)
#        print('#x = {}, newX = {} width 1 {}'.format(x, newX, width))

    return newX, partialRecOne, partialRecTwo

def xRight(x, velocity, winWidth):
    newX = x + velocity

    return newX

def yDown(y, velocity, winHeight):
    newY = y + velocity

    return newY

def yUp(y, velocity, winHeight):
    newY = y - velocity

    return newY

partialRecOne = None
partialRecTwo = None

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x, partialRecOne, partialRecTwo = xLeft(x, width, velocity, WIN_WIDTH)

    if keys[pygame.K_RIGHT]:
        x = xRight(x, velocity, WIN_WIDTH)

    if keys[pygame.K_UP]:
        y = yUp(y, velocity, WIN_HEIGHT)

    if keys[pygame.K_DOWN]:
        y = yDown(y, velocity, WIN_HEIGHT)

    win.fill((0, 0, 0)) #erasing previous rectangle

    if partialRecOne:
        pygame.draw.rect(win, (255, 0, 0), [partialRecOne[0], y, partialRecOne[1], height])
    if partialRecTwo:
        pygame.draw.rect(win, (255, 0, 0), [partialRecTwo[0], y, partialRecTwo[1], height])

    if not partialRecOne and not partialRecTwo:
        pygame.draw.rect(win, (255, 0, 0), [x, y, width, height])

    pygame.display.update()
pygame.quit()