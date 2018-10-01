#!/usr/bin/python3
"""
Print UnicornPHAT Header

This is the print_unicornphat_header module for my Pimoroni
UnicornPHAT programs.

....................

Functions:

- print_unicornphat_header: Prints a header

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""


def print_unicornphat_header():
    """
    Prints a header


    This function will print out the program header in a randomly
    selected color.
    """

    import random

    color_list = ['\033[1;31;40m', '\033[1;32;40m', '\033[1;33;40m',
                  '\033[1;34;40m', '\033[1;35;40m', '\033[1;36;40m',
                  '\033[1;37;40m']

    color = random.choice(color_list)

    print(color)
    print(r"""
  _   _       _                        ____  _   _    _  _____
 | | | |_ __ (_) ___ ___  _ __ _ __   |  _ \| | | |  / \|_   _|
 | | | | '_ \| |/ __/ _ \| '__| '_ \  | |_) | |_| | / _ \ | |
 | |_| | | | | | (_| (_) | |  | | | | |  __/|  _  |/ ___ \| |
  \___/|_| |_|_|\___\___/|_|  |_| |_| |_|   |_| |_/_/   \_\_|


    """)


if __name__ == '__main__':
    print_unicornphat_header()
