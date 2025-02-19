from src.classes.Bow_Tower import Bow_Tower

from src.classes.Player import Player
from src.classes.Tile import Tile
from src.sprites.sprites import all_sprites


def create_player(level):
    coords = None
    coords_bow_tower = None
    mob_coords = []
    new_player, pos_x, pos_y = None, None, None
    mobs =  None
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
            elif level[y][x] == 'a':
                Tile('bow_tower1', x, y)
            elif level[y][x] == 'b':
                Tile('bow_tower2', x, y)
            elif level[y][x] == 'c':
                Tile('bow_tower3', x, y)
            elif level[y][x] == 'd':
                Tile('bow_tower4', x, y)
            elif level[y][x] == 'e':
                Tile('bow_tower5', x, y)
            elif level[y][x] == 'f':
                Tile('bow_tower6', x, y)
            elif level[y][x] == 'j':
                Tile('bow_tower7', x, y)
            elif level[y][x] == 'k':
                Tile('bow_tower8', x, y)
                coords_bow_tower = x, y
            elif level[y][x] == 'l':
                Tile('bow_tower9', x, y)
            elif level[y][x] == 'm':
                Tile('bow_tower10', x, y)
            elif level[y][x] == 'n':
                Tile('bow_tower11', x, y)
            elif level[y][x] == 'o':
                Tile('bow_tower12', x, y)
            elif level[y][x] == '&':
                Tile('ground', x, y)
            elif level[y][x] == '5':
                Tile('ground', x, y)
                print(x, y)
                mob_coords.append((x, y))

            elif level[y][x] == '@':
                Tile('ground', x, y)
                coords = x, y
    new_player = Player(*coords)
    bow_tower = Bow_Tower(*coords_bow_tower, image_path='bow_tower8.jpg')
    return new_player, bow_tower, pos_x, pos_y, mob_coords
