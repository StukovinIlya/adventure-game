from src.classes.Player import Player



def create_mario_player(pos_x, pos_y) -> Player:
    coords = x, y = pos_x, pos_y
    mario_player = Player(*coords)
    return mario_player, x, y
