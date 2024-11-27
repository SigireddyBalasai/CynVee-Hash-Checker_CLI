import os
import sys
import hashlib


print("Starting... ")


def main():
    userConfig = input("File name or path? (n/p, case insensitive. You can also type [ex]it to exit the program) ").lower()
    if userConfig == "n":
        userPath = os.path.dirname(os.path.abspath(sys.argv[0]))
        print("Current directory = " + userPath)
        userFile = input("Input file name: ")
        filePath = userPath + "/" + userFile
        print(hash_file(filePath))
    elif userConfig == "p":
        filePath = input("Input file path: ")
        print(hash_file(filePath))
    elif userConfig == "ex" or userConfig == "exit":
        sys.exit("Exiting Program...")
    else:
        print("Input not accepted. Starting again...")
        main()


def hash_file(filePath):
    h1 = hashlib.sha1()
    h224 = hashlib.sha224()
    h256 = hashlib.sha256()
    h384 = hashlib.sha384()
    h512 = hashlib.sha512()
    m5 = hashlib.md5()
    with open(filePath, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
            h224.update(chunk)
            h256.update(chunk)
            h384.update(chunk)
            h512.update(chunk)
            m5.update(chunk)
    return "Sha1:   " + h1.hexdigest() + "\nSha224: " + h224.hexdigest() + "\nSha256: " + h256.hexdigest() + "\nSha384: " + h384.hexdigest() + "\nSha512: " + h512.hexdigest() + "\nMd5:    " + m5.hexdigest()


main()
