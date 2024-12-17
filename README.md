# CynVee-Hash-Checker (CLI)

The CLI version of CynVee-Hash-Checker, written in Python.
You can find the GUI version here: https://github.com/Cyncrovee/CynVee-Hash-Checker

## Currently supports:
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

## Usage:
### Requirements:
- Python installed on your system (if it's not working, try upgrading your version of Python and/or adding Python to your PATH)
- The questionary and tqdm python packages, which can be installed via pip:
```
pip install questionary tqdm
```

### Running:
To use, simply download the directory then open a terminal and use 
```
python cynvee_hash_checker
```
There may be more ways of doing it, so feel free to use what works for you

### Arguments:
-n or --name will skip the first prompt and go straight to asking for the file name (from your current working directory)

-p or --path will skip the first prompt and go straight to asking for the file path

### Create .txt file with hashes:
Once the program has finished generating the hashes, it should prompt you to optionally save a .txt file with the hashes stored inside. If you accept, it should prompt you to name said .txt file. It will save the file in the current working directory. If there already a .txt file of the same name in the directory, it will likely be overwritten by the program, so be careful what you name it!
