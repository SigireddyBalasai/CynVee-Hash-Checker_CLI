# Installation Guide

This guide will help you install and set up the CLI version of CynVee-Hash-Checker.

## Requirements:
- Python installed on your system. If it's not working, try upgrading your version of Python and/or adding Python to your PATH.
- The `questionary` and `tqdm` Python packages, which can be installed via pip:
    ```sh
    pip install questionary tqdm
    ```

## Installation Steps:
1. **Clone the Repository:**
     ```sh
     git clone https://github.com/Cyncrovee/CynVee-Hash-Checker.git
     ```
2. **Navigate to the Directory:**
     ```sh
     cd CynVee-Hash-Checker
     ```
3. **Install Dependencies:**
     Ensure you have the required Python package installed:
     ```sh
     pip install questionary tqdm
     ```

## Running the Program:
To use the CLI, open a terminal and run:
```sh
python cynvee_hash_checker
```
There may be more ways of doing it, so feel free to use what works for you.

## Arguments:
- `-n` or `--name` will skip the first prompt and go straight to asking for the file name (from your current working directory).
- `-p` or `--path` will skip the first prompt and go straight to asking for the file path.

## Create .txt File with Hashes:
Once the program has finished generating the hashes, it should prompt you to optionally save a .txt file with the hashes stored inside. If you accept, it should prompt you to name said .txt file. It will save the file in the current working directory. If there is already a .txt file of the same name in the directory, it will likely be overwritten by the program, so be careful what you name it!
