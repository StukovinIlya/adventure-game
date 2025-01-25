import pygame
from pygame import Surface

from src.constants.constants import get_velocity
from src.sprites.sprites import all_sprites
from src.units.load_images import load_image


class Player:
    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 image_path: str,
                 mario
                 ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        mario.image = load_image(image_path)
        mario.image = pygame.transform.scale(mario.image, (width, height))
        mario.rect = mario.image.get_rect()
        self.velocity = get_velocity()
        self.hero = mario


    def draw(self, screen: Surface) -> None:
        all_sprites.draw(screen)

    def update(self, key, frame_time):
        if key[pygame.K_DOWN]:
            self.hero.rect.top += self.velocity * frame_time
        if key[pygame.K_UP]:
            self.hero.rect.top -= self.velocity * frame_time
        if key[pygame.K_RIGHT]:
            self.hero.rect.left += self.velocity * frame_time
        if key[pygame.K_LEFT]:
            self.hero.rect.left -= self.velocity * frame_time
