import pygame.sprite
from pygame import Surface
from typer.colors import YELLOW

from src.sprites.sprites import all_sprites, bullets
from src.units.load_images import load_image, load_tile_image


class Bullet(pygame.sprite.Sprite):
    def __init__(
            self, x: int,
            y: int,

            image_path: str,
    ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_path)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10


    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()
