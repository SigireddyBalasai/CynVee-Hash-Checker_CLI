import os
import sys
import hashlib


def hash_file(filePath):
    # h1 = hashlib0.sha1
    h256 = hashlib.sha256()
    h512 = hashlib.sha512()
    with open(filePath, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h256.update(chunk)
            h512.update(chunk)
    return "Sha256: " + h256.hexdigest() + "\nSha512: " + h512.hexdigest()


def main():
    if userConfigFile == "n":
        userPath = os.path.dirname(os.path.abspath(sys.argv[0]))
        print("Current directory = " + userPath)
        userFile = input("Input file name: ")
        filePath = userPath + "/" + userFile
        print(hash_file(filePath))
    elif userConfigFile == "p":
        filePath = input("Input file path: ")
        print(hash_file(filePath))
    else:
        print("Input not accepted. Starting again...")
        main()


print("Starting... ")
userConfigFile = input("File name or path? (n/p, case insensitive) ").lower()
main()
