from time import time

import pygame
from pygame import Surface

from src.classes.Camera import Camera
from src.sprites.sprites import all_sprites
from src.players.create_players import create_mario_player

position_x, position_y = 0, 0


def play(screen: Surface, FPS=60) -> None:
    global position_x, position_y
    player, x, y = create_mario_player(position_x, position_y)

    clock = pygame.time.Clock()

    camera = Camera(screen.get_size())
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)
        print(player.rect.x, player.rect.y)
        position_x, position_y = player.rect.x, player.rect.y

        screen.fill((255, 255, 255))
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
