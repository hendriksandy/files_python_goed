__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil


path = './files/cache'              # de current directory is files
zip_list = './files/data.zip'


def clean_cache():

    if os.path.isdir(path):
        shutil.rmtree(path)  # delete folder/cache
        os.mkdir(path)  # create folder/cache
    else:
        return os.mkdir(path)


def cache_zip(file_path: str, cache_dir_path: str):
    clean_cache()
    return shutil.unpack_archive(file_path, cache_dir_path)


cache_zip(zip_list, path)


def cached_files():
    total_list = os.path.abspath(path)
    return total_list


print(cached_files())


def find_password(cached_files):
    search_pw = "password"
    for i in cached_files:
        f = open(i, "r")
        for line in f:
            if search_pw in line:
                password = line.split(" ")[1].strip()
                return password


# print(find_password(cached_files()))
