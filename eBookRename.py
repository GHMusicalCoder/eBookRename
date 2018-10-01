import pathlib
import os
from platform import platform


master_folder = "SitePoint Academy"


def get_windows_path():
    return pathlib.Path("C:\Temp") / master_folder


def get_linux_path():
    return pathlib.PurePath("/home/chris/Work") / master_folder


def process_folder(path):
    for folder in os.listdir(str(path)):
        print(folder)


def main():
    operating_system = platform()
    if operating_system[:5] == "Windo":
        main_path = get_windows_path()
    elif operating_system[:5] == "Linux":
        main_path = get_linux_path()

    process_folder(main_path)


if __name__ == '__main__':
    main()
