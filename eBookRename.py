import pathlib
import os
from zipfile import ZipFile
from platform import platform


master_folder = "SitePoint Academy"


def get_windows_path():
    return pathlib.Path("C:\Temp") / master_folder


def get_linux_path():
    return pathlib.PurePath("/home/chris/Work") / master_folder


# go through the zip file because some zips have all the files, and we only want the pdf
def get_pdf_file_from_zip_file(zip_file):
    zipped_files = ZipFile(zip_file).namelist()
    for file in zipped_files:
        if file[-4:] == ".pdf":
            return file


def process_folder(path):
    for folder in pathlib.Path(path).iterdir():
        name = str(folder.parts[-1])
        print("Folder Name >>> " + name)
        os.chdir(folder)
        for file in folder.iterdir():
            if file.suffix == ".zip":   # this is done because epub shows up as a zipped file if I use .is_zipped
                zipped_file = get_pdf_file_from_zip_file(file)
                ZipFile(file).extract(zipped_file)
                pdf_file = folder / zipped_file
                new_file = folder / str(name + pdf_file.suffix)
                os.rename(pdf_file, new_file)
                ZipFile(file).close()
                print(str(pdf_file) + " has been renamed to > " + str(new_file))
                os.remove(file)
                print("The zip file > " + str(file) + " has been removed.")
            else:
                new_file = folder / str(name + file.suffix)
                os.rename(file, new_file)
                print(str(file) + " has been renamed to > " + str(new_file))
        os.chdir(path)
        new_folder = path / str(name).replace(' ', '_')
        os.rename(folder, new_folder)
        print("*******************")


def main():
    operating_system = platform()
    if operating_system[:5] == "Windo":
        main_path = get_windows_path()
    elif operating_system[:5] == "Linux":
        main_path = get_linux_path()
    else:
        main_path = get_linux_path()

    os.chdir(main_path)
    process_folder(main_path)


if __name__ == '__main__':
    main()
