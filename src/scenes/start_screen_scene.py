import pygame
from pygame import Surface

from src.buttons.create_buttons import create_quit_button
from src.scenes.terminate import terminate
from src.units.load_start_screen import load_start_screen
from src.buttons.handle_event import running_handle_event
from src.buttons.button_methods import button_methods


def start_screen(screen: Surface) -> None:
    load_start_screen(screen)
    quit_button = create_quit_button(s)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT and event.button == quit_button:
                terminate()

            quit_button.handle_event(event)
            # start_play_button.handle_event(event)

        quit_button.check_hover(pygame.mouse.get_pos())
        quit_button.draw(screen)
        # start_play_button.check_hover(pygame.mouse.get_pos())
        # start_play_button.draw(screen)
        pygame.display.flip()
