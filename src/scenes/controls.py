from time import time

from pygame import Surface
import pygame

from src.buttons.create_buttons import create_quit_button
from src.scenes.terminate import terminate
from src.units.load_controls_screen import load_controls_screen
from src.units.load_start_screen import load_start_screen


def controls(screen: Surface) -> None:
    frame_time = 0
    frame_start_time = time()
    load_controls_screen(screen)
    quit_button = create_quit_button(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT and event.button == quit_button:
                load_start_screen(screen)
                return

            quit_button.handle_event(event)

        quit_button.check_hover(pygame.mouse.get_pos())
        quit_button.draw(screen)
        pygame.display.flip()
        frame_end_time = time()
        frame_time = (frame_end_time - frame_start_time)
        frame_start_time = frame_end_time
        pygame.display.flip()
