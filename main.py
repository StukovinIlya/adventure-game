from src.scenes.init_screen import init_screen
from src.scenes.play import play
from src.scenes.start_screen_scene import start_screen
from src.scenes.terminate import terminate
from src.sprites.load_images import load_images


def main() -> None:
    screen = init_screen()
    load_images()

    start_screen(screen)
    play(screen)
    terminate()


if __name__ == '__main__':
    main()
