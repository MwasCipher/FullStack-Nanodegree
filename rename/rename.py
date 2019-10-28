import os
from string import digits
import re

def rename_files():
    file_list = os.listdir('/home/mufasa/Desktop/prank')
    path = os.getcwd()

    os.chdir('/home/mufasa/Desktop/prank')

    for file_name in file_list:
        # print("Old name: " + file_name)
        # print("new name: " + file_name.translate(str.maketrans('', '', '0123456789')))

        # remove = '0123456789'
        # my_table = str.maketrans("", "", remove)

        os.rename(file_name, file_name.translate(str.maketrans('', '', '0123456789')))

        os.chdir(path)


rename_files()
