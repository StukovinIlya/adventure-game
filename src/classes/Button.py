import pygame
from pygame import Surface

from src.units.load_images import load_image
from src.units.load_sound import load_sound


class Button:
    def __init__(
            self, x: int,
            y: int,
            width: int,
            height: int,
            text: None | str,
            image_path: str,
            hover_image_path=None,
            sound_path=None
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = load_image(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path is not None:
            self.hover_image = load_image(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path is not None:
            self.sound = load_sound(sound_path)
        self.is_hovered = False

    def draw(self, screen: Surface) -> None:
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        if self.text is not None:
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_position: tuple[int, int]) -> None:
        self.is_hovered = self.rect.collidepoint(mouse_position)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
