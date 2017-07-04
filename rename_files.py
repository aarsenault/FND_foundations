# Program to programatically rename files in a directory based on certain rules.

import os

# using convention of leaving '/' off end
path = os.getcwd() + '/prank'

def rename_files(mypath):
    # 1 todo get files from folder
    jpg_files = get_file_names(mypath)


    # 2 todo rename files
    change_name(mypath, jpg_files)


def get_file_names(mypath):

    jpg_files = []

    for (dirpath, dirnames, filenames) in os.walk(mypath):

        for file in filenames:
            if file.endswith(".jpg"):
                jpg_files.append(file)

    return jpg_files


def change_name(mypath, file_list):

    for file in file_list:

        new_name = ''.join([i for i in file if not i.isdigit()])

        src = mypath + '/' + file
        dst = mypath + '/' + new_name

        os.rename(src, dst)




rename_files(path)