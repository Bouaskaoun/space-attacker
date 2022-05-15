from numpy import empty
import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Attacker")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
backgroundImg = pygame.image.load('space-v1.png')
score_value = 0
score_font = pygame.font.Font('With You.otf',32)
game_over_font = pygame.font.Font('With You.otf',64)

textx = 10
texty = 10

playerImg = pygame.image.load('space-invaders.png')
playerx = 370
playery = 480
playerx_step = 0

bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_step = 0
bullety_step = 10
bullet_state = "ready"

enemyImg = []
enemyx = []
enemyy = []
enemyx_step = []
enemyy_step = []
numberOfenemy = 6
for num in range(numberOfenemy):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    enemyx_step.append(3)
    enemyy_step.append(40)


def addPlayer(x,y):
    screen.blit(playerImg,(x,y))

def addEnemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def addBullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16,y + 10))

def isCollision(enemyx,enemyy,bulletx,bullety):
    x = math.pow(enemyx - bulletx,2)
    y = math.pow(enemyy - bullety,2)
    distance = math.sqrt(x + y)
    if distance < 27:
        return True
    else:
        return False

def show_score(x,y):
    score = score_font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(270,250))

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(backgroundImg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_step += -4
            if event.key == pygame.K_RIGHT:
                playerx_step += 4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sounds = pygame.mixer.Sound('laser.wav')
                    bullet_sounds.play()
                    bulletx = playerx
                    addBullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_step = 0

        
    playerx += playerx_step

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    for num in range(numberOfenemy):
        if enemyy[num] > 440:
            for j in range(numberOfenemy):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[num] += enemyx_step[num]
        if enemyx[num] <= 0:
            enemyx_step[num] = 3
            enemyy[num] += enemyy_step[num]
        elif enemyx[num] >= 736:
            enemyx_step[num] = -3
            enemyy[num] += enemyy_step[num]
        
        collision = isCollision(enemyx[num],enemyy[num],bulletx,bullety)
        if collision:
            explusion_sound = pygame.mixer.Sound('explosion.wav')
            explusion_sound.play()
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            enemyx[num] = random.randint(0,735)
            enemyy[num] = random.randint(50,150)
        
        addEnemy(enemyx[num],enemyy[num],num)
    
    
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        addBullet(bulletx,bullety)
        bullety -= bullety_step
    
    addPlayer(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()