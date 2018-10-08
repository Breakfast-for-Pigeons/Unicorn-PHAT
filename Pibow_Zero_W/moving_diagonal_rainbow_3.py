#!/usr/bin/python3
"""
Moving Diagonal Rainbow 3 - Pibow Zero W

Retrieves the rainbows and sends them to the move function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows move
from the top left to the bottom right.

....................

Functions:
- moving_diagonal_rainbow_3: Retrieves the rainbows and sends them to
      the move function.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from bfp_unicornphat import get_diagonal_rainbows_2
from bfp_unicornphat import move_diagonally


########################################################################
#                            Functions                                 #
########################################################################


def moving_diagonal_rainbow_3():
    """
    Gets 4 rainbows and sends them to the move_diagonally function
    """

    rainbow00, rainbow01, rainbow02, \
        rainbow03 = get_diagonal_rainbows_2()

    move_diagonally(rainbow00, rainbow01, rainbow02, rainbow03)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        moving_diagonal_rainbow_3()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
