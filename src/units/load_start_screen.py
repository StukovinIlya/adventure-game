from pygame import Surface

from src.units.get_background import get_background


def load_start_screen(screen: Surface) -> None:
    background = get_background('start_screen.jpg', screen)
    screen.blit(background, (0, 0))
