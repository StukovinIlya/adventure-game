from pathlib import Path

import pygame
from pygame import Surface


def load_images() -> None:
    main_window = load_image('start_screen.jpg')


def load_image(name: str) -> Surface:
    fullname = Path() / 'assets' / 'images' / name
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    return image
