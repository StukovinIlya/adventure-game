from pathlib import Path

import pygame
from pygame import Surface


def load_sound(name: str) -> Surface:
    fullname = Path() / 'assets' / 'sound' / name
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound', name)
        raise SystemExit(message)
    return sound
