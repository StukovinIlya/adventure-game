from src.classes.Player import Player

from src.sprites.sprites import mario


def create_mario_player() -> Player:
    mario_player = Player(
        100,
        100,
        24,
        40,
        'player.png',
        mario

    )
    return mario_player
