from src.buttons.buttons import (
    quit_button,
    start_play_button,
)


def running_handle_event(event) -> None:
    quit_button.handle_event(event)
    start_play_button.handle_event(event)

