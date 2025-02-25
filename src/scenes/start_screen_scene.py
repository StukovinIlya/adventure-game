from time import time

import pygame
from pygame import Surface

from src.buttons.button_methods import methods
from src.buttons.create_buttons import create_quit_button, create_start_play_button, create_controls_button
from src.scenes.levels_menu import levels_menu
from src.scenes.terminate import terminate
from src.units.load_start_screen import load_start_screen
from src.scenes.controls import controls


def start_screen(screen: Surface) -> None:
    frame_time = 0
    frame_start_time = time()
    load_start_screen(screen)
    quit_button = create_quit_button(screen)
    start_play_button = create_start_play_button(screen)
    controls_button = create_controls_button(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT and event.button == quit_button:
                terminate()
            if event.type == pygame.USEREVENT and event.button == start_play_button:
                levels_menu(screen)
            if event.type == pygame.USEREVENT and event.button == controls_button:
                controls(screen)

            quit_button.handle_event(event)
            start_play_button.handle_event(event)
            controls_button.handle_event(event)

        methods(quit_button, start_play_button, controls_button, screen)
        frame_end_time = time()
        frame_time = (frame_end_time - frame_start_time)
        frame_start_time = frame_end_time
        pygame.display.flip()
