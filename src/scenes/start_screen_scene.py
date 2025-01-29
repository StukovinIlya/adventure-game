from time import time

import pygame
from pygame import Surface

from src.buttons.button_methods import methods
from src.buttons.create_buttons import create_quit_button, create_start_play_button
from src.scenes.terminate import terminate
from src.units.load_start_screen import load_start_screen


def start_screen(screen: Surface) -> None:
    frame_time = 0
    frame_start_time = time()
    load_start_screen(screen)
    quit_button = create_quit_button()
    start_play_button = create_start_play_button()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT and event.button == quit_button:
                terminate()
            if event.type == pygame.USEREVENT and event.button == start_play_button:
                return

            quit_button.handle_event(event)
            start_play_button.handle_event(event)

        methods(quit_button, start_play_button, screen)
        pygame.display.flip()
        frame_end_time = time()
        frame_time = (frame_end_time - frame_start_time)
        frame_start_time = frame_end_time
        pygame.display.flip()
