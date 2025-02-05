from pygame import Surface

from src.units.get_background import get_background


def load_controls_screen(screen: Surface) -> None:
    background = get_background('controls.jpg', screen)
    screen.blit(background, (0, 0))
