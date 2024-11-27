import os
import sys
import hashlib


print("Starting... ")


def main():
    user_config = input("File name or path? (n/p, case insensitive. You can also type [ex]it to exit the program) ").lower()
    if user_config == "n":
        user_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        print("Current directory = " + user_path)
        user_file = input("Input file name: ")
        file_path = user_path + "/" + user_file
        print(hash_file(file_path))
    elif user_config == "p":
        file_path = input("Input file path: ")
        print(hash_file(file_path))
    elif user_config == "ex" or user_config == "exit":
        sys.exit("Exiting Program...")
    else:
        print("Input not accepted. Starting again...")
        main()


def hash_file(file_path):
    h1 = hashlib.sha1()
    h224 = hashlib.sha224()
    h256 = hashlib.sha256()
    h384 = hashlib.sha384()
    h512 = hashlib.sha512()
    h3_224 = hashlib.sha3_224()
    h3_256 = hashlib.sha3_256()
    h3_384 = hashlib.sha3_384()
    h3_512 = hashlib.sha3_512()
    m5 = hashlib.md5()
    b2b = hashlib.blake2b()
    b2s = hashlib.blake2s()
    with open(file_path, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
            h224.update(chunk)
            h256.update(chunk)
            h384.update(chunk)
            h512.update(chunk)
            h3_224.update(chunk)
            h3_256.update(chunk)
            h3_384.update(chunk)
            h3_512.update(chunk)
            m5.update(chunk)
            b2b.update(chunk)
            b2s.update(chunk)
    return "SHA1:     " + h1.hexdigest() + "\nSHA224:   " + h224.hexdigest() + "\nSHA256:   " + h256.hexdigest() + "\nSHA384:   " + h384.hexdigest() + "\nSHA512:   " + h512.hexdigest() + "\nSHA3_224: " + h3_224.hexdigest() + "\nSHA3_256: " + h3_256.hexdigest() + "\nSHA3_384: " + h3_384.hexdigest() + "\nSHA3_512: " + h3_512.hexdigest() + "\nMD5:      " + m5.hexdigest() + "\nBLAKE2b:  " + b2b.hexdigest() + "\nBLAKE2s:  " + b2s.hexdigest()



main()