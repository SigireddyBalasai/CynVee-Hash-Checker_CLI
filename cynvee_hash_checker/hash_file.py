"""
This module provides a function to compute multiple hash values for a file.
"""

import hashlib


def hash_file(file_path):
    """
    Computes multiple hash values for a given file and optionally writes them
    to a text file.

    Args:
        file_path (str): The path to the file to be hashed.
        Create a .txt file with the hashes at current working directory? (y/n):
            If 'y', prompts for the name of the file and writes the hash values
            to it.
        None

    Prompts:
        Create a .txt file with the hashes at current working directory? (y/n):
            If 'y', prompts for the name of the file and writes the hash
            values to it.
            If 'n', does not create a file.

    Hash Algorithms Used:
        - SHA1
        - SHA224
        - SHA256
        - SHA384
        - SHA512
        - SHA3_224
        - SHA3_256
        - SHA3_384
        - SHA3_512
        - MD5
        - BLAKE2b
        - BLAKE2s

    Example:
        hash_file('example.txt')
    """
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
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            for h in hash_list:
                h.update(chunk)
    hash_name_iter = iter(hash_name_list)
    full_hash_list = []
    for x in hash_list:
        next_hash_name = next(hash_name_iter)
        full_hash = next_hash_name + x.hexdigest()
        print(next_hash_name + x.hexdigest())
        full_hash_list.append(full_hash)
    create = input(
        "Create a .txt file with the hashes at current"
        "working directory? (y/n): "
    ).lower()
    if create == "y":
        name = input(
            "Write the name of the file (if there is a .txt file"
            "of the same name in the directory, "
            "it will likely be overwritten!): "
        )
        with open(name + ".txt", "w") as f:
            f.write("Hashes for file: " + file_path + "\n")
            for x in full_hash_list:
                f.write(x + "\n")
        print("Created file: " + f.name)
    else:
        print("File not created")
