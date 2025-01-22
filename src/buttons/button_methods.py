import pygame
from pygame import Surface

from src.buttons.buttons import (
    quit_button,
    start_play_button,
)


def button_methods(screen: Surface) -> None:
    quit_button.check_hover(pygame.mouse.get_pos())
    quit_button.draw(screen)
    start_play_button.check_hover(pygame.mouse.get_pos())
    start_play_button.draw(screen)
