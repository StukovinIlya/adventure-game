import pygame

from src.classes.Button import Button


def methods(quit_button: Button,
            start_play_button: Button,
            controls_button: Button,

            screen):
    quit_button.check_hover(pygame.mouse.get_pos())
    quit_button.draw(screen)
    start_play_button.check_hover(pygame.mouse.get_pos())
    start_play_button.draw(screen)
    controls_button.check_hover(pygame.mouse.get_pos())
    controls_button.draw(screen)


def methods_for_level_menu(quit_button: Button, firth_level: Button, screen) -> None:
    quit_button.check_hover(pygame.mouse.get_pos())
    quit_button.draw(screen)
    firth_level.check_hover(pygame.mouse.get_pos())
    firth_level.draw(screen)
