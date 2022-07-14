import pygame



class Platform(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('data/platform-top.png'), (30,30))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
    def update(self):
        pass




class Castle(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('data/castle.png'), (150,150))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
    def update(self):
        pass





