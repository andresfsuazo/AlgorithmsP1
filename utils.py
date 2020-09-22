import sys
from os import system, name

def exit_app():
    sys.exit()

def clear():
    """Clear the terminal screen"""
    # for windows
    if name == 'nt':
        system('cls')

    # for mac and linux
    else:
        system('clear')

def single_dict_key(dict):
    return [a for a, b in dict.items()][0]
