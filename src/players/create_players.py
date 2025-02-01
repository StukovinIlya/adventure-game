from src.classes.Player import Player
from src.classes.Tile import Tile


def create_mario_player(level) -> Player:
    coords = None
    new_player, pos_x, pos_y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('wall', x, y)
            elif level[y][x] == '1':
                Tile('ground', x, y)
            elif level[y][x] == '3':
                Tile('die_tile', x, y)
            elif level[y][x] == '2':
                Tile('steps', x, y)
            elif level[y][x] == '@':
                Tile('ground', x, y)
                coords = x, y
    print(coords)
    new_player = Player(*coords)
    return new_player, pos_x, pos_y