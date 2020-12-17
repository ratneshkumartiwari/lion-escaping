import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1450,625))

k = random.randint(10,3500)
l = random.randint(10,3500)
m = random.randint(10,3500)
n = random.randint(10,3500)
o = random.randint(10,3500)
p = random.randint(10,3500)
q = random.randint(10,3500)
r = random.randint(10,3500)
s = 200
t=  1200
u = 700



k_change = -5

#backgroung
background= pygame.image.load("bg2.png")

#home & school
home1 = pygame.image.load("home1.png")
home2 = pygame.image.load("home2.png")
home3 = pygame.image.load("home3.png")
cloud = pygame.image.load("cloud.png")
cloud2 = pygame.image.load("cloud2.png")
church = pygame.image.load("church.png")
school = pygame.image.load("school.png")
rain = pygame.image.load("rain.png")
grass = pygame.image.load("grass1.png")
flower = pygame.image.load("flower.png")
sun = pygame.image.load("sun.png")
lion = pygame.image.load("lion.png")

lionY = 325
lionX = 50
lion_changeX = 0
lion_changeY = 0

#lion
def animal(x,y):
    screen.blit(lion, (x,y))











running= True
while running:
    screen.blit(background, (0,0))
    screen.blit(sun, (1200, 45))


    screen.blit(home1, (k,309))
    k += k_change
    if k<= -200:
        k = random.randint(1600,3500)

    screen.blit(church, (m, 309))
    m += k_change
    if m <= -200:
        m = random.randint(1600, 3500)

    screen.blit(school, (n, 314))
    n += k_change
    if n <= -200:
        n = random.randint(1600, 3500)

    screen.blit(cloud, (p, 55))
    p += k_change
    if p <= -200:
        p = random.randint(1600, 2000)

    screen.blit(cloud2, (q, 150))
    q += k_change
    if q <= -200:
        q = random.randint(1600, 2000)

    screen.blit(home2, (l, 314))
    l += k_change
    if l <= -200:
        l = random.randint(1600, 3500)

    screen.blit(home3, (o, 314))
    o += k_change
    if o <= -200:
        o = random.randint(1600, 3500)

    screen.blit(rain, (r, 75))
    r += k_change
    if r <= -200:
        r = random.randint(1600, 2500)

    screen.blit(grass, (s, 450))
    s += k_change
    if s <= -300:
        s = 1900

    screen.blit(grass, (t, 450))
    t += k_change
    if t <= -300:
        t = 1900

    screen.blit(flower, (u, 450))
    u += k_change
    if u <= -300:
        u = 1900



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                lion_changeX = 10
            if event.key == pygame.K_LEFT:
                lion_changeX = -10
            if event.key == pygame.K_SPACE:
                lion_changeY = -10
            if event.key == pygame.K_DOWN:
                lion_changeY = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_DOWN:
                lion_changeY = 3
            else:
                lion_changeX = 0



    lionX += lion_changeX
    lionY += lion_changeY

    if lionX >= 1320:
        lionX = 1320
    if lionX <= 0:
        lionX = 0

    if lionY <= 0:
        lionY = 0
    if lionY >=325:
        lionY =325


    animal(lionX,lionY)
    pygame.display.update()