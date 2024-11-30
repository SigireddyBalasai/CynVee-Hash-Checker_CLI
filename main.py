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
        print("Exiting Program...")
        sys.exit(0)
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
    full_hash_list = []
    for x in hash_list:
        next_hash_name = next(hash_name_iter)
        full_hash = next_hash_name + x.hexdigest()
        print(next_hash_name + x.hexdigest())
        full_hash_list.append(full_hash)
    create = input("Create a .txt file with the hashes at current directory? (y/n): ").lower()
    if create == "y":
        name = input("Write the name of the file: ")
        with open(name + ".txt", "w") as f:
            f.write("Hashes for file: " + file_path + "\n")
            for x in full_hash_list:
                f.write(x + "\n")
        print("Created file: " + f.name)
    else:
        print("File not created")
    sys.exit(0)


try:
    if sys.argv[1] == "-n" or sys.argv[1] == "--name":
        file_config()
    elif sys.argv[1] == "-p" or sys.argv[1] == "--path":
        path_config()
    else:
        main()
except IndexError:
    main()
