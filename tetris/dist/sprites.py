import pygame

import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


bangs = pygame.sprite.Group()


class Bang(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(bangs)
        self.image = load_image('frame_1.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.count = 1

    def update(self):
        self.count += 1
        if self.count <= 20:
            image_name = 'frame_' + str(self.count) + '.gif'
            self.image = load_image(image_name)