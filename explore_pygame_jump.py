import pygame

class Rectangle:
    def __init__(self, x, y, width, height, velocity, surface):
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

    surface.fill(S_BACKGROUND)
    rec.draw()
    pygame.display.update()
    pygame.time.wait(50) #less precise than delay, but consumes less procesSing power

pygame.quit()