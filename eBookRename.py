import pathlib
import os
from zipfile import ZipFile
from platform import platform


master_folder = "SitePoint Academy"


def get_windows_path():
    return pathlib.Path("C:\Temp") / master_folder


def get_linux_path():
    return pathlib.PurePath("/home/chris/Work") / master_folder


def process_folder(path):
    for folder in pathlib.Path(path).iterdir():
        name = str(folder.parts[-1])
        print("Folder Name >>> " + name)
        for file in folder.iterdir():
            if file.suffix == ".zip":
                os.chdir(folder)
                print("this one is zipped: " + file.name)
                zipped_file = ZipFile(file).namelist()[0]
                # ZipFile(file).extract(zipped_file)
                pdf_file = folder / zipped_file
                new_name = folder / str(name + pdf_file.suffix)
                print(str(pdf_file) + " will become >> " + str(new_name))
                print("*** zip end ***")
                # ZipFile(file).extractall()
                # os.remove(file)
                # at this point - the pdf exists but the zip file doesn't and the system won't see the pdf file
                # so we need to rename the pdf file
            else:
                print("Rename attempt will be >>> " + file.stem + file.suffix + " >>> " + name + file.suffix)
        print("*******************")
    # for folder in os.listdir(str(path)):
    #     name = folder
    #     print("Folder name is " + name)
    #     print("renamed folder would be " + folder.replace(' ', '_'))
    #     # os.rename(folder, folder.replace(' ', '_'))
    #     print("files in the folder are:")
    #     for file in os.listdir(folder):
    #         if zipfile.is_zipfile(file):
    #             print("this one is zipped: " + file)
    #         print(file)
    #     print("----------")


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
