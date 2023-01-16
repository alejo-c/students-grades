import os, platform


def clear() -> None:
    os.system('clear' if platform.system() == "Linux" else 'cls')


def pause(message: str = '') -> None:
    input(f'{message}\n...Press <ENTER> to continue...\n')