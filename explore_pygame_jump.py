from abc import ABCMeta
from abc import abstractmethod

import pygame

class Jump:
    '''
    Class managing the Shape jump behavior.
    '''
    def __init__(self, shape, func, jumpCount, divider):
        self.shape = shape
        self.func = func
        self.jumpCount, self.maxJump = jumpCount, jumpCount
        self.divider = divider
        self.isJumping = False

    def jumpShape(self):
        jumpHeight = self.func(self.jumpCount) / self.divider

        if self.jumpCount >= 0:
            self.jumpCount -= 1
            self.shape.vertMove(jumpHeight)
            self.isJumping = True
        elif self.jumpCount >= -self.maxJump:
            self.jumpCount -= 1
            self.shape.vertMove(-jumpHeight)
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
    def __init__(self, x, y, width, height, velocity, surface):
        def f(x):
            return x ** 2
        super().__init__(Jump(self, f, 10, 2))
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

rec = Rectangle(x=S_WIDTH / 2, y=S_HEIGHT / 2, width=20, height=20, velocity=5, surface=surface)

run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        rec.moveRight()

    if keys[pygame.K_LEFT]:
        rec.moveLeft()

    if not rec.isJumping():
        if keys[pygame.K_DOWN]:
            rec.moveDown()

        if keys[pygame.K_UP]:
            rec.moveUp()
    else:
        rec.jump()

    if keys[pygame.K_SPACE]:
        rec.jump()

    surface.fill(S_BACKGROUND)
    rec.draw()
    pygame.display.update()
    pygame.time.wait(50) #less precise than delay, but consumes less procesSing power

pygame.quit()