import random

import pygame
from typer.colors import RED

from src.classes.Tile import tile_width, tile_height
from src.units.load_images import load_tile_image


class Mob(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_tile_image('mob.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect()
        self.speed = 3
        self.direction = ['down', 'left', 'right', 'up']

    def update(self):
        direction = random.choice(self.direction)
        if direction == 'down':
            self.rect.y -= self.speed
        if direction == 'up':
            self.rect.y += self.speed
        if direction == 'left':
            self.rect.x -= self.speed
        if direction == 'up':
            self.rect.x += self.speed
