import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Attacker")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

backgroundImg = pygame.image.load('space-v1.png')
score = 0

playerImg = pygame.image.load('space-invaders.png')
playerx = 370
playery = 480
playerx_step = 0

bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_step = 0
bullety_step = 40
bullet_state = "ready"

enemyImg = pygame.image.load('alien.png')
enemyx = random.randint(0,800)
enemyy = random.randint(50,150)
enemyx_step = 4
enemyy_step = 40

def addPlayer(x,y):
    screen.blit(playerImg,(x,y))

def addEnemy(x,y):
    screen.blit(enemyImg,(x,y))

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

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(backgroundImg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_step += -5
            if event.key == pygame.K_RIGHT:
                playerx_step += 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
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

    enemyx += enemyx_step

    if enemyx <= 0:
        enemyx_step = 4
        enemyy += enemyy_step
    elif enemyx >= 736:
        enemyx_step = -4
        enemyy += enemyy_step
    
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        addBullet(playerx,bullety)
        bullety -= bullety_step

    collision = isCollision(enemyx,enemyy,bulletx,bullety)
    if collision:
        bullety = 480
        bullet_state = "ready"
    
    addPlayer(playerx,playery)
    addEnemy(enemyx,enemyy)
    pygame.display.update()