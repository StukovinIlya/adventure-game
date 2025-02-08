from time import time

import pygame
from pygame import Surface

from src.classes.Camera import Camera
from src.sprites.sprites import all_sprites, bullets, player_group
from src.Animated_souls.create_players import create_player
from src.units.load_level import load_level


def play(screen: Surface, FPS=60) -> None:
    player, bow_tower, x, y = create_player(load_level('cave.txt'))
    player_group.add(player, bow_tower)

    clock = pygame.time.Clock()

    camera = Camera(screen.get_size())
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        all_sprites.update()

        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((255, 255, 255))

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
