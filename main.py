import pygame, sys

from mario import Mario
from platform import *
from enemies import *
from cannon import *

pygame.init()
screen = pygame.display.set_mode((800, 510))
clock = pygame.time.Clock()
jump = False
alive = True
cannon_fired = False

bowser_alive = True

sprites = pygame.sprite.Group()
platform = Platform(0,450)
castle = Castle(0,300)
cannon = Cannon(768,400)
dino = Dino(650,400)
fireball = Bowser_Fireball(dino.pos_x-35,dino.pos_y+9)
mario = Mario(0, 400)
bullet = Bullet(700,395)
cloud = Cloud(450,50)
cloud2 = Cloud(250,35)
cloud3 = Cloud(600,35)

bush = Bush(160,418)


sprites.add(castle)
sprites.add(cannon)
sprites.add(cloud)
sprites.add(cloud2)
sprites.add(cloud3)
sprites.add(bush)

sprites.add(fireball)




for i in range(800):
    sprites.add(Platform(30*i,450))
    sprites.add(Platform(30 * i, 480))

sprites.add(mario)
sprites.add(dino)

game_bg_img = pygame.image.load('data/background-2.png').convert()
game_bg = pygame.transform.scale(game_bg_img,(800,600))



while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_d]:
            mario.update()
            if jump:
                mario.pos_x += 10

        if pygame.key.get_pressed()[pygame.K_a]:
            mario.update_left()
            if jump:
                mario.pos_x -= 10
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            jump = True

    if jump:
        mario.jump()
        if mario.speed < -mario.height:
            jump = False
            mario.speed = mario.height
            mario.initial_state()

    if mario.rect.colliderect(fireball.rect):
        alive = False

    if mario.rect.colliderect(dino.rect):
        alive = False

    if not alive:

        mario.die()
    if mario.rect.colliderect(cannon.rect):
        mario.rect.bottom = cannon.rect.top
        cannon_fired = True


    if bullet.rect.colliderect(dino.rect):

        bowser_alive = False


    if not bowser_alive:
        dino.die()


    if cannon_fired:

        cannon.update()
        sprites.add(bullet)
        bullet.launch()

    dino.update()
    fireball.update()

    screen.fill((0, 0, 0))
    screen.blit(game_bg, (0, 0))
    sprites.draw(screen)

    # sprites.update()
    pygame.display.flip()
    clock.tick(20)