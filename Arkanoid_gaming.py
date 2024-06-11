import pygame
from random import randrange
width =1300
height = 800
paddle_h = 30
paddle_w = 300
fps = 60
score = 0
paddle = pygame.Rect(width / 2 - paddle_w / 2, height - paddle_h - 10, paddle_w, paddle_h)
paddle_speed = 15
Baller_R = 20
Baller_D = Baller_R * 2
Baller_speed = 7
trail = []
Baller = pygame.Rect(randrange(Baller_D, width - Baller_D), height / 2, Baller_D, Baller_D)
d_y = -1
d_x = 1
def kasatsa (d_x, d_y, Baller, rect):
    if d_x > 0:
        x = Baller.right - rect.left
    else:
        x = rect.right - Baller.left
    if d_y > 0:
        y = Baller.bottom - rect.top
    else:
        y = rect.bottom - Baller.top
    if abs (x - y) < 10:
        d_x = -d_x
        d_y = -d_y
    elif x > y:
        d_y = -d_y
    elif x < y:
        d_x = -d_x
    return d_x, d_y
bricks = [
    pygame.Rect(10 + 120 * i, 10 + 70 * j,100,50)
    for i in range(11)
    for j in range(4)
]
colors = [
    (randrange(30, 256),randrange(30, 256),randrange(30,256))
    for i in range(11)
    for j in range(4)
]
pygame.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("A.R.K.A.N.O.I.D. PREMIUM DELUXE LUXARY RTX EDITION")
load = pygame.image.load("ya hochy kakat.jpg").convert()
win = pygame.image.load("win.jpg").convert()
lose = pygame.image.load("pixil-frame-0-_4_.jpg").convert()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    window.blit(load, (0,0))
    pygame.draw.rect(window, pygame.Color("darkorange"), paddle)
    pygame.draw.circle(window, pygame.Color("darkblue"), Baller.center, Baller_R)
    [
        pygame.draw.rect(window, colors[color], block)
        for color,block in enumerate(bricks)
    ]
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    trail.append([Baller.centerx, Baller.centery, d_x, d_y, 255])
    for element in trail:
        element[0] += element[2]
        element[1] += element[3]
    if element[4] >= 0:element[4] /= 2
    if len(trail) > 8:
        trail.remove(element)
    pygame.draw.circle(surface, (255, 255, 255, int(element[4])), (int(element[0]), int(element[1])), Baller_R)
    window.blit(surface, (0, 0))
    Baller.x += Baller_speed * d_x
    Baller.y += Baller_speed * d_y
    if Baller.centerx < Baller_R or Baller.centerx > width - Baller_R:
        d_x = - d_x
    elif Baller.centery < Baller_R:
        d_y = - d_y
    elif Baller.colliderect(paddle) and d_y > 0:
        d_x,d_y = kasatsa(d_x,d_y,Baller,paddle)
    hit = Baller.collidelist(bricks)
    if hit != -1:
        block = bricks.pop(hit)
        d_x, d_y = kasatsa(d_x, d_y, Baller, block)
        score += 100
        fps += 1
    # if Baller.bottom > height or not len (bricks):
    #     exit()
    if not len (bricks):
        win = pygame.transform.scale(win, (window.get_width(), window.get_height()))
        window.blit(win, (0, 0))
    elif Baller.bottom > height:
        lose = pygame.transform.scale(lose, (window.get_width(), window.get_height()))
        window.blit(lose, (0, 0))
    key = pygame.key.get_pressed()
    if (key[pygame.K_LEFT] or key[pygame.K_a]) and paddle.left>0:
        paddle.left -= paddle_speed
    elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and paddle.right<width:
        paddle.right += paddle_speed
    score_font = pygame.font.Font(None, 48)
    score_text = score_font.render(str(score), True, (255, 255, 255))
    window.blit(score_text, (1100, 650))
    pygame.display.flip()
    clock.tick(fps)