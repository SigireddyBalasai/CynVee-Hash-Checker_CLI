"""
Module for file configuration and hashing.
"""

import os
from hash_file import hash_file


def file_config():
    """
    Function to configure file path and print its hash.
    """
    user_path = os.getcwd()
    print("Current directory = " + user_path)
    user_file = input("Input file name: ")
    if os.path.isfile(user_path + "/" + user_file):
        file_path = user_path + "/" + user_file
        print(hash_file(file_path))
    else:
        print("File not found")
