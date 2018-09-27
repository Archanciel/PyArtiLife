import pygame
WALK_SPEED_MULTIPLIER = 1
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

bg = pygame.image.load('expl_pygame_resources/bg.jpg')

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1 * WALK_SPEED_MULTIPLIER

        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

        self.walkRight = [pygame.image.load('expl_pygame_resources/R1.png'),
                          pygame.image.load('expl_pygame_resources/R2.png'),
                          pygame.image.load('expl_pygame_resources/R3.png'),
                          pygame.image.load('expl_pygame_resources/R4.png'),
                          pygame.image.load('expl_pygame_resources/R5.png'),
                          pygame.image.load('expl_pygame_resources/R6.png'),
                          pygame.image.load('expl_pygame_resources/R7.png'),
                          pygame.image.load('expl_pygame_resources/R8.png'),
                          pygame.image.load('expl_pygame_resources/R9.png')]
        self.walkLeft = [pygame.image.load('expl_pygame_resources/L1.png'),
                         pygame.image.load('expl_pygame_resources/L2.png'),
                         pygame.image.load('expl_pygame_resources/L3.png'),
                         pygame.image.load('expl_pygame_resources/L4.png'),
                         pygame.image.load('expl_pygame_resources/L5.png'),
                         pygame.image.load('expl_pygame_resources/L6.png'),
                         pygame.image.load('expl_pygame_resources/L7.png'),
                         pygame.image.load('expl_pygame_resources/L8.png'),
                         pygame.image.load('expl_pygame_resources/L9.png')]
        self.characterImg = pygame.image.load('expl_pygame_resources/standing.png')

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(self.characterImg, (self.x, self.y))



def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    
    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
run = True
while run:
    clock.tick(27 * WALK_SPEED_MULTIPLIER)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()


