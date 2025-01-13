import pygame
pygame.init()

win = pygame.display.set_mode((900, 800))
run = True
pygame.display.set_caption("Pokemon Gamma Emerald")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = 
        self.rect


walkRight = [pygame.image.load("./assets/B right walk.png"), pygame.image.load("./assets/brendan look right stand.png"), pygame.image.load("./assets/B look right walk.png")]
walkLeft = [pygame.image.load("./assets/B look left walk 1.png"), pygame.image.load("./assets/B look left stand.png"), pygame.image.load("./assets/B look left walk 2.png")]
walkUp = [pygame.image.load("./assets/brendan walk behind 1.png"), pygame.image.load("./assets/brendan look back stand.png"), pygame.image.load("./assets/brendan walk behind 2.png")]
walkDown = [pygame.image.load("./assets/Brendan walk 1.png"), pygame.image.load("./assets/standingBrendan.png"), pygame.image.load("./assets/brendand walk 2.png")]
bg = pygame.image.load("./assets/littleroot.png")
char = pygame.image.load("./assets/standingBrendan.png")

clock = pygame.time.Clock()
x = 250#where object starts
y = 250#where object starts
width = 13
height = 21
vel = 6
left = False
right = False
up = False
down = False
walkCount = 0

def reDrawGameWindow():
    global walkCount

    win.blit(bg, (0,0))

    if walkCount >= 3:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount], (x,y))
        walkCount += 1
    elif up:
        win.blit(walkUp[walkCount], (x,y))
        walkCount += 1
    elif down:
        win.blit(walkDown[walkCount], (x,y))
        walkCount += 1
    else: 
        win.blit(char, (x,y))

    pygame.display.update()

while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 70:
        x -= vel
        left = True
        right = False
        down = False
        up = False
    elif keys[pygame.K_RIGHT] and x < 900 - 70:#second condition is a way to set the bondary 
        x += vel
        right = True
        left = False
        up = False
        down = False
    elif keys[pygame.K_UP] and y > 80:
        y -= vel
        up = True
        down = False
        right = False
        left = False
    elif keys[pygame.K_DOWN] and y < 700 - 80:
        y += vel
        up = False
        down = True
        right = False
        left = False
    else:
        up = False
        down = False
        right = False
        left = False


    reDrawGameWindow()

pygame.quit()
