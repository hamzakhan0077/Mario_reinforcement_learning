
import pygame



class Mario(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()

        self.sprites = []


        # self.sprites.append(pygame.image.load('data/mario1.png'))
        # self.sprites.append(pygame.image.load('data/mario2.png'))
        # self.sprites.append(pygame.image.load('data/mario3.png'))
        # self.sprites.append(pygame.image.load('data/mario4.png'))
        # self.sprites.append(pygame.image.load('data/mario5.png'))

        self.sprites.append(pygame.transform.scale(pygame.image.load('data/mario1.png'), (50,50)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('data/mario2.png'), (50,50)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('data/mario3.png'), (50,50)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('data/mario4.png'), (50,50)))
        # self.sprites.append(pygame.transform.scale(pygame.image.load('data/mario5.png'), (50,50))) # jump image
        self.flipped_sprites = [pygame.transform.flip(image, True, False) for image in self.sprites]



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.height = 10
        self.speed = 3
        self.gravity = 5

        # 00
    def initial_state(self):
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.image = pygame.transform.scale(pygame.image.load('data/mario1.png'), (50, 50))


    def update(self):
        # for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_d:
        self.current_sprite += 1
        self.pos_x += 5
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect.topleft = [self.pos_x, self.pos_y]

    def update_left(self):
        self.current_sprite += 1
        self.pos_x -= 5
        if self.current_sprite >= len(self.flipped_sprites):
            self.current_sprite = 0
        self.image = self.flipped_sprites[self.current_sprite]
        self.rect.center = [self.pos_x, self.pos_y]

    def jump(self):
        self.pos_y -= self.speed
        self.speed -= self.gravity
        self.image = pygame.transform.scale(pygame.image.load('data/mario5.png'), (50,50))
        self.rect.center = [self.pos_x, self.pos_y]






        # self.pos_y -= 10
        # self.rect.center = [self.pos_x, self.pos_y]
        # self.pos_y += 5
        # self.rect.center = [self.pos_x, self.pos_y]







if __name__ == '__main__':
    pass