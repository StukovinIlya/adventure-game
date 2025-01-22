import pygame
from pygame import Surface

from src.units.load_images import load_image


def get_background(file: str, screen: Surface) -> Surface:
    background = pygame.transform.scale(load_image(file), screen.get_size())
    return background
