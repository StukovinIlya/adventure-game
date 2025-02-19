import random

import pygame
from pygame import Surface
from typer.colors import RED

from src.classes.Tile import tile_width, tile_height
from src.units.load_images import load_tile_image, load_image
SCREEN_WIDTH = 7936
SCREEN_HEIGHT = 2752


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = load_image('mob.png')
        self.rect = self.image.get_rect()
        self.rect.x = 32 * pos_x
        self.rect.y = 32 * pos_y
        self.speed = random.randint(1, 3)
        self.direction = random.choice(["up", "down", "left", "right"])

    def update(self):
        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

        # Если враг выходит за пределы экрана, меняем направление
        if self.rect.left < 0:
            self.direction = "right"
        elif self.rect.right > SCREEN_WIDTH:
            self.direction = "left"
        elif self.rect.top < 0:
            self.direction = "down"
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.direction = "up"