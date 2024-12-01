"""
    Main module for the hash checker program.
"""
import sys
from file_config import file_config
from path_config import path_config


def main():
    """
    Main function to handle user input for file or path configuration.

    Prompts the user to input either 'n' for file configuration, 'p'
    for path configuration,
    or 'ex'/'exit' to exit the program. Based on the input,
    it calls the appropriate function
    or exits the program.

    Raises:
        SystemExit: If the user chooses to exit the program.
    """
    user_config = input(
        "File name or path? (n/p, case insensitive."
        "You can also type [ex]it to exit the program) "
        ).lower()
    if user_config == "n":
        file_config()
    elif user_config == "p":
        path_config()
    elif user_config == "ex" or user_config == "exit":
        print("Exiting Program...")
        sys.exit(0)
    else:
        print("Input not accepted")
