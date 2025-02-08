import pygame

from src.classes.Bullet import Bullet
from src.sprites.sprites import all_sprites, bullets
from src.units.load_images import load_tile_image


class Bow_Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = load_tile_image(image_path)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.health = 1000
