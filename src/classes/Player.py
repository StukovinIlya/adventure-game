import pygame
from pygame.key import ScancodeWrapper
from pygame.sprite import spritecollideany

from src.classes.Bullet import Bullet
from src.sprites.sprites import player_group, all_sprites, wall_group, bullets
from src.units.load_images import load_image
from src.classes.Tile import tile_width, tile_height


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = load_image('player.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.max_speed = 3
        self.min_speed = 1
        self.speed = 10
        self.cooldown = 0
        self.cooldown_time = 3
        self.direction = 'down'
        self.health = 100

    def move(self, keys: ScancodeWrapper):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if keys[pygame.K_LSHIFT]:
                self.rect.x -= self.max_speed
                if spritecollideany(self, wall_group) is not None:
                    self.rect.x += self.speed
            elif keys[pygame.K_LCTRL]:
                self.rect.x -= self.min_speed
            else:
                self.rect.x -= self.speed
            # if spritecollideany(self, wall_group) is not None:
            #     self.rect.x += self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if keys[pygame.K_LSHIFT]:
                self.rect.x += self.max_speed
                if spritecollideany(self, wall_group) is not None:
                    self.rect.x -= self.speed
            elif keys[pygame.K_LCTRL]:
                self.rect.x += self.min_speed
            else:
                self.rect.x += self.speed
            # if spritecollideany(self, wall_group) is not None:
            #     self.rect.x -= self.speed

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if keys[pygame.K_LSHIFT]:
                self.rect.y -= self.max_speed
                if spritecollideany(self, wall_group) is not None:
                    self.rect.y += self.speed
            elif keys[pygame.K_LCTRL]:
                self.rect.y -= self.min_speed
            else:
                self.rect.y -= self.speed
            # if spritecollideany(self, wall_group) is not None:
            #     self.rect.y += self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if keys[pygame.K_LSHIFT]:
                self.rect.y += self.max_speed
                if spritecollideany(self, wall_group) is not None:
                    self.rect.y -= self.speed
            elif keys[pygame.K_LCTRL]:
                self.rect.y += self.min_speed
            else:
                self.rect.y += self.speed
            # if spritecollideany(self, wall_group) is not None:
            #     self.rect.y -= self.speed

    def shoot(self) -> Bullet:
        bullet = Bullet(self.rect.x, self.rect.y, 'arrow.png')
        all_sprites.add(bullet)
        bullets.add(bullet)

