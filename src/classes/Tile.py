import pygame

from src.sprites.sprites import tiles_group, all_sprites, wall_group, die_group
from src.units.load_images import load_tile_image

tile_width = tile_height = 32


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        tile_images = {
            'wall': load_tile_image('wall.png'),
            'ground': load_tile_image('ground.png'),
            'steps': load_tile_image('steps.png'),
            'die_tile': load_tile_image('die_tile.png'),
            'bow_tower1': load_tile_image('bow_tower.jpg'),
            'bow_tower2': load_tile_image('bow_tower2.jpg'),
            'bow_tower3': load_tile_image('bow_tower3.jpg'),
            'bow_tower4': load_tile_image('bow_tower4.jpg'),
            'bow_tower5': load_tile_image('bow_tower5.jpg'),
            'bow_tower6': load_tile_image('bow_tower6.jpg'),
            'bow_tower7': load_tile_image('bow_tower7.jpg'),
            'bow_tower8': load_tile_image('bow_tower8.jpg'),
            'bow_tower9': load_tile_image('bow_tower9.jpg'),
            'bow_tower10': load_tile_image('bow_tower10.jpg'),
            'bow_tower11': load_tile_image('bow_tower11.jpg'),
            'bow_tower12': load_tile_image('bow_tower12.jpg'),

        }
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        if tile_type == "wall":
            wall_group.add(self)
        if tile_type == "die_tile":
            die_group.add(self)
