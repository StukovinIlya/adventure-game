from time import time

import pygame
from pygame import Surface

from src.buttons.button_methods import methods_for_level_menu
from src.buttons.create_buttons import create_quit_button, create_level_button
from src.scenes.first_level import play
from src.scenes.terminate import terminate
from src.units.load_start_screen import load_start_screen


def levels_menu(screen: Surface) -> None:
    frame_time = 0
    frame_start_time = time()
    load_start_screen(screen)
    quit_button = create_quit_button(screen)
    firth_level = create_level_button(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT and event.button == quit_button:
                return
            if event.type == pygame.USEREVENT and event.button == firth_level:
                play(screen, 60)

            quit_button.handle_event(event)
            firth_level.handle_event(event)
        frame_end_time = time()
        frame_time = (frame_end_time - frame_start_time)
        frame_start_time = frame_end_time
        methods_for_level_menu(quit_button, firth_level, screen)
        pygame.display.flip()
