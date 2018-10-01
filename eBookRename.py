import pathlib
import os
import zipfile
from platform import platform


master_folder = "SitePoint Academy"


def get_windows_path():
    return pathlib.Path("C:\Temp") / master_folder


def get_linux_path():
    return pathlib.PurePath("/home/chris/Work") / master_folder


def process_folder(path):
    for folder in os.listdir(str(path)):
        name = folder
        print("Folder name is " + name)
        print("renamed folder would be " + folder.replace(' ', '_'))
        # os.rename(folder, folder.replace(' ', '_'))
        print("files in the folder are:")
        for file in os.listdir(folder):
            if zipfile.is_zipfile(file):
                print("this one is zipped: " + file)
            print(file)
        print("----------")


def main():
    operating_system = platform()
    if operating_system[:5] == "Windo":
        main_path = get_windows_path()
    elif operating_system[:5] == "Linux":
        main_path = get_linux_path()

    os.chdir(main_path)
    process_folder(main_path)


if __name__ == '__main__':
    main()
