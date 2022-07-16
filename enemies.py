import pygame



class Bowser_Fireball(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()

        self.bowser_fireball_images = []
        self.bowser_fireball_images = []

        self.bowser_fireball_images.append(pygame.transform.scale(pygame.image.load('data/bowser-fireball1.png'), (48, 16)))
        self.bowser_fireball_images.append(pygame.transform.scale(pygame.image.load('data/bowser-fireball2.png'), (48, 16)))
        self.bowser_fireball_images.append(pygame.transform.scale(pygame.image.load('data/bowser-fireball3.png'), (48, 16)))

        self.current_image = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = self.bowser_fireball_images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    def update(self):
        self.current_image += 1
        if self.current_image >= len(self.bowser_fireball_images):
            self.current_image = 0
            self.pos_x -= 10
        self.image = self.bowser_fireball_images[self.current_image]
        self.rect.topleft = [self.pos_x, self.pos_y]




class Dino(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.dino_images = []
        self.dino_images.append(pygame.transform.scale(pygame.image.load('data/bowser1.png'), (50, 50)))
        self.dino_images.append(pygame.transform.scale(pygame.image.load('data/bowser2.png'), (50, 50)))
        self.dino_images.append(pygame.transform.scale(pygame.image.load('data/bowser3.png'), (50, 50)))
        self.dino_images.append(pygame.transform.scale(pygame.image.load('data/bowser4.png'), (50, 50)))



        self.current_image = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = self.dino_images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.in_limit = True
        self.panic = True

    def update(self):
        self.current_image += 1
        if self.current_image >= len(self.dino_images):
            self.current_image = 0
        if self.pos_x <= 450:
            self.in_limit = False
        if self.pos_x == 690:
            self.in_limit = True
        if self.in_limit:
            self.pos_x -= 1
        else:
            self.pos_x += 1
        self.image = self.dino_images[self.current_image]
        self.rect.topleft = [self.pos_x, self.pos_y]

    def die(self):
        if self.pos_y <= 300:
            self.panic = False
        if self.panic:
            self.pos_y -= 15
        else:
            self.pos_y += 15

        self.rect.topleft = [self.pos_x, self.pos_y]









