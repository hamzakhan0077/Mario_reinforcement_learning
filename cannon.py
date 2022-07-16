import pygame




class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('data/cannonbullet1.png'), (30, 20))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    def launch(self):
        self.pos_x -= 4
        self.rect.topleft = [self.pos_x, self.pos_y]

class Cannon(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()

        self.cannon_img_initial = pygame.transform.scale(pygame.image.load('data/cannon1.png'), (32, 64))
        self.cannon_img_pressed = pygame.transform.scale(pygame.image.load('data/cannon2.png'), (32, 64))
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = self.cannon_img_initial
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    def update(self):
        self.image = self.cannon_img_pressed
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

