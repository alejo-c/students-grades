import os, platform


def clear() -> None:
    os.system('clear' if platform.system() == "Linux" else 'cls')


def pause() -> None:
    input('\n...Press <ENTER> to continue...\n')