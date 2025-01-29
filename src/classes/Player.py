import pygame
from pygame.key import ScancodeWrapper

from src.sprites.sprites import player_group, all_sprites
from src.units.load_images import load_image




class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = load_image('player.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)

        self.speed = 50
        self.cooldown = 0
        self.coldown_time = 3

    def move(self, keys: ScancodeWrapper):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_s]:
            self.rect.y += self.speed
