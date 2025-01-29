from src.classes.Button import Button


def create_quit_button() -> Button:
    quit_button = Button(
        120,
        700,
        100,
        100,
        '',
        "quit_button.png",
        'hover_quit_button.png',
        None
    )
    return quit_button


def create_start_play_button() -> Button:
    start_play_button = Button(
        1125,
        550,
        250,
        50,
        'Play',
        'start_play.png',
        None,
        None
    )
    return start_play_button
