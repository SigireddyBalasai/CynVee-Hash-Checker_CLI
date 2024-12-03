"""
This module provides a function to compute multiple hash values for a file.
"""

import hashlib
import timeit
import questionary as qy


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
    start_time = timeit.default_timer()
    hash_name_list = [
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3_224",
        "sha3_256",
        "sha3_384",
        "sha3_512",
        "md5",
        "blake2b",
        "blake2s"
    ]
    hash_list = []
    choice_list = qy.checkbox(
        "Select hashing methods:",
        choices=hash_name_list,
    ).ask()

    for c in choice_list:
        hash_list.append("hashlib." + c + "()")
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            for h in hash_list:
                eval(h).update(chunk)
    
    choice_list_iter = iter(choice_list)
    full_choice_list = []
    for h in hash_list:
        next_choice_name = next(choice_list_iter).upper()
        full_hash = next_choice_name + ": " + eval(h).hexdigest()
        full_choice_list.append(full_hash)
        print(next_choice_name + ": " + eval(h).hexdigest())
    
    end_time = timeit.default_timer()
    print("Finished")
    print("Process completed in approximately: " + str(end_time - start_time) + " seconds")


    create = input(
        "Create a .txt file with the hashes at current "
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
            for c in full_choice_list:
                f.write(c + "\n")
        print("Created file: " + f.name)
    else:
        print("File not created")
