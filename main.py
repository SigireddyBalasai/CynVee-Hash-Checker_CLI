import os
import sys
import hashlib


def main():
    user_config = input("File name or path? (n/p, case insensitive. You can also type [ex]it to exit the program) ").lower()
    if user_config == "n":
        file_config()
    elif user_config == "p":
        path_config()
    elif user_config == "ex" or user_config == "exit":
        sys.exit("Exiting Program...")
    else:
        print("Input not accepted")


def file_config():
    user_path = os.getcwd()
    print("Current directory = " + user_path)
    user_file = input("Input file name: ")
    if os.path.isfile(user_path + "/" + user_file):
        file_path = user_path + "/" + user_file
        print(hash_file(file_path))
    else:
        print("File not found")



def path_config():
    user_file = input("Input file path: ")
    if os.path.isfile(user_file):
        file_path = user_file
        print(hash_file(file_path))
    else:
        print("File not found")


def hash_file(file_path):
    print("Starting...")
    hash_list = [
        hashlib.sha1(),
        hashlib.sha224(),
        hashlib.sha256(),
        hashlib.sha384(),
        hashlib.sha512(),
        hashlib.sha3_224(),
        hashlib.sha3_256(),
        hashlib.sha3_384(),
        hashlib.sha3_512(),
        hashlib.md5(),
        hashlib.blake2b(),
        hashlib.blake2s()
    ]
    hash_name_list = [
        "SHA1: ",
        "SHA224: ",
        "SHA256: ",
        "SHA384: ",
        "SHA512: ",
        "SHA3_224: ",
        "SHA3_256: ",
        "SHA3_384: ",
        "SHA3_512: ",
        "MD5: ",
        "BLAKE2b: ",
        "BLAKE2s: "
    ]
    with open(file_path, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            for h in hash_list:
                h.update(chunk)
    hash_name_iter = iter(hash_name_list)
    for x in hash_list:
        next_hash_name = next(hash_name_iter)
        print(next_hash_name + x.hexdigest())
    sys.exit("Finished")

try:
    if sys.argv[1] == "-n" or "--name":
        file_config()
    elif sys.argv[1] == "-p" or "--path":
        path_config()
except:
    main()