from src.scenes.init_screen import init_screen
from src.scenes.first_level import play
from src.scenes.levels_menu import levels_menu
from src.scenes.start_screen_scene import start_screen
from src.scenes.terminate import terminate



def main() -> None:
    screen = init_screen()


    start_screen(screen)

    play(screen)
    terminate()


if __name__ == '__main__':
    main()