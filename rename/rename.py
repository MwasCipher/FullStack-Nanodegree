import os


def rename_files():
    os.chdir('/home/mufasa/Desktop/prank')
    file_list = os.listdir('/home/mufasa/Desktop/prank')
    path = os.getcwd()
    # os.chdir('/home/mufasa/Desktop/prank')
    # print(file_list)
    # print("We are in: " +path)

    for file_name in file_list:
        os.rename(file_name, file_name.translate("0123456789"))

    os.chdir(path)


rename_files()
