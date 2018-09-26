from abc import ABCMeta
from abc import abstractmethod

import pygame

class Jump:
    '''
    Class managing the Shape jump behavior.
    '''
    def __init__(self, func, jumpCount, divider):
        self.shape = None
        self.func = func
        self.jumpCount, self.maxJump = jumpCount, jumpCount
        self.divider = divider
        self.isJumping = False

    def setShape(self, shape):
        self.shape = shape

    def jumpShape(self):
        jumpHeight = self.func(self.jumpCount) / self.divider
        #print("jumpHeight: {}, jumpCount: {}".format(jumpHeight, self.jumpCount))
        if self.jumpCount >= 0:
            self.jumpCount -= 1
            self.shape.vertMove(jumpHeight)
            self.isJumping = True
        elif self.jumpCount >= -self.maxJump:
            self.jumpCount -= 1
            self.shape.vertMove(self.func(-1) * -jumpHeight)
            self.isJumping = True
        else:
            self.isJumping = False
            self.jumpCount = self.maxJump

class Shape(metaclass=ABCMeta):
    '''
    Abstract class hosting code common to all child classes.
    '''
    def __init__(self, jumpObj):
        self.jumpObj = jumpObj

    def jump(self):
        self.jumpObj.jumpShape()

    def isJumping(self):
        return self.jumpObj.isJumping

class Rectangle(Shape):
    def __init__(self, x, y, width, height, velocity, jumpO, surface):
        jumpO.setShape(self)
        super().__init__(jumpO)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.surface = surface

    def moveRight(self):
        self.x += self.velocity

        if self.x + self.width > surface.get_width() - 1:
            self.x = surface.get_width() - self.width - 1

    def moveLeft(self):
        self.x -= self.velocity

        if self.x < 1:
            self.x = 1

    def moveDown(self):
        self.y += self.velocity

        if self.y + self.height > surface.get_height() - 1:
            self.y = surface.get_height() - self.height - 1

    def moveUp(self):
        self.y -= self.velocity

        if self.y < 1:
            self.y = 1
            
    def vertMove(self, height):
        self.y -= height

    def draw(self):
        pygame.draw.rect(self.surface, (255, 0, 0), [self.x, self.y, self.width, self.height])

pygame.init()

S_WIDTH = 500
S_HEIGHT = 500
S_BACKGROUND = (0, 0, 0)
FPS = 30


surface = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Explore Pygame jump')
clock = pygame.time.Clock()

jumpObj1 = Jump(func=lambda x : x ** 3, jumpCount=8, divider=4)
rec1 = Rectangle(x=S_WIDTH / 2, y=S_HEIGHT - 20, width=20, height=20, velocity=5, jumpO=jumpObj1, surface=surface)
jumpObj2 = Jump(func=lambda x : x ** 2, jumpCount=10, divider=2)
rec2 = Rectangle(x=S_WIDTH / 3, y=S_HEIGHT - 20, width=20, height=20, velocity=5, jumpO=jumpObj2, surface=surface)
jumpObj3 = Jump(func=lambda x : x ** 3, jumpCount=10, divider=7)
rec3 = Rectangle(x=S_WIDTH / 4, y=S_HEIGHT - 20, width=20, height=20, velocity=5, jumpO=jumpObj3, surface=surface)

run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        rec1.moveRight()
        rec2.moveRight()
        rec3.moveRight()

    if keys[pygame.K_LEFT]:
        rec1.moveLeft()
        rec2.moveLeft()
        rec3.moveLeft()

    if not rec1.isJumping():
        if keys[pygame.K_DOWN]:
            rec1.moveDown()

        if keys[pygame.K_UP]:
            rec1.moveUp()
    else:
        rec1.jump()

    if not rec2.isJumping():
        if keys[pygame.K_DOWN]:
            rec2.moveDown()

        if keys[pygame.K_UP]:
            rec2.moveUp()
    else:
        rec2.jump()

    if not rec3.isJumping():
        if keys[pygame.K_DOWN]:
            rec3.moveDown()

        if keys[pygame.K_UP]:
            rec3.moveUp()
    else:
        rec3.jump()

    if keys[pygame.K_SPACE]:
        rec1.jump()
        rec2.jump()
        rec3.jump()

    surface.fill(S_BACKGROUND)
    rec1.draw()
    rec2.draw()
    rec3.draw()
    pygame.display.update()
    pygame.time.wait(50) #less precise than delay, but consumes less procesSing power

pygame.quit()