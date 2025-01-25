from time import time

import pygame
from pygame import Surface


def play(screen: Surface) -> None:

    frame_start_time = time()
    frame_time = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('pink')
        pygame.display.flip()

        frame_end_time = time()
        frame_time = frame_end_time - frame_start_time
        frame_start_time = frame_end_time
