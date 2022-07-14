import pygame, sys
from mario import Mario
from platform import Platform,Castle
from enemies import *
from cannon import *

pygame.init()
screen = pygame.display.set_mode((800, 510))
clock = pygame.time.Clock()
jump = False

sprites = pygame.sprite.Group()
mario = Mario(0, 400)
platform = Platform(0,450)
castle = Castle(0,300)
cannon = Cannon(750,400)
dino = Dino(690,400)


sprites.add(castle)
# sprites.add(Platform(0,50))
sprites.add(cannon)
sprites.add(dino)
sprites.add(mario)

for i in range(800):
    sprites.add(Platform(30*i,450))
    sprites.add(Platform(30 * i, 480))




game_bg_img = pygame.image.load('data/background-2.png').convert()
game_bg = pygame.transform.scale(game_bg_img,(800,600))



while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_d]:
            sprites.update()
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

    dino.update()
    screen.fill((0, 0, 0))
    screen.blit(game_bg, (0, 0))
    sprites.draw(screen)

    # sprites.update()
    pygame.display.flip()
    clock.tick(20)