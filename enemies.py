import pygame



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






    def update(self):
        pointer = 2
        self.current_image += 1
        self.pos_x -= pointer
        if self.current_image >= len(self.dino_images):
            self.current_image = 0
        if self.pos_x >= 450:
            self.pos_x = pointer*-1
        if self.pos_x >= 740:
            self.pos_x = pointer*-1
        self.image = self.dino_images[self.current_image]



