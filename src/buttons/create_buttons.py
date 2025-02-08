from pygame import Surface

from src.classes.Button import Button


def create_quit_button(screen: Surface) -> Button:
    widht, height = screen.get_size()
    quit_button = Button(
        widht * 0.08,
        height * 0.75,
        100,
        100,
        '',
        "quit_button.png",
        'hover_quit_button.png',
        None
    )
    return quit_button


def create_start_play_button(screen: Surface) -> Button:
    widht, height = screen.get_size()
    start_play_button = Button(
        widht * 0.73,
        height * 0.60,
        250,
        50,
        'Play',
        'start_play.png',
        None,
        None
    )
    return start_play_button


def create_controls_button(screen: Surface) -> Button:
    widht, height = screen.get_size()
    controls_button = Button(
        widht * 0.73,
        height * 0.67,
        250,
        50,
        'Controls',
        'start_play.png',
        None,
        None,
    )
    return controls_button

def create_level_button(screen: Surface) -> Button:
    widht, height = screen.get_size()
    level_button = Button(
        widht * 0.18,
        height * 0.14,
        80,
        100,
        None,
        'level1.jpg',
        None,
        None,
    )
    return level_button