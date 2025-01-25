import pygame

from src.classes.Button import Button
from src.classes.Player import Player


def methods(quit_button: Button,
            start_play_button: Button,
            screen):
    quit_button.check_hover(pygame.mouse.get_pos())
    quit_button.draw(screen)
    quit_button.check_hover(pygame.mouse.get_pos())
    quit_button.draw(screen)
    start_play_button.check_hover(pygame.mouse.get_pos())
    start_play_button.draw(screen)
    start_play_button.check_hover(pygame.mouse.get_pos())
    start_play_button.draw(screen)
