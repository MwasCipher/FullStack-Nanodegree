import os

from string import digits
import string


def rename():
    os.chdir('/home/mufasa/Downloads/Audio/Billboard Hot 100 Singles Chart (24.08.2019)')

    home_dir = os.path.expanduser("~")
    path = "{}/{}".format(home_dir, "Downloads/Audio/Billboard Hot 100 Singles Chart (24.08.2019)")

    file_list = os.listdir(path)

    print(file_list)

    for file_name in file_list:
        new_filename = file_name.translate(str.maketrans('', '', digits))
        print("New Name: " + new_filename)

        src = '{}/{}'.format(path, file_name)
        dest = '{}/{}'.format(path, new_filename)

        os.rename(src, dest)


rename()

