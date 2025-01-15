import pygame
from pygame import Surface


def init_screen() -> Surface:
    pygame.init()
    pygame.display.set_caption('Игра')

    display_info = pygame.display.Info()
    size = display_info.current_w, display_info.current_h
    screen = pygame.display.set_mode(size)
    return screen
